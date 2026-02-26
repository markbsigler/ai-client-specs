# Verification and Validation

This section defines the User Acceptance Testing (UAT) plan that validates all requirements specified in this SRS. The following test cases must be passed to meet the **Definition of Done (DoD)**.

---

## Test Group 1: Extension Installation & Activation

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-1.1** | Install extension on VS Code (Windows) | Extension installs and activates without errors | Must |
| **UAT-1.2** | Install extension on VS Code (macOS) | Extension installs and activates without errors | Must |
| **UAT-1.3** | Install extension on VS Code (Linux) | Extension installs and activates without errors | Must |
| **UAT-1.4** | Install plugin in Eclipse | Plugin installs and activates without errors | Must |
| **UAT-1.5** | Extension activation with no configuration | Extension activates; shows "configure AI" prompt | Must |

---

## Test Group 2: Configuration

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-2.1** | Configure via VS Code settings UI | Settings saved; AI features become available | Must |
| **UAT-2.2** | Configure via `settings.json` directly | Settings parsed correctly; AI features work | Must |
| **UAT-2.3** | Workspace settings override user settings | Workspace `baseUrl` used over user `baseUrl` | Must |
| **UAT-2.4** | Invalid `baseUrl` format | Validation error shown; setting not accepted | Must |
| **UAT-2.5** | Model alias resolves to provider model | Request uses mapped `provider_id` | Must |

---

## Test Group 3: Credential Management

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-3.1** | Store API key in macOS Keychain | Key saved; retrieved on next use | Must |
| **UAT-3.2** | Store API key in Windows Credential Manager | Key saved; retrieved on next use | Must |
| **UAT-3.3** | Store API key via Linux Secret Service | Key saved; retrieved on next use | Must |
| **UAT-3.4** | Retrieve API key from environment variable | `OPENAI_API_KEY` env var used successfully | Must |
| **UAT-3.5** | No API key configured | User prompted to enter key; clear instructions shown | Must |
| **UAT-3.6** | Invalid API key | Clear error message; prompt to re-enter key | Must |

---

## Test Group 4: Provider Connectivity

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-4.1** | Connect to Azure OpenAI | AI request succeeds with correct `api-version` header | Must |
| **UAT-4.2** | Connect to OpenAI API | AI request succeeds | Must |
| **UAT-4.3** | Connect via enterprise gateway | AI request succeeds with custom headers | Should |
| **UAT-4.4** | "Test Connection" command | Shows success/failure with helpful message | Should |
| **UAT-4.5** | Connection via corporate proxy | Request routed through configured proxy | Should |

---

## Test Group 5: AI Features

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-5.1** | Code completion (text generation) | Streaming response displayed in editor | Must |
| **UAT-5.2** | Chat conversation | Multi-turn conversation works | Must |
| **UAT-5.3** | Function calling with `tools` parameter | Tool calls returned and handled | Must |
| **UAT-5.4** | Structured output (`response_format: json`) | Valid JSON response received | Must |
| **UAT-5.5** | Image generation (basic) | Image generated and displayed | Should |
| **UAT-5.6** | Streaming progress indicator | UI shows streaming in progress | Must |

---

## Test Group 6: Error Handling

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-6.1** | Provider returns 401 (unauthorized) | Clear "check API key" message | Must |
| **UAT-6.2** | Provider returns 429 (rate limited) | Automatic retry; success or clear message | Must |
| **UAT-6.3** | Provider returns 500 (server error) | Retry with backoff; eventual error message | Must |
| **UAT-6.4** | Network timeout | Clear timeout message with troubleshooting hint | Must |
| **UAT-6.5** | No network connectivity | "Check network connection" message | Must |

---

## Test Group 7: Privacy & Security

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-7.1** | Verify no telemetry without opt-in | Network capture shows no telemetry calls | Must |
| **UAT-7.2** | API key not in logs | Extension logs contain no API keys | Must |
| **UAT-7.3** | API key not in settings file (if keychain used) | `settings.json` contains no API key | Must |
| **UAT-7.4** | Prompts not persisted to disk | No prompt content in extension storage | Must |

---

## Test Group 8: Prompt Construction & Message Roles

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-8.1** | Construct messages with system + user roles | Request sent with correct message array | Must |
| **UAT-8.2** | Multi-turn with assistant role | Conversation context preserved correctly | Must |
| **UAT-8.3** | Token count estimation | Estimate within 10% of actual token usage | Should |
| **UAT-8.4** | Context truncation with priority | High-priority context retained; low-priority truncated | Should |
| **UAT-8.5** | Prompt template substitution | Variables correctly replaced in template | Should |

---

## Test Group 9: Structured Output

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-9.1** | Request with `response_format: json_object` | Valid JSON response received | Must |
| **UAT-9.2** | JSON response parsed to typed object | Response correctly typed; properties accessible | Must |
| **UAT-9.3** | Malformed JSON from provider | Graceful error with raw response for debugging | Must |
| **UAT-9.4** | Schema validation failure | Clear error indicating which field failed validation | Should |

---

## Test Group 10: Function Calling

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-10.1** | Define and send tools array | Tools included in request; accepted by provider | Must |
| **UAT-10.2** | Receive and parse tool_calls | Function name and arguments correctly parsed | Must |
| **UAT-10.3** | Send tool result back to model | Tool role message accepted; conversation continues | Must |
| **UAT-10.4** | Multi-step tool calling loop | Multiple tool calls handled until final response | Should |
| **UAT-10.5** | `tool_choice: required` forces function call | Model returns tool_call, not text response | Should |
| **UAT-10.6** | Parallel tool calls | Multiple simultaneous tool_calls handled correctly | Should |

---

## Test Group 11: Provider-Agnostic Interface

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-11.1** | Configure custom `BASE_URL` in Settings | Extension sends requests to configured endpoint | Must |
| **UAT-11.2** | Switch `BASE_URL` from OpenAI to enterprise gateway | Extension calls new endpoint with zero code changes | Must |
| **UAT-11.3** | Configure custom `MODEL_NAME` | Requests include configured model identifier | Must |
| **UAT-11.4** | No vendor-specific SDK imported | Extension source does not depend on `@openai/openai` or `@anthropic-ai/sdk` | Must |
| **UAT-11.5** | Custom headers passed through | Provider receives custom headers (e.g., `api-version`) as configured | Must |

---

## Test Group 12: BYOK / SecretStorage

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-12.1** | Store API key via "Set API Key" command | Key persisted in `SecretStorage`; confirmation shown | Must |
| **UAT-12.2** | API key injected into `Authorization` header | Outgoing request includes `Authorization: Bearer <key>` | Must |
| **UAT-12.3** | API key injected into `X-Api-Key` header | Outgoing request includes custom header with key from `SecretStorage` | Must |
| **UAT-12.4** | Key not present in `globalState` or settings | No API key found in `settings.json`, `globalState`, or `workspaceState` | Must |
| **UAT-12.5** | Key rotation via "Set API Key" | New key overwrites old; next request uses new key | Should |

---

## Test Group 13: MCP Agentic Capabilities

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-13.1** | Extension registers as MCP Server | `vscode.lm.registerMcpServerDefinitionProvider` called on activation | Must |
| **UAT-13.2** | MCP tool `search_codebase` exposed | Tool listed with correct JSON Schema parameters | Must |
| **UAT-13.3** | MCP tool `read_file_context` executed | Returns file contents for requested path and line range | Must |
| **UAT-13.4** | Model tool-call triggers local execution | Extension executes tool via VS Code API and returns result | Must |
| **UAT-13.5** | Invalid tool call handled gracefully | Error returned to model without crashing extension | Should |

---

## Test Group 14: Enterprise Graduation

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-14.1** | SSO login via `vscode.authentication` | Extension obtains bearer token from session; attaches to requests | Must |
| **UAT-14.2** | `X-Request-Id` header present on requests | All outgoing calls include a UUID v4 `X-Request-Id` header | Must |
| **UAT-14.3** | Proxy settings respected | Requests routed through VS Code / env var proxy configuration | Should |
| **UAT-14.4** | Switch from BYOK to SSO (zero code change) | Only `BASE_URL` and auth settings change; no extension code modified | Must |

---

## Test Group 15: Request Cancellation & Progress UX

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-15.1** | Cancel streaming request via Stop button | Request aborted; UI cleared; "Request cancelled" message shown | Must |
| **UAT-15.2** | Cancel via Escape key | Same behavior as Stop button | Should |
| **UAT-15.3** | Progress indicator during long request | Elapsed time shown; cancellable indicator visible | Should |
| **UAT-15.4** | Cancellation cleans up HTTP connection | No lingering connections after cancellation | Should |

---

## Test Group 16: Concurrent Requests & Multi-Provider

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-16.1** | Open two chat sessions simultaneously | Both sessions work independently without blocking | Must |
| **UAT-16.2** | Rapid-fire multiple requests | Requests queued; rate limits respected | Should |
| **UAT-16.3** | Configure multiple provider profiles | Profiles saved in settings correctly | Should |
| **UAT-16.4** | Switch active provider profile | New profile applied; subsequent requests use new provider | Should |

---

## Test Group 17: Context Window Overflow & Provider Capabilities

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-17.1** | Prompt exceeds 90% of context window | Warning shown before sending request | Should |
| **UAT-17.2** | Provider returns `context_length_exceeded` | Automatic truncation attempted; retry succeeds | Should |
| **UAT-17.3** | Truncation notification shown to user | User informed of context reduction; log shows removed messages | Should |
| **UAT-17.4** | Provider lacks vision support | Feature disabled gracefully; user notified | Should |
| **UAT-17.5** | Provider capability detection cached | `/v1/models` called once per session, not per request | Should |

---

## Test Group 18: Extension Lifecycle & Cleanup

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-18.1** | Reload extension during active request | Request cancelled; connections closed cleanly | Must |
| **UAT-18.2** | Deactivate extension | All event listeners disposed; no memory leaks | Must |
| **UAT-18.3** | IDE shutdown with active request | Request cancelled within 5s timeout | Should |
| **UAT-18.4** | Configuration schema migration (upgrade) | Old settings automatically migrated to new schema | Should |

---

## Test Group 19: Provider-Specific Compatibility

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-19.1** | Configure Ollama provider (type: ollama, authMode: none) | Connection succeeds; no auth header sent | Must |
| **UAT-19.2** | Ollama streaming response | Tokens stream correctly; UI updates incrementally | Must |
| **UAT-19.3** | Anthropic provider via OpenAI-compatible endpoint | Chat completions succeed; tool calling works | Must |
| **UAT-19.4** | OpenShift AI provider (KServe/vLLM backend) | Model list retrieved; completions succeed | Should |
| **UAT-19.5** | AWS Bedrock via OpenAI-compatible gateway | Requests routed correctly; responses parsed | Should |

---

## Test Group 20: Security Edge Cases

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-20.1** | Prompt injection via malicious HTML response | Response content-type validation fails; request rejected (REQ-API-006) | Must |
| **UAT-20.2** | SSO token expires during streaming request | Request fails gracefully; user prompted to re-authenticate | Must |
| **UAT-20.3** | SSO token refresh during active session | New token obtained transparently; request continues | Should |
| **UAT-20.4** | Custom CA certificate configured (corporate proxy) | HTTPS connection succeeds with corporate CA (REQ-CRED-003) | Must |
| **UAT-20.5** | CA certificate file missing or invalid | Clear error shown with CA setup instructions (REQ-CRED-005) | Should |
| **UAT-20.6** | API key deleted via "Delete API Key" command | Credential removed from SecretStorage; subsequent requests fail (REQ-CRED-012a) | Must |
| **UAT-20.7** | SecretStorage unavailable, OS stores unavailable | Persistent warning shown; env var fallback documented (REQ-CRED-007a) | Must |
| **UAT-20.8** | X-Request-Id header uniqueness | 1000 concurrent requests all have unique UUIDs (REQ-ENT-003) | Should |

---

## Test Group 21: Tool Execution Safety

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-21.1** | Tool-call loop exceeds maxLoopIterations (default 25) | Loop terminated; error returned to model (REQ-TOOL-007) | Must |
| **UAT-21.2** | Individual tool execution exceeds timeout (default 30s) | Tool cancelled; timeout error returned (REQ-TOOL-008) | Must |
| **UAT-21.3** | Destructive tool requires approval (REQ-TOOL-009) | User prompt shown before execution; requires confirmation | Must |
| **UAT-21.4** | Destructive tool in untrusted workspace | Tool execution blocked; read-only context only (REQ-ENT-004b) | Must |
| **UAT-21.5** | Tool result exceeds 10,000 characters | Result truncated with notice before sending to model (REQ-PROMPT-007) | Must |

---

## Test Group 22: Performance & NFR Validation

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-22.1** | Measure extension activation time | < 2 seconds from activation trigger to ready state | Must |
| **UAT-22.2** | Measure extension memory footprint (idle) | < 100MB in IDE memory profiler | Must |
| **UAT-22.3** | Measure CPU usage (idle with no requests) | < 5% average CPU usage over 5 minutes | Should |
| **UAT-22.4** | Measure CPU usage (active streaming) | < 20% average during 60s streaming response | Should |
| **UAT-22.5** | Measure time to first token (after provider responds) | < 500ms from SSE first byte to UI display | Must |
| **UAT-22.6** | Measure extension overhead (request latency) | < 50ms overhead excluding network/provider time | Should |
| **UAT-22.7** | Extension bundle size (VS Code) | < 10MB .vsix package size | Should |
| **UAT-22.8** | Extension bundle size (Eclipse) | < 15MB with dependencies | Should |
| **UAT-22.9** | Network timeout: connection establishment | Fails after 10 seconds (PERF-006) | Must |
| **UAT-22.10** | Network timeout: streaming read | Fails after 60 seconds inactivity (PERF-006) | Must |
| **UAT-22.11** | Network timeout: non-streaming read | Fails after 30 seconds (PERF-006) | Must |
| **UAT-22.12** | Response size limit enforcement | 1MB response truncated with warning (PERF-007) | Must |

---

## Test Group 23: Accessibility Compliance

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-23.1** | Keyboard-only navigation (Command Palette) | All AI commands accessible via keyboard (A11Y-001) | Must |
| **UAT-23.2** | Screen reader announces streaming status | "Thinking...", "Generating response...", "Response complete" announced (A11Y-002) | Must |
| **UAT-23.3** | Focus management during streaming | Focus predictable; status changes announced | Must |
| **UAT-23.4** | High contrast theme support | UI elements visible in high contrast mode | Should |
| **UAT-23.5** | Zoom level 200% (VS Code) | UI remains usable at 200% zoom | Should |

---

## Test Group 24: Telemetry & Observability

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-24.1** | Telemetry disabled by default | No network calls to telemetry endpoints without opt-in (SEC-004) | Must |
| **UAT-24.2** | Telemetry opt-in via settings UI | Setting enabled; events collected (TELEM-002) | Should |
| **UAT-24.3** | Telemetry event schema validation | Events match defined schema: ai.request.started, completed, failed, tool.executed (TELEM-001) | Should |
| **UAT-24.4** | Telemetry excludes PII | No prompts, API keys, file paths in telemetry payloads (TELEM-001) | Must |
| **UAT-24.5** | X-Request-Id in all LLM requests | UUID v4 header present in captured network traffic (REQ-ENT-003) | Must |

---

## Test Group 25: Internationalization Readiness

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-25.1** | English (en-US) locale default | All UI strings display correctly in English (I18N-002) | Must |
| **UAT-25.2** | Code inspection: externalized strings | All user-facing strings use i18n framework (I18N-001) | Should |
| **UAT-25.3** | Message key convention validation | Keys follow `extension.category.message` pattern (I18N-002) | Should |

---

## Test Group 26: Architectural Hedge Validation

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| **UAT-26.1** | ToolOrchestrator interface abstraction | Tool-call loop implementation behind interface/abstract class (REQ-ARCH-001) | Must |
| **UAT-26.2** | thread_id assignment on new conversations | Every conversation assigned UUID v4 thread_id (REQ-ARCH-002) | Must |
| **UAT-26.3** | Event-typed streaming layer | Streaming emits typed events (token, tool_call, tool_result, status, error) not raw strings (REQ-ARCH-003) | Must |
| **UAT-26.4** | Multi-step UI progress display | UI shows step-by-step tool-call progress, not single progress bar (REQ-ARCH-004) | Should |

---

## Test Coverage Summary

### Requirements Coverage

| Requirement Category | Total Requirements | Covered by UAT | Coverage % |
|---------------------|-------------------|----------------|------------|
| Configuration (CFG) | 6 | 6 | 100% |
| Credentials (CRED) | 11 | 11 | 100% |
| API (API) | 8 | 8 | 100% |
| Provider (PROV) | 11 | 11 | 100% |
| UX (UX) | 10 | 10 | 100% |
| Prompt Engineering (PROMPT) | 8 | 8 | 100% |
| JSON/Structured Output (JSON) | 4 | 4 | 100% |
| Tool Calling (TOOL) | 10 | 10 | 100% |
| MCP (MCP) | 6 | 6 | 100% |
| Enterprise (ENT) | 6 | 6 | 100% |
| Lifecycle (LIFE) | 3 | 3 | 100% |
| Architecture (ARCH) | 16 | 16 | 100% |
| **Total Functional** | **99** | **99** | **100%** |
| **Non-Functional (NFRs)** | **26** | **26** | **100%** |

### Test Execution Plan

**Phase 1: Core Functionality** (UAT Groups 1-10)
- Focus: Installation, configuration, basic AI features, error handling
- Timeline: Week 1-2 of QA
- Pass criteria: 100% of "Must" priority tests pass

**Phase 2: Advanced Features** (UAT Groups 11-19)
- Focus: Provider compatibility, MCP, enterprise features, tool calling
- Timeline: Week 3-4 of QA
- Pass criteria: 95% of "Must" tests, 80% of "Should" tests pass

**Phase 3: Quality & Compliance** (UAT Groups 20-26)
- Focus: Security, performance, accessibility, i18n, architectural hedges
- Timeline: Week 5-6 of QA
- Pass criteria: 100% of security tests, 90% of NFR tests pass

---

[← Previous](api-patterns.md) | [Back to main](../ai-client-srs.md) | [Next →](document-control.md)
