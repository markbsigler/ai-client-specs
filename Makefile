VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

# Master index file
MASTER := ai-client-srs.md

# All docs in reading order
DOCS := docs/01-introduction.md \
        docs/02-overall-description.md \
        docs/03-system-features.md \
        docs/04-external-interfaces.md \
        docs/05-nonfunctional-requirements.md \
        docs/06-other-requirements.md \
        docs/appendix-a-traceability-matrix.md \
        docs/appendix-b-glossary.md \
        docs/appendix-c-analysis-models.md \
        docs/verification.md \
        docs/api-patterns.md \
        docs/document-control.md

PDF := ai-client-srs.pdf

.PHONY: venv install markdown-lint lint-code-blocks lint lint-all pdf clean

venv:
	@test -d $(VENV) || python3 -m venv $(VENV)

install: venv
	$(PIP) install --upgrade pip ruff

markdown-lint:
	npx --yes markdownlint-cli2 --fix "**/*.md"

lint-code-blocks: install
	$(PYTHON) scripts/lint_markdown_with_ruff.py docs/api-patterns.md

lint: markdown-lint

lint-all: markdown-lint lint-code-blocks

pdf:
	pandoc $(MASTER) $(DOCS) -o $(PDF) --pdf-engine=weasyprint --filter mermaid-filter --template scripts/weasyprint.template.html

clean:
	rm -f $(PDF)