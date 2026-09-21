# Adapt to the project, not just its screens

Read only the relevant row. Reuse existing behavioral templates and customize goals; these are not mandatory extra personas or separate audits. For mixed projects select the consequential journey and its adjacent handoffs within the existing count/budget. Infer project type from supplied evidence; do not add an intake questionnaire.

| Project | Relevant people and success | Evidence and recovery probes | Do not infer |
|---|---|---|---|
| Web/mobile product | Actual user/operator; completes the intended task | UI state, saved result, permissions, interruption and correction | Backend enforcement or accessibility from appearance |
| API/CLI/developer tool | Developer, integrator, or operator as actually relevant; achieves the intended side effect | Exact command/request, sanitized response, exit status, persisted state; timeout, retry and idempotency | An HTTP success proves the intended side effect; new tool user lacks domain expertise |
| AI/agent automation | Delegator, affected operator, output reviewer; can judge, intervene and recover | Approved task, tool/action trace, output review, stop/escalation and partial completion | Fluent output proves correctness, tool execution or authorized action |
| Course/teaching | Learner and teacher when relevant; performs the intended learning task | Prerequisites, example, practice, feedback, transfer task; failed attempt and next explanation | Lesson completion, enjoyment or simulated student agreement proves learning |
| Service/internal procedure | Actual requester, fulfiller and accountable role; reliable handoff and completion | Service blueprint or authorized rehearsal with actor, time/state and outcome; absence, delay, changed owner and cancellation | A written procedure was executed; all steps need an app screen |
| Content/pitch/concept | Intended reader or decision-maker; understands enough to take the intended next step | Supplied text, evidence for claims, comprehension questions, alternative/workaround | Simulated persuasion proves demand, conversion or audience response |

A document-based rehearsal stays concept/design evidence. Actual CLI execution or a service rehearsal is interactive evidence with its precise method; distinguish sandbox from live service. A course plan alone cannot establish learning. Missing access means untested, not broken. Pure performance, security, financial, legal or scientific correctness needs suitable specialist evidence; explain the limited contribution of personas without pretending this skill certifies those properties.

## Two worked adaptations

**CLI:** T01 is a skilled developer trying this CLI for the first time. Goal: create exactly one test resource. Product syntax is unfamiliar, domain knowledge is retained. A supplied timeout response leaves creation unknown. Inspect the documented status/idempotency path; only an authorized isolated execution can establish what persisted. A documented safe retry may refute a conceptual duplicate-creation concern; it does not prove runtime enforcement.

**Course:** T01 is an experienced accountant new to the taught software. Goal: reconcile a sample discrepancy independently. Inspect whether examples, practice and feedback support that goal. A completion badge proves only completion. Recommend an observed transfer task with a new discrepancy; successful unaided reconciliation would weaken the concern about transfer. Do not invent real learner performance or schedule a live class.
