# Document Control

This section contains version history, approvals, and licensing information for this Software Requirements Specification.

---

## Document Information

**Document ID**: SRS-AI-CLIENT-001  
**Version**: 0.17  
**Date**: 2026-02-26  
**Standard**: ISO/IEC/IEEE 29148:2018  
**Status**: Draft  
**Author**: Mark Sigler

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2026-02-01 | Mark Sigler | Initial document structure and executive summary |
| 0.2 | 2026-02-02 | Mark Sigler | Added personas, goals, and assumptions |
| 0.3 | 2026-02-03 | Mark Sigler | Added data flow architecture and security considerations |
| 0.4 | 2026-02-04 | Mark Sigler | Added functional requirements (initial set) |
| 0.5 | 2026-02-05 | Mark Sigler | Added configuration schema and error handling |
| 0.6 | 2026-02-06 | Mark Sigler | Added UAT plan |
| 0.7 | 2026-02-07 | Mark Sigler | Added MCP support, BYOK via SecretStorage, Enterprise SSO graduation path |
| 0.8 | 2026-02-08 | Mark Sigler | Added prompt engineering patterns and structured output requirements |
| 0.9 | 2026-02-09 | Mark Sigler | Added function calling (tools) requirements and examples |
| 0.10 | 2026-02-10 | Mark Sigler | Added system architecture diagrams and component overview |
| 0.11 | 2026-02-11 | Mark Sigler | Added image generation requirements (limited scope: single image generation only) |
| 0.12 | 2026-02-12 | Mark Sigler | Added design-phase requirements (§7) — provider-agnostic interface, BYOK, MCP, enterprise graduation, architectural hedges |
| 0.13 | 2026-02-13 | Mark Sigler | P4 Priority tier: added 16 new requirements (REQ-68 through REQ-78, REQ-79-85) for URL path construction, tool execution safety, user interaction patterns, concurrent requests, provider capability detection, multi-provider config, context window overflow handling |
| 0.14 | 2026-02-14 | Mark Sigler | P4 follow-up: added 3 extension lifecycle requirements (REQ-89, REQ-90, REQ-99) |
| 0.15 | 2026-02-15 | Mark Sigler | P4 NFR additions: added 9 new NFR rows and requirements (bundle size limit, CPU usage limit, i18n support, accessibility compliance, telemetry event schema, telemetry settings UI, SecretStorage API unavailable degradation path, response size limit, network timeouts, activation event constraints) — added REQ-07a, REQ-91-99 |
| 0.16 | 2026-02-16 | Mark Sigler | P5 Test Coverage: added 8 new UAT test groups (19-26) covering provider-specific compatibility, security edge cases, tool safety, performance/NFR validation, accessibility, telemetry, i18n, architectural hedge validation (47 new test scenarios) |
| 0.17 | 2026-02-26 | Mark Sigler | **IEEE 29148 Migration**: Restructured document into ISO/IEC/IEEE 29148:2018 format with modular file organization. All 99 requirements remapped to domain-prefixed IDs. Added formal traceability matrix. No content removed. |

---

## Document Approvals

**Status**: Draft — pending final stakeholder review

| Role | Name | Date | Signature |
|------|------|------|-----------|
| **Product Owner** | Mark Sigler | 2026-02-26 | [Approved] |
| **Development Lead** | [Pending] | [Pending] | [Pending] |
| **QA Lead** | [Pending] | [Pending] | [Pending] |
| **Technical Architect** | [Pending] | [Pending] | [Pending] |

---

## Change Control Process

**For Document Versions 0.x (Draft)**:
- Changes may be made without formal approval
- Version number incremented with each substantive change
- Change log maintained in Revision History table

**For Document Versions 1.x+ (Released)**:
- All changes require approval from Product Owner
- Breaking changes (major version) require approval from all stakeholders
- Non-breaking changes (minor version) require approval from Product Owner and Development Lead
- Change requests must be documented with rationale and impact assessment

---

## License and Attribution

### License

This document is licensed under the **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** license.

**You are free to**:
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material for any purpose, even commercially

**Under the following terms**:
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made
- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original

### TASL Attribution

**Title**: AI Client Software Requirements Specification  
**Author**: [Mark Sigler](https://www.linkedin.com/in/markbsigler/)  
**Source**: [ai-client-specs](https://github.com/yourorg/ai-client-specs/ai-client-srs.md) *(update with actual repository URL)*  
**License**: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode)

**Full License Text**: See [LICENSE.md](../LICENSE.md) in the project root directory.

---

## Third-Party Components and Dependencies

This SRS references several third-party technologies and standards:

### Standards and Specifications

| Component | Source | License/Terms |
|-----------|--------|---------------|
| **ISO/IEC/IEEE 29148:2018** | International Organization for Standardization | [ISO Copyright](https://www.iso.org/copyright.html) |
| **OpenAI Chat Completions API** | OpenAI | [OpenAI Terms](https://openai.com/policies/terms-of-use) |
| **Model Context Protocol (MCP)** | Anthropic | [Apache 2.0](https://github.com/anthropics/anthropic-mcp/blob/main/LICENSE) |
| **EARS (Easy Approach to Requirements Syntax)** | Alistair Mavin et al. | Public domain methodology |

### Software Libraries (Referenced in Requirements)

| Component | Purpose | License |
|-----------|---------|---------|
| **VS Code Extension API** | IDE integration | [MIT License](https://github.com/microsoft/vscode/blob/main/LICENSE.txt) |
| **Eclipse RCP/JFace** | IDE integration | [Eclipse Public License 2.0](https://www.eclipse.org/legal/epl-2.0/) |
| **SecretStorage API (VS Code)** | Credential management | [MIT License](https://github.com/microsoft/vscode/blob/main/LICENSE.txt) |
| **Eclipse Secure Storage** | Credential management | [Eclipse Public License 2.0](https://www.eclipse.org/legal/epl-2.0/) |

**Note**: This SRS does not distribute these components. They are referenced as integration dependencies only. Implementers must comply with each component's respective license terms.

---

## Compliance and Standards

This document is structured in accordance with:

- **ISO/IEC/IEEE 29148:2018** — Systems and software engineering — Life cycle processes — Requirements engineering
- **EARS (Easy Approach to Requirements Syntax)** — Requirements writing methodology
- **MoSCoW Prioritization** — Must have, Should have, Could have, Won't have

### Requirements Traceability

All requirements defined in this specification are:
- Uniquely identified with domain-prefixed IDs (e.g., REQ-CFG-001, REQ-API-005)
- Written using EARS syntax patterns (Ubiquitous, Event-driven, Unwanted behavior, State-driven, Optional)
- Mapped to User Acceptance Test cases in [Appendix A: Traceability Matrix](appendix-a-traceability-matrix.md)
- Prioritized using MoSCoW framework

### Test Coverage

All functional requirements (99 total) and all non-functional requirements (26 total) are covered by User Acceptance Test cases defined in [Verification](verification.md).

**Coverage Statistics**:
- Functional Requirements Coverage: **100%** (99/99)
- Non-Functional Requirements Coverage: **100%** (26/26)
- Total Test Cases: **130+ scenarios** across 26 test groups

---

## Related Documents

- **[Introduction](01-introduction.md)** — Purpose, scope, and context
- **[Overall Description](02-overall-description.md)** — Product perspective and constraints
- **[System Features](03-system-features.md)** — Complete functional requirements (99 requirements)
- **[External Interfaces](04-external-interfaces.md)** — Interface specifications
- **[Non-Functional Requirements](05-nonfunctional-requirements.md)** — Quality attributes (26 NFRs)
- **[Other Requirements](06-other-requirements.md)** — Database, i18n, legal
- **[Appendix A: Traceability Matrix](appendix-a-traceability-matrix.md)** — Requirements ↔ Tests mapping
- **[Appendix B: Glossary](appendix-b-glossary.md)** — Definitions and terminology
- **[Appendix C: Analysis Models](appendix-c-analysis-models.md)** — Architecture diagrams
- **[API Patterns](api-patterns.md)** — Developer implementation guide
- **[Verification](verification.md)** — User Acceptance Testing plan

---

## Contact Information

**Document Owner**: Mark Sigler  
**Email**: [Contact via LinkedIn](https://www.linkedin.com/in/markbsigler/)  
**Organization**: [Your Organization Name]  
**Project Repository**: [GitHub/GitLab repository URL]

For questions, clarifications, or change requests, please contact the document owner or submit an issue in the project repository.

---

[← Previous](verification.md) | [Back to main](../ai-client-srs.md)
