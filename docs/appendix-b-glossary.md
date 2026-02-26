# Appendix B: Glossary

This glossary defines all technical terms, acronyms, and domain-specific concepts used throughout this specification.

| Term | Definition |
|------|------------|
| **IDE Extension** | Our plugin for VS Code or Eclipse that provides AI-powered developer features |
| **Provider** | The AI cloud service (Azure OpenAI, OpenAI, enterprise gateway) that processes requests |
| **OpenAI API** | REST API specification for LLM interactions; industry standard implemented by multiple providers |
| **Azure OpenAI** | Microsoft's Azure-hosted OpenAI service; common enterprise choice |
| **Enterprise Gateway** | Customer's internal API gateway that may proxy requests to AI providers |
| **base_url** | The endpoint URL for the AI provider (e.g., `https://api.openai.com/v1`) |
| **Model Alias** | User-friendly name (e.g., "fast") mapped to provider model ID (e.g., "gpt-3.5-turbo") |
| **SSE** | Server-Sent Events — HTTP streaming protocol for real-time token delivery |
| **Keychain** | OS-level secure credential storage (macOS Keychain, Windows Credential Manager) |
| **settings.json** | VS Code's JSON configuration file for user and workspace settings |
| **Message Role** | The role of a message in a conversation: `system`, `user`, `assistant`, or `tool` |
| **System Prompt** | Instructions defining the AI's behavior, persona, and constraints |
| **Prompt Template** | Reusable prompt structure with variable placeholders for programmatic use |
| **Function Calling** | OpenAI API feature allowing models to invoke defined functions/tools |
| **Tools** | Function definitions sent to the model describing callable operations |
| **tool_calls** | Model's response requesting execution of defined functions |
| **Structured Output** | OpenAI API feature for requesting JSON-formatted responses (`response_format`) |
| **JSON Mode** | Setting `response_format: { type: "json_object" }` to ensure valid JSON output |
| **Few-shot Prompting** | Including examples in the prompt to guide model output format |
| **Context Window** | Maximum tokens (input + output) a model can process in one request |
| **Token** | Basic unit of text processing; roughly 4 characters or 0.75 words in English |
| **EARS** | Easy Approach to Requirements Syntax — format for unambiguous requirements |
| **MoSCoW** | Prioritization framework: Must have, Should have, Could have, Won't have |
| **MCP** | Model Context Protocol — standard for AI tool integration; used for agentic capabilities via `vscode.lm` API |
| **MCP Server** | An extension or service that exposes tools and capabilities via the Model Context Protocol |
| **MCP Client / Host** | A consumer that discovers MCP tools and orchestrates their invocation; the extension acts as both MCP Server *and* a lightweight MCP Client for its own tool-call loop |
| **MCP Tool** | A capability exposed by an MCP Server (e.g., `search_codebase`, `read_file_context`) described with JSON Schema parameters |
| **Tool-Call Orchestrator** | The modular loop that sends tool definitions to the model, executes returned `tool_calls`, and repeats until a final text response — encapsulated behind a `ToolOrchestrator` interface for future replaceability |
| **thread_id** | UUID v4 assigned to each conversation or multi-turn interaction for correlation; maps to future agent framework thread concepts (e.g., LangGraph threads) |
| **Event-Typed Streaming** | Internal streaming architecture that emits typed events (`token`, `tool_call`, `tool_result`, `status`, `error`) rather than raw strings, enabling future extension without contract breakage |
| **LangGraph** | A Python-based agent framework by LangChain for stateful, graph-defined AI workflows; explicitly out of scope for v1 but architecture preserves future optionality |
| **Universal LLM Client** | The extension's provider-agnostic HTTP client that targets the OpenAI Chat Completions wire format without vendor SDKs |
| **SecretStorage** | VS Code API (`context.secrets`) for persisting sensitive data (e.g., API keys) in OS-level secure storage |
| **Header Injection** | Dynamic population of HTTP authentication headers from `SecretStorage` at request time |
| **BYOK** | Bring Your Own Key — users supply their own API key for direct SaaS access during evaluation |
| **Gateway Graduation** | Zero-code-change transition from direct SaaS (BYOK) to enterprise-governed AI Gateway access |
| **vscode.authentication** | VS Code API for SSO / OIDC / OAuth authentication flows used in enterprise gateway integration |
| **X-Request-Id** | UUID v4 header included in all outgoing LLM calls for end-to-end observability and tracing |
| **AI Gateway** | Enterprise-managed API gateway (e.g., Kong, Cloudflare AI Gateway) that governs LLM traffic |
| **Red Hat OpenShift AI** | Kubernetes-native AI/ML platform (part of Red Hat OpenShift) that provides model serving via KServe/vLLM with OpenAI-compatible inference endpoints |
| **Agents** | Autonomous AI systems that can take actions; v1 supports model-driven tool-call loops via MCP (no local agent runtime). Full agent frameworks (LangGraph, etc.) deferred to v2+ |
| **IEEE 29148** | ISO/IEC/IEEE 29148:2018 — International standard for systems and software engineering requirements specification |
| **SRS** | Software Requirements Specification — formal document describing software system requirements |
| **UAT** | User Acceptance Testing — validation that system meets business requirements |
| **NFR** | Non-Functional Requirement — constraint on system operation (performance, security, etc.) rather than specific behavior |
| **PKI** | Public Key Infrastructure — framework for managing digital certificates and encryption |
| **HTTPS** | Hypertext Transfer Protocol Secure — encrypted HTTP communication using TLS/SSL |
| **TLS** | Transport Layer Security — cryptographic protocol for secure network communication |
| **OAuth** | Open Authorization — standard protocol for token-based authentication and authorization |
| **OIDC** | OpenID Connect — identity layer on top of OAuth 2.0 for federated authentication |
| **SSO** | Single Sign-On — authentication scheme allowing user to access multiple systems with one set of credentials |
| **GDPR** | General Data Protection Regulation — European Union data privacy and protection law |
| **PII** | Personally Identifiable Information — data that can identify a specific individual |
| **WCAG** | Web Content Accessibility Guidelines — international accessibility standards for digital content |
| **ARIA** | Accessible Rich Internet Applications — technical specifications for improving accessibility of web content |
| **i18n** | Internationalization — designing software to support multiple languages and locales |
| **l10n** | Localization — adapting internationalized software for specific languages and regions |
| **UUID** | Universally Unique Identifier — 128-bit identifier used to uniquely identify information |
| **JSON** | JavaScript Object Notation — lightweight data interchange format |
| **YAML** | YAML Ain't Markup Language — human-readable data serialization format |
| **REST** | Representational State Transfer — architectural style for distributed systems using HTTP |
| **API** | Application Programming Interface — set of definitions and protocols for building software |
| **SDK** | Software Development Kit — collection of tools, libraries, and documentation for developing software |
| **CI/CD** | Continuous Integration / Continuous Deployment — automated software development practices |
| **GPO** | Group Policy Object — Windows Active Directory feature for centralized configuration management |
| **MDM** | Mobile Device Management — software for managing and securing enterprise devices |
| **SemVer** | Semantic Versioning — versioning scheme using MAJOR.MINOR.PATCH format |
| **VSIX** | Visual Studio Extension — package format for VS Code extensions |

---

[← Previous](appendix-a-traceability-matrix.md) | [Back to main](../ai-client-srs.md) | [Next →](appendix-c-analysis-models.md)
