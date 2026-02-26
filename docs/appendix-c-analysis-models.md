# Appendix C: Analysis Models

This appendix contains all system architecture diagrams, data flow models, and visual representations extracted from the requirements specification.

---

## C.1 Deployment Model

This diagram illustrates the high-level deployment context where the extension runs on developer workstations and communicates directly with customer-configured AI providers.

```mermaid
graph TD
    subgraph WORKSTATION["Developer Workstation (Windows / macOS / Linux)"]
        subgraph IDE["IDE"]
            subgraph EXT["Our Extension / Plugin"]
                CONFIG["Configuration<br/>(JSON / YAML)<br/>─────────────<br/>• Provider URL<br/>• API Key ref<br/>• Model mapping"]
                FEATURES["AI Features<br/>─────────────<br/>• Code generation<br/>• Text generation<br/>• Structured output<br/>• Function calling<br/>• Image generation"]
                CONFIG -->|drives| FEATURES
            end
        end
    end

    FEATURES -->|HTTPS · OpenAI API| PROVIDER["Customer's AI Provider<br/>─────────────<br/>• Azure OpenAI Service<br/>• OpenAI API<br/>• Enterprise AI Gateway<br/>• Other OpenAI-compatible service"]
```

**Context:** This "zero-infrastructure" evaluation path enables prospects to go from installation to first AI interaction in minutes, not weeks—removing a common deal blocker in enterprise sales cycles.

---

## C.2 Data Flow Architecture

This diagram shows how data flows through the extension, with credentials stored securely in OS-level credential stores and all AI traffic going directly to the customer's provider.

```mermaid
graph TD
    subgraph WORKSTATION["Developer Workstation"]
        subgraph IDE["IDE"]
            subgraph EXT["Our Extension"]
                STEP1["1. Read config<br/>(settings.json / preferences)"]
                STEP2["2. Retrieve API key<br/>(keychain / env var / config)"]
                STEP3["3. Send request to<br/>configured provider"]
                STEP4["4. Stream response<br/>to IDE"]
                STEP1 --> STEP2 --> STEP3 --> STEP4
            end
        end
        CRED["OS Credential Store<br/>─────────────<br/>macOS Keychain ·<br/>Windows Credential Manager ·<br/>Linux Secret Service"]
        EXT <-.->|API Key stored securely| CRED
    end

    EXT -->|HTTPS| PROVIDER["Customer's AI Provider<br/>─────────────<br/>• Azure OpenAI<br/>• OpenAI API<br/>• Enterprise AI Gateway<br/>(Customer's subscription)"]
```

**Security**: The vendor (us) never sees customer prompts, completions, or API keys. All data flows directly between the developer's workstation and their configured provider.

---

## C.3 Component Overview

This diagram illustrates the internal architecture of the extension, showing the key components and their interactions.

```mermaid
graph TD
    subgraph WORKSTATION["Developer Workstation (Windows / macOS / Linux)"]
        subgraph IDE["IDE (VS Code / Eclipse)"]
            subgraph EXT["Our Extension"]
                CM["Config Manager<br/>──────────<br/>• Load settings<br/>• Merge configs<br/>• Validate"]
                AI["AI Service Client<br/>──────────<br/>• HTTP client<br/>• SSE streaming<br/>• Retry logic"]
                CH["Credential Helper<br/>──────────<br/>• SecretStorage<br/>• OS keychain<br/>• Env vars"]
            end
            SETTINGS["settings.json<br/>(VS Code) /<br/>preferences (Eclipse)"]
            NETWORK["Network<br/>(HTTPS)"]
            CREDSTORE["OS Credential Store<br/>(Keychain / Cred Manager)"]
            CM --> SETTINGS
            AI --> NETWORK
            CH --> CREDSTORE
        end
    end

    NETWORK -->|HTTPS · OpenAI API format| PROVIDER["Customer's AI Provider<br/>──────────<br/>A: Azure OpenAI<br/>B: OpenAI API<br/>C: Enterprise AI Gateway"]
```

**Key Components:**
- **Config Manager**: Loads, merges, and validates configuration from settings files
- **AI Service Client**: Universal LLM Client implementing OpenAI-compatible wire protocol with streaming and retry logic
- **Credential Helper**: Manages API key retrieval from SecretStorage, OS keystores, or environment variables

---

## C.4 Request Flow Sequence

This sequence diagram shows the complete flow of a typical AI request, from user invocation through streaming response display.

```mermaid
sequenceDiagram
    participant Dev as Developer
    participant IDE as IDE + Our Extension
    participant Cred as OS Credential Store
    participant Provider as AI Provider

    Dev->>IDE: Trigger AI feature
    IDE->>IDE: Load configuration (settings.json)
    IDE->>Cred: Get API key
    Cred-->>IDE: Return API key
    
    IDE->>Provider: POST /v1/chat/completions
    Note right of IDE: model, messages, tools, etc.
    
    Provider-->>IDE: Stream tokens (SSE)
    IDE-->>Dev: Display AI response
```

**Flow Details:**
1. Developer triggers an AI feature (e.g., code generation, chat)
2. Extension loads configuration from settings
3. Extension retrieves API key from secure storage
4. Extension sends HTTPS request to configured provider
5. Provider streams response tokens via Server-Sent Events
6. Extension displays streaming response in IDE UI

---

## C.5 Configuration Hierarchy

This diagram illustrates the multi-level configuration system, showing how settings are merged with precedence rules.

```mermaid
flowchart TB
  L4["4 · User Override (if permitted) — ~/.vscode/settings.json — Highest priority"]
  L3["3 · Workspace Settings — .vscode/settings.json in project"]
  L2["2 · Managed Configuration Profile (v1.1) — Deployed by IT via GPO / MDM"]
  L1["1 · Extension Defaults — Built into extension — Lowest priority"]

  L4 --> L3 --> L2 --> L1
```

**Configuration Precedence:**
- **Level 4** (Highest): User-specific overrides in global settings
- **Level 3**: Workspace-specific settings (project-level)
- **Level 2**: Managed configuration deployed by IT (v1.1 feature)
- **Level 1** (Lowest): Built-in extension defaults

**Note**: In v1.0, levels 1, 3, and 4 are implemented. Level 2 (managed configuration) is deferred to v1.1.

---

## C.6 Enterprise AI Gateway Pattern

This diagram shows the optional enterprise AI gateway pattern, where customers deploy a central gateway for governance and observability.

```mermaid
graph LR
    subgraph WS["Developer Workstation"]
        EXT["IDE + Extension<br/>(base_url → gateway)"]
    end

    subgraph ENT["Enterprise Infrastructure"]
        GW["Enterprise AI Gateway<br/>(Kong / Apigee / custom)<br/>──────────<br/>• Rate limiting<br/>• Audit logging<br/>• Credential injection"]
        PROVIDER["Azure OpenAI / OpenAI"]
        GW --> PROVIDER
    end

    EXT -->|HTTPS| GW
```

**Enterprise Gateway Benefits:**
- **Rate limiting**: Enforce usage quotas across organization
- **Audit logging**: Complete request/response logging for compliance
- **Credential injection**: Centralized credential management
- **Policy enforcement**: Content filtering, model selection policies
- **Cost tracking**: Charge-back to business units

**Zero-Code-Change Transition**: Moving from direct SaaS access to enterprise gateway requires only changing the `base_url` configuration—no code changes to the extension.

---

## C.7 Eclipse Preferences UI Structure

This diagram shows the hierarchical structure of the Eclipse preferences UI for AI configuration.

```mermaid
graph TD
    PREFS["Preferences"] --> PROD["Our Product"]
    PROD --> AI["AI Services"]
    AI --> PROV["Provider<br/>──────────<br/>Type: Azure OpenAI ▼<br/>Base URL: ___<br/>API Version: 2024-02-15-preview<br/>Default Model: gpt-4-turbo"]
    AI --> CRED["Credentials<br/>──────────<br/>Source: ● Secure Storage<br/>○ Environment Variable<br/>[Store API Key…]"]
    AI --> MODELS["Models<br/>──────────<br/>Table: Alias → Provider Model ID"]
    AI --> NET["Network<br/>──────────<br/>✓ Use System Proxy<br/>Custom CA Certificate: Browse…"]
```

**UI Organization:**
- **Provider**: Base configuration (endpoint, type, auth mode)
- **Credentials**: API key source and storage options
- **Models**: Model aliasing table (friendly name → provider model ID)
- **Network**: Proxy and certificate configuration

---

## C.8 Error Handling & Retry Strategy

This flowchart shows the extension's retry logic for transient errors.

```mermaid
flowchart TD
    FAIL["Request Failed"] --> RETRYABLE{"Retryable error?<br/>(429, 5xx, timeout)"}
    RETRYABLE -->|No| SHOW_ERR["Show error to user"]
    RETRYABLE -->|Yes| CHECK{"Retries < 3?"}
    CHECK -->|No| FINAL_ERR["Show final error to user"]
    CHECK -->|Yes| WAIT["Wait (exponential backoff)<br/>1 s → 2 s → 4 s"]
    WAIT --> RETRY["Retry request"]
    RETRY --> RETRYABLE
```

**Retry Policy:**
- **Retryable errors**: HTTP 429 (rate limit), 5xx (server error), network timeout
- **Non-retryable errors**: HTTP 401 (auth), 403 (forbidden), 400 (bad request)
- **Max retries**: 3 attempts
- **Backoff strategy**: Exponential (1s, 2s, 4s)
- **Respect Provider Signals**: Honor `Retry-After` header if present

**Error Sanitization**: Provider error messages are sanitized before display to remove internal URLs, resource identifiers, and API key patterns (REQ-UX-009).

---

## C.9 Model Context Protocol (MCP) Tool Execution Flow

This diagram illustrates the dual MCP role architecture: MCP Server registration for external consumers + internal tool-call orchestration loop.

```mermaid
sequenceDiagram
    participant Model as Cloud Model<br/>(GPT-4, Claude)
    participant Ext as Extension<br/>(Tool Orchestrator)
    participant Tools as Local Tools<br/>(VS Code API)
    participant External as External MCP Host<br/>(e.g., GitHub Copilot)

    Note over Ext: Extension registers as MCP Server on startup
    External->>Ext: Discover MCP tools
    Ext-->>External: Return tool catalog (search_codebase, etc.)
    
    Note over Model,Tools: Internal tool-call loop (model-driven)
    Model->>Ext: chat/completions + tools array
    Ext->>Model: Response with tool_calls
    Ext->>Tools: Execute tool (direct function call, not MCP protocol)
    Tools-->>Ext: Return result
    Ext->>Model: chat/completions + tool role message
    Model-->>Ext: Final text response
```

**Key Points:**
- **Dual Role**: Extension is both MCP Server (for external hosts) and tool-call orchestrator (for internal use)
- **Direct Execution**: Internal orchestrator uses direct function calls for performance, not MCP serialization
- **Stateless Execution**: Model is the planner, extension is the executor—no local agent runtime
- **Risk Classification**: Tools classified as `safe`, `read-only`, `write-only`, `destructive` with permission model

---

## C.10 Configuration Schema Migration

This table shows how configuration settings are migrated across major versions:

| Version | Schema Version | Migration Path | Deprecated Settings |
|---------|----------------|----------------|---------------------|
| v0.x | Legacy | N/A (pre-release) | N/A |
| v1.0 | 1.0 | Automatic from v0.x | `ai.apiKey` (moved to SecretStorage) |
| v1.1 | 1.1 | Supports v1.0 and v0.x | TBD |
| v2.0 | 2.0 | Supports v1.1 and v1.0 | TBD |

**Backward Compatibility**: Extension supports settings from previous 2 major versions with automatic migration and deprecation warnings.

---

## C.11 Thread ID & Event-Typed Streaming Model

This conceptual model shows the architectural hedges for future agent framework integration:

```
Conversation Session
├── thread_id: UUID v4 (in-memory correlation ID)
├── Streaming Layer (event-typed)
│   ├── Event: token (content: "Hello")
│   ├── Event: tool_call (function: search_codebase, args: {...})
│   ├── Event: tool_result (result: [...])
│   ├── Event: status (status: "Thinking...")
│   └── Event: error (error: "Rate limited")
└── ToolOrchestrator Interface (replaceable)
    ├── v1 Implementation: Iterative loop (Chat Completions tool_calls)
    └── Future: LangGraph orchestrator or agent endpoint
```

**Future-Proofing Goals:**
- **Modular orchestrator**: Behind interface for easy replacement
- **Thread IDs**: Maps to LangGraph thread concept for future state management
- **Typed events**: Extensible without breaking streaming contract
- **Multi-step UX**: UI prepared for complex agent workflows

---

[← Previous](appendix-b-glossary.md) | [Back to main](../ai-client-srs.md) | [Next →](api-patterns.md)
