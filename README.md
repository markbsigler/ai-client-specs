# AI Client SRS (Software Requirements Specification)

Product requirements for an OpenAI-compatible AI client architecture used in IDE extensions (VS Code and Eclipse).

## Overview

This folder contains the primary SRS (Software Requirements Specification) and license for the AI client initiative. The SRS defines:

- product scope and assumptions
- functional requirements (EARS format)
- security and compliance expectations
- non-functional requirements (performance, accessibility, compatibility)
- user acceptance testing (UAT) coverage
- revision history for traceability

## Current Status

- Document status: Draft
- Current SRS version: 0.16
- Last updated: 2026-02-26

## Files

- [AI_Client-SRS.md](AI_Client-SRS.md) — main requirements document
- [LICENSE.md](LICENSE.md) — project license (CC BY-SA 4.0)

## How to Use This SRS

1. Start with the executive summary and goals.
2. Review architecture and design-phase requirements.
3. Map implementation tasks to REQ IDs.
4. Validate implementation using the UAT groups.
5. Track changes through the revision history.

## Contributing / Change Process

When updating [AI_Client-SRS.md](AI_Client-SRS.md), keep requirement traceability intact:

1. Add or update requirements in EARS format under the correct section.
2. Keep requirement IDs unique and monotonic (`REQ-xx`); avoid reusing existing IDs.
3. If a requirement is superseded, keep historical references and document the supersession.
4. Add or update corresponding UAT scenarios so each new/changed requirement is testable.
5. If behavior changes, update relevant NFR rows and error-handling guidance as needed.
6. Update the document header version/date and add a concise entry in revision history.

Recommended checklist for each SRS change:

- Scope updated (in-scope / out-of-scope alignment)
- Functional requirement updated (REQ)
- Validation updated (UAT)
- Quality constraints updated (NFR), if impacted
- Revision history updated

## License

Licensed under [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/).

Required attribution (TASL):

- **Title:** AI Client SRS (Software Requirements Specification)
- **Author:** [Mark Sigler](https://www.linkedin.com/in/markbsigler/)
- **Source:** [AI_Client-SRS.md](AI_Client-SRS.md)
- **License:** Creative Commons Attribution-ShareAlike 4.0 International ([https://creativecommons.org/licenses/by-sa/4.0/legalcode.en](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en))
