from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


FENCE_PATTERN = re.compile(
    r"```(?P<lang>python|py|py3)\s*\n(?P<code>.*?)\n```",
    re.DOTALL | re.IGNORECASE,
)


def extract_python_blocks(markdown_text: str) -> str:
    blocks: list[str] = []
    blocks_iter = FENCE_PATTERN.finditer(markdown_text)
    for idx, match in enumerate(blocks_iter, start=1):
        code = match.group("code").strip()
        if not code:
            continue
        blocks.append(f"# --- code block {idx} ---\n{code}\n")
    return "\n".join(blocks)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Lint Python fenced code blocks in a Markdown file "
            "using Ruff."
        )
    )
    parser.add_argument("markdown_file", type=Path)
    args = parser.parse_args()

    if not args.markdown_file.exists():
        print(f"File not found: {args.markdown_file}", file=sys.stderr)
        return 2

    markdown_text = args.markdown_file.read_text(encoding="utf-8")
    python_source = extract_python_blocks(markdown_text)

    if not python_source.strip():
        message = (
            f"No Python fenced code blocks found in {args.markdown_file}; "
            "nothing to lint."
        )
        print(message)
        return 0

    command = [
        "ruff",
        "check",
        "--stdin-filename",
        f"{args.markdown_file.name}.py",
        "-",
    ]
    completed = subprocess.run(command, input=python_source, text=True)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
