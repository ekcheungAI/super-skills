# Superloop Prompt Patterns

Choose one shape per stage; compose only the stages the project needs with
explicit handoffs and one overall budget. Do not concatenate every template. These are authoring templates,
not executable goals. Include readiness and the interaction clause from
[question checkpoints](question-checkpoints.md) in every runnable prompt. Replace placeholders with supplied context or clearly label
the result an incomplete draft. Include the actual target/input reference in the
final prompt. Never claim files or baseline measurements already exist.

## Improvement

Use the Enhancer's field names so its existing linter can check the filled prompt.
Add the deliverables field; users should not need to infer the final artifact from
the cycle ledger.

```text
/goal Improve [target] so [observable outcome for the consumer].
Inputs: [artifact/source and relevant context].
Baseline: [measure current result first if unknown]; primary metric/rubric [criterion]; fixed evaluation set [cases]; material improvement [threshold]; guardrails [preserved behavior].
Evidence routing: History: [required/optional/skipped] because [reason]; Online: [required/optional/skipped] because [reason].
Verification: [reproducible tests, sources or artifact evidence and output location].
Constraints: [behavior, cost, style and authorization to preserve].
Boundaries: [allowed edits and excluded systems].
Acceptance gate: [candidate validation allowing reversible refinement, and final deterministic/independent/owner acceptance; preserve any mandatory per-cycle gate].
Iteration policy: [exactly/at most N] Measure → Diagnose → Change → Verify → Decide cycles; one falsifiable hypothesis and one focused change each; compare with best-known state; keep material gains and revert regressions; in maximum mode stop after 2 consecutive cycles without material improvement; in exact mode stop unsupported changes and finish remaining passes with distinct verification/coverage. Hard budget and blockers apply to both.
Cycle ledger: [baseline, hypothesis, change, result, guardrails, decision, evidence pointer].
Deliverables: [final artifact and format/location], [comparison/evidence], [unresolved items].
Stop when: [target reached, no supported bottleneck, or cap].
Pause if: [missing material input, new scope/cost/authority, or evaluation-contract change].
```

See [the filled help-center example](example-improvement-prompt.md) for a complete
contract with explicit deliverables and an honestly unmeasured baseline.
See [the exact-pass example](example-exact-prompt.md) for a bounded improvement loop
that switches to verification after convergence.

## Audit or exploration

```text
Inspect [fixed target] to answer [question for the consumer].
Inputs: [source locations and context].
Run [exactly/up to N] passes covering [distinct perspectives or coverage].
For each pass: inspect evidence, record source locations, distinguish facts from hypotheses, and deduplicate prior findings. Do not edit the target unless explicitly allowed.
Acceptance: [coverage, source-backed findings and uncertainty requirements].
Deliverables: [one consolidated findings table with severity/evidence/action], [remaining uncertainties], [recommended next step].
Stop: [requested coverage/count and time budget]; report no new findings honestly.
Pause: [missing required source or unavailable access]. No external actions are authorized by this audit.
```

## Repeated processing

```text
Process [eligible inputs from source] into [output for consumer].
For each item: [read, transform, verify and record completion].
Eligibility and identity: [selection rule and stable ID; skip already completed items].
Acceptance: [output schema, quality tests and rejected-item handling].
Boundary: [allowed write location and source preservation].
Budget: [batch/item/time limit]; retry safe transient failures at most [N] times.
Deliverables: [processed artifacts], [manifest mapping input IDs to outputs and evidence], [exceptions requiring action].
Stop when: no eligible items remain or the budget is reached. Save a checkpoint for remaining items.
Pause if: [uncertain external effect, unavailable input or new authority]. Reconcile uncertain effects before retries; do not duplicate outputs.
```

## Monitoring

```text
Observe [source/state] for [meaningful event] for [duration/review date].
Check at [cadence and timezone]. This is a prompt specification; do not install a schedule unless separately requested.
Verify: [read-only signal and corroboration before alerting].
Notify: [authorized destination, event threshold, compact content and deduplication/recovery rules]. Keep unchanged checks quiet.
Record: [existing ledger location, timestamp, observed state, check/delivery errors and next action].
Budget: [check/runtime/retry limit]. Reconcile uncertain sends before repeating them.
Deliverables: [event alerts with source evidence], [minimal run record], [final status on expiry if requested].
Stop/pause: [expiry, cancellation, sustained failure, missing access, or destination/authority uncertainty].
```

## Handoff fields for composed or resumable work

Carry forward stage input/output and gate, count mode and remaining budget,
verified access/tools, accepted artifact, provisional candidate, evidence,
unresolved decisions and answer/resume rule. Use the existing checkpoint; do not
create a second ledger. See [project patterns](project-patterns.md) for examples.

## Quality pass before handing it over

- Is readiness verified, reported or missing, and does each prompt explain when to ask during execution?
- Can a fresh agent identify the target, input, desired result and allowed actions?
- Does the repeated unit fit the task, and is exact versus maximum count preserved?
- Are success criteria and final deliverables observable rather than “make it better”?
- Are unknown baselines and proposed criteria labeled honestly?
- Can the agent stop or report failure without inventing output or expanding authority?
- Is the prompt complete enough to run, or explicitly marked draft with open decisions?
