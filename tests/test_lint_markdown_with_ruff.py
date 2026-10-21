"""Tests for scripts/lint_markdown_with_ruff.py."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest


@pytest.fixture
def lint_module() -> Any:
    import importlib.util

    path = Path(__file__).resolve().parent.parent / "scripts" / "lint_markdown_with_ruff.py"
    spec = importlib.util.spec_from_file_location("lint_markdown_with_ruff", path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_extracts_multiple_block_styles(lint_module: Any) -> None:
    markdown = """
```python
x = 1
```

```py
y = 2
```

```py3
z = 3
```
"""

    source = lint_module.extract_python_blocks(markdown)

    assert "# --- code block 1 ---" in source
    assert "x = 1" in source
    assert "# --- code block 2 ---" in source
    assert "y = 2" in source
    assert "# --- code block 3 ---" in source
    assert "z = 3" in source


def test_skips_empty_blocks_but_keeps_numbering(lint_module: Any) -> None:
    markdown = """
```python
```

```python
x = 1
```
"""

    source = lint_module.extract_python_blocks(markdown)

    assert "code block 1" not in source
    assert "# --- code block 2 ---" in source


def test_ignores_non_python_blocks(lint_module: Any) -> None:
    markdown = """
```json
{"a": 1}
```

```bash
echo hi
```
"""

    assert lint_module.extract_python_blocks(markdown) == ""


def test_main_reports_missing_file(
    lint_module: Any,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    missing = tmp_path / "missing.md"

    assert lint_module.main([str(missing)]) == 2
    assert "File not found" in capsys.readouterr().err


def test_main_reports_no_python_blocks(
    lint_module: Any,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    path = tmp_path / "doc.md"
    path.write_text("# No code\n", encoding="utf-8")

    assert lint_module.main([str(path)]) == 0
    assert "nothing to lint" in capsys.readouterr().out


def test_main_pipes_blocks_to_ruff(
    lint_module: Any,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = tmp_path / "doc.md"
    path.write_text("```python\nx = 1\n```\n", encoding="utf-8")
    captured: dict[str, Any] = {}

    def fake_run(command: list[str], *, input: str, text: bool) -> subprocess.CompletedProcess[str]:
        captured["command"] = command
        captured["input"] = input
        captured["text"] = text
        return subprocess.CompletedProcess(command, 0)

    monkeypatch.setattr(subprocess, "run", fake_run)

    assert lint_module.main([str(path)]) == 0
    assert captured["command"][:3] == [sys.executable, "-m", "ruff"]
    assert captured["command"][3:5] == ["check", "--stdin-filename"]
    assert captured["command"][5] == "doc.md.py"
    assert "x = 1" in captured["input"]
    assert captured["text"] is True


def test_main_returns_ruff_exit_code(
    lint_module: Any,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = tmp_path / "doc.md"
    path.write_text("```python\nx=1\n```\n", encoding="utf-8")

    def fake_run(command: list[str], *, input: str, text: bool) -> subprocess.CompletedProcess[str]:
        return subprocess.CompletedProcess(command, 1)

    monkeypatch.setattr(subprocess, "run", fake_run)

    assert lint_module.main([str(path)]) == 1
