---
name: superpersona
description: Test an idea, product concept, feature, or UI/UX flow with relevant simulated user personas and independent reviewers. Select task-relevant personas and audit depth automatically, honor explicit run-size choices, and report value assumptions, logic gaps, usability errors, feedback, and prioritized changes with evidence. Use for persona-based product and usability audits, not persona marketing copy or visual style extraction alone.
---

# Superpersona

Determine whether a product solves the intended problem, whether its flow makes sense, and whether its rules produce understandable outcomes. Define task-relevant personas, run bounded independent walkthroughs, and produce a prioritized UX report. These are simulated perspectives, not interviews, real user research, or proof of usability.

## 1. Establish the target and run size

Reuse context for the idea or feature, intended audience, user goal, decision to make, and available brief, research, URL, local preview, design, screenshots, specification, or code. Inspect enough to identify the intended outcome, key journey, constraints, and scope. If the target cannot be identified, ask for it; do not select an unrelated project. A short idea description is sufficient to begin; do not demand screens for an unbuilt concept.

Read [review modes](references/review-modes.md) for Fast, Deep, Auto, native execution and optional bounded persona interaction. Explicit counts override mode defaults; an omitted mode never blocks the audit. Both modes work with the calling runtime and do not require a MiroFish installation. External simulation engines and their credential setup are not bundled in this student edition. If requested, explain that limitation; never claim a native audit ran an external engine.

For non-UI, AI automation, or mixed projects, read the relevant row in [project adaptations](references/project-adaptations.md); keep the same evidence and count rules. Do not invent human roles for a purely technical check.

Read [evidence and modes](references/evidence-and-modes.md) during intake. Select concept, research-informed, design, interactive, implementation, or mixed review. Distinguish what is proposed, reported, inspected, and exercised before constructing personas. Reuse authoritative product intent and design-system decisions; do not infer user needs solely from existing implementation.

Read the [persona selection guide](references/persona-selection.md) and choose the smallest useful panel and loop count from the task. Missing counts are routine planning decisions, not blockers: do not ask how many personas or loops to run merely because either was omitted. The user does not need to say “you decide.” Apply this order:

1. Honor explicit persona counts, loop counts, presets, maxima, exact counts, and time/cost limits from the current task context. If only one count is supplied, infer only the other. Do not replace an explicit choice with a default or expand it because the feature is complex.
2. Infer any missing values from distinct user roles, goals, journeys, consequential rules, recovery paths, evidence available, and requested depth. Use the table as a starting point; choose actual counts and explain why. “Quick” favors a compact check; “comprehensive” or “deep” normally includes three distinct loops. Thin evidence changes the type and confidence of findings; it does not prevent a concept review.
3. Show the persona roster, each persona's task and expected feedback, the chosen counts, loop outputs, and evidence limits. State which counts were explicit versus inferred, then immediately proceed. This preview is information, not an approval gate. Do not end at a recommendation or say the review is pending run-size selection.
4. Ask about sizing only if the user explicitly requested a choice/approval before execution, or if conflicting/invalid instructions or a binding resource limit prevent a coherent plan. Resolve harmless ambiguity using context; preserve explicit limits. For example, “exactly 0 loops” needs clarification, while “a few personas” invites judgment. Uncertainty about what count to choose is not a request to pause.

One loop is one pass by each selected persona over its assigned tasks.

| Task scope | Starting panel | Maximum loops when inferred | Coverage |
|---|---:|---:|---|
| Narrow idea or one short journey; quick check | 2–3 | 1 | Rationale, core journey, and the most relevant failure in a combined pass |
| Typical feature with distinct roles, branches, or recovery | 3–5 | 2 | Rationale/core journey, then recovery and evidence challenge |
| Comprehensive review or consequential, interconnected rules | 4–7 | 3 | Value and logic, journey and recovery, then evidence challenge |

If the user selects a named preset, keep its established counts: Quick = 3 × 1, Standard = 5 × 2, Complete review = 5 × 3, Broad = 7 × 3. A generic request for a quick or comprehensive audit can use the task-based ranges above; do not force a fixed preset unless selected.

These are workflow heuristics, not validated sample sizes or quality guarantees. Persona count follows meaningful perspectives; loop count follows review depth. A narrow concept can therefore use 3 personas × 3 loops when three loops are requested. Use fewer personas than a row suggests when coverage warrants it; never invent irrelevant roles to fill a quota. When auto-sizing, stay within 7 personas and 3 loops; report omitted scope rather than silently expanding. User-specified larger counts remain valid within explicit budgets and tool constraints. A 5 × 2 plan allows up to 10 persona passes, not necessarily 10 concurrent agents. More loops on an unchanged design do not create independent user evidence.

Example start: “I’ll use 3 personas × 2 loops for this invitation flow: new invitee, returning member, and workspace owner. The roles cover account choice, expired-link recovery, and permission decisions; the second loop checks recovery and challenges the findings. These are simulated perspectives based on the supplied specification.” Then perform the review without waiting for a reply.

Validate counts as positive whole numbers. If a real clarification is necessary, continue independent inspection and coverage preparation; do not treat silence as an answer to an explicit approval request. Read-only audit is the default; fixing the product requires a request to implement fixes.

When the user changes the target, roles, depth, or constraints mid-run, record the scope delta and evidence version, preserve completed history, and replan only remaining work. Stop incompatible active assignments; keep their results historical rather than merging them into the current verdict. Carry forward only findings whose evidence still applies. Report completed passes separately from the revised remaining plan; completed work still counts toward a cumulative budget and an unchanged total loop limit. A request for additional loops adds work only when explicit. Ask only if a material conflict cannot be resolved from the latest instruction; never reset the budget or restart all loops silently.

Record the selected persona count, maximum/exact loops, selection rationale, explicit versus inferred values, target version, audit mode, and any time or cost budget. Explicit requests to run exactly a count override convergence stopping, but still report access failures or safety stops honestly.

## 2. Define personas from the feature

Read the [persona template library](references/persona-templates.md), select relevant behavioral templates, and customize a card for every selected persona. Use its product panels as suggestions; record template IDs and evidence basis, avoid filler roles, and preserve explicit counts. Build a coverage matrix before dispatch. Each persona needs:

- Stable ID and a short behavioral label; use fictional, task-based profiles.
- Why this user is relevant to this feature, with a source or an explicit assumption.
- Goal, success condition, starting knowledge, and expected mental model.
- Context that changes behavior: experience, device/input method, language, interruption, permissions, or assistive technology where relevant.
- Assigned entry point, realistic task, and one likely failure/recovery scenario.
- Feedback contribution: the product decision, flow risk, or logic assumption this persona can help examine.
- Construction basis: research-derived, context-derived, or hypothetical stress case, with attribute-level uncertainty where material. Identify the primary persona and any secondary/stakeholder role.
- Task behavior: likely first move, information required before committing, and a condition for seeking help or stopping; label unsupported predictions.

Select distinct behaviors rather than cosmetic demographic variations. For example, an invitation flow may need a new invitee, a returning member, and an administrator with different permissions. A first-time mobile buyer, keyboard user, or interrupted operator is useful only when the target warrants it. Do not invent diagnoses or infer ability from demographic traits.

Include shared core tasks for comparison and distinct tasks for coverage. Explain omissions when the selected count cannot cover all material roles. Keep IDs, goals, initial knowledge, permissions, and constraints stable across loops unless evidence correction or a recorded scenario transition changes them. Reviewer learning must not silently turn a first-time persona into an expert. If a role replacement is necessary, record it and preserve historical results within the agreed count.

Design/accessibility specialists are review lenses, not automatically customer personas. Apply their checks in the parent synthesis or identify them separately if the user requests specialist agents; disclose any additional agent work. Show the concise roster and run plan, then proceed within the selected scope without another routine approval.

## 3. Execute independent walkthroughs

Use subagents when available for independent persona perspectives; this skill explicitly calls for bounded delegation. Keep worker depth at one and give each worker only its persona, target evidence, task, constraints, and the [worker contract](references/worker-contract.md). Do not give first-pass workers other personas' conclusions or a predetermined defect list.

Read the [coverage and logic guide](references/coverage-and-logic.md) when assigning cases. Select relevant dimensions and record covered, partially covered, untested, and not-applicable areas. Use its transition format for material logic branches. Comprehensive means deliberate risk coverage with explicit limits, not filling every checklist or promising to test all possible ideas equally well.

Keep one active assignment per persona. Reuse its worker for later loops where supported; record actual launches, completed passes, and failed passes separately. Use bounded batches (normally up to three workers, lower when resources require). Follow the runtime's completion protocol; in Codex, call `interrupt_agent` when a child finishes so it is marked done.

Never operate the same browser tab, app session, or mutable test fixture concurrently. Use isolated sessions/accounts/fixtures where available, or let one operator capture the journey and send evidence to the persona workers. Label evidence-only reviews accordingly. If delegation is unavailable, use separate sequential persona passes and disclose that there were no independent agents.

For each task, record the steps, expected behavior, actual evidence, outcome, recovery, and any likely user reaction. For exercised tasks, use success / friction / product-blocked / untested. Distinguish review-access/tooling blockers from product blockers. For a concept or static design, use coherent / contradictory / unresolved and record execution as not performed or not applicable. A persona should reason from what its user could see and know. Separate source-code analysis from the user's observable experience.

Evidence modes:

- **Interactive:** exercised the actual interface, CLI/API, or authorized service/procedure rehearsal; record the method, environment and reproducible steps. A real rehearsal is evidence only for its test conditions, not production or learning effectiveness.
- **Design/specification:** inspected supplied screens, prototype, text, or code; identify absent states as unknown, not proven broken.
- **Mixed:** label the evidence mode per finding and task.

These are evidence-access categories; apply the more specific intake mode from the evidence guide. In concept mode the journey is a rehearsal of a proposal, not executed product behavior.

Use only available, documented tools. Prefer local previews and safe test data. An audit does not authorize purchases, messages, production data changes, external uploads, or publishing. Stop before such a boundary and record the untested step; continue independent safe coverage. Simulate errors only in isolated test conditions without disrupting shared services.

## 4. Give each loop a purpose

For a three-loop run, keep the same personas and give each a distinct assignment per loop:

| Loop | Question | Work and required output |
|---|---|---|
| 1 — Product value and logic | Does this help this user achieve a meaningful goal, and do its rules make sense? | Inspect the intended job, current workaround, promised outcome, required information, permissions, and decision rules. Produce a persona-to-goal map and an assumption ledger. Mark inferred needs as hypotheses; flag unnecessary requirements or contradictions with evidence. |
| 2 — Journey and recovery | Can this user complete the goal and recover when something goes wrong? | Walk through entry, comprehension, actions, branching, completion feedback, and relevant failure/recovery states. Produce a journey matrix with reproducible errors, friction, and untested paths. |
| 3 — Evidence challenge and recommendations | Which findings survive scrutiny, and what should change first? | Give each persona a bounded claim to challenge and a task that could disprove it. Recheck high-impact issues, conflicting needs, logic branches, and proposed fixes against evidence. Produce a deduplicated issue register, reasoned dispositions, prioritized changes, and acceptance checks. |

Use the parent to translate persona expectations into a compact logic map where useful: starting state + action + condition -> next state + user-visible result. Compare expected and observed rules for role restrictions, validation, saved work, cancel/back, retry, and success as relevant. A persona's preference does not establish a functional rule; cite a specification or mark the rule as inferred. Do not claim backend correctness from screens alone.

In loop 3, try to falsify a finding rather than ask workers to endorse it. Give the task and claim without another worker's severity, vote count, or persuasive rationale. Preserve the original independent first-pass record. Classify each reviewed claim as supported, narrowed, rejected, disputed, or still untested, with reasons. Agreement is not a requirement for completion.

If fixes were separately authorized and applied, loop 3 may retest them against the recorded version and check nearby regressions. Otherwise recommendations remain proposals: never call an unchanged-design review fix verification. Only record fixed-and-verified after observing a changed artifact and a passing acceptance check.

For one loop, combine a brief rationale check with the main walkthrough and report the omitted challenge/recovery coverage. For two loops, combine rationale and the main walkthrough in loop 1, then recovery and evidence challenge in loop 2. Additional loops target named unresolved risks or changed versions; never repeat the same prompt to fill the count.

After each loop, the parent checks evidence for high-impact findings, merges duplicate root causes, preserves disagreements, and chooses the next tasks. Give the user a short checkpoint: completed coverage, material findings, uncertainties, and the next loop's purpose. Continue automatically within the chosen count and scope. Repeated reports of one issue increase persona reach, not defect count or statistical confidence. Keep a stable finding ID and status: new, confirmed, hypothesis, disputed, rejected, fixed-and-verified, or untested.

Stop at the selected maximum, the agreed budget, or earlier when all planned coverage is complete and a further loop has no new actionable findings or unresolved testable risks. Explain early stopping and report planned versus completed work. If the user requested an exact count, use remaining passes for distinct evidence checks and report no-new-findings honestly. Never extend the count silently or promise an error-free product.

## 5. Produce the consolidated report

Read and use the [report contract](references/report-contract.md), including its compact Fast rendering. Keep detailed cards and trace records in working evidence; they need not all appear in the visible answer. Lead with whether the audited flow supports its intended tasks and the most consequential blockers, scoped to the evidence actually examined. Include what worked as well as errors and friction.

Before delivery, check the acceptance criteria in the [persona test standard](references/test-standard.md). Correct unsupported claims and any materially incomplete planned coverage; mark genuine evidence limits. For skill maintenance or evaluation requests, that reference also defines how to run independent refinement rounds without confusing them with the audit's persona loops.

Deliver the report inline or in the target project's verified writable `drafts/` location, using its existing conventions. Link any saved artifact. Keep raw personal data and secrets out of evidence. Do not modify the audited product as part of writing the report. End with prioritized fixes and the smallest useful next validation, such as a specific real-user task, rather than automatically launching another run.
