# Project-Sized Loop Plans

Choose relevant evidence, not every row. Check actual inputs/tools before claiming
readiness. A compact prompt may be one paragraph covering outcome, repeated unit,
input, acceptance, deliverables, boundary, count/budget and questions/stop rules.
Use the long contract only when complexity warrants it. Do not invent tool names,
source paths, performance numbers, access or publishing authority.

| Work | Evidence and acceptance | Deliverables |
|---|---|---|
| Code/product | Reproduction, related tests and visible behavior; preserve correctness and existing work | Verified patch, test evidence, remaining limitations |
| Research | Source-backed claims, coverage of the question, contradictions and freshness; check current external facts when needed | Cited answer, evidence table, explicit gaps |
| Design/UI | Named user flow, representative states/viewports and actual screenshots; independent/owner judgment for taste | Preview/artifact, visual comparison and usability findings |
| Content/teaching | Audience and learning/action goal, supported claims, clarity rubric, examples | Revised material plus concise rationale; final taste review if required |
| Data/batch | Eligibility, stable IDs, schema, completeness, deduplication and exception policy | Outputs, input/output manifest, rejected items, resume checkpoint |
| Monitoring | Reliable observation, meaningful threshold, deduplication, authorized destination and expiry | Event alerts, minimal run record, explicit failure state |

Separate candidate validation (safe to continue reversible drafting) from final
acceptance (objective checks plus required independent/owner review). An unavailable
mandatory checker is a real dependency, not permission to call self-review approval.

## Composed example: research into a teaching draft

One project plan, with one overall time/cost budget and bounded stage limits:

1. Research/audit: use supplied sources, identify supported claims and uncertainty.
   Output: evidence packet. Gate: enough verified material for the agreed question.
2. Process: convert the accepted packet into a teaching draft for the named audience.
   Output: draft referencing packet claims. Gate: no unsupported additions.
3. Improve: refine clarity against fixed criteria for at most the agreed number of
   passes. Output: provisional final draft and source/clarity checks.
4. Final acceptance: objective coverage check and owner review only if specified.

If research cannot support the intended claim, ask whether to narrow the claim or
obtain more evidence. Pause the dependent draft rather than fabricate a connection.
Stage retries consume the overall budget; do not return to research indefinitely.
Publishing remains separate from generating a ready-to-review draft.
