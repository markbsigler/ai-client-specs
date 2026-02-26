VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

SRC := ai-client-srs.md
PDF := ai-client-srs.pdf

.PHONY: venv install markdown-lint lint-code-blocks lint lint-all pdf clean

venv:
	@test -d $(VENV) || python3 -m venv $(VENV)

install: venv
	$(PIP) install --upgrade pip ruff

markdown-lint:
	npx --yes markdownlint-cli2 --fix "**/*.md"

lint-code-blocks: install
	$(PYTHON) scripts/lint_markdown_with_ruff.py $(SRC)

lint: markdown-lint

lint-all: markdown-lint lint-code-blocks

pdf:
	pandoc $(SRC) -o $(PDF) --pdf-engine=weasyprint --filter mermaid-filter --template scripts/weasyprint.template.html

clean:
	rm -f $(PDF)