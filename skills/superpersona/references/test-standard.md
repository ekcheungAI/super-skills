# Acceptance standard and skill evaluation

## Acceptance for each persona audit

Before delivering a report, verify the following against the actual artifacts. Use pass, partial, or fail with a reason; do not manufacture a numerical quality score.

1. **Useful framing:** the target, intended decision, mode, version, and constraints are explicit. An idea can be reviewed without pretending there is an interface.
2. **Relevant panel:** personas differ in meaningful behavior, role, or context; each maps to a task and expected feedback. Selected template IDs and customized cards have a reason; generic biographies or filler roles do not satisfy coverage. Primary and secondary roles have a reason. Uncertain attributes are labeled.
3. **Stable simulation:** personas retain their knowledge, goals, and restrictions across loops; changes have a recorded cause. Other agents' opinions are not presented as fresh user observations.
4. **Traceable coverage:** cases include starting conditions, actions/questions, expected outcomes or rule sources, evidence, and results. Relevant omitted dimensions and untested paths are visible.
5. **Evidence integrity:** no invented actions, quotes, research, measurements, demand, compliance, or fix verification. Reported and inferred claims remain distinguishable from observations. No review-access failure is mislabeled a product defect.
6. **Distinct loops:** every loop answers a different question or tests a named unresolved risk. The challenge loop can reject or narrow findings. Duplicate reports are merged by root cause while preserving contexts and disagreement.
7. **Actionable decisions:** consequential findings connect user impact to a concrete change or experiment, with an acceptance/disconfirmation check. Suggestions respect actual constraints and dependencies.
8. **Bounded execution:** missing counts are selected from task scope without a setup gate, partial counts are completed automatically, and explicit counts and budgets are honored; selection rationale, plan versus actual work, and stopping reasons are recorded. Explicit requests to choose or approve the run before execution are respected. Resource ownership and permitted actions are respected; workers finish cleanly.
9. **Mode and interaction integrity:** explicit counts override Fast/Deep defaults; native execution does not require external API setup. Any persona interaction retains independent first-pass records, information boundaries and bounded exchanges. Do not label a native rehearsal as a MiroFish run.

An unsupported factual claim, unauthorized action, or concealed untested core path is a fail that requires correction before calling the audit complete. Evidence limitations may remain partial if clearly reported; never fill them with invented observations. Claim readiness only for the tested modes and scenarios.

## Evaluate changes to this skill

Skill-refinement rounds are different from the audit's persona loops. A refinement round runs a frozen skill version on a fixture, inspects the output against the criteria above, makes targeted corrections, and reruns affected cases. Counting files, headings, or persona mentions does not establish behavioral quality.

For a material extension, use three refinement rounds when requested:

1. **Concept baseline:** an unbuilt idea with uncertain audience/value and conflicting assumptions. Does the skill still produce useful decisions without inventing UI or demand?
2. **Design and logic:** a supplied flow with happy path, failure, permissions, and evidence gaps. Does the revised skill distinguish specification contradictions, hypotheses, and runtime unknowns?
3. **Challenge and regression:** retest an earlier case plus a fresh negative-control/uncertainty case. Check false positives, count discipline, persona drift, evidence handling, and remedy recommendations. Use different assessors when available.

Give an independent evaluator the frozen skill, original fixture, user request, and permitted resources. Do not reveal intended findings, previous conclusions, or the grader's answer key. If nested delegation is unavailable or disallowed for the evaluation, explicitly require sequential persona simulation and label it; this does not test parallel orchestration. Use temporary fixture workspaces, synthetic data, and no external mutations.

The parent grades the actual output against known fixture facts and this standard. Retain version hashes, prompt, output, finding dispositions, changes, and relevant limitations in the task's evaluation report. Report number of executed behavioral runs separately from declared scenarios and deterministic routing checks. A passing model run is bounded evidence, not proof that the skill works on every product.

Use synthetic evaluation fixtures and reserve at least one fresh case for a new revision. Historical private evaluation logs are not included in this edition. Run live-interface checks separately when claiming interactive execution support. Live customer research, compliance certification, and product improvement measurements are outside these synthetic skill evaluations.

## Retain reproducible evaluation evidence

For material changes, keep a small evaluation folder with a manifest: audit ID/date, hashes of the frozen SKILL.md and loaded references/scripts, fixture IDs and exact input files, complete worker dispatch/follow-up prompts, original outputs or durable resolvable locators, parent grades/dispositions, changes between revisions, and execution limits. Keep synthetic fixtures public and secrets/private source material out. A private input uses an authorized private locator and digest, not a copied transcript. Hash the evaluated artifacts, not a commit that cannot yet include its own evaluation report. If instructions change, record a new snapshot and rerun affected cases.

Include a parent-orchestrated three-loop native case before claiming full Deep orchestration: dispatch one assignment per persona per loop, synthesize between loops, then send bounded falsification tasks without other workers’ votes/severity. Also exercise a cross-project Fast case and a coherent negative control. Test mid-run steering as a separate recorded scenario when changing replan behavior. Report these behavioral runs separately from code unit tests and from actual live-user or engine execution. Older summary-only evaluations remain historical; do not backfill invented original outputs or hashes.
