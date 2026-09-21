# Questions During Planning and Execution

Ask when an answer changes the next action, not to show activity. Carry the same
interaction contract into every stage and executor; an intake-only interview is
insufficient. Use the user's language and normal available question tools.

## Decision pattern

1. State the verified observation and its effect in one sentence.
2. Ask one concrete decision question; offer a recommendation and short tradeoff
   where useful. Separate facts, user reports, proposals and unknowns.
3. Mark the dependent step awaiting input and save the checkpoint. Continue
   independent work; do not decide on the user's behalf just because time passed.
4. Incorporate the answer into the active contract: target, deliverables, scope,
   criterion, dependency, count and remaining budget as affected. Retire conflicting
   assumptions. Changing criteria requires the proper review and a new baseline.

Use existing answers and standing authorization. A user selecting a format is
not authorization for an upload. Do not use an optional preference tool for
permission escalation; follow the runtime's prescribed mechanism.

| Moment | Ask if | Example question |
|---|---|---|
| Planning | Desired outcome is unknown | 「完成後，你最想得到甚麼？」 |
| Readiness | A necessary source is absent | 「要等完整資料，還是先做已提供部分並列明缺口？」 |
| Execution | The evidence exposes a real goal tradeoff | 「縮短後會刪走兩個必要例子；你較重視篇幅還是保留例子？我建議保留例子。」 |
| Execution | A rubric has ambiguous intended meaning | 「這裏的『完成』是草稿可審閱，還是必須已發布？」 |
| Recovery | Failed approach cannot proceed within scope | 「目前工具取不到歷史資料；先交現況分析，還是等資料補齊？」 |
| Final review | Owner judgment was explicitly retained | 「這是候選版本及對照證據；哪一處仍未符合你的預期？」 |

Do not ask when tests identify a routine fix, the answer is discoverable, the
brief is complete, or an unchanged result is an allowed outcome. Do not turn
examples in a skill-design conversation into new product tasks.

## State and unattended work

Use the existing task ledger/checkpoint, not private assistant memory. A compact
record is enough: contract revision, stage/pass, accepted artifact, provisional
candidate, evidence, remaining budget, unresolved question, owner and resume rule.
If no answer channel is available, persist `awaiting-input` and report that limit.
Notify once only if an appropriate destination is already authorized. Unchanged
scheduled runs must not repeatedly ask the same question. Resume only after an
answer or new evidence resolves the dependency; do not reset consumed budget.

## Portable interaction clause

Include a tailored version in each runnable prompt:

> Ask one focused question when missing information, conflicting evidence, a
> meaningful tradeoff or exhausted safe recovery changes the plan. State the
> observation and recommendation. Pause only dependent work, preserve the
> checkpoint and remaining budget, and update the active plan after the answer.
> Reuse existing decisions and authority; silence is not approval. For unattended
> runs, record awaiting-input and use only the authorized notification channel.
