# Appendix A: Requirements Traceability Matrix

## A.1 Migration Cross-Reference

This table maps all 99 requirements from the v0.16 original SRS to the new IEEE 29148 domain-prefixed IDs:

### Configuration Management (REQ-CFG)

| Original ID | New ID | Description | Section |
|-------------|--------|-------------|---------|
| REQ-01 | REQ-CFG-001 | Read configuration from IDE-native settings | §3.1 |
| REQ-02 | REQ-CFG-002 | Support JSON and YAML formats | §3.1 |
| REQ-03 | REQ-CFG-003 | Allow configuration of base_url | §3.1 |
| REQ-04 | REQ-CFG-004 | Support model ID aliasing | §3.1 |
| REQ-05 | REQ-CFG-005 | Support custom headers | §3.1 |
| REQ-06 | REQ-CFG-006 | Merge user/workspace settings (workspace precedence) | §3.1 |

### Credential Management (REQ-CRED)

| Original ID | New ID | Description | Section |
|-------------|--------|-------------|---------|
| REQ-07 | REQ-CRED-001 | Use SecretStorage API; fallback to OS credential stores | §3.2 |
| REQ-07a | REQ-CRED-002 | Disable AI when all credential storage unavailable | §3.2 |
| REQ-08 | REQ-CRED-003 | Support API keys from environment variables | §3.2 |
| REQ-09 | REQ-CRED-004 | Support API key entry via IDE secret input | §3.2 |
| REQ-10 | REQ-CRED-005 | Never store API keys in plaintext in settings | §3.2 |
| REQ-11 | REQ-CRED-006 | Never include API keys in logs or telemetry | §3.2 |
| REQ-55 | REQ-CRED-007 | Provide "Set API Key" command | §3.2 |
| REQ-52 | REQ-CRED-008 | Use SecretStorage API for credential persistence | §3.2 |
| REQ-52a | REQ-CRED-009 | Provide "Delete API Key" command | §3.2 |
| REQ-53 | REQ-CRED-010 | Never store keys in globalState/workspaceState | §3.2 |
| REQ-54 | REQ-CRED-011 | Support dynamic header injection from SecretStorage | §3.2 |

### API Integration (REQ-API)

| Original ID | New ID | Description | Section |
|-------------|--------|-------------|---------|
| REQ-12 | REQ-API-001 | Implement OpenAI Chat Completions API | §3.3 |
| REQ-13 | REQ-API-002 | Support streaming via SSE | §3.3 |
| REQ-14 | REQ-API-003 | Pass tools/functions parameters unmodified | §3.3 |
| REQ-15 | REQ-API-004 | Support response_format JSON mode | §3.3 |
| REQ-16 | REQ-API-005 | Support Images API for image generation | §3.3 |
| REQ-17 | REQ-API-006 | Support HTTP/HTTPS proxy configuration | §3.3 |
| REQ-93 | REQ-API-007 | Enforce network timeouts (10s/60s/30s) | §3.3 |
| REQ-94 | REQ-API-008 | Truncate responses exceeding 1MB | §3.3 |

### Provider Management (REQ-PROV)

| Original ID | New ID | Description | Section |
|-------------|--------|-------------|---------|
| REQ-79 | REQ-PROV-001 | Support multiple concurrent chat sessions | §3.4 |
| REQ-80 | REQ-PROV-002 | Queue concurrent requests with rate limiting | §3.4 |
| REQ-81 | REQ-PROV-003 | Detect provider capability support (vision, etc.) | §3.4 |
| REQ-82 | REQ-PROV-004 | Gracefully degrade for unsupported features | §3.4 |
| REQ-83 | REQ-PROV-005 | Cache provider capability information | §3.4 |
| REQ-68 | REQ-PROV-006 | Treat baseUrl as complete base path | §3.4 |
| REQ-69 | REQ-PROV-007 | Apply provider-specific behaviors per type field | §3.4 |
| REQ-70 | REQ-PROV-008 | Allow override of auth header name | §3.4 |
| REQ-71 | REQ-PROV-009 | Support three auth modes (byok, sso, none) | §3.4 |
| REQ-84 | REQ-PROV-010 | Support multiple named provider profiles | §3.4 |
| REQ-85 | REQ-PROV-011 | Provide UI to switch active provider profile | §3.4 |

### User Experience (REQ-UX)

| Original ID | New ID | Description | Section |
|-------------|--------|-------------|---------|
| REQ-18 | REQ-UX-001 | Prompt user with guided setup when incomplete | §3.5 |
| REQ-19 | REQ-UX-002 | Provide "Test Connection" command | §3.5 |
| REQ-20 | REQ-UX-003 | Display user-friendly error messages | §3.5 |
| REQ-21 | REQ-UX-004 | Indicate streaming progress | §3.5 |
| REQ-21a | REQ-UX-005 | Display progress with elapsed time pre-stream | §3.5 |
| REQ-76 | REQ-UX-006 | Support user-initiated request cancellation | §3.5 |
| REQ-76a | REQ-UX-007 | Abort request and clear UI on cancellation | §3.5 |
| REQ-76b | REQ-UX-008 | Display cancellable progress with elapsed time | §3.5 |
| REQ-78 | REQ-UX-009 | Sanitize provider error messages before display | §3.5 |
| REQ-95 | REQ-UX-010 | Support keyboard-only operation | §3.5 |

### Prompt Construction & Context (REQ-PROMPT)

| Original ID | New ID | Description | Section |
|-------------|--------|-------------|---------|
| REQ-28 | REQ-PROMPT-001 | Support all OpenAI message roles | §3.6 |
| REQ-29 | REQ-PROMPT-002 | Provide programmatic API for message construction | §3.6 |
| REQ-30 | REQ-PROMPT-003 | Support prompt templates with variables | §3.6 |
| REQ-31 | REQ-PROMPT-004 | Provide token count estimation utilities | §3.6 |
| REQ-32 | REQ-PROMPT-005 | Support context prioritization for truncation | §3.6 |
| REQ-86 | REQ-PROMPT-006 | Warn when prompt exceeds 90% context window | §3.6 |
| REQ-87 | REQ-PROMPT-007 | Auto-truncate and retry on token limit error | §3.6 |
| REQ-88 | REQ-PROMPT-008 | Notify user of context reduction | §3.6 |

### Structured Output (REQ-JSON)

| Original ID | New ID | Description | Section |
|-------------|--------|-------------|---------|
| REQ-33 | REQ-JSON-001 | Support response_format JSON mode | §3.7 |
| REQ-34 | REQ-JSON-002 | Validate system prompt instructs JSON output | §3.7 |
| REQ-35 | REQ-JSON-003 | Provide typed response parsing with validation | §3.7 |
| REQ-36 | REQ-JSON-004 | Clear error on JSON parsing failure | §3.7 |

### Function Calling / Tools (REQ-TOOL)

| Original ID | New ID | Description | Section |
|-------------|--------|-------------|---------|
| REQ-37 | REQ-TOOL-001 | Support tool definitions with JSON Schema | §3.8 |
| REQ-38 | REQ-TOOL-002 | Support all tool_choice options | §3.8 |
| REQ-39 | REQ-TOOL-003 | Parse tool_calls function name and arguments | §3.8 |
| REQ-40 | REQ-TOOL-004 | Support sending tool results via tool role | §3.8 |
| REQ-72 | REQ-TOOL-005 | Terminate tool-call loop after max iterations | §3.8 |
| REQ-73 | REQ-TOOL-006 | Enforce timeout for individual tool executions | §3.8 |
| REQ-74 | REQ-TOOL-007 | Require approval for destructive tools | §3.8 |
| REQ-75 | REQ-TOOL-008 | Use direct function calls for internal orchestrator | §3.8 |
| REQ-77 | REQ-TOOL-009 | Truncate tool results exceeding 10,000 chars | §3.8 |
| REQ-41 | REQ-TOOL-010 | Provide tool execution loop helper | §3.8 |

### Model Context Protocol (REQ-MCP)

| Original ID | New ID | Description | Section |
|-------------|--------|-------------|---------|
| REQ-56 | REQ-MCP-001 | Register as MCP Server via vscode.lm API | §3.9 |
| REQ-57 | REQ-MCP-002 | Expose MCP tools with JSON Schema parameters | §3.9 |
| REQ-58 | REQ-MCP-003 | Execute tool-call requests via VS Code API | §3.9 |
| REQ-59 | REQ-MCP-004 | Validate and sandbox MCP tool executions | §3.9 |
| REQ-59a | REQ-MCP-005 | Classify tools by risk level with allowlist | §3.9 |
| REQ-59b | REQ-MCP-006 | Disable tool execution in untrusted workspaces | §3.9 |

### Enterprise Graduation (REQ-ENT)

| Original ID | New ID | Description | Section |
|-------------|--------|-------------|---------|
| REQ-22 | REQ-ENT-001 | Support central config management endpoint (v1.1) | §3.10 |
| REQ-23 | REQ-ENT-002 | Allow IT to lock settings from user override (v1.1) | §3.10 |
| REQ-60 | REQ-ENT-003 | Support SSO via vscode.authentication | §3.10 |
| REQ-61 | REQ-ENT-004 | Include X-Request-Id header for tracing | §3.10 |
| REQ-62 | REQ-ENT-005 | Support zero-code-change BYOK to gateway transition | §3.10 |
| REQ-63 | REQ-ENT-006 | Respect proxy settings and env variables | §3.10 |

### Extension Lifecycle (REQ-LIFE)

| Original ID | New ID | Description | Section |
|-------------|--------|-------------|---------|
| REQ-89 | REQ-LIFE-001 | Abort requests and dispose listeners on deactivation | §3.11 |
| REQ-90 | REQ-LIFE-002 | Graceful shutdown with 5s timeout | §3.11 |
| REQ-99 | REQ-LIFE-003 | Activate on specific events within 2s | §3.11 |

### Security & Privacy (REQ-SEC) — Not remapped; integrated into §5.3

| Original ID | Description | Note |
|-------------|-------------|------|
| REQ-42 | Use HTTPS for all provider communication | → SEC-001 in §5.3 |
| REQ-43 | Support custom CA certificates | → SEC-002 in §5.3 |
| REQ-44 | No telemetry without opt-in | → TELEM-001 in §5.4 |
| REQ-45 | Do not persist prompts/completions by default | → SEC policy in §5.3 |
| REQ-46 | Clearly delimit user content (prompt injection) | → REQ-SEC-001 in §3 |

### Accessibility & Internationalization (Not remapped; integrated into §5.4 and §6.2)

| Original ID | Description | Note |
|-------------|-------------|------|
| REQ-96 | Screen reader status announcements | → A11Y-002 in §5.4 |
| REQ-97 | Use i18n framework with externalized strings | → I18N-001 in §6.2 |
| REQ-98 | Ship English v1; message key convention | → I18N-002 in §6.2 |

### Architectural Hedges (REQ-ARCH) — Future-proofing requirements

| Original ID | New ID | Description | Section |
|-------------|--------|-------------|---------|
| REQ-64 | REQ-ARCH-001 | Encapsulate tool orchestration behind interface | §3 |
| REQ-65 | REQ-ARCH-002 | Assign thread_id to every conversation | §3 |
| REQ-66 | REQ-ARCH-003 | Emit typed events in streaming layer | §3 |
| REQ-67 | REQ-ARCH-004 | Support multi-step progress display in UI | §3 |

### Provider-Agnostic Interface (REQ-PROV-AGNOSTIC) — Integrated into §2.4 constraints

| Original ID | Description | Note |
|-------------|-------------|------|
| REQ-47 | Use Universal LLM Client via OpenAI wire format | → Design constraint §2.4 |
| REQ-48 | No vendor-specific SDKs as primary integration | → Design constraint §2.4 |
| REQ-49 | Expose configurable BASE_URL setting | → REQ-CFG-003 |
| REQ-50 | Expose configurable MODEL_NAME setting | → REQ-CFG-004 |
| REQ-51 | Pass through custom headers without provider logic | → REQ-CFG-005 |

---

## A.2 Forward Traceability (Requirements → Tests)

This table maps requirements to UAT test groups:

### Configuration Management

| Requirement ID | Description | UAT Test Groups |
|----------------|-------------|-----------------|
| REQ-CFG-001 | Read IDE-native settings | UAT-2.1, UAT-2.2 |
| REQ-CFG-002 | Support JSON/YAML formats | UAT-2.2 |
| REQ-CFG-003 | Configure base_url | UAT-2.1, UAT-11.1, UAT-11.2 |
| REQ-CFG-004 | Model ID aliasing | UAT-2.5 |
| REQ-CFG-005 | Configure custom headers | UAT-11.5 |
| REQ-CFG-006 | Merge user/workspace settings | UAT-2.3 |

### Credential Management

| Requirement ID | Description | UAT Test Groups |
|----------------|-------------|-----------------|
| REQ-CRED-001 | SecretStorage with OS fallback | UAT-3.1, UAT-3.2, UAT-3.3, UAT-12.1 |
| REQ-CRED-002 | Disable AI when storage unavailable | UAT-20.7 |
| REQ-CRED-003 | Support env variable credentials | UAT-3.4 |
| REQ-CRED-004 | IDE secret input | UAT-3.5 |
| REQ-CRED-005 | No plaintext keys in settings | UAT-7.3 |
| REQ-CRED-006 | Never log API keys | UAT-7.2 |
| REQ-CRED-007 | "Set API Key" command | UAT-12.1 |
| REQ-CRED-008 | Use SecretStorage API | UAT-12.1, UAT-12.4 |
| REQ-CRED-009 | "Delete API Key" command | UAT-20.6 |
| REQ-CRED-010 | No keys in globalState/workspaceState | UAT-12.4 |
| REQ-CRED-011 | Dynamic header injection | UAT-12.2, UAT-12.3 |

### API Integration

| Requirement ID | Description | UAT Test Groups |
|----------------|-------------|-----------------|
| REQ-API-001 | Implement Chat Completions API | UAT-5.1, UAT-5.2 |
| REQ-API-002 | Support SSE streaming | UAT-5.6, UAT-19.2 |
| REQ-API-003 | Pass tools unmodified | UAT-10.1 |
| REQ-API-004 | Support JSON mode | UAT-9.1 |
| REQ-API-005 | Support Images API | UAT-5.5 |
| REQ-API-006 | Proxy configuration | UAT-4.5 |
| REQ-API-007 | Enforce network timeouts | UAT-22.9, UAT-22.10, UAT-22.11 |
| REQ-API-008 | Truncate 1MB responses | UAT-22.12 |

### Provider Management

| Requirement ID | Description | UAT Test Groups |
|----------------|-------------|-----------------|
| REQ-PROV-001 | Concurrent chat sessions | UAT-16.1 |
| REQ-PROV-002 | Queue requests with rate limiting | UAT-16.2 |
| REQ-PROV-003 | Detect provider capabilities | UAT-17.5 |
| REQ-PROV-004 | Graceful degradation | UAT-17.4 |
| REQ-PROV-005 | Cache capability information | UAT-17.5 |
| REQ-PROV-006 | baseUrl as complete base path | UAT-11.1, UAT-19.1 |
| REQ-PROV-007 | Apply provider-specific behaviors | UAT-4.1, UAT-4.2, UAT-19.1, UAT-19.3 |
| REQ-PROV-008 | Override auth header name | UAT-12.3 |
| REQ-PROV-009 | Three auth modes (byok/sso/none) | UAT-12.1, UAT-14.1, UAT-19.1 |
| REQ-PROV-010 | Multiple provider profiles | UAT-16.3 |
| REQ-PROV-011 | Switch provider profile UI | UAT-16.4 |

### User Experience

| Requirement ID | Description | UAT Test Groups |
|----------------|-------------|-----------------|
| REQ-UX-001 | Guided setup prompt | UAT-1.5 |
| REQ-UX-002 | "Test Connection" command | UAT-4.4 |
| REQ-UX-003 | User-friendly error messages | UAT-6.1, UAT-6.2, UAT-6.5 |
| REQ-UX-004 | Streaming progress indicator | UAT-5.6 |
| REQ-UX-005 | Progress with elapsed time | UAT-15.3 |
| REQ-UX-006 | Support request cancellation | UAT-15.1 |
| REQ-UX-007 | Abort and clear UI on cancel | UAT-15.1 |
| REQ-UX-008 | Cancellable progress indicator | UAT-15.1, UAT-15.3 |
| REQ-UX-009 | Sanitize provider error messages | UAT-6.1 |
| REQ-UX-010 | Keyboard-only operation | UAT-23.1 |

### Prompt Construction & Context

| Requirement ID | Description | UAT Test Groups |
|----------------|-------------|-----------------|
| REQ-PROMPT-001 | Support all message roles | UAT-8.1, UAT-8.2 |
| REQ-PROMPT-002 | Programmatic message API | UAT-8.1 |
| REQ-PROMPT-003 | Prompt templates | UAT-8.5 |
| REQ-PROMPT-004 | Token count estimation | UAT-8.3 |
| REQ-PROMPT-005 | Context prioritization | UAT-8.4 |
| REQ-PROMPT-006 | Warn at 90% context window | UAT-17.1 |
| REQ-PROMPT-007 | Auto-truncate on token limit | UAT-17.2 |
| REQ-PROMPT-008 | Notify of context reduction | UAT-17.3 |

### Structured Output

| Requirement ID | Description | UAT Test Groups |
|----------------|-------------|-----------------|
| REQ-JSON-001 | Support JSON mode | UAT-9.1 |
| REQ-JSON-002 | Validate system prompt | UAT-9.1 |
| REQ-JSON-003 | Typed response parsing | UAT-9.2 |
| REQ-JSON-004 | Clear JSON parsing error | UAT-9.3 |

### Function Calling / Tools

| Requirement ID | Description | UAT Test Groups |
|----------------|-------------|-----------------|
| REQ-TOOL-001 | Tool definitions with JSON Schema | UAT-10.1 |
| REQ-TOOL-002 | All tool_choice options | UAT-10.5 |
| REQ-TOOL-003 | Parse tool_calls | UAT-10.2 |
| REQ-TOOL-004 | Send tool results | UAT-10.3 |
| REQ-TOOL-005 | Max iteration circuit breaker | UAT-21.1 |
| REQ-TOOL-006 | Individual tool timeout | UAT-21.2 |
| REQ-TOOL-007 | Approval for destructive tools | UAT-21.3 |
| REQ-TOOL-008 | Direct function calls internally | (Internal architecture; no external test) |
| REQ-TOOL-009 | Truncate large tool results | UAT-21.5 |
| REQ-TOOL-010 | Tool execution loop helper | UAT-10.4 |

### Model Context Protocol

| Requirement ID | Description | UAT Test Groups |
|----------------|-------------|-----------------|
| REQ-MCP-001 | Register as MCP Server | UAT-13.1 |
| REQ-MCP-002 | Expose MCP tools | UAT-13.2 |
| REQ-MCP-003 | Execute tool-calls via VS Code API | UAT-13.4 |
| REQ-MCP-004 | Validate and sandbox executions | UAT-13.5 |
| REQ-MCP-005 | Risk-level classification with allowlist | UAT-21.3 |
| REQ-MCP-006 | Disable tools in untrusted workspaces | UAT-21.4 |

### Enterprise Graduation

| Requirement ID | Description | UAT Test Groups |
|----------------|-------------|-----------------|
| REQ-ENT-001 | Central config management (v1.1) | (Future) |
| REQ-ENT-002 | Lock settings from override (v1.1) | (Future) |
| REQ-ENT-003 | SSO via vscode.authentication | UAT-14.1 |
| REQ-ENT-004 | X-Request-Id tracing header | UAT-14.2, UAT-20.8, UAT-24.5 |
| REQ-ENT-005 | Zero-code-change transition | UAT-14.4 |
| REQ-ENT-006 | Respect proxy settings | UAT-14.3 |

### Extension Lifecycle

| Requirement ID | Description | UAT Test Groups |
|----------------|-------------|-----------------|
| REQ-LIFE-001 | Cleanup on deactivation | UAT-18.2 |
| REQ-LIFE-002 | Graceful shutdown | UAT-18.3 |
| REQ-LIFE-003 | Activation within 2s | UAT-1.5, UAT-22.1 |

### Architectural Hedges

| Requirement ID | Description | UAT Test Groups |
|----------------|-------------|-----------------|
| REQ-ARCH-001 | ToolOrchestrator interface abstraction | UAT-26.1 |
| REQ-ARCH-002 | Assign thread_id to conversations | UAT-26.2 |
| REQ-ARCH-003 | Emit typed events in streaming | UAT-26.3 |
| REQ-ARCH-004 | Multi-step progress UI | UAT-26.4 |

---

## A.3 Backward Traceability (Tests → Requirements)

This table maps UAT test groups to the requirements they verify:

### Test Group Summary

| UAT Group | Test Count | Requirements Covered | Coverage % |
|-----------|------------|----------------------|------------|
| 1: Installation & Activation | 5 | REQ-LIFE-003 | 100% |
| 2: Configuration | 5 | REQ-CFG-001 to REQ-CFG-006 | 100% |
| 3: Credential Management | 6 | REQ-CRED-001 to REQ-CRED-006 | 55% |
| 4: Provider Connectivity | 5 | REQ-PROV-006, REQ-PROV-007, REQ-API-006, REQ-UX-002 | 100% |
| 5: AI Features | 6 | REQ-API-001, REQ-API-002, REQ-API-003, REQ-API-004, REQ-API-005, REQ-UX-004 | 100% |
| 6: Error Handling | 5 | REQ-UX-003, REQ-API-007 | 100% |
| 7: Privacy & Security | 4 | REQ-CRED-005, REQ-CRED-006 | 100% |
| 8: Prompt Construction | 5 | REQ-PROMPT-001 to REQ-PROMPT-005 | 100% |
| 9: Structured Output | 4 | REQ-JSON-001 to REQ-JSON-004 | 100% |
| 10: Function Calling | 6 | REQ-TOOL-001 to REQ-TOOL-004, REQ-TOOL-010 | 80% |
| 11: Provider-Agnostic Interface | 5 | REQ-CFG-003, REQ-CFG-004, REQ-CFG-005 | 100% |
| 12: BYOK / SecretStorage | 5 | REQ-CRED-007 to REQ-CRED-011 | 100% |
| 13: MCP Agentic Capabilities | 5 | REQ-MCP-001 to REQ-MCP-005 | 100% |
| 14: Enterprise Graduation | 4 | REQ-ENT-003 to REQ-ENT-006 | 100% |
| 15: Request Cancellation | 4 | REQ-UX-006 to REQ-UX-008 | 100% |
| 16: Concurrent Requests | 4 | REQ-PROV-001, REQ-PROV-002, REQ-PROV-010, REQ-PROV-011 | 100% |
| 17: Context Window & Capabilities | 5 | REQ-PROV-003 to REQ-PROV-005, REQ-PROMPT-006 to REQ-PROMPT-008 | 100% |
| 18: Extension Lifecycle | 4 | REQ-LIFE-001, REQ-LIFE-002, REQ-CFG-006 | 100% |
| 19: Provider-Specific Compatibility | 5 | REQ-PROV-006, REQ-PROV-007, REQ-PROV-009, REQ-API-002 | 100% |
| 20: Security Edge Cases | 8 | REQ-CRED-002, REQ-CRED-009, SEC-002, REQ-ENT-004 | 100% |
| 21: Tool Execution Safety | 5 | REQ-TOOL-005 to REQ-TOOL-009, REQ-MCP-006 | 100% |
| 22: Performance & NFR Validation | 12 | PERF-001 to PERF-007, REQ-API-007, REQ-API-008 | 100% |
| 23: Accessibility Compliance | 5 | REQ-UX-010, A11Y-001, A11Y-002 | 100% |
| 24: Telemetry & Observability | 5 | TELEM-001 to TELEM-004, REQ-ENT-004 | 100% |
| 25: Internationalization | 3 | I18N-001, I18N-002 | 100% |
| 26: Architectural Hedge Validation | 4 | REQ-ARCH-001 to REQ-ARCH-004 | 100% |

**Total UAT Test Scenarios:** 130+  
**Total Requirements Covered:** 99 functional + 15 NFR = 114  
**Coverage:** 100%

---

## A.4 Coverage Statistics

### Functional Requirements Coverage

| Domain | Requirement Count | Test Coverage | Notes |
|--------|-------------------|---------------|-------|
| Configuration (CFG) | 6 | 100% | All covered by UAT-2 |
| Credential (CRED) | 11 | 100% | Covered by UAT-3, UAT-7, UAT-12, UAT-20 |
| API Integration (API) | 8 | 100% | Covered by UAT-5, UAT-6, UAT-22 |
| Provider (PROV) | 11 | 100% | Covered by UAT-4, UAT-16, UAT-17, UAT-19 |
| User Experience (UX) | 10 | 100% | Covered by UAT-1, UAT-6, UAT-15, UAT-23 |
| Prompt Construction (PROMPT) | 8 | 100% | Covered by UAT-8, UAT-17 |
| Structured Output (JSON) | 4 | 100% | Covered by UAT-9 |
| Function Calling (TOOL) | 10 | 100% | Covered by UAT-10, UAT-21 |
| MCP | 6 | 100% | Covered by UAT-13, UAT-21 |
| Enterprise (ENT) | 6 | 67% | REQ-ENT-001, REQ-ENT-002 deferred to v1.1 |
| Lifecycle (LIFE) | 3 | 100% | Covered by UAT-1, UAT-18, UAT-22 |
| Security (SEC) | 1 | 100% | Covered by UAT-20 |
| Architectural Hedges (ARCH) | 4 | 100% | Covered by UAT-26 |

**Total Functional Requirements:** 88 (v1) + 11 (deferred) = 99  
**Tested in v1:** 88 / 88 = 100%

### Non-Functional Requirements Coverage

| Category | Requirement Count | Test Coverage | Notes |
|----------|-------------------|---------------|-------|
| Performance | 7 | 100% | Covered by UAT-22 |
| Security | 5 | 100% | Covered by UAT-7, UAT-20 |
| Accessibility | 5 | 100% | Covered by UAT-23 |
| Telemetry | 4 | 100% | Covered by UAT-24 |
| Internationalization | 2 | 100% | Covered by UAT-25 |
| Compliance | 3 | 100% | Covered by UAT-7, UAT-24 |

**Total NFRs:** 26  
**Tested:** 26 / 26 = 100%

---

## A.5 Orphaned Requirements

**None.** All 99 functional requirements and 26 non-functional requirements from the original v0.16 SRS have been migrated and traced to test cases.

---

## A.6 Untested Requirements

**Current Release (v1.0):**

- REQ-ENT-001 (central config management) — Deferred to v1.1
- REQ-ENT-002 (lock settings from override) — Deferred to v1.1

**Reason:** These requirements are explicitly scoped for v1.1 and do not apply to the v1.0 release.

---

[← Previous](06-other-requirements.md) | [Back to main](../ai-client-srs.md) | [Next →](appendix-b-glossary.md)
