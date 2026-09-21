# Guide the user to useful personas

Read this before selecting the run size and presenting the roster. Draft a small feature-specific panel from observed roles, tasks, and conditions. The examples below are selection aids, not a mandatory cast.

Use the [template library](persona-templates.md) to turn the selected perspectives into concrete cards. Include template IDs in the roster and customize tasks, permissions, starting knowledge, recovery and disconfirming checks. Use [review modes](review-modes.md) to scale coverage without changing explicit user choices.

## Choose by risk

| Feature evidence or risk | Candidate behavioral perspective | Feedback it can contribute |
|---|---|---|
| A new visitor must understand an unfamiliar workflow | First-time product user; establish domain knowledge separately | Unclear value, terminology, entry points, and assumptions about prior knowledge |
| The task repeats frequently | Returning or frequent operator | Repeated effort, defaults, shortcuts, consistency, and efficiency |
| Multiple roles control or share work | Relevant member, approver, or administrator | Ownership, permissions, handoffs, approval states, and conflicting expectations |
| Users must commit money, sensitive information, or substantial effort | Cautious decision-maker with a relevant goal | Missing explanations, confidence in outcomes, control, and reversibility; no transactions without authorization |
| Work spans sessions, devices, or interruptions | Interrupted or returning user under those conditions | Saved state, resume behavior, feedback, retry, and recovery |
| The intended audience uses different input methods, devices, or languages | A user with one evidenced access/context constraint | Reading order, reachable controls, keyboard use, mobile constraints, or comprehension; label actual versus simulated testing |

Prefer materially different task conditions over five versions of a beginner. Do not insert an administrator in a single-user tool merely to fill a slot. A persona may cover several relevant dimensions, but avoid stacking so many constraints that the result is impossible to interpret.

## Show a preview before dispatch

Present one compact table:

| Proposed persona | Why relevant / evidence or assumption | Task and success condition | Expected feedback |
|---|---|---|---|

Include primary versus secondary/stakeholder priority and research/context/hypothesis basis in the table or one short note. The first persona need not be the paying customer: choose based on the current decision. When buyer, operator, and affected person differ, make that distinction explicit where it changes the product. Do not turn a small but consequential access need into an out-of-scope group merely because its frequency is unknown.

Then state the selected counts, why they fit the task, planned loop outputs, and limits. Follow the automatic sizing rules in SKILL.md: preserve supplied counts and infer any missing count. Show the preview and proceed; do not solicit a routine selection or wait for roster approval. The user can steer the roster or depth while work continues. Pause for selection only when the user explicitly requested it, or a material conflict prevents a coherent plan. A required target may still need clarification; a missing count does not.

If the user chooses fewer personas, retain coverage of the primary goal and materially different roles first; explain what becomes untested. More personas should add a distinct behavior or task rather than a fictional biography. Describe expected feedback as areas of investigation, never promised defects or predetermined negative reactions.

## Worked example: team invitation flow

Assume the inspected feature contains invitations, role selection, existing members, and expired links. A three-person panel could be:

| Persona | Task | Useful feedback |
|---|---|---|
| New invitee | Understand the invitation and join the correct workspace | Value clarity, identity/account choice, explanation of access, recognizable success |
| Existing member with an expired invitation | Reach the intended workspace or recover access | Duplicate membership, expired-state explanation, retry and navigation logic |
| Workspace owner | Invite someone with appropriate access | Role clarity, permission boundaries, pending/sent states, and revocation expectations |

Loop 1 asks why each role uses invitations and what access each expects. Loop 2 traces invite, accept, expire, retry, and revoke where supported. Loop 3 challenges suspected contradictions and recommends changes with acceptance checks. Without a running interface, these remain design/specification assessments; missing screens are evidence gaps.

The final report connects each proposed change to a user goal and a verified problem or labeled hypothesis. It does not promise that this panel represents all customers or validates market demand.
