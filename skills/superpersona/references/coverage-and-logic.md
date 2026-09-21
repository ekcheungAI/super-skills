# Persona test coverage

Read when planning tasks and loop 2. Cover relevant risks comprehensively without turning every small idea into an exhaustive checklist.

## Build the test matrix

Choose tasks that distinguish the personas' needs and include one shared core task when comparison is useful. For each case record:

`Case ID | persona | goal | initial state/data | action | condition | expected outcome and rule source | evidence available | loop | result`

A case needs an observable success condition or, in concept mode, an explicit question of consistency. Vary one important condition at a time where possible. Keep input data and versions stable when comparing personas or designs. Record counterbalancing/order limitations when the same reviewer learns the flow; repeated passes are not fresh-user observations.

## Select relevant dimensions

| Dimension | Questions to apply when relevant |
|---|---|
| Value and adoption | What job improves over the current workaround? What effort, cost, trust, or habit change is required? Who uses, pays, approves, or bears consequences? |
| Information and content | Does the user know where to start, what a term means, what is required, and what will happen next? Are errors specific enough to act on? |
| Interaction and efficiency | Can the primary and returning users complete the task? Do steps or defaults create unnecessary work? Are destructive actions reversible? |
| State and service behavior | What happens during pending, partial success, failure, stale data, timeout, interruption, retry, resume, and confirmed success? |
| Logic and multi-role work | Do permissions, eligibility, limits, ownership, approvals, expiry, and handoffs produce consistent visible outcomes? |
| Inclusive access | Can the relevant task work with keyboard, focus movement, programmatic names, status announcements, zoom/reflow, language, and the actual device/context? |
| Trust and control | Are data use, automation limits, commitments, uncertainty, consent, and recovery understandable where consequential? |
| System fit and dependencies | Does a proposed fix preserve established components and terminology? Which evidenced shared flows, services, or support processes might change? |

Mark a dimension **covered**, **partially covered**, **untested**, or **not applicable**, with a reason. Missing tools or material mean untested, not not applicable. A covered dimension means its selected cases were examined, not that every possible defect is excluded. Persona count and loop count are not substitutes for coverage.

## Inspect transitions

For each consequential transition use:

`given state + actor + action + condition -> resulting state + visible feedback + saved data + recovery`

Separate prescribed rules from assumptions. Check boundary values or competing actions only when the feature warrants them: last available slot, two actors claiming it, retries after a timeout, expired authorization, rejected eligibility, or a partial operation. A timeout can mean the outcome is unknown; it does not automatically prove failure. Reuse an existing adequate state rather than inventing a new screen per condition.

Trace a high-impact recommendation into the actual dependent tasks or roles. Explain affected scope and unresolved dependency questions. An expert lens can spot a potential rule defect, but simulated persona preference cannot prove that the implementation violates a requirement.

## Accessibility evidence

Report the precise method: visual inspection, semantic/source inspection, keyboard execution, or assistive-technology execution. A visual icon without text may still have a programmatic name. Do not convert missing visual evidence into a confirmed inaccessible control, and do not claim compliance from this audit. If a numeric standard or criterion is material, verify it against current authoritative documentation and state the review baseline. Do not invent scores or simulate disability as if it were lived experience.

## Compare proposed fixes

When a tradeoff matters, evaluate options against the same persona goals and constraints. Include an acceptance example: `given X, when Y, then visible Z; verify data/recovery W`. Distinguish the expected benefit from a verified effect. Do not prescribe a fix merely because it attracts more persona votes.
