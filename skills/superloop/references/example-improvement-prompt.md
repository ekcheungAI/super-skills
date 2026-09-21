# Example: Improve a Help-Center Answer

A filled planning example for a user who has supplied an answer and its approved
source notes. The baseline is deliberately measured during execution. The prompt
is a contract, not evidence that a run has occurred. In a new task, attach the two
inputs described below before asking the agent to execute it.

```text
/goal Improve the supplied help-center answer so a first-time user can follow its steps without guessing, while preserving every supported factual claim.
Inputs: the answer and approved source notes attached to this task. If either is missing, request it before editing. The consumer is a first-time product user.
Baseline: measure the original before editing using a clarity rubric: each action names what to do, prerequisites appear before the action, and each claimed result is supported by the notes. Freeze this fixed evaluation set for every version. Primary metric is the number of failed rubric checks; material improvement means at least one fewer failure. Guardrails: preserve supported facts, avoid invented features, and keep all required steps.
Evidence routing: History: required because this is an existing answer; read the supplied original and any revision notes that actually exist. Online: skipped because the approved source packet defines the scope; if external verification becomes necessary, report that gap before relying on an unsupported fact.
Verification: retain artifact evidence in a before/after rubric table with exact text excerpts, a source-to-claim checklist, and the final answer. Mark unsupported claims as unresolved rather than inventing support.
Constraints: revise wording and sequence only; no publication, external upload, or change to the approved sources. Treat clarity judgments as proposed until reviewer acceptance.
Boundaries: work on the supplied answer in the response only; do not edit unrelated files or product settings.
Acceptance gate: reproducible source and required-step checks permit further reversible refinement of provisional candidates; final acceptance requires human approval of the clarity comparison. Keep the original as the accepted baseline until then. No human review is required between drafting passes. Label the final candidate awaiting review if that review is unavailable; do not claim subjective acceptance.
Iteration policy: at most 3 Measure → Diagnose → Change → Verify → Decide cycles; use one falsifiable hypothesis and one focused change each cycle; compare with the best-known state; keep improvements as provisional candidates only when candidate checks pass and revert regressions; promote to accepted state only after final review. Stop after 2 consecutive cycles without material improvement. Do not silently self-approve final acceptance.
Cycle ledger: record rubric baseline, hypothesis, exact change, metric delta, guardrail results, acceptance status and evidence excerpts for each attempted cycle.
Interaction: ask one focused question if sources conflict, the goal is ambiguous or a tradeoff needs owner direction. Explain the finding and recommendation, pause dependent work, preserve the checkpoint and update the plan after the answer. Reuse existing answers; no response is not approval.
Deliverables: the best accepted answer as Markdown; any unapproved candidate separately labeled; a compact before/after table; the source checklist; unresolved questions and the reason execution stopped.
Stop when: all rubric checks pass and the acceptance gate is satisfied, no supported improvement remains, or the cycle cap is reached. If the original already passes, return it with the baseline evidence and no unnecessary rewrite.
Pause if: required inputs are missing, final acceptance needs the reviewer, source claims conflict, or the next step needs changed criteria or broader authority.
```
