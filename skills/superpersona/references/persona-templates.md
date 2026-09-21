# Reusable persona templates

Templates are behavioral starting points, not research participants or mandatory cast members. Select by the audited goal and observed roles. Customize every selected card; never paste a generic biography into a report. Demographics, diagnoses, spending power and preferences require evidence or an explicit relevant hypothesis.

## Build a panel

1. Identify the primary job, real roles, consequential decisions and relevant constraints.
2. Select the fewest templates that cover materially different behaviors. One persona can use a primary template plus one context modifier. Two template labels do not automatically mean two personas.
3. Ground each card in the supplied artifact/research; mark hypothetical additions. Evidence about one attribute does not validate the whole persona.
4. Give personas one shared task for comparison, plus a distinguishing branch. Keep common starting facts consistent; preserve legitimate differences in permissions and knowledge.
5. Show the roster, why each matters, and likely feedback areas. Start within the selected limits without a routine approval question. Record excluded roles and why.

## Template library

Replace bracketed objects with the actual feature. Each row includes a behavioral trigger and a check that could disprove the anticipated concern. Expected feedback is a question to examine, never a promised defect.

| ID / template | Choose when / avoid when | Goal and starting model | Task and recovery probe | Feedback / disconfirming check |
|---|---|---|---|---|
| T01 First-time user | Unfamiliar entry or onboarding; avoid assuming low domain knowledge solely from new account status | Reach first useful outcome; knows the goal but not product terminology | Find entry, interpret labels, complete first task; recover from a wrong choice | Discoverability and learning; concern weakens if visible guidance supports the next action |
| T02 Frequent operator | Repeated work is relevant; avoid inventing bulk operations in a one-off tool | Complete recurring work accurately with minimal repetition; knows normal path only | Repeat core task, inspect defaults; correct one mistaken action | Efficiency and consistency; test whether shortcuts preserve necessary checks |
| T03 Returning/interrupted user | Work spans sessions or breaks; avoid forcing persistence requirements on deliberately ephemeral tasks | Resume without losing orientation; remembers intent but not every previous step | Leave a partial task and return; reconcile saved versus unsaved state | Continuity and feedback; explicit resume/status cues may resolve the concern |
| T04 Cautious evaluator/buyer | Choice involves cost, effort or sensitive data; avoid adding a buyer to a free personal workflow | Decide with sufficient information and control; lacks internal pricing/data-policy knowledge | Compare terms before committing; inspect cancellation or withdrawal | Trust and informed choice; clear terms and reversible commitment may suffice |
| T05 Workspace owner/admin | Actual configuration or permission role exists; avoid single-user products | Grant appropriate access and retain control; knows policy but not hidden implementation | Invite/configure/revoke; recover from wrong role or expired invitation | Least-privilege clarity and ownership; visible scope and effective revocation can refute risk |
| T06 Member/collaborator | Shared work and handoffs exist; avoid inventing collaboration | Contribute within granted access; knows own work, not private admin context | Accept handoff, edit/share within scope; handle denied or changed access | Status, ownership and permission explanations; clear read-only states may be correct behavior |
| T07 Approver/decision-maker | Explicit review or approval step exists; avoid equating any buyer with approver | Make a justified decision from permitted evidence | Review, approve/reject; examine stale requests or conflicting decisions | Decision information and state transitions; explicit pending/approved rules may be coherent |
| T08 Service/inventory operator | Someone fulfills requests or manages scarce capacity | Deliver the promised outcome while keeping shared state accurate | Allocate/fulfill, cancel, reconcile; probe concurrent demand and repeated retry | Capacity, handoffs and recovery; a specified atomic allocation rule disproves a conceptual overbooking claim, not runtime failure |
| T09 Support/recovery user | A user-facing help or recovery path matters | Recover a blocked goal without unavailable knowledge or permissions | Follow an error, seek help, retry; preserve previously valid work | Actionable errors and escalation; a clear self-service path may make human support unnecessary |
| T10 Auditor/accountable reviewer | Traceability is an actual requirement; avoid asserting compliance duties without a source | Reconstruct who changed what and under which authority | Inspect a delegated/reversed decision and its history | Provenance and consistency; sufficient specified records can satisfy concept review while execution remains untested |
| T11 Access-constrained user | Relevant input, language, device or network condition exists or is a named stress case | Complete the same primary goal using the selected condition | Traverse core action and recover under one constraint | Reachability, reading order, comprehension or connectivity; actual tests or semantic evidence can overturn visual guesses |
| T12 AI-output reviewer | AI-generated output influences a task or decision | Determine what to accept, edit or reject; does not know hidden model reasoning | Inspect a draft/result, revise, reject or retry; handle unsupported or inconsistent output | Controllability, provenance and uncertainty; output can be useful without citations when the task is creative, so ground criteria in the actual job |

T09 represents a user seeking recovery. A support employee is a separate actual role only when the product exposes staff tools. Accessibility/design specialists are review lenses, not substitutes for T11 or claims of lived experience.

## Context modifiers

Apply only supported or explicitly hypothetical conditions: phone/narrow layout; keyboard-only input; screen reader; unfamiliar product language; low bandwidth/offline transition; time pressure; interrupted session. State what changes in the task and what remains constant. Do not bundle every disadvantage into one persona. A screenshot review cannot establish keyboard behavior, a programmatic name or assistive-technology compliance.

## Copyable persona card

```text
Persona ID / behavioral label:
Template ID(s) / primary or secondary priority:
Why this perspective fits this feature:
Evidence locator per material attribute / basis (research, context, hypothesis):
Goal / observable success criterion:
Starting knowledge / expected mental model:
Permissions / information visible / information unavailable:
Relevant context modifier / uncertainty:
Entry point / starting state:
Shared core task / distinct branch:
Likely first action (prediction) / information needed before commitment:
Failure or interruption / recovery task:
Help-seeking or stopping condition:
Expected feedback question / observation that would disprove the concern:
Loop assignments / stable facts / allowed scenario transitions:
Excluded scope:
```

For concept-only cards, success means a coherent proposed outcome, not a claim that a user completed an interface. Each card must support a runnable assignment under the worker contract, even when the review is sequential.

## Suggested panels — adapt, never use wholesale

| Product / decision | Fast starting panel | Deep additions when relevant |
|---|---|---|
| Personal capture or reading queue | T01 + T03, optional T09 | T02 and one justified T11 context; retain a small panel if other roles add nothing |
| Team invitations and permissions | T01 invitee + T05 owner + T06 member | T03 expired/returning context, T09 recovery; T10 only with traceability requirements |
| Checkout or subscription | T04 buyer + T01 new user + T09 recovery | T02 repeat buyer, relevant T11 condition; staff roles only if fulfillment is in scope |
| Booking, approval or scarce inventory | Actual requester (T01/T06) + T07 approver + T08 operator | T03 returning requester, T10 accountable reviewer when required |
| AI writing/generation tool | T01 new creator + T12 output reviewer + T03 interrupted creator | T02 frequent operator, T06 collaborator if shared review exists |
| Marketplace | Buyer T04 + seller T08 + recovery T09 | Actual moderator/approver T07, repeat participant T02; preserve conflicting incentives |

These panels are coverage suggestions, not representative population samples. Fast never suppresses a serious supported finding to keep the report short. Deep does not create extra personas simply to meet a range.

## Worked customized card

P1: first-time invitee, T01, primary. The supplied invitation spec says an addressed email must match the signed-in account (context-derived). Goal: join the intended workspace with the stated role. Knows sender and workspace from the visible invite; cannot see admin settings. Starts signed in to another account (hypothetical recovery case). Shared task: accept invitation. Distinct branch: wrong-account explanation and switch-account path. Success in specification review: a coherent route to the addressed account without granting unintended access. Stop if identity or workspace cannot be established. Feedback question: is account switching understandable? Disconfirming evidence: an explicit mismatch message naming the required account and a documented switch action. Loops: inspect value/identity rules, trace mismatch and expiry, then challenge any unsupported claim that a mismatch necessarily blocks joining. No invitation is sent or accepted without appropriate test authorization.
