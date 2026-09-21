---
name: superloop
description: Plan a loop, clarify what the user wants to repeat and their goal, and write a copy-ready loop prompt with instructions, inputs, deliverables, and stopping rules. Use for vague loop ideas, loop briefs, or planning before execution; also execute bounded cycles when the user asks to run them.
---

# Superloop

Turn “I want to loop this” into a clear, usable working agreement. Superloop is
the user-facing planning entry point for the loop family. Help the user express
what they want, choose the right repetition, and leave them with a prompt they
can paste into a fresh task. Do not make them learn loop-engineering vocabulary.

## 1. Understand before prescribing

Extract what is already known from the request, supplied artifacts, and relevant
conversation. Reuse existing authorization. Identify:

- **Target and input:** what repeats, on which artifact, workflow, or new items?
- **Outcome:** what should be different or true when finished, and for whom?
- **Deliverables:** what should the user receive, in what format and location?
- **Boundary:** planning only, read-only passes, local edits, or authorized effects?
- **Budget and end:** exact passes or a maximum; time/cost limit or review date?

Do not ask for information already supplied or cheaply discoverable. For missing
material information, ask one focused question at a time, usually about the
desired result first. Bundle at most three only when the choices are inseparable. Use the
runtime's appropriate question tool when available, otherwise concise natural
questions. Ask in the user's language. Prefer concrete choices tailored to their
context, with free text available; do not force unrelated presets.

Useful wording, adapted rather than recited:

1. “What would you like to achieve by repeating this work?” / 「反覆做這件事，你最想得到甚麼成果？」
2. “Which artifact or workflow should we work on?” / 「今次想處理哪份內容或哪個流程？」
3. “What would you like back: the finished artifact, findings, or both?” / 「最後想收到成品、發現清單，還是兩者？」

Ask target/outcome first if neither is known. Keep confirmed facts, proposed
choices, and unresolved decisions distinct. Ask a focused follow-up when evidence
or an answer reveals a material uncertainty, including during execution. Continue independent inspection while
waiting; never treat elapsed time as an answer. Do not invent the target, desired
outcome, paid budget, external destination, or authority. For reversible planning
choices, state a proposed default and keep drafting. If the user wants a template
without answering, provide a clearly labeled draft with open fields, not a
runnable contract. This skill's own maintenance request is not a reason to quiz
the user about an unrelated loop.

## 2. Choose the repetition that fits

| Kind | Repeated unit | Success and stopping |
|---|---|---|
| Improve | Evaluate → change → compare the same target | Frozen criteria; keep gains, revert regressions; normally at most 3 cycles |
| Audit/explore | A distinct perspective or evidence pass | Requested coverage and consolidated findings; honor exact pass counts |
| Process | One eligible input item or batch | Required output for each item; checkpoint, deduplicate, stop at batch/budget limit |
| Monitor | Observe a state at an authorized interval | Detect a meaningful change; quiet unchanged runs; expiry or review date |

A single action that does not benefit from repetition should become a one-pass
plan. Explain that simply. “Repeat” does not always mean “optimize.” Do not impose
baseline experiments or three improvement cycles on batch processing or monitoring.
Record count mode explicitly: `exact` or `maximum`. For “exactly N,” finish N
passes unless blocked, unsafe, cancelled, or the hard budget is exhausted. If
improvement converges, use remaining passes for distinct verification/coverage;
do not invent changes. For “up to N,” stop early when done. Pass count mode to
the executor; never silently convert exact work into a maximum. If the user
requires N actual changes rather than passes and no justified change remains,
ask about that conflict. Record no new findings honestly.

Mixed projects can compose stages (research → draft → audit → improve). Choose a
mode per stage, each with input, output, acceptance and handoff condition. Use one
overall budget plus bounded stage limits; feedback retries count toward that
budget. Do not restart upstream stages indefinitely when downstream checks fail.

## 3. Check readiness and make the agreement concrete

Before calling a prompt runnable, verify what is available locally: inputs and
access, required tools, writable destination, executor and any mandatory checker,
plus cadence/timezone/destination for scheduled work. Label each as verified,
user-reported, or missing. Do not test access by making external changes. Return
`ready`, `draft-only`, or `blocked: missing X`; only dependent steps wait. A tool
unavailable in this runtime is not a permission denial.

Use task-sized verification from [project patterns](references/project-patterns.md).
Code, research, design, content and data need different evidence; domain examples
are options, not mandatory extra workflows.

Draft a short overview: **target → repeated action → success → deliverables**.
Translate vague goals into observable criteria and label proposed criteria as
proposals. If the baseline has not been measured, say so and make measurement
step zero; never invent a starting score. For subjective goals, use a short rubric
with pass/fail examples. Separate candidate validation from final acceptance:
reversible drafts may be refined within scope and labeled provisional; independent
or owner review occurs at the declared acceptance checkpoint, not automatically
after every edit. Never call self-review independent. If a mandatory per-cycle
gate exists, preserve it and pause that cycle until satisfied.

Specify the input source, allowed changes, verification, per-pass feedback,
final output shape, budget, stop/pause rules, and unresolved decisions. A useful
deliverable is concrete: final copy plus changes, a cited findings table, processed
files plus exceptions, or alerts plus a run record. Avoid reports about reports.

## 4. Ask at meaningful checkpoints

Include this interaction contract inside the generated prompt; it must survive
handoff to another agent. Read [question checkpoints](references/question-checkpoints.md)
when a loop will run interactively or unattended.

- Before execution: resolve choices that change the target, acceptance, outputs,
  budget or effects. A complete authorized brief needs no ritual confirmation.
- During execution: when evidence contradicts the brief, required input/checker
  is missing, competing goals need a tradeoff, or a failed approach has no supported
  next step, state the observation and ask one decision-focused question with a
  recommendation. Do not ask the user to diagnose a technical failure you can test.
- After an answer: update the active contract, scope, remaining budget and affected
  verification; supersede contradictory assumptions. If criteria change, establish
  a new baseline instead of claiming an improvement against incomparable scores.
- While waiting: preserve checkpoint and best accepted output; continue independent
  work. No response is not approval. In unattended mode record `awaiting-input`,
  send at most the authorized actionable notification, and do not retry the same
  question every tick.
- At completion: deliver evidence and only genuine remaining decisions. An exact
  pass with no new findings is not a reason to ask for more work or create changes.

## 5. Deliver the prompt

Return in this order, scaled to the task:

1. One sentence explaining the proposed loop and any consequential assumptions.
2. A single copy-ready fenced prompt, using the relevant shape in
   [prompt patterns](references/prompt-patterns.md). Fill known fields; keep
   unresolved fields only in explicitly labeled drafts. Put sufficient context
   inside the prompt for a fresh task to use it without this conversation.
3. A short deliverables list with format/location, acceptance owner if needed,
   and evidence for completion. Include readiness and unresolved dependencies.
4. Only the remaining decisions that actually prevent execution, if any.

For improvement execution, use the bundled [execution guide](references/execution.md).
Check the prompt against its declared inputs, outputs, budget, verification,
failure and stop conditions. Compact loops need no extra files; save only when
requested or useful for an authorized deliverable.

## 6. Handoff or execute within the request

“Write a prompt,” “plan,” or “help me define” ends with the deliverable. It does
not create a runtime goal or scheduled task. “Run this” or “improve this” permits
execution within the supplied scope once material choices are resolved; do not
ask for permission again when it is already present. Scope and external-action
rules still apply. Creating a schedule requires an explicit scheduling request
with its necessary details, using the runtime's supported automation mechanism.

Use the bundled [execution guide](references/execution.md) for state,
retries, recovery and notification behavior. Scheduling needs an actual supported
scheduler; a prompt alone does not keep running after a conversation ends.
