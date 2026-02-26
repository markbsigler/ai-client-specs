# AI Client SRS (Software Requirements Specification)

Product requirements for an OpenAI-compatible AI client architecture used in IDE extensions (VS Code and Eclipse).

## Overview

This repository contains a comprehensive Software Requirements Specification (SRS) structured according to **ISO/IEC/IEEE 29148:2018** standards. The SRS defines:

- Product scope, stakeholder needs, and system context
- 99 functional requirements organized into 11 feature domains
- Non-functional requirements (performance, security, accessibility, compliance)
- External interface specifications (UI, software interfaces, communications)
- Full requirements traceability matrix (requirements ↔ tests)
- User acceptance testing (UAT) coverage with 130+ test scenarios across 26 test groups
- API usage patterns and developer guidance
- Complete glossary and system architecture models

## Current Status

- **Document Status**: Draft
- **Version**: 0.17
- **Standard**: ISO/IEC/IEEE 29148:2018
- **Last Updated**: 2026-02-26

## Document Structure

The SRS is organized into modular files following IEEE 29148 conventions:

### Core Specification

- **[ai-client-srs.md](ai-client-srs.md)** — Master index with document control, table of contents, and approvals

### Main Sections (docs/)

1. **[docs/01-introduction.md](docs/01-introduction.md)** — Purpose, scope, product perspective, definitions, references
2. **[docs/02-overall-description.md](docs/02-overall-description.md)** — Product functions, user classes, operating environment, constraints, assumptions
3. **[docs/03-system-features.md](docs/03-system-features.md)** — All 99 functional requirements organized into 11 domains (REQ-CFG-*, REQ-CRED-*, REQ-API-*, etc.)
4. **[docs/04-external-interfaces.md](docs/04-external-interfaces.md)** — User interfaces, software interfaces, communications interfaces
5. **[docs/05-nonfunctional-requirements.md](docs/05-nonfunctional-requirements.md)** — Performance, security, quality attributes, compliance
6. **[docs/06-other-requirements.md](docs/06-other-requirements.md)** — Internationalization, legal, operational requirements

### Appendices

- **[docs/appendix-a-traceability-matrix.md](docs/appendix-a-traceability-matrix.md)** — Requirements-to-tests mapping, migration cross-reference (REQ-XX → REQ-DOMAIN-XXX)
- **[docs/appendix-b-glossary.md](docs/appendix-b-glossary.md)** — Complete definitions of 67 technical terms
- **[docs/appendix-c-analysis-models.md](docs/appendix-c-analysis-models.md)** — 11 system architecture diagrams (Mermaid)

### Supporting Documentation

- **[docs/verification.md](docs/verification.md)** — User Acceptance Testing (UAT) plan with 26 test groups, 130+ scenarios
- **[docs/api-patterns.md](docs/api-patterns.md)** — API usage patterns and prompt engineering guidance for developers
- **[docs/document-control.md](docs/document-control.md)** — Revision history (16 versions), approvals, license information

### Additional Files

- **[LICENSE.md](LICENSE.md)** — Project license (Creative Commons Attribution-ShareAlike 4.0 International)
- **[Makefile](Makefile)** — Build automation (lint, PDF generation)
- **ai-client-srs-v0.16-original.md** — Archived version prior to IEEE 29148 migration

## How to Use This SRS

1. **Start with the master index**: [ai-client-srs.md](ai-client-srs.md) provides the complete table of contents
2. **Understand the context**: Read [01-introduction.md](docs/01-introduction.md) for purpose, scope, and product perspective
3. **Review stakeholder needs**: See [02-overall-description.md](docs/02-overall-description.md) for user personas and success criteria
4. **Map implementation tasks**: Use [03-system-features.md](docs/03-system-features.md) to find specific functional requirements
5. **Check interfaces**: Review [04-external-interfaces.md](docs/04-external-interfaces.md) for configuration schemas and API contracts
6. **Validate quality requirements**: See [05-nonfunctional-requirements.md](docs/05-nonfunctional-requirements.md) for performance, security, and compliance
7. **Verify traceability**: Use [appendix-a-traceability-matrix.md](docs/appendix-a-traceability-matrix.md) to trace requirements to tests
8. **Run tests**: Reference [verification.md](docs/verification.md) for the complete UAT test plan

## Requirement ID Convention

Version 0.17 introduced domain-prefixed requirement IDs per IEEE 29148 conventions:

| Domain Prefix | Category | Example |
|---------------|----------|---------|
| **REQ-CFG-** | Configuration Management | REQ-CFG-001 |
| **REQ-CRED-** | Credential Management | REQ-CRED-001 |
| **REQ-API-** | API Integration | REQ-API-001 |
| **REQ-PROV-** | Provider Management | REQ-PROV-001 |
| **REQ-UX-** | User Experience | REQ-UX-001 |
| **REQ-PROMPT-** | Prompt Construction | REQ-PROMPT-001 |
| **REQ-JSON-** | Structured Output | REQ-JSON-001 |
| **REQ-TOOL-** | Function Calling (Tools) | REQ-TOOL-001 |
| **REQ-MCP-** | Model Context Protocol | REQ-MCP-001 |
| **REQ-ENT-** | Enterprise Graduation | REQ-ENT-001 |
| **REQ-LIFE-** | Extension Lifecycle | REQ-LIFE-001 |
| **PERF-** | Performance (NFR) | PERF-001 |
| **SEC-** | Security (NFR) | SEC-001 |
| **A11Y-** | Accessibility (NFR) | A11Y-001 |
| **I18N-** | Internationalization | I18N-001 |

**Migration Cross-Reference**: See [Appendix A](docs/appendix-a-traceability-matrix.md) for complete mapping of old REQ-XX IDs to new domain-prefixed IDs.

## Build Commands

```bash
# Run markdown linter (fixes formatting issues automatically)
make lint

# Generate PDF from all markdown files
make pdf

# Run all linters (markdown + Python code blocks)
make lint-all

# Clean generated files
make clean
```

## Contributing / Change Process

When updating the SRS, maintain requirement traceability and IEEE 29148 compliance:

1. **Identify the affected section**: Use the master index to locate the appropriate docs/ file
2. **Update requirements in EARS format**: Follow existing patterns (WHEN/WHILE/IF/WHERE/SHALL)
3. **Maintain unique requirement IDs**: Use the domain prefix convention; never reuse existing IDs
4. **Update traceability**: Add corresponding entries in [appendix-a-traceability-matrix.md](docs/appendix-a-traceability-matrix.md)
5. **Add or update UAT scenarios**: Update [verification.md](docs/verification.md) so each requirement is testable
6. **Update quality constraints**: If behavior changes, update [05-nonfunctional-requirements.md](docs/05-nonfunctional-requirements.md)
7. **Document the change**: Add an entry to the revision history in [document-control.md](docs/document-control.md)

**Recommended checklist for each SRS change**:

- [ ] Functional requirement added/updated with EARS syntax
- [ ] Requirement ID follows domain prefix convention
- [ ] Traceability matrix updated (requirement → tests)
- [ ] UAT test scenarios added/updated
- [ ] Non-functional requirements updated (if applicable)
- [ ] Revision history entry added with version bump
- [ ] PDF builds successfully (`make pdf`)
- [ ] Linter passes (`make lint`)

## License

Licensed under [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/).

**Required Attribution (TASL)**:

- **Title**: AI Client SRS (Software Requirements Specification)
- **Author**: [Mark Sigler](https://www.linkedin.com/in/markbsigler/)
- **Source**: [ai-client-srs.md](ai-client-srs.md)
- **License**: Creative Commons Attribution-ShareAlike 4.0 International ([Legal Code](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en))

See [LICENSE.md](LICENSE.md) for full license text.
