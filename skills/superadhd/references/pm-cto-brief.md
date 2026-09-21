# From spoken thoughts to a PM/CTO delivery brief

Use this reference for product and engineering input. The user provides the
raw thoughts; the assistant supplies the structure. A PM should understand the
problem, scope, priority, and acceptance. A CTO should understand the evidence,
technical unknowns, dependencies, and work that can responsibly be assigned.

## Drafting rules

- Ground requirements in a concise paraphrase of the user's intent. Label
  intent as user-stated/confirmed, proposed, or unresolved. Separately label
  technical evidence as reported, observed, or verified. A confirmed preference
  is not a verified reproduction. A proposal becomes a decision only with actual
  evidence of agreement.
- Make the handoff understandable without the chat. Include the affected
  product and journey if known, constraints, current versus desired behavior,
  evidence links, and the decisions still needed. Omit raw personal transcripts.
- Use lightweight IDs such as R1 and W1 when multiple requirements or packages
  need traceability. A small request can use one task with acceptance bullets.
- Assign work by outcome, not vague activities such as "improve performance".
  Each package should be independently checkable, or state the dependency
  preventing independent completion. Do not invent file ownership before
  inspecting the code; propose module or role boundaries where appropriate.
- Avoid an intake questionnaire. Produce the brief from available information
  with explicit gaps. Ask only for information needed to unblock the next
  assignment. Dates and estimates stay unspecified unless supported; proposed
  severity, priority, effort, or sequencing includes a reason and uncertainty.
- Reuse the receiving team's existing ticket/PRD format and acceptance or
  completion conventions. The format below is a recommended minimum when none
  is provided; it does not require adopting Scrum or a formal specification.

## Brief structure

Adapt the following sections to the size of the work; omit irrelevant sections.
For a substantial handoff, preserve all decision-relevant fields even when the
user-facing summary is short.

### 1. Product intent

- **Problem and affected user:** Who encounters what difficulty, in which journey?
- **Current / desired behavior:** What happens now versus what should happen?
- **Outcome and priority:** Why this matters, and what the user wants first.
- **Scope:** Included work, deferred work, and unresolved boundaries. Label
  assistant-suggested exclusions instead of treating them as user decisions.
- **Admission and current commitments, when relevant:** Distinguish captured
  ideas, proposed discovery, accepted backlog, and committed delivery. Reference
  ongoing work and its owner when known. State whether new input clarifies it,
  proposes an amendment, or belongs in a separate candidate item. Make capacity
  and displacement questions explicit without inventing availability or approval.

### 2. Requirements and acceptance

| ID | Required behavior or outcome | Intent status / source | Technical evidence | Acceptance evidence |
|---|---|---|---|---|
| R1 | Observable behavior, not an assumed implementation | User-stated, confirmed, proposed, or unresolved | Reported symptom, observed artifact, verified result, or unknown | Reproducible scenario or measurable result |

For bugs, capture reproduction steps, device/environment, actual versus
expected behavior, and frequency if known. Mark missing evidence explicitly.
For a feature, describe the user action, expected result, and material failure
or empty states. For performance, define the journey, timing boundaries,
conditions, and baseline collection before choosing targets.

Keep competing success criteria together. If the user wants speed and writing
quality, compare equivalent inputs and assess both. A candidate quality rubric
can include factual fidelity, completeness, requested language/tone, structure,
and editing needed; label it proposed until agreed. Do not invent a numeric
quality score or silently treat shorter output as an improvement.

### 3. Engineering assessment

- **Known evidence:** Reproduced behavior, measurements, relevant artifacts.
- **Unknowns / hypotheses:** Questions to investigate, separately from facts.
- **Affected areas:** Verified systems/modules, or candidate boundaries to inspect.
- **Approach:** A justified proposal with relevant tradeoffs; otherwise a bounded
  discovery task. Mention alternatives only when they affect a real decision.
- **Dependencies and risks:** Include compatibility, data handling, rollout, or
  rollback only when the proposed change makes them relevant. No generic audit.
- **Behavior at system boundaries, when relevant:** Identify what operations
  such as save, completion, retry, or reload promise and which system owns the
  result. Keep latency, reliability, data integrity, and other relevant quality
  constraints visible. Unknown behavior becomes a discovery question; do not
  invent architecture or force a nonfunctional-requirements checklist.

### 4. Work packages

Use a compact table or one small card per package:

| Field | Required content |
|---|---|
| ID / title | An outcome-oriented title; link to requirement IDs. |
| Owner | Confirmed person if known, otherwise a suggested role. |
| Scope | What this package changes or investigates; boundaries preventing overlap. |
| Inputs / dependencies | Evidence, decisions, or other packages needed first. |
| Deliverable | The tangible output and intended location if known. |
| Acceptance / validation | What a reviewer checks to accept it. |
| Reviewer / decision | Confirmed or proposed accepting role, and what that review decides. |
| Readiness | Ready for discovery, ready for implementation, or blocked, with reason. |

For discovery, add the question to answer, evidence scope, and stopping condition.
A documented inconclusive result is valid: include attempts, limiting evidence,
and the next discriminating check. Use an agreed budget when available; otherwise
propose a bounded first pass and flag any budget needed for assignment. Never
invent a timebox or keep investigating indefinitely until a cause is found.

Split packages when questions have independent evidence paths or owners. Reuse
shared reproduction/input collection; explain dependencies where splitting
would otherwise duplicate work. Keep a repair umbrella unassignable until
discovery has produced separately checkable implementation tasks.

Show the execution order and genuinely independent work. Include priority or
effort only if helpful and supported. Do not imply these packages have been
created in a tracker, accepted by an owner, or dispatched merely by writing them.

### 5. Decisions and review

List only material open decisions, their impact, and a recommended next step.
For each unresolved question, identify the dependent package and whether the
answer needs the user, the PM/CTO, or technical investigation. Record substantive
answers and propagate corrections to the active requirements and work packages.
Name the confirmed decision owner or a proposed deciding role for scope,
priority, and acceptance; this may differ from the execution owner. Do not
assume that a PM/CTO job title alone conveys the team's decision authority.
Specify what the next PM/CTO review will accept: discovery findings, an approach,
or completed implementation. A report being complete does not mean its fixes
are complete. Implementation acceptance does not itself authorize release;
apply the team's release criteria only when release is in scope. State the next
assignable package clearly.

## Example: mobile rewrite experience

This is a planning example, not a verified diagnosis or authorization to act.

**Intent:** Improve the journey from a mobile user submitting a link to receiving
a usable rewritten article with its intended media. Investigate latency while
preserving content quality. The product URL, stack, measurements, reproduction
conditions, and owners have not been supplied.

**User reports:** Rewrite problems, missing media, possible layout defects, slow
responses, and a wish for stronger articles/scripts. These are separate concerns;
they are not proof of a shared root cause.

**Proposed sequence:** Investigate rewrite reliability, media, and latency first;
baseline writing quality can run independently when inputs and capacity permit.
Retain layout and editorial improvements as candidates for follow-up; this does
not commit them to the current delivery scope.

| Requirement | Acceptance direction, proposed unless stated otherwise |
|---|---|
| R1 — Reliable link-to-rewrite journey | Document reproducible successes/failures; later fixes pass the agreed reproduction and failure-state checks. |
| R2 — Media retained or failure explained | Trace expected media through the journey; supported cases retain it, and unsupported/failing cases do not silently lose it. |
| R3 — Faster completion | Measure elapsed time under documented comparable conditions; set a target after baseline discovery. |
| R4 — Writing quality preserved/improved | Review matched input/output examples against a stated rubric; speed gains must not hide quality regressions. |
| R5 — Usable mobile layout | Identify affected views/devices, then define observable layout checks for confirmed defects. |

**W1a — Locate the media-loss boundary (R1–R2)**

- Suggested owner: engineer, with QA support where available.
- Inputs: product target/access and a representative failing link/device case.
- Scope: trace intended media through generation, save, and reload on a selected
  case, identifying the loss boundary if reproducible.
- Deliverable: reproduction/evidence record with a supported finding or an
  explicit inconclusive result and next discriminating check.
- Acceptance and stopping condition: complete the selected trace or document
  why it cannot be completed; report conditions, expected/actual behavior, and
  evidence. Propose additional investigation separately; no guaranteed diagnosis.
- Proposed reviewer: engineering lead, accepting the evidence and next experiment.
- Readiness: blocked on the target/access; ready for discovery once supplied.

**W1b — Establish where rewrite time goes (R1, R3)**

- Suggested owner: engineer; share representative inputs and reproduction setup
  with W1a instead of collecting them twice.
- Scope: measure start/end and observed stage timings for comparable runs.
- Deliverable: timing evidence and a supported next investigation or repair
  recommendation; state instrumentation gaps where timings cannot be obtained.
- Acceptance and stopping condition: the selected comparable run set is reported
  with conditions and failures, or the evidence gap is documented. A latency
  target remains proposed until the baseline and decision are available.
- Proposed reviewer: engineering lead for evidence, product decision owner for
  the eventual user-facing target; roles remain unassigned.
- Readiness: blocked on target/access and cases; independent of W1a findings.

**W2 — Establish the content-quality baseline (R4)**

- Suggested owner: PM/content lead, with engineering support for sample capture.
- Inputs: representative source/output pairs and the intended writing audience.
- Deliverable: proposed rubric and annotated examples of acceptable and weak output.
- Acceptance: factual fidelity, tone, structure, and editing effort are assessed
  on comparable examples; unresolved editorial preferences are explicit.
- Stopping condition: finish the selected sample batch or record missing
  evidence and unresolved preferences; propose further sampling separately.
- Proposed reviewer: designated content/product decision owner, not yet named.
- Readiness: ready for discovery once samples are available; can run alongside W1a/W1b.

**W3 — Implement selected repairs and verify the full journey (R1–R5 as selected)**

- Suggested owner: engineering; split ownership after W1a/W1b identify affected areas.
- Dependencies: W1a/W1b findings, W2 baseline, and selected scope/targets.
- Deliverable: verified repairs plus before/after evidence.
- Acceptance: agreed reproduction cases pass; speed, media handling, layout,
  and content quality meet the selected criteria under comparable conditions.
- Readiness: blocked on discovery and scope selection; not ready for coding yet.
  This is an umbrella, to be split into repair tasks after evidence is available.
  R5 layout candidates need their own reproduction and scope decision before
  being included; no unseen layout defect is implicitly assigned here.

**Next PM/CTO decision:** Supply the target and examples to unlock discovery.
After discovery, select repair packages and targets using the measured impact.
When this is merely an example during skill design, display these gaps; do not
interrupt creation of the skill to request the website's access details.

## Handling a new batch of ideas during ongoing work

Input: "The rewrite repair is underway. Also add streaming and team permissions.
Sales has a Thursday demo, but I have not promised features. Billing is in progress."

- Existing repair and billing: retain their known commitments; obtain references
  and owners only as needed to avoid duplicate or conflicting assignments.
- Streaming and permissions: captured ideas; scope, value, and admission remain
  unresolved. They do not become Thursday deliverables merely by being mentioned.
- Next proposed PM decision: establish the demo journey and whether any change
  to current priorities is actually needed. State what work a proposed change
  would displace and who can decide it.
- Technical lead: express accepted additions as a scoped amendment to the
  existing work or a separate package, with ownership and acceptance clear.

This can be a short update; it does not require a fresh PRD for every new thought.
