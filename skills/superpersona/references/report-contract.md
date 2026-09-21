# Consolidated UX report

Scale detail to the run. Keep one finding per root cause; cross-reference affected personas, steps, and loops.

If a root cause is unknown, keep independently testable concerns as separate finding or validation IDs. Shared actor, screen, or severity does not make capacity enforcement, permission enforcement, and contact visibility one issue. A high-level theme may group IDs for readability, but each keeps its own evidence, disposition, and acceptance check.

## Compact Fast rendering

Fast defaults to one decision-led answer: verdict, compact roster/counts, supported findings, material unknowns, and the smallest next validation. Include each serious supported finding, even if that makes the answer longer. Fold evidence, impact and acceptance checks into the findings; do not print separate eight-part sections, full persona cards, matrices and ledgers unless needed for the decision or requested. Maintain sufficient working traces to support the answer. Do not create persistent files unless requested or needed for handoff.

Example shape for a concept (illustrative, not research): “Test the reminder idea before building. Two perspectives × one loop: occasional freelancer and frequent operator. Existing manual reminders are the stated workaround. The proposal leaves control of message timing unresolved; decide whether users preview or auto-send, then test that choice with a sample overdue invoice. Demand and actual delivery behavior remain untested.” A report may find no consequential issue; do not fill a findings quota.

Deep uses the full contract below, combining sections where clearer. Fast is a rendering choice, not permission to skip evidence discipline or hide execution limits.

## Report structure

1. **Verdict and scope:** separate assessments of product value, user flow, and logic/rules, each with its strongest evidence and remaining uncertainty. Include target/version/date, evidence modes, and limits of this simulated audit. Avoid a global pass/fail verdict when key steps remain untested. Product value hypotheses do not establish market demand.
2. **Run summary:** requested/selected review depth (Fast, Deep or Auto), execution method and any mode/count override; selected personas and maximum/exact loops, explicit versus inferred counts and the task-based selection rationale; actual loops, completed/failed review passes, agent launches and concurrency; early-stop reason if any. Count reviewed cases separately from executed user interactions and untested interactions. A completed concept review can have zero executed interactions. Include budget use only when measured.
3. **Persona coverage:** ID, template ID(s), goal, relevant context, basis/assumption, assigned tasks, expected feedback contribution, actual coverage, and omissions. Explain any difference from the initial roster preview.
4. **Journey and coverage matrix:** persona × task with execution status and finding IDs. Executed tasks use success/friction/product-blocked/untested; conceptual or static tasks use coherent/contradictory/unresolved. Include relevant dimensions and omitted cases. Separate access/tooling limits from product failures. Report what worked so fixes preserve it. Avoid invented conversion rates, timings, satisfaction scores, or population-level percentages.
5. **Prioritized findings:** use the compact table below, with detail beneath for reproducible issues.
6. **Loop progression:** the goal/assumption ledger from loop 1, journey evidence from loop 2, and challenged claims with dispositions from loop 3, as applicable to the chosen count. Include new/confirmed/disputed/rejected/fixed-and-verified IDs, changed versions, and remaining hypotheses. Include the logic map when relevant. Do not count duplicate reports as new defects.
7. **Recommended changes:** order by impact, decision urgency, and dependencies; include acceptance checks, conflicting persona needs, and any tradeoff. Separate observed errors, evidence-backed usability friction, and speculative preferences. For an idea, lead with assumptions to validate and build/reframe decisions, not a fictional bug backlog. Effort estimates require a basis; otherwise mark them unknown.
8. **Open questions and next validation:** untested paths, unresolved disagreements, evidence needed, and a focused real-user validation task if helpful.

## Finding table

| ID | Severity | Issue and category | Affected personas / step | Evidence and confidence | Status | Suggested fix |
|---|---|---|---|---|---|---|

For each material finding provide: environment/version, initial state, trigger and steps, expected versus actual behavior, provenance, evidence locator, impact, recommendation, and an observable acceptance check. Hypotheses need a validation method rather than fabricated reproduction evidence. Evidence locators must resolve to inspected material; do not manufacture files or screenshots. Each research suggestion should state what observation would contradict the assumption and what decision that would change.

## Severity and confidence

Severity reflects task impact, not how many agents agree:

For assumptions, unanswered design decisions, and evidence-only gaps in any review mode, use **decision priority** instead of defect severity: resolve before committing to the concept, before implementation/release, or during later refinement, with a reason. Keep severity **not applicable** unless a concrete artifact defect or consequential contradiction is supported. Predicted risk may be serious without being an observed failure. Do not assign High simply because the brief has not answered a question.

- **Critical:** observed severe harm or irreversible loss within the audited scope; identify precise evidence and affected conditions.
- **High:** a core task is blocked or seriously misleading, with no reasonable workaround.
- **Medium:** substantial confusion, avoidable errors, or friction with a workable recovery path.
- **Low:** localized clarity, consistency, or efficiency improvement with limited task impact.

Confidence is separate: **high** for directly reproducible or clearly inspectable facts; **medium** for strong but incomplete evidence; **low** for a plausible untested hypothesis. Label predicted impact as predicted even when the underlying interface fact is certain. A low-confidence potentially severe concern warrants validation, not an assertion of confirmed harm.

Preserve conflicting observations when sessions, roles, or expectations differ. A majority vote does not establish correctness. Report verified fixes only with before/after evidence from distinct recorded versions and a passing acceptance check.
