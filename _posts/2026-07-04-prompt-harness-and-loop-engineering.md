---
layout: post
title: "Prompt, Harness, and Loop Engineering for General-Purpose Autonomous LLM Agents"
date: 2026-07-04
category: llm
---

## TL;DR

The most important lesson from 2025–2026 agent engineering is not “use a more complicated framework.” It is almost the opposite: **push complexity into the model and the context, not into brittle scaffolding**. Anthropic’s [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) argues that successful production systems tend to use “simple, composable patterns” and recommends starting with the simplest solution before adding orchestration.

A useful mental model separates agent engineering into three layers:

1. **Prompt engineering**: instructions, tool descriptions, examples, output schemas.
2. **Harness engineering**: tools, sandboxes, memory, state, files, permissions, observability.
3. **Loop engineering**: the repeated think/action/observe/verify cycle.

In 2025, this vocabulary increasingly collapsed into a broader discipline: **context engineering**. Anthropic defines context engineering as curating and maintaining the optimal tokens used during inference, including prompts, tools, MCP resources, external data, and message history; it frames context as a finite resource with diminishing returns.

The agent loop can be written as:

$$
a_t \sim \pi_\theta(\cdot \mid C_t), \qquad
o_t = \mathcal{E}(a_t), \qquad
C_{t+1} = g(C_t, a_t, o_t)
$$

where $C_t$ is the context at step $t$, $a_t$ is the model-selected action, $o_t$ is the observation returned by the environment or tool, and $g$ is the harness logic that decides what gets preserved, summarized, cleared, or retrieved for the next step.

The core engineering problem is therefore:

$$
\max_{C_t \subseteq \mathcal{I}_t} ; \mathbb{E}[\text{task success} \mid C_t]
\quad \text{s.t.} \quad |C_t| \le B
$$

where $\mathcal{I}_t$ is all potentially relevant information and $B$ is the model’s context budget.

---

## 1. Why “context engineering” replaced “prompt engineering”

Classic prompt engineering optimized a single input: role, task, constraints, examples, and output format. That still matters, but agents run over many turns. They call tools, read documents, create files, make mistakes, recover, and accumulate history. In that setting, the hard question is no longer just “what should the system prompt say?” It is:

> What should the model see **right now** so that the next action is most likely to be useful?

Anthropic’s [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) explicitly frames the shift this way: building with language models is less about finding perfect wording and more about deciding what configuration of context will produce the desired behavior.

A practical context can be decomposed as:

$$
C_t = [S, U_t, H_t, T_t, R_t, M_t, A_t]
$$

where:

* $S$: system prompt and policy instructions
* $U_t$: current user request
* $H_t$: relevant conversation history
* $T_t$: tool definitions and schemas
* $R_t$: retrieved documents or search results
* $M_t$: persistent memory, notes, summaries, files
* $A_t$: artifacts created so far, such as code, plans, tables, or drafts

The danger is that more context is not always better. Anthropic notes that as context grows, agents may lose focus before they hit the hard token limit; this is often described as **context rot**.

A simple heuristic is:

$$
\text{useful context} =
\frac{\text{signal}}{\text{tokens} + \text{staleness} + \text{ambiguity}}
$$

The goal is not to maximize tokens. The goal is to maximize **decision quality per token**.

---

## 2. Prompt engineering: instructions, examples, schemas, and tools

Prompt engineering still matters, but for agents it should be treated as **interface design**.

A good system prompt should specify:

* the agent’s role
* the task boundary
* available tools
* decision heuristics
* safety constraints
* output format
* when to stop
* when to ask for help

Anthropic’s [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) distinguishes **workflows**, where LLMs and tools follow predefined code paths, from **agents**, where LLMs dynamically direct their own tool use and process. This distinction matters because prompts for deterministic workflows can be narrower, while prompts for agents must teach decision-making.

### Tool descriptions are prompts

Every tool name, parameter, and description becomes part of the model’s context. Anthropic’s [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) emphasizes that tool descriptions and specs are loaded into the agent’s context and steer tool-calling behavior. It recommends meaningful tool results, token-efficient responses, clear parameters, pagination, truncation, and actionable error messages.

Bad tool interface:

```text
search(query: string)
```

Better tool interface:

```text
search_recent_docs(
  query: string,
  source_type: "docs" | "issues" | "pull_requests",
  max_results: integer
)
```

The model should not have to infer whether `user` means username, user ID, email, or profile object. In agent systems, ambiguity compounds over steps.

### Structured outputs

For actions, structured outputs are usually better than free text. A function call or JSON schema reduces parsing ambiguity:

```json
{
  "action": "search",
  "query": "Anthropic Building effective agents simple composable patterns",
  "max_results": 5
}
```

But schemas should not become a second programming language. If the model has to fill an over-engineered object with many nullable fields, the harness has shifted complexity away from the model’s reasoning and into brittle serialization.

### Prompt caching

Long agent prompts often contain stable blocks: system instructions, tool definitions, policy text, repo summaries, or large documents. Anthropic’s [prompt caching documentation](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) explains that caching reuses prompt prefixes and can reduce processing time and cost for prompts with repeated structure. Anthropic’s May 2025 API announcement also states that extended prompt caching can reduce costs by up to 90% and latency by up to 85% for long prompts.

A cache-friendly context layout is:

```text
[stable system prompt]
[stable tool definitions]
[stable project background]
[semi-stable memory / summary]
[dynamic user request]
[dynamic tool results]
```

The rule of thumb:

$$
\text{cache benefit} \propto \text{stable prefix length} \times \text{reuse frequency}
$$

---

## 3. Harness engineering: tools, state, memory, files, and permissions

The **harness** is everything around the model that lets it act in the world. This includes:

* tool execution
* function calling
* code sandboxes
* file systems
* memory stores
* retrieval systems
* permissions
* approval checkpoints
* logging
* tracing
* retries
* rate limits
* state persistence

The simplest agent loop is tiny:

```python
while not done:
    message = build_context(state)
    action = model(message)
    observation = run_tool_or_respond(action)
    state = update_state(state, action, observation)
```

Most production complexity lives around this loop.

Anthropic’s [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) argues that long-running agents need ways to bridge context windows. Their Claude Agent SDK approach uses artifacts such as initialization scripts, progress files, git history, and incremental clean-state work so that later sessions can resume without guessing what happened.

### Memory is not just chat history

For agents, memory should be externalized. A useful distinction:

| Memory type      |           Scope | Example                                          |
| ---------------- | --------------: | ------------------------------------------------ |
| Short-term state |     current run | current plan, open subtasks, recent tool results |
| Working memory   | current project | `todo.md`, `progress.txt`, scratch files         |
| Long-term memory |   cross-session | user preferences, durable facts, past decisions  |
| Retrieval memory |    large corpus | docs, codebase, tickets, papers                  |

LangGraph’s persistence layer, for example, separates short-term thread-scoped memory via checkpoints from long-term cross-thread memory via stores.

### Compaction, clearing, and memory

Long-running agents eventually face context pressure. Anthropic’s Claude cookbook on [memory, compaction, and tool clearing](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools) describes three complementary strategies:

* **Compaction**: summarize the active context into a smaller high-fidelity state.
* **Tool-result clearing**: remove bulky, re-fetchable tool outputs while preserving the fact that the tool call happened.
* **Memory**: write durable notes into external storage.

A useful compaction objective is:

$$
\text{summary}^* =
\arg\min_s |s|
\quad \text{s.t.} \quad
I(s; \text{future actions}) \approx I(H; \text{future actions})
$$

In plain English: make the summary as short as possible while preserving the information needed for future decisions.

### MCP as the tool interface layer

The [Model Context Protocol](https://modelcontextprotocol.io/) became the default vocabulary for connecting agents to external tools and data. Anthropic introduced MCP in November 2024 as a standard protocol for sharing resources, tools, and prompts across data sources; The Verge summarized it as a way to avoid custom integrations for every dataset.

Anthropic later added an [MCP connector](https://claude.com/blog/agent-capabilities-api) to the Claude API, letting developers connect Claude to remote MCP servers without writing custom client code. OpenAI’s Agents SDK also lists MCP server tool calling as a built-in feature.

The architectural direction is clear:

```text
LLM agent
  ↕
agent harness
  ↕
MCP tools / APIs / files / databases / browsers / code execution
```

MCP does not remove the need for security. It standardizes connection, but it also expands the attack surface.

---

## 4. Loop engineering: think, act, observe, verify

The core agent loop is a generalization of ReAct. The original [ReAct paper](https://arxiv.org/abs/2210.03629) proposed interleaving reasoning traces and actions so that language models can update plans based on external observations.

A production-grade loop usually has these stages:

1. **Context assembly**: choose the prompt, memory, tools, and retrieved data.
2. **Action selection**: ask the model to respond or call a tool.
3. **Execution**: run the tool, code, search, browser, or API.
4. **Observation**: return structured results to the model.
5. **Verification**: check whether the result satisfies the task.
6. **State update**: write memory, update files, compact, or clear.
7. **Termination**: stop, ask for human approval, or continue.

Mathematically:

$$
\begin{aligned}
C_t &= \text{assemble}(S, H_t, M_t, T_t, R_t) \
a_t &= \text{LLM}*\theta(C_t) \
o_t &= \text{execute}(a_t) \
v_t &= \text{verify}(a_t, o_t, \text{goal}) \
H*{t+1}, M_{t+1} &= \text{update}(H_t, M_t, a_t, o_t, v_t)
\end{aligned}
$$

### Termination is part of the loop

A weak agent does not know when to stop. A production loop should define explicit stop conditions:

* final answer produced
* test suite passes
* verifier approves
* max iterations reached
* token budget reached
* confidence threshold met
* human approval required
* irreversible action requested

For long tasks, termination should be hierarchical:

```text
task done?
  ├─ if yes: final answer
  ├─ if no but blocked: ask human / escalate
  ├─ if no and budget remains: continue
  └─ if no and budget exhausted: summarize partial progress
```

### Reflection and self-correction

Reflection can improve quality, especially for code, math, and verifiable tasks. The [Reflexion](https://arxiv.org/abs/2303.11366) framework showed that agents can improve by writing verbal feedback into memory rather than updating model weights.

But reflection is not free. It adds latency, cost, and sometimes fake confidence. A practical pattern is:

$$
\text{reflect only if} \quad
P(\text{error}) \times \text{cost(error)}

>

\text{cost(reflection)}
$$

Use reflection for:

* code before merge
* data analysis before reporting
* math or logic-heavy answers
* irreversible actions
* security-sensitive workflows

Do not reflexively add reflection to every step.

---

## 5. Simple vs. complex loops

The dominant debate in 2025–2026 is whether to build elaborate orchestration or let stronger models handle more of the planning internally.

Anthropic’s position in [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) is pragmatic: start simple, and increase complexity only when needed. It notes that agentic systems trade cost and latency for better task performance.

This is the agent version of the “bitter lesson”:

$$
\text{capability} \approx f(\text{model quality}, \text{compute}, \text{context}, \text{tools})
$$

Hand-built orchestration helps when it provides:

* deterministic control
* safety boundaries
* observability
* state persistence
* human approval
* domain-specific tool routing

It hurts when it creates:

* duplicated state
* hidden prompts
* conflicting planners
* excessive tool choices
* brittle routing logic
* debugging opacity

A good escalation rule is:

$$
\text{add scaffolding only if}
\quad
\Delta \text{success} >
\Delta \text{cost} + \Delta \text{latency} + \Delta \text{maintenance}
$$

---

## 6. Single-agent vs. multi-agent

The multi-agent debate became sharply defined in 2025.

Anthropic’s [multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) reported that a Claude Opus 4 lead agent with Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on an internal research evaluation. The same post says multi-agent systems are especially useful for breadth-first research queries that can pursue many independent directions in parallel.

But Anthropic also gives the caveat: agents used about 4× more tokens than chat interactions, and multi-agent systems used about 15× more tokens than chats. It also notes that domains requiring shared context or many dependencies are not good fits for multi-agent systems today.

Cognition’s [Don’t Build Multi-Agents](https://cognition.com/blog/dont-build-multi-agents) argues the opposite default for production work: share context, because actions carry implicit decisions and conflicting decisions create bad results.

A concise decision rule:

$$
\text{use multi-agent}
\iff
\text{parallelism gain} >
\text{coordination cost} + \text{context loss}
$$

Use **multi-agent** when:

* the task is read-heavy
* subtasks are independent
* breadth matters more than deep consistency
* separate context windows are an advantage
* outputs can be merged cleanly

Use **single-agent** when:

* actions depend on previous actions
* shared mutable state matters
* coding consistency matters
* decisions are hard to merge
* the agent must maintain one coherent plan

In short:

```text
Research breadth → multi-agent can help.
Codebase surgery → single shared context usually wins.
```

---

## 7. CodeAct and executable actions

Another important design split is whether the model should emit structured tool calls or executable code.

Traditional tool calling:

```json
{
  "tool": "search",
  "arguments": {
    "query": "agent context engineering"
  }
}
```

CodeAct-style action:

```python
results = search("agent context engineering", max_results=5)
summary = summarize(results)
```

Hugging Face’s [smolagents](https://huggingface.co/docs/smolagents/en/index) emphasizes minimalist agents, and its code-agent guide says code agents generate Python tool calls as actions, making action representations efficient, expressive, and accurate.

The advantage of code actions is composability:

$$
\text{one code action} \approx \text{many JSON tool calls}
$$

This can reduce loop iterations and make complex transformations easier. The downside is security: executable code must run in a sandbox with strict permissions.

Use CodeAct when:

* the task involves data transformation
* tool calls need composition
* intermediate variables matter
* Python is a natural substrate
* sandboxing is available

Avoid CodeAct when:

* tools are destructive
* permissions are unclear
* execution cannot be isolated
* deterministic audit trails matter more than flexibility

---

## 8. Framework landscape

The agent framework ecosystem is crowded, but the durable options map to different needs.

| Framework / tool                                                                                             | Best for                            | Notes                                                       |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------- | ----------------------------------------------------------- |
| [LangGraph](https://docs.langchain.com/oss/python/langgraph/persistence)                                     | stateful, auditable workflows       | persistence, checkpoints, stores, human-in-the-loop         |
| [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)                                          | lightweight production agents       | agents, tools, handoffs, guardrails, sessions, tracing, MCP |
| [Claude Agent SDK](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)        | Claude-centric long-running agents  | compaction, tools, coding workflows, progress artifacts     |
| [Google ADK](https://adk.dev/)                                                                               | Gemini / Google Cloud agent systems | open framework, context management, deployment paths        |
| [A2A](https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade) | agent-to-agent interoperability     | protocol for collaborative agents across platforms          |
| [Pydantic AI](https://pydantic.dev/)                                                                         | type-safe Python agent apps         | type safety, validation, evals, observability               |
| [smolagents](https://huggingface.co/docs/smolagents/en/index)                                                | minimal open-source code agents     | small abstraction layer, CodeAct style                      |
| [DSPy](https://dspy.ai/)                                                                                     | prompt/program optimization         | “program, don’t prompt”; signatures and optimizers          |

OpenAI’s Agents SDK describes itself as a lightweight, production-ready upgrade from Swarm with a small primitive set: agents, handoffs, guardrails, tracing, sessions, function tools, MCP support, and human-in-the-loop mechanisms. OpenAI’s tracing docs also note that the SDK records LLM generations, tool calls, handoffs, guardrails, and custom events.

Google’s ADK documentation says ADK can work with almost any generative AI model and manages context through sessions, memory, tool outputs, artifacts, summarization, lazy-loading, and token tracking. Google’s A2A updates add native A2A support in ADK and describe A2A as a protocol for interoperable agent collaboration.

DSPy is different from most agent frameworks. It is not mainly an orchestration harness; it is a way to express LLM tasks as structured signatures and optimize them programmatically rather than hand-writing prompts.

---

## 9. Evaluation and observability

Agents cannot be improved if their trajectories are invisible.

A useful evaluation stack has three levels:

1. **End-state evals**: Did the final answer or artifact solve the task?
2. **Trajectory evals**: Did the agent take reasonable steps?
3. **Tool evals**: Did each tool call use valid arguments and produce useful results?

End-state metrics often matter most:

$$
\text{score} =
\alpha \cdot \text{task success}

* \beta \cdot \text{quality}

- \gamma \cdot \text{cost}
- \delta \cdot \text{latency}
- \lambda \cdot \text{risk}
  $$

For coding agents, the strongest eval is usually objective:

```text
tests pass?
lint passes?
build succeeds?
diff is minimal?
security checks pass?
```

For research agents, use:

```text
claims supported?
sources credible?
dates correct?
contradictions handled?
uncertainty stated?
```

For workflow agents, use:

```text
task completed?
right tools used?
no unauthorized actions?
human approval respected?
state recoverable?
```

Observability should log:

* model inputs and outputs
* tool calls
* tool results
* errors
* retries
* token usage
* latency
* cost
* approval events
* state transitions
* final artifacts

A trace is not just a debug convenience. It is the audit trail of the agent’s reasoning environment.

---

## 10. Security: prompt injection, excessive agency, and tool risk

Agent security is harder than chatbot security because agents can act.

OWASP lists [Prompt Injection](https://owasp.org/www-project-top-10-for-large-language-model-applications/) as LLM01 and describes it as crafted inputs that can lead to unauthorized access, data breaches, and compromised decision-making. The same OWASP list includes insecure output handling, insecure plugin design, excessive agency, overreliance, and model theft.

A safe agent harness should assume:

```text
all retrieved content is untrusted
all webpage instructions are untrusted
all tool outputs may be adversarial
all generated code may be wrong
all irreversible actions need approval
```

A basic security policy:

$$
\text{permission}(a_t) =
\begin{cases}
\text{allow} & \text{read-only and low risk} \\
\text{review} & \text{write, send, delete, pay, deploy} \\
\text{deny} & \text{credential exfiltration or policy violation}
\end{cases}
$$

Practical defenses:

* tool allowlists
* scoped credentials
* read/write separation
* sandboxed code execution
* human approval for destructive actions
* content provenance
* output validation
* least privilege
* audit logs
* rate limits
* secrets redaction
* MCP server trust review

The key idea is **privilege separation**. The model may decide what it wants to do, but the harness decides what it is allowed to do.

---

## 11. Practical architecture recommendations

### Recommendation 1: Start with one agent

Start with a single ReAct-style loop:

```text
assemble context → model action → tool execution → observation → update state
```

Only add planners, routers, subagents, or graph workflows after you observe a specific failure mode.

### Recommendation 2: Treat tools as product surfaces

A tool is not just an API wrapper. It is an interface for a probabilistic user. Good tools have:

* obvious names
* strict schemas
* clear descriptions
* useful errors
* pagination
* filtering
* concise responses
* permission metadata
* stable semantics

### Recommendation 3: Externalize state

Do not rely on conversation history alone. Use:

```text
notes.md
todo.md
progress.txt
artifacts/
logs/
state.json
```

The best long-running agents leave a workspace that another agent—or a human—can understand.

### Recommendation 4: Compact before context rot

Do not wait until the context window is full. Compact when:

$$
\frac{|C_t|}{B} > \tau
$$

where $\tau$ might be 0.5–0.7 depending on task complexity.

Compaction should preserve:

* goal
* constraints
* decisions made
* failed attempts
* current plan
* open questions
* artifact locations
* next action

### Recommendation 5: Use multi-agent only when the task shape fits

Multi-agent systems are powerful when the work is parallelizable. But they are expensive and coordination-heavy.

Use this checklist:

```text
Can subtasks be done independently?
Can outputs be merged without conflict?
Is breadth more important than consistency?
Is the task valuable enough for 10x+ token cost?
Does each subagent need only scoped context?
```

If not, stay single-agent.

### Recommendation 6: Build evals before scaling

Before adding more agents, add tests.

A minimal eval set should include:

* 20 easy cases
* 20 normal cases
* 20 edge cases
* 10 adversarial cases
* 10 regression cases from real failures

For each, record:

$$
(\text{input}, \text{expected behavior}, \text{allowed tools}, \text{success criteria})
$$

### Recommendation 7: Delete scaffolding periodically

As models improve, some scaffolding becomes obsolete. Every model generation, run an experiment:

```text
old harness + old model
old harness + new model
simpler harness + new model
raw model + minimal tools
```

If the simpler version matches or beats the complex version, delete code.

---

## 12. The bottom line

The durable agent stack is not a giant maze of orchestrators. It is a small loop surrounded by excellent context management, safe tools, state persistence, observability, and evals.

The core formula is:

$$
\text{agent quality}
=

f(\text{model}, \text{context}, \text{tools}, \text{loop}, \text{evals}, \text{permissions})
$$

Prompt engineering teaches the model what to do.

Harness engineering gives it a safe world to act in.

Loop engineering decides how it keeps going.

Context engineering ties all three together.

The best practical advice remains:

> Start simple. Make context excellent. Add complexity only when measured failures justify it.
