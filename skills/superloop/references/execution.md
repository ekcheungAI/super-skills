# Bounded execution

Freeze the target version, criteria, allowed edits, budget and exact/maximum count.
For improvement: measure a baseline, choose one evidence-backed change, apply it,
verify against the same criteria, retain gains and undo only your own regressions.
Never revert someone else's work or compare changed criteria as though identical.
For audits: give each pass a distinct question and consolidate duplicates.
For batches: assign stable input IDs, checkpoint completed items and avoid duplicate
side effects. Separate rejected items from successful outputs.

Record each pass: input version, action, evidence, result, remaining budget and next
step. Stop on cancellation, exhausted budget, missing dependent access or unsafe
scope. Maximum counts may end at convergence; exact counts use remaining passes
for distinct checks and honestly report no new findings.

Retries consume the budget. Retry only a diagnosed transient failure; preserve the
best accepted artifact and checkpoint if blocked. Ask one consequential question
when a user decision is needed. Silence is not approval.

Monitoring requires a real scheduler and an authorized destination, cadence,
timezone and expiry. Stay quiet on unchanged states unless periodic reports were
requested. Notify only meaningful changes or actionable failures. Do not promise
future execution from a prompt alone. Do not publish, spend, send messages or
change permissions beyond the user's explicit task scope.
