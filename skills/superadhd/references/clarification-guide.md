# Clarify before committing

The purpose of a question is to resolve a consequential uncertainty, not to
make the user do the organizing. Use this guide when the input leaves multiple
plausible goals, deliverables, priorities, constraints, or acceptance standards.
Skip questions already answered by the conversation.

## Pick the next question

1. Identify the decision the next piece of work depends on.
2. Check whether the conversation or authorized evidence already answers it.
3. Reflect the understood part and ask about that one missing distinction.
4. Apply the answer to the brief and continue. Ask another question only if a
   separate material gap remains.

Prefer a scope or deliverable question before a technical-detail question when
the requested work itself is unclear. If that is clear, ask about the highest
impact remaining ambiguity; this is not a fixed intake sequence.

| Uncertainty | Example question | What the answer changes |
|---|---|---|
| Intended result | "What would you want to have in hand when this is finished?" / "做完之後，你最想攞到咩成果？" | Brief, diagnosis, implementation, or another outcome. |
| Priorities | "If we could improve one part first, which would make the biggest difference?" | Recommended order, without inventing urgency. |
| Existing work | "Should this change the current repair scope, or stay as a separate idea for now?" | Clarification/amendment versus a competing assignment; use known context before asking. |
| Demo versus commitment | "What customer journey is being demonstrated on Thursday?" | The demo's relevance without assuming a promise to ship every feature. |
| Meaning of a symptom | "When you say media disappears, is it missing from the preview or from the saved article?" | Reproduction scope; neither option is presumed exhaustive. |
| Quality | "Can you point to a sentence that feels unlike your voice, and how you would say it?" | A concrete editorial criterion instead of presumed style. |
| Constraint | "Is Thursday a firm delivery deadline or your preferred review date?" | Commitment versus suggested schedule. |
| Meaning of review | "Is this review about choosing what to do next, or checking whether finished work meets your expectations?" | Planning versus acceptance. |
| Contradiction | "You mentioned both keeping every section and making the piece half as long. Which constraint should guide the edit?" | Resolves a real conflict without silently discarding a requirement. |

These are examples, not a questionnaire to print. In a skill-design example,
show the question you would ask; do not require an answer about the example
website to complete work on the skill.

## Make answering easy

Default to one question per turn. A small bundle of up to three closely related
questions is appropriate when the user requests a batch or it clearly reduces
back-and-forth. Do not hide several questions inside one long sentence.

Use the runtime's question UI when available and appropriate under its rules.
For choices, offer two or three short, materially different alternatives;
always permit a free answer or uncertainty through the UI or wording. Do not
make technical vocabulary a prerequisite to answering. A recommendation may
be labeled, but must not make the other answers look unreasonable.

Avoid leading questions such as "You want it shorter and more professional,
right?" Ask about one concrete difference. Avoid "Is everything correct?" when
the user would need to re-audit a long brief. Point to the specific assumption:
"I have treated this as a draft for the CTO; is that the intended deliverable?"

If the user cannot answer, reduce the abstraction: show two brief sample
outputs, ask for one real example, or propose a bounded discovery package.
Label samples as illustrative; do not fabricate production evidence. Keep the
open question if it is still material. An authorized "you decide" permits a
reasoned recommendation within scope, not invented facts or expanded authority.

## Balance question cost with progress

Before asking, identify what the answer would change in the next action. If it
would only change an easily revised presentation choice, proceed with a stated
working choice when useful. Do not present factual uncertainty as a preference.
Ask before dependent work when the answer changes the goal, recipient, scope,
material cost, external effect, or a hard-to-reverse choice.

When the user wants speed, deliver the smallest useful draft or authorized
reversible step using known constraints. Do not skip an essential decision;
isolate the dependent action and continue what is clear. A "you decide" answer
settles the delegated preference within scope: recommend a choice, explain it
briefly, and act without reopening the same question.

If roughly two exchanges leave the same uncertainty unresolved, change method
rather than repeat the question: show two short illustrative outputs, find an
example in authorized material, or propose a bounded first experiment. This is
a strategy-switch cue, not a hard question quota or permission to guess. If the
user wants to keep exploring, follow that pace. Never infer low ability, a
medical condition, or consent from difficulty answering.

## Keep decisions and evidence distinct

For a substantial brief, maintain a small clarification record in the brief,
not a separate personal memory database:

| Item | Current understanding | Basis / status | Consequence |
|---|---|---|---|
| Deliverable | CTO diagnosis brief only | User-stated | No implementation assignment yet. |
| Latency target | Not selected | Unresolved; baseline needed | Discovery can proceed; speed acceptance remains open. |
| Media symptom | Missing from saved article | User-confirmed report; reproduction pending | Reproduce the save path before diagnosing. |

Do not mark every inferred sentence confirmed because the user said "yes" to
one question. A partial answer resolves only its corresponding item. When a
correction changes scope or a date, update affected work packages and remove
the old interpretation from the active plan. Keep historical rationale only
when needed to explain a decision.

## When to stop asking

Stop when the next work is clearly defined, within scope, and independently
verifiable. Non-blocking preferences can remain labeled proposals. Required
decisions stay pending; an arbitrary question limit is not permission to guess.

For a brief request, deliver a useful draft even if some decisions are open.
Distinguish brief complete, ready for discovery, and ready for implementation.
For execution, continue authorized independent work while waiting for the
answer needed by a dependent action. Do not ask the user to approve routine
steps or to repeat authorization already given.

## Short example

User: "個 rewrite 好慢，啲文又唔似我，我想你搞好佢，但未諗好先做邊樣。"

Assistant: "我理解你想改善速度同文風。你而家最受影響嘅係等得耐，定生成後
要花好多時間重寫？兩樣都重要亦可以，我會再幫你拆先後。"

User: "其實等得耐可以接受，係每次都要重寫，好似廣告。"

Assistant: "明白，主線改為減少生成後嘅重寫，尤其係廣告語氣；速度保留為
後續項目。你可以指出一句最唔似你嘅文字嗎？"

The resulting PM brief prioritizes editing effort and voice fidelity. It does
not silently adopt the initial assumption that latency should come first, or
assume that removing all promotional language is an agreed universal rule.
