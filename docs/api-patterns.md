# Prompt Engineering & API Patterns

This section defines how developers building features within our extensions should construct and manage AI interactions. These patterns ensure consistency, reusability, and reliable outputs.

---

## 1. Message Roles

The OpenAI Chat Completions API uses distinct message roles. Our extension SDK must properly support all roles:

| Role | Purpose | When to Use |
|------|---------|-------------|
| **system** | Sets behavior, persona, and constraints for the model | Once at the start of each conversation/request; defines "who" the AI is |
| **user** | Contains the actual user request or input | For prompts derived from user actions or code context |
| **assistant** | Contains previous AI responses | For multi-turn conversations; providing examples (few-shot) |
| **tool** | Contains tool execution results | Sending function call results back to the model |

**Example: Programmatic Prompt Construction**

```typescript
// Code review feature - programmatic prompt (not interactive chat)
const messages: ChatMessage[] = [
  {
    role: "system",
    content: `You are a senior software engineer performing code review.
Focus on: security vulnerabilities, performance issues, and maintainability.
Be concise. Use bullet points. Do not rewrite the code unless asked.`
  },
  {
    role: "user", 
    content: `Review this code:\n\n\`\`\`${language}\n${codeSnippet}\n\`\`\``
  }
];
```

---

## 2. Prompt Templates

For reusable, programmatic prompts (not user-authored chat), the extension should support templated prompts:

**Template Structure**

```yaml
# Prompt template: code-review.yaml
id: code-review
name: "Code Review"
description: "Analyze code for issues and improvements"
version: "1.0"

system_prompt: |
  You are a senior software engineer performing code review.
  Focus on: {{focus_areas}}
  Language: {{language}}
  Be concise. Use bullet points.

user_prompt_template: |
  Review this {{language}} code:
  
  ```{{language}}
  {{code}}
  ```
  
  {{#if specific_concern}}
  Pay special attention to: {{specific_concern}}
  {{/if}}

parameters:
  - name: language
    type: string
    required: true
  - name: code
    type: string
    required: true
  - name: focus_areas
    type: string
    default: "security, performance, maintainability"
  - name: specific_concern
    type: string
    required: false

model_settings:
  temperature: 0.3  # Lower for more consistent analysis
  max_tokens: 1024
```

**Programmatic Usage**

```typescript
const result = await ai.executeTemplate("code-review", {
  language: "typescript",
  code: selectedText,
  focus_areas: "security, error handling",
  specific_concern: "SQL injection"
});
```

---

## 3. Instruction Following Best Practices

To ensure reliable model outputs, prompts should follow these patterns:

| Pattern | Description | Example |
|---------|-------------|---------|
| **Role Definition** | Clearly define who/what the model is | "You are a TypeScript expert..." |
| **Task Specification** | Explicitly state the task | "Your task is to refactor this function to..." |
| **Output Format** | Specify desired format | "Respond with a JSON object containing..." |
| **Constraints** | Define what NOT to do | "Do not include explanations. Only output code." |
| **Examples (Few-shot)** | Provide input/output examples | Include 1-3 examples in system or user message |

**Anti-patterns to Avoid**

| Anti-pattern | Problem | Better Approach |
|--------------|---------|-----------------|
| Vague instructions | Inconsistent outputs | Be specific: "List exactly 3 issues" |
| No output format | Hard to parse results | Always specify format |
| Overly long prompts | Token waste, confusion | Keep focused; use separate calls for different tasks |
| Prompt injection risk | User input may override instructions | Clearly delimit user content with markers |

---

## 4. Structured Output Handling

For features requiring parseable responses, use the `response_format` parameter or explicit JSON instructions:

### Method 1: JSON Mode (Recommended)

```typescript
const response = await ai.complete({
  messages: [...],
  response_format: { type: "json_object" },
  // When using JSON mode, instruct the model what JSON to produce
});

// System prompt must mention JSON:
// "Respond with a JSON object containing: { issues: [...], summary: string }"
```

### Method 2: Explicit Schema in Prompt

```typescript
const systemPrompt = `
Analyze the code and respond with this exact JSON structure:
{
  "issues": [
    {
      "severity": "high" | "medium" | "low",
      "line": number,
      "description": string,
      "suggestion": string
    }
  ],
  "overall_quality": "good" | "needs_work" | "poor",
  "summary": string
}

Respond ONLY with valid JSON. No additional text.
`;
```

### Response Parsing

```typescript
interface CodeReviewResult {
  issues: Array<{
    severity: "high" | "medium" | "low";
    line: number;
    description: string;
    suggestion: string;
  }>;
  overall_quality: "good" | "needs_work" | "poor";
  summary: string;
}

const result = await ai.complete<CodeReviewResult>({
  messages,
  response_format: { type: "json_object" },
  responseSchema: CodeReviewResultSchema  // Runtime validation
});
```

---

## 5. Function Calling (Tools)

For features that need the model to invoke defined functions:

### Defining Tools

```typescript
const tools: Tool[] = [
  {
    type: "function",
    function: {
      name: "get_file_contents",
      description: "Read the contents of a file in the workspace",
      parameters: {
        type: "object",
        properties: {
          file_path: {
            type: "string",
            description: "Relative path to the file"
          }
        },
        required: ["file_path"]
      }
    }
  },
  {
    type: "function",
    function: {
      name: "run_terminal_command",
      description: "Execute a terminal command. **WARNING:** This tool executes arbitrary commands and is classified as DESTRUCTIVE. Requires explicit user approval when `requireApprovalForDestructiveTools` is enabled. Not exposed to external MCP hosts by default.",
      parameters: {
        type: "object",
        properties: {
          command: { type: "string", description: "Shell command to execute" },
          working_directory: { type: "string", description: "Working directory (optional)" }
        },
        required: ["command"]
      }
    }
  }
];
```

### Handling Tool Calls

```typescript
const response = await ai.complete({
  messages,
  tools,
  tool_choice: "auto"  // or "required" or { type: "function", function: { name: "..." } }
});

if (response.tool_calls) {
  for (const toolCall of response.tool_calls) {
    const args = JSON.parse(toolCall.function.arguments);
    
    // Execute the tool
    const result = await executeFunction(toolCall.function.name, args);
    
    // Send result back to model
    messages.push(
      { role: "assistant", content: null, tool_calls: [toolCall] },
      { role: "tool", tool_call_id: toolCall.id, content: JSON.stringify(result) }
    );
  }
  
  // Continue conversation with tool results
  const finalResponse = await ai.complete({ messages, tools });
}
```

### Tool Execution Loop

For multi-turn tool calling until the model produces a final text response:

```typescript
async function executeWithTools(
  initialMessages: ChatMessage[],
  tools: Tool[],
  maxIterations: number = 25
): Promise<string> {
  let messages = [...initialMessages];
  let iterations = 0;

  while (iterations < maxIterations) {
    const response = await ai.complete({ messages, tools, tool_choice: "auto" });

    if (!response.tool_calls || response.tool_calls.length === 0) {
      // Final text response received
      return response.content;
    }

    // Execute tool calls
    messages.push({ role: "assistant", content: null, tool_calls: response.tool_calls });

    for (const toolCall of response.tool_calls) {
      const result = await executeTool(toolCall);
      messages.push({
        role: "tool",
        tool_call_id: toolCall.id,
        content: JSON.stringify(result)
      });
    }

    iterations++;
  }

  throw new Error(`Tool execution loop exceeded maximum ${maxIterations} iterations`);
}
```

---

## 6. Context Management

For features that incorporate workspace context (code, files, symbols):

| Context Type | How to Include | Token Considerations |
|--------------|----------------|----------------------|
| **Selected Code** | Include in user message with language markers | Count tokens; truncate if needed |
| **File Contents** | Include relevant portions, not entire files | Summarize or chunk large files |
| **Symbol Definitions** | Include type signatures, interfaces | Prioritize relevant symbols |
| **Error Messages** | Include full error with stack trace | May truncate very long traces |
| **Documentation** | Include relevant doc snippets | Use RAG pattern for large docs |

### Context Prioritization

```typescript
interface ContextBuilder {
  // Add context with priority (higher = more important to keep)
  addContext(content: string, priority: number, label: string): void;
  
  // Build final context respecting token budget
  build(maxTokens: number): string;
}

const context = new ContextBuilder();
context.addContext(errorMessage, 100, "error");      // Highest priority
context.addContext(selectedCode, 90, "selection");    // High
context.addContext(fileContents, 50, "file");         // Medium
context.addContext(relatedTypes, 30, "types");        // Lower

const finalContext = context.build(4000);  // Fits in context window
```

### Context Window Management

**Token Estimation:**

```typescript
// Rough estimation: 1 token ≈ 4 characters or 0.75 words in English
function estimateTokens(text: string): number {
  return Math.ceil(text.length / 4);
}

// Use tiktoken library for accurate counting (model-specific)
import { encoding_for_model } from "tiktoken";

function countTokens(text: string, model: string = "gpt-4"): number {
  const enc = encoding_for_model(model);
  const tokens = enc.encode(text);
  enc.free();
  return tokens.length;
}
```

**Truncation Strategies:**

```typescript
interface TruncationStrategy {
  // Remove oldest non-system messages
  truncateOldest(messages: ChatMessage[], targetTokens: number): ChatMessage[];
  
  // Summarize long messages
  summarize(messages: ChatMessage[], targetTokens: number): ChatMessage[];
  
  // Keep high-priority context, remove low-priority
  priorityBased(messages: ChatMessage[], priorities: Map<string, number>, targetTokens: number): ChatMessage[];
}
```

---

## 7. Error Handling in Prompts

### Handling Invalid Model Outputs

```typescript
async function robustCompletion<T>(
  messages: ChatMessage[],
  schema: Schema,
  maxRetries: number = 2
): Promise<T> {
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      const response = await ai.complete({
        messages,
        response_format: { type: "json_object" }
      });

      // Validate against schema
      const parsed = JSON.parse(response.content);
      const validated = schema.validate(parsed);
      
      return validated as T;
    } catch (error) {
      if (attempt === maxRetries) {
        throw new Error(`Failed to get valid response after ${maxRetries + 1} attempts: ${error.message}`);
      }

      // Add correction instruction for next attempt
      messages.push(
        { role: "assistant", content: response.content },
        { role: "user", content: `The response was invalid: ${error.message}. Please correct and respond with valid JSON.` }
      );
    }
  }
}
```

### Rate Limit Handling

```typescript
async function completionWithBackoff(
  messages: ChatMessage[],
  maxRetries: number = 3
): Promise<ChatResponse> {
  let lastError: Error;

  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      return await ai.complete({ messages });
    } catch (error) {
      if (error.status === 429) {
        // Rate limited - exponential backoff
        const delayMs = Math.pow(2, attempt) * 1000;
        await sleep(delayMs);
        lastError = error;
      } else {
        throw error;
      }
    }
  }

  throw lastError;
}
```

---

## 8. Best Practices Summary

### DO's

✅ **Clear Instructions**: Always provide explicit, unambiguous instructions  
✅ **Output Format**: Specify the exact format you expect (Markdown, JSON, code block)  
✅ **Delimit User Content**: Use clear markers (e.g., triple backticks, XML tags) to separate user input  
✅ **Few-shot Examples**: Include 1-3 examples when format matters  
✅ **Token Awareness**: Estimate tokens before sending; truncate intelligently  
✅ **Error Handling**: Validate outputs; implement retry logic with backoff  
✅ **Context Prioritization**: Include most important context first  
✅ **Streaming**: Use SSE streaming for better UX on long responses  
✅ **Tool Descriptions**: Write clear, detailed descriptions for function calling  

### DON'Ts

❌ **Vague Prompts**: Avoid "analyze this code" without specifics  
❌ **No Validation**: Never trust model output without validation  
❌ **Ignore Token Limits**: Don't send prompts that exceed context window  
❌ **Hardcode Model Names**: Use configuration for model selection  
❌ **Log Sensitive Data**: Never log API keys, user code, or completions  
❌ **Block UI**: Always use async/streaming to avoid freezing the IDE  
❌ **Assume Perfect Output**: Models can hallucinate or produce invalid formats  
❌ **Prompt Injection**: Never directly concatenate untrusted user input into system prompts  

---

## 9. Example Patterns

### Code Generation

```typescript
const messages = [
  {
    role: "system",
    content: "You are a TypeScript expert. Generate production-quality code with error handling and TypeScript types."
  },
  {
    role: "user",
    content: `Generate a function that ${userRequest}.\n\nRequirements:\n- Use TypeScript with strict types\n- Include error handling\n- Add JSDoc comments\n\nRespond with ONLY the code, no explanations.`
  }
];
```

### Code Explanation

```typescript
const messages = [
  {
    role: "system",
    content: "You are a senior software engineer explaining code to junior developers. Be clear and concise."
  },
  {
    role: "user",
    content: `Explain what this code does:\n\n\`\`\`${language}\n${code}\n\`\`\`\n\nUse bullet points. Focus on the main logic.`
  }
];
```

### Bug Diagnosis

```typescript
const messages = [
  {
    role: "system",
    content: "You are a debugging expert. Analyze errors and suggest fixes."
  },
  {
    role: "user",
    content: `I'm getting this error:\n\n\`\`\`\n${errorMessage}\n\`\`\`\n\nIn this code:\n\n\`\`\`${language}\n${code}\n\`\`\`\n\nWhat's the likely cause and how do I fix it?`
  }
];
```

### Refactoring Suggestions

```typescript
const messages = [
  {
    role: "system",
    content: "You are a code quality expert. Suggest improvements for maintainability, performance, and best practices."
  },
  {
    role: "user",
    content: `Suggest improvements for this code:\n\n\`\`\`${language}\n${code}\n\`\`\`\n\nFocus on: ${focusAreas.join(", ")}`
  }
];
```

---

[← Previous](appendix-c-analysis-models.md) | [Back to main](../ai-client-srs.md) | [Next →](verification.md)
