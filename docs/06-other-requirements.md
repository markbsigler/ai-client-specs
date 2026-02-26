# 6. Other Requirements

## 6.1 Database Requirements

**Not applicable.** The extension does not require a database. All configuration is stored in IDE-native settings files, and credentials are stored in OS-level secure storage (SecretStorage API, macOS Keychain, Windows Credential Manager, Linux Secret Service).

**State Management:**

- **Configuration:** Stored in VS Code `settings.json` or Eclipse preferences (file-based)
- **Credentials:** Stored in OS credential stores via SecretStorage API or equivalent
- **Session State:** In-memory only; not persisted across IDE restarts
- **Conversation History:** Not persisted by default (feature-specific opt-in if implemented)

---

## 6.2 Internationalization Requirements

| ID | Priority | Requirement |
|----|----------|-------------|
| **I18N-001** | Should | **The extension shall** use an i18n framework (e.g., `vscode-nls`, Eclipse NLS) with externalized strings in resource bundles, enabling future localization without code changes. |
| **I18N-002** | Should | **The extension shall** ship with English (en-US) locale in v1; message keys shall follow convention `extension.category.message` for easy translation in v1.1+. |

**Implementation Notes:**

- All user-facing strings must be externalized (no hardcoded UI text)
- String keys follow hierarchical naming: `extension.category.message`
  - Example: `ai-client.config.missingApiKey` → "API key not found. Run 'Configure AI API Key' command."
- Resource bundles organized by locale: `nls/en-US.json`, `nls/es-ES.json`, etc.
- String formatting supports parameterization: `"Request failed after {0} retries"`

**Locale Support Roadmap:**

| Version | Locales Supported |
|---------|-------------------|
| v1.0 | English (en-US) |
| v1.1 | English (en-US), Spanish (es-ES), French (fr-FR), German (de-DE), Japanese (ja-JP) |
| v1.2+ | Additional locales based on customer demand |

---

## 6.3 Legal Requirements

### Licensing

The extension is distributed under the terms specified in the `LICENSE.md` file in the project root. All customers must accept the license terms during installation.

**License Summary:**

- Extension source code and binaries are licensed under [specify license type]
- Third-party dependencies are listed in `NOTICES` or equivalent attribution file
- Customer data (prompts, completions) remains customer property; vendor does not claim ownership

**Attribution:**

The extension includes or depends on the following third-party components:

- OpenAI API specification (informational reference; no code dependency)
- Model Context Protocol specification (MIT License)
- VS Code Extension API (Microsoft)
- Eclipse Platform API (Eclipse Foundation)
- Node.js `fetch` API or equivalent HTTP client libraries
- JSON Schema validation libraries

All third-party licenses are listed in the `NOTICES` file distributed with the extension.

### Data Privacy & Compliance

**GDPR Compliance:**

- **Telemetry:** Opt-in only; no data collected without explicit user consent
- **PII Exclusion:** No personally identifiable information in telemetry events
- **Data Minimization:** Only essential anonymized metadata collected
- **Right to Deletion:** Users can disable telemetry at any time; no historical data retained

**Customer Data:**

- **Prompts and Completions:** Sent directly from customer workstation to customer's provider; vendor never sees this data
- **API Keys:** Stored locally on customer machines; never transmitted to vendor infrastructure
- **Configuration:** Local to customer machines; no central registry or reporting

### Credential Storage Legal Requirements

**Compliance with Enterprise Security Policies:**

The extension's credential storage mechanism must comply with enterprise security policies:

- **No plaintext storage:** API keys never stored in plaintext in settings files (REQ-CRED-005, REQ-CRED-010)
- **OS-level secure storage:** Use platform-native credential stores (SecretStorage, Keychain, Credential Manager)
- **Credential rotation:** Support immediate credential updates without caching delays
- **Audit trail:** Enterprise gateways can log API access via X-Request-Id tracing (REQ-ENT-004)

**Export Control:**

The extension does not contain encryption technology subject to export control regulations. All cryptographic operations (HTTPS/TLS) are provided by the underlying platform (Node.js, operating system).

---

## 6.4 Operational Requirements

### Installation & Deployment

**Installation Methods:**

| Method | Platforms | Use Case |
|--------|-----------|----------|
| **VS Code Marketplace** | Windows, macOS, Linux | Individual developer installation |
| **Eclipse Marketplace** | Windows, macOS, Linux | Individual developer installation |
| **VSIX Package** | Windows, macOS, Linux | Enterprise distribution via GPO/MDM |
| **Eclipse Update Site** | Windows, macOS, Linux | Enterprise distribution |

**Prerequisites:**

- VS Code version: Latest 3 major versions
- Eclipse version: Latest 2 major versions
- Operating system: Windows 10+, macOS 11+, Ubuntu 20.04+, RHEL 8+
- Network access: HTTPS connectivity to customer's AI provider
- (Optional) Enterprise: Corporate proxy configuration if required

### Updates & Maintenance

**Update Distribution:**

- **Automatic updates:** Via VS Code / Eclipse marketplace (default)
- **Manual updates:** VSIX / update site package download
- **Enterprise control:** IT can disable auto-updates and control version deployment

**Breaking Changes:**

- Extension follows semantic versioning (SemVer)
- Major version changes may include breaking configuration changes
- Configuration schema migration provided for backward compatibility (2 major versions)

**Deprecation Policy:**

- Features deprecated with at least 1 major version notice
- Deprecated settings continue to work with warnings for 2 major versions
- Migration path documented in release notes

---

[← Previous](05-nonfunctional-requirements.md) | [Back to main](../ai-client-srs.md) | [Next →](appendix-a-traceability-matrix.md)
