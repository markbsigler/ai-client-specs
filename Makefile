UV ?= uv
PYTHON := $(UV) run python

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

.PHONY: install sync fmt lint-python format-check typecheck test check \
        markdown-lint lint-code-blocks lint lint-all pdf clean

install: ## Create the environment and install locked dependencies
	$(UV) sync --locked

sync: ## Sync the environment with uv.lock
	$(UV) sync --locked

fmt: ## Auto-fix and format the Python tooling
	$(UV) run ruff check --fix scripts tests
	$(UV) run ruff format scripts tests

lint-python: ## Lint the Python tooling
	$(UV) run ruff check scripts tests

format-check: ## Check Python formatting
	$(UV) run ruff format --check scripts tests

typecheck: ## Type-check the Python tooling (strict)
	$(UV) run mypy

test: ## Run the Python test suite with coverage
	$(UV) run pytest

check: lint-python format-check typecheck test ## Run all Python checks

markdown-lint: ## Auto-fix Markdown formatting
	npx --yes markdownlint-cli2 --fix "**/*.md"

lint-code-blocks: ## Lint Python fenced code blocks with Ruff
	$(UV) run scripts/lint_markdown_with_ruff.py docs/api-patterns.md

lint: markdown-lint ## Run the Markdown linter

lint-all: markdown-lint lint-code-blocks ## Run Markdown and code-block linters

pdf: ## Build the SRS PDF
	pandoc $(MASTER) $(DOCS) -o $(PDF) --pdf-engine=weasyprint --filter mermaid-filter --template scripts/weasyprint.template.html

clean: ## Remove generated files
	rm -f $(PDF)
