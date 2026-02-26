# 5. Non-Functional Requirements

## 5.1 Performance Requirements

| ID | Category | Requirement | Target | Measurement |
|----|----------|-------------|--------|-------------|
| **PERF-001** | Latency | Extension overhead (excluding provider time) | < 50ms | Performance profiling |
| **PERF-002** | Responsiveness | Time to first token displayed | < 500ms after provider responds | User testing |
| **PERF-003** | Bundle Size | Extension package size | < 10MB (VS Code), < 15MB (Eclipse with dependencies) | Build artifact size check |
| **PERF-004** | CPU | Idle CPU usage | < 5% when no AI requests active | Profiling |
| **PERF-005** | CPU | Active CPU usage | < 20% during streaming response | Profiling |
| **PERF-006** | Memory | Extension memory footprint | < 100MB | IDE memory profiling |
| **PERF-007** | Startup | Extension activation time | < 2 seconds | Activation timing |

**Additional Performance Constraints:**

- **Streaming latency:** Time from SSE first byte to UI display must be < 500ms
- **Network timeouts:** See REQ-API-007 (10s connection, 60s streaming, 30s non-streaming)
- **Response size limits:** See REQ-API-008 (1MB truncation with warning)

---

## 5.2 Safety Requirements

**Not applicable.** This software does not operate in safety-critical environments. The extension provides AI-assisted development tools and does not control any safety-critical systems.

**Risk Mitigation:**

While not safety-critical, the extension implements safeguards to prevent unintended workspace modifications:

- Tool execution requires explicit approval for destructive operations (REQ-TOOL-007)
- Workspace Trust integration disables tool execution in untrusted workspaces (REQ-MCP-006)
- Tool result truncation prevents context window overflow (REQ-TOOL-009)
- Circuit breaker prevents infinite tool-call loops (REQ-TOOL-005)

---

## 5.3 Security Requirements

| ID | Category | Requirement | Implementation |
|----|----------|-------------|----------------|
| **SEC-001** | Encryption | All provider communication must use HTTPS | TLS 1.2 or higher required (REQ-CRED-001) |
| **SEC-002** | PKI Support | Support custom CA certificates for enterprise PKI environments | Custom CA certificate configuration (REQ-ENT-006) |
| **SEC-003** | Credential Protection | API keys never logged or included in error reports | Credential sanitization (REQ-CRED-006, REQ-UX-009) |
| **SEC-004** | Credential Storage | API keys stored in OS-level secure storage (SecretStorage) | Never in plaintext settings files (REQ-CRED-005, REQ-CRED-010) |
| **SEC-005** | Prompt Injection | User content clearly delimited to reduce injection risk | Content delimitation in prompt construction (REQ-SEC-001) |

**Additional Security Constraints:**

- **No data persistence:** Prompts, completions, or conversation history not persisted to disk unless explicitly enabled for a feature
- **SecretStorage API unavailable degradation:** When SecretStorage unavailable, fall back to OS credential stores with warning; when both unavailable, disable AI features and display persistent warning (REQ-CRED-002)
- **Error message sanitization:** Provider error messages sanitized before display, removing internal URLs, resource identifiers, and API key patterns (REQ-UX-009)
- **Workspace Trust integration:** Tool execution disabled in untrusted workspaces; only read-only context from open files permitted (REQ-MCP-006)

---

## 5.4 Software Quality Attributes

### Reliability

| ID | Attribute | Requirement | Target |
|----|-----------|-------------|--------|
| **QUAL-001** | Error Recovery | Automatic retry with exponential backoff for transient errors | 3 retries max for 429, 5xx, timeout (see error handling strategy) |
| **QUAL-002** | Graceful Degradation | Continue operation when provider capabilities unavailable | Feature-specific fallbacks (REQ-PROV-004) |
| **QUAL-003** | Circuit Breaker | Prevent infinite loops in tool-call orchestration | Max 25 iterations (REQ-TOOL-005) |
| **QUAL-004** | Request Cancellation | Support user-initiated cancellation of in-progress requests | Clean abort with confirmation (REQ-UX-006, REQ-UX-007) |

### Accessibility

| ID | Attribute | Requirement | Target |
|----|-----------|-------------|--------|
| **A11Y-001** | Keyboard Navigation | All AI commands accessible via keyboard shortcuts | No mouse-only features (REQ-UX-010) |
| **A11Y-002** | Screen Reader Support | Status changes announced to screen readers | ARIA live regions for "Thinking...", "Generating...", "Complete" notifications |
| **A11Y-003** | Focus Management | Predictable focus flow during streaming; status changes announced | Accessibility testing |
| **A11Y-004** | High Contrast | UI elements visible in high contrast mode | Theme compatibility testing |
| **A11Y-005** | Zoom Support | UI remains usable at 200% zoom | VS Code zoom testing |

**Implementation:** See REQ-UX-010 (keyboard operation) and the accessibility requirements for detailed specifications.

### Telemetry & Observability

| ID | Attribute | Requirement | Implementation |
|----|-----------|-------------|----------------|
| **TELEM-001** | Opt-in Only | No telemetry without explicit user consent | Default disabled; user must enable via settings |
| **TELEM-002** | Event Schema | Structured event types with anonymized metadata | Defined event types: `ai.request.started`, `ai.request.completed`, `ai.request.failed`, `ai.tool.executed` |
| **TELEM-003** | PII Exclusion | No prompts, API keys, file paths in telemetry payloads | Data sanitization before transmission |
| **TELEM-004** | Request Tracing | X-Request-Id header on all LLM requests | UUID v4 header for end-to-end observability (REQ-ENT-004) |

**Telemetry Event Schema Example:**

```typescript
interface TelemetryEvent {
  event_type: "ai.request.started" | "ai.request.completed" | "ai.request.failed" | "ai.tool.executed";
  timestamp: string;  // ISO 8601
  session_id: string;  // UUID v4 (session-scoped, not persisted)
  provider_type: "azure-openai" | "openai" | "anthropic" | "ollama" | "compatible";
  model_family: string;  // e.g., "gpt-4", "gpt-3.5" (no specific deployment ID)
  feature: string;  // e.g., "code_completion", "chat", "code_review"
  duration_ms?: number;
  error_type?: string;  // e.g., "rate_limit", "auth_error", "network_error"
  // NO prompts, completions, API keys, or file paths
}
```

---

## 5.5 Compliance Requirements

| ID | Category | Requirement | Implementation |
|----|----------|-------------|----------------|
| **COMP-001** | Privacy | GDPR compliance for telemetry | Opt-in telemetry; data minimization; no PII |
| **COMP-002** | Data Residency | Customer data never transits vendor infrastructure | Extension communicates directly with customer's provider |
| **COMP-003** | Credential Management | Support enterprise credential management policies | SecretStorage API integration; SSO support |

### Internationalization (i18n)

| ID | Requirement | Target | Notes |
|----|-------------|--------|-------|
| **I18N-001** | Framework | Use i18n framework (e.g., `vscode-nls`, Eclipse NLS) with externalized strings | Resource bundles; no hardcoded strings |
| **I18N-002** | English v1 | Ship with English (en-US) locale in v1; message keys follow convention `extension.category.message` | Localization-ready architecture; future locales in v1.1+ |

### Platform Compatibility

| Platform | Requirement | Target |
|----------|-------------|--------|
| **VS Code** | Support latest 3 major versions | CI test matrix |
| **Eclipse** | Support latest 2 major versions | CI test matrix |
| **OS** | Windows 10+, macOS 11+, Ubuntu 20.04+, RHEL 8+ | CI test matrix |
| **Architecture** | x64 and ARM64 | Binary compatibility |

### Configuration Compatibility

| Requirement | Target | Verification |
|-------------|--------|-------------|
| **Schema Versioning** | Automatic migration of deprecated settings | Unit tests |
| **Backward Compatibility** | Support settings from previous 2 major versions | Integration tests |

---

## Non-Functional Requirement Summary

### By Priority

**Must Have:**

- Extension activation < 2 seconds (PERF-007)
- Memory footprint < 100MB (PERF-006)
- Time to first token < 500ms (PERF-002)
- HTTPS for all provider communication (SEC-001)
- Keyboard-only operation (A11Y-001)
- Screen reader status announcements (A11Y-002)
- Opt-in telemetry (TELEM-001)

**Should Have:**

- CPU usage < 5% idle, < 20% active (PERF-004, PERF-005)
- Bundle size < 10MB VS Code, < 15MB Eclipse (PERF-003)
- Extension overhead < 50ms (PERF-001)
- High contrast theme support (A11Y-004)
- 200% zoom support (A11Y-005)

**Could Have:**

- Advanced telemetry analytics dashboard
- Performance optimization for large workspaces
- Additional locale support (i18n expansion)

---

[← Previous](04-external-interfaces.md) | [Back to main](../ai-client-srs.md) | [Next →](06-other-requirements.md)
