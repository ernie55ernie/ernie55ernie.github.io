---

layout: post
title: "Choosing Claude Models in 2026: Fable, Opus, Sonnet, Haiku, and Effort"
date: 2026-07-01
category: AI
---

## TL;DR

* **Use Claude Sonnet 5 as the default production model.** It is the best balance of speed, intelligence, and cost for coding, data analysis, tool use, writing, and most agentic workflows, according to Anthropic's current [model overview](https://platform.claude.com/docs/en/about-claude/models/overview) and [model-selection guide](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model).
* **Escalate to Claude Opus 4.8 for hard reasoning and long-horizon agentic coding.** Opus 4.8 is positioned as Anthropic's strongest Opus-tier model for complex reasoning, long-horizon coding, and high-autonomy work, with a $$1\text{M}$$ token context window and up to $$128\text{k}$$ output tokens in the synchronous Messages API.
* **Use Claude Haiku 4.5 for speed, scale, and simple tasks.** Haiku 4.5 is the fastest and cheapest current Claude model in the main Opus/Sonnet/Haiku ladder, useful for routing, extraction, lightweight classification, sub-agent work, and high-volume workloads.
* **Use Claude Fable 5 only when you need the highest available capability.** Fable 5 is Anthropic's most capable widely released model, priced above Opus, and aimed at the most demanding reasoning and long-horizon agentic work; see Anthropic's [Fable 5 / Mythos 5 launch notes](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5).
* **Do not treat “thinking” as one universal switch.** Current Claude models are moving from manual `budget_tokens` toward **adaptive thinking** plus an `effort` control. On newer Opus/Sonnet/Fable models, the practical knob is usually `output_config.effort`, not a manually chosen chain-of-thought budget; see Anthropic's [extended thinking guide](https://platform.claude.com/docs/en/build-with-claude/extended-thinking).
* **Optimize cost with caching and batching before downgrading intelligence.** Prompt cache hits are much cheaper than fresh input tokens, and the [Batch API](https://platform.claude.com/docs/en/about-claude/pricing) gives a $$50%$$ discount on both input and output tokens for asynchronous work.

## The 2026 Claude lineup

Anthropic's current public model ladder is no longer just "Opus vs Sonnet vs Haiku." As of July 2026, the practical lineup is:

| Tier               |    Current model | Best use                                                       | API ID             |         Context |      Max output |                        Pricing |
| ------------------ | ---------------: | -------------------------------------------------------------- | ------------------ | --------------: | --------------: | -----------------------------: |
| Highest capability |   Claude Fable 5 | Most demanding reasoning and long-horizon agentic work         | `claude-fable-5`   |   $$1\text{M}$$ | $$128\text{k}$$ |         $$\$10 / \$50$$ per MTok |
| Opus               |  Claude Opus 4.8 | Complex reasoning, agentic coding, high-autonomy workflows     | `claude-opus-4-8`  |   $$1\text{M}$$ | $$128\text{k}$$ |          $$\$5 / \$25$$ per MTok |
| Sonnet             |  Claude Sonnet 5 | Default model for coding, agents, analysis, and knowledge work | `claude-sonnet-5`  |   $$1\text{M}$$ | $$128\text{k}$$ | $$\$3 / \$15$$ per MTok standard |
| Haiku              | Claude Haiku 4.5 | Fast, cheap, high-volume, simple or parallel subtasks          | `claude-haiku-4-5` | $$200\text{k}$$ |  $$64\text{k}$$ |           $$\$1 / \$5$$ per MTok |

`MTok` means one million tokens. Anthropic's pricing page also notes that Sonnet 5 has introductory pricing of $$\$2$$ input and $$\$10$$ output per MTok through August 31, 2026, after which the standard $$\$3 / \$15$$ pricing applies; verify this on the live [Claude pricing page](https://platform.claude.com/docs/en/about-claude/pricing) before budgeting.

A simple synchronous API cost approximation is:

$$
\text{cost}
=

\frac{T_{\text{in}}}{10^6}P_{\text{in}}
+
\frac{T_{\text{out}}}{10^6}P_{\text{out}}
+
\text{feature add-ons}
$$

where $$T_{\text{in}}$$ and $$T_{\text{out}}$$ are input and output token counts, and $$P_{\text{in}}$$ and $$P_{\text{out}}$$ are the model's per-million-token prices.

## What changed from the older Opus/Sonnet/Haiku advice?

The older rule was:

> Default to Sonnet, escalate to Opus, use Haiku for volume.

That rule is still directionally correct, but it now needs two updates.

First, **Fable 5 sits above Opus** for users who need Anthropic's most capable widely released model. It is not the default because it costs more than Opus and may introduce integration considerations around refusals, fallback handling, and billing, but it is now the top of the capability ladder.

Second, **thinking controls have changed.** Older Claude 4-era advice often focused on manual extended thinking:

```python
thinking = {
    "type": "enabled",
    "budget_tokens": 10000
}
```

That still matters for some models, especially legacy or Haiku-style use cases, but the newer direction is **adaptive thinking** plus an `effort` level. Anthropic's [extended thinking docs](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) say that when manual extended thinking is deprecated or unsupported, developers should use:

```python
thinking = {"type": "adaptive"}
output_config = {"effort": "high"}
```

The important product-design shift is:

> Instead of guessing a fixed reasoning budget for every request, let the model decide when thinking is needed, then use `effort` to trade quality against latency and cost.

## Understanding `effort`, adaptive thinking, and extended thinking

### 1. Manual extended thinking

Manual extended thinking uses a token budget:

```python
thinking = {
    "type": "enabled",
    "budget_tokens": N
}
```

The parameter $$N$$ sets the maximum number of tokens the model can use for internal reasoning. The docs note that `budget_tokens` must be less than `max_tokens`, and larger budgets can improve quality on complex problems, though the model may not use the full budget.

A useful mental model is:

$$
\text{total output budget}
=

\text{thinking tokens}
+
\text{visible answer tokens}
$$

So increasing the thinking budget can improve difficult reasoning, but it also increases latency and output-token cost.

Use manual extended thinking only when the target model supports it and the task genuinely needs it: proof-style math, deep debugging, multi-step planning, complex architecture, or hard research synthesis.

### 2. Adaptive thinking

Adaptive thinking lets Claude decide when and how much to reason. For newer Claude models, this is increasingly the preferred path. Anthropic's docs list Opus 4.8, Opus 4.7, Sonnet 5, Fable 5, and Mythos 5 as models that use adaptive thinking rather than the older manual budget style.

This is better for mixed workloads. For example, the same product might receive:

* a trivial extraction request,
* a medium-difficulty code edit,
* a hard multi-file debugging task,
* a long-context legal or financial analysis.

A fixed `budget_tokens = 10000` wastes money on the first task and may be too small for the last. Adaptive thinking plus `effort` is a cleaner abstraction.

### 3. The `effort` parameter

`effort` is a compute-quality-latency dial. Anthropic's [choosing-model guide](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model) says recent Opus and Sonnet models support effort settings that trade intelligence for latency and cost within a single model.

For Claude Opus 4.8, Anthropic notes that the default effort level is `high`, and recommends `xhigh` for coding, high-autonomy work, and the most intelligence-demanding tasks.

A practical mapping:

| Task type                                  | Suggested model            | Thinking / effort                            |
| ------------------------------------------ | -------------------------- | -------------------------------------------- |
| Simple extraction, routing, classification | Haiku 4.5                  | No heavy thinking; optimize latency          |
| Daily coding and data analysis             | Sonnet 5                   | Adaptive thinking; `medium` or `high`        |
| Agentic coding with tools                  | Sonnet 5 or Opus 4.8       | Adaptive thinking; `high`                    |
| Hard multi-file refactor                   | Opus 4.8                   | Adaptive thinking; `xhigh` if available      |
| Highest-stakes reasoning                   | Fable 5 or Opus 4.8        | Adaptive thinking; `high` or above           |
| Cheap background processing                | Haiku 4.5 / Sonnet 5 Batch | Batch API; tune down effort if quality holds |

## Model-by-model guidance

### Claude Haiku 4.5

Choose Haiku 4.5 when speed and cost dominate. It is the right fit for:

* structured extraction,
* tagging,
* lightweight classification,
* routing,
* autocomplete-style edits,
* moderation pre-checks,
* sub-agent tasks launched in parallel,
* high-volume customer-support preprocessing.

Haiku is usually not the model to start with for deep reasoning, fragile code edits, difficult math, or long-horizon agents. It is best when a mistake is cheap, the task is narrow, or another stronger model can review the final result.

### Claude Sonnet 5

Sonnet 5 is the default recommendation for most serious work. It gives the best blend of speed and intelligence in the current main Claude lineup, and it is cheaper than Opus or Fable.

Use Sonnet 5 for:

* normal software engineering,
* code review,
* debugging,
* data analysis,
* writing and editing,
* research synthesis,
* tool-using agents,
* medium-to-long context tasks,
* enterprise workflows where cost matters.

A good production pattern is:

1. Start with Sonnet 5.
2. Run an eval set on real tasks.
3. Track failure modes.
4. Escalate only the failing slice to Opus 4.8 or Fable 5.
5. Send simple subtasks to Haiku 4.5.

This gives better cost-quality control than using one model for everything.

### Claude Opus 4.8

Opus 4.8 is the model to use when Sonnet is good but not enough. Anthropic describes it as the strongest Opus-tier model for complex reasoning, long-horizon agentic coding, and high-autonomy work.

Use Opus 4.8 for:

* multi-hour autonomous coding,
* large refactors,
* ambiguous debugging,
* systems architecture,
* complex research synthesis,
* vision-heavy workflows,
* high-autonomy agents,
* tasks where the cost of a subtle mistake is high.

Do not use Opus 4.8 for every request by default. A common mistake is paying Opus prices for tasks that Sonnet or Haiku can solve equally well.

### Claude Fable 5

Fable 5 is above Opus in capability and price. Anthropic describes it as the most capable widely released Claude model, built for the most demanding reasoning and long-horizon agentic work.

Use Fable 5 when:

* Opus 4.8 still fails your evals,
* correctness matters more than cost,
* the task has deep multi-step dependencies,
* the task is long-horizon and high-autonomy,
* you need the strongest available Claude model.

Do not blindly migrate every Opus or Sonnet workload to Fable. Re-baseline quality, latency, refusal behavior, and total cost first.

### Claude Mythos 5

Mythos 5 is not a general self-serve default. Anthropic describes it as limited availability through Project Glasswing and sharing Fable 5's capabilities without the same safety classifiers. For most developers, the practical public decision is between Haiku 4.5, Sonnet 5, Opus 4.8, and Fable 5.

## Cost controls: caching, batching, and routing

### Prompt caching

Prompt caching is often more important than model downgrading. Anthropic's pricing table shows separate rates for:

* base input tokens,
* 5-minute cache writes,
* 1-hour cache writes,
* cache hits and refreshes,
* output tokens.

For current models, cache hits are roughly $$10%$$ of the base input price. If a repeated prompt prefix is large, caching can dominate savings.

A simplified cache-hit model:

$$
C_{\text{cache hit}}
\approx
0.1 \times C_{\text{fresh input}}
$$

Use prompt caching for:

* long system prompts,
* repeated tool definitions,
* repeated documents,
* repeated codebase context,
* repeated policy or instruction blocks,
* multi-turn workflows with stable prefixes.

### Batch API

The Batch API gives a $$50%$$ discount on both input and output tokens for asynchronous workloads.

$$
C_{\text{batch}}
\approx
0.5 \times C_{\text{synchronous}}
$$

Use batching for:

* nightly document processing,
* offline evaluation,
* bulk classification,
* dataset labeling,
* large-scale summarization,
* background research extraction,
* non-interactive code analysis.

The rule of thumb:

> Use a stronger model interactively where quality matters, and use Batch API plus caching for scale.

### Model routing

A strong production router can look like this:

```text
if task_is_simple_and_high_volume:
    use Haiku 4.5
elif task_is_default_coding_or_analysis:
    use Sonnet 5
elif task_requires_deep_reasoning_or_agentic_coding:
    use Opus 4.8
elif Opus_fails_or_quality_is_paramount:
    use Fable 5
```

You can also add a verifier step:

```text
Haiku/Sonnet draft → Sonnet/Opus review → final answer
```

This is often cheaper than running every first-pass request through Opus or Fable.

## Coding and Claude Code

Anthropic's [Claude Code documentation](https://code.claude.com/docs/en/overview) describes Claude Code as an agentic coding tool that can read and edit files, run commands, and integrate with development tools.

For coding workflows:

| Coding task                       | Recommended model                     |
| --------------------------------- | ------------------------------------- |
| Small edit                        | Haiku 4.5 or Sonnet 5                 |
| Normal feature implementation     | Sonnet 5                              |
| Code review                       | Sonnet 5                              |
| Debugging with logs/tests         | Sonnet 5, escalate to Opus 4.8        |
| Multi-file refactor               | Opus 4.8                              |
| Long-horizon autonomous coding    | Opus 4.8 or Fable 5                   |
| Highest-risk production migration | Fable 5 or Opus 4.8 with strong tests |

The key is not just model choice. For coding agents, the biggest quality multipliers are:

* good repository context,
* tight tool permissions,
* test execution,
* small checkpoints,
* explicit acceptance criteria,
* deterministic review steps,
* human review for risky changes.

## Decision framework

Ask five questions.

### 1. How expensive is a wrong answer?

If the downside is small, use Haiku or Sonnet. If the downside is high, start with Sonnet and add Opus/Fable verification. If the downside is severe, start with Opus or Fable and require evidence.

### 2. Is the task latency-sensitive?

If users are waiting in real time, prefer Haiku or Sonnet and avoid unnecessarily high effort. If the task runs in the background, use Batch API and consider stronger models.

### 3. Is the task reasoning-bound or context-bound?

Reasoning-bound tasks need better models and higher effort. Context-bound tasks may need retrieval, chunking, caching, or the $$1\text{M}$$ context window. Do not assume that adding more context always improves results.

### 4. Does the same context repeat?

If yes, prompt caching may save more than downgrading the model.

### 5. Can you measure quality?

Do not select models by vibes. Build a small eval set:

* $$50$$ to $$200$$ representative prompts,
* expected answers or grading rubrics,
* edge cases,
* cost and latency logs,
* failure categories.

Then compare:

$$
\text{utility}
=

\alpha \cdot \text{quality}

- \beta \cdot \text{latency}

- \gamma \cdot \text{cost}
$$

where $$\alpha, \beta, \gamma$$ reflect your product priorities.

## Common mistakes

### Mistake 1: Using the strongest model for everything

Fable or Opus for every request is simple, but usually wasteful. Most workloads have a long tail of easy requests.

### Mistake 2: Treating thinking as free

Thinking tokens count toward output behavior and cost. Higher effort can improve quality, but it should be justified by evals.

### Mistake 3: Migrating old `budget_tokens` code blindly

Manual extended thinking is deprecated or unsupported on several newer models. Newer Opus/Sonnet/Fable workflows should usually move toward adaptive thinking and explicit effort controls.

### Mistake 4: Ignoring tokenizer and migration effects

Per-token price is not the same as per-task price. If a new model tokenizes the same text differently, actual cost can move even when the listed per-MTok price is unchanged.

### Mistake 5: Using $$1\text{M}$$ context as a substitute for retrieval

Long context is powerful, but it is not always the cheapest or most accurate architecture. For large corpora, retrieval plus citations is often better than dumping everything into one request.

## Practical recommendations

1. **Default to Sonnet 5** for most coding, writing, research, analysis, and agentic work.
2. **Use Haiku 4.5** for cheap, fast, high-volume subtasks.
3. **Escalate to Opus 4.8** when Sonnet fails on complex reasoning, large refactors, or high-autonomy workflows.
4. **Use Fable 5** only when you need the highest available capability and can justify the price and integration constraints.
5. **Use adaptive thinking and `effort`** on newer models instead of manually tuning `budget_tokens`.
6. **Use prompt caching** whenever repeated context is large.
7. **Use the Batch API** for asynchronous bulk work.
8. **Build model routing around evals**, not intuition.

## Final rule of thumb

For most teams:

```text
Haiku 4.5 = fast worker
Sonnet 5 = default expert
Opus 4.8 = difficult-problem specialist
Fable 5 = maximum-capability escalation
```

The best Claude setup is not one model. It is a routing system: cheap models for easy work, Sonnet for the main path, Opus for hard failures, Fable for the highest-stakes edge cases, and caching/batching underneath to keep the economics sane.
