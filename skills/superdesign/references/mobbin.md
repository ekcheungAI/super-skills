# Mobbin research for new design and UX

## When to use it

Before selecting a direction for a new website, app, screen or user flow, call
Mobbin MCP to ground the design in relevant real interface examples. Also call
it for UX tasks on existing products: navigation, information architecture,
onboarding, checkout, forms, usability audits and flow improvements.

This is reference research, not permission to redesign beyond the task. Preserve
an audit-only boundary. Skip the research detour for isolated timing fixes,
copy typos, mechanical refactors and exact visual replication without UX decisions.
Honor an explicit no-external-research request. Reuse already inspected Mobbin
references within the same task when still relevant; do not repeat identical calls.

## Discover, call, inspect

1. Discover the actual Mobbin MCP tools exposed by the current runtime. Use tool
   search if available. Read the returned tool schema; never invent tool names,
   parameters, endpoints or account access.
2. Search using the platform, user goal and concrete pattern (for example mobile
   onboarding or desktop checkout), not just a fashionable brand. Send generic
   pattern terms; do not upload private screenshots, customer data or confidential
   briefs merely to find comparable interfaces.
3. Use available retrieval/view tools to inspect a small relevant set, normally
   two or three examples. Prefer complete flow sequences for UX decisions. A
   search-result title alone is insufficient evidence of the design pattern.
4. Record actual source URLs or IDs, the screen/flow inspected, concrete observed
   behavior, and what fits or conflicts with this project's users and constraints.
   Keep observations separate from proposed changes. Stop when references answer
   the design question; avoid an open-ended research exercise.
5. Summarize the chosen pattern and why, then continue the requested design,
   critique or implementation. Put this short evidence trail in the existing
   DESIGN.md or QA report when one exists; otherwise include it in the response.

Mobbin examples are inspiration, not proof of usability, conversion lift or
accessibility. Do not copy proprietary assets or claim permission to reuse them.
For screenshot matching, the user's visual source stays the fidelity target;
Mobbin research must not silently replace it.

## Unavailable or insufficient evidence

If discovery exposes no Mobbin tool, state that the integration is unavailable
in this session. If a call returns an authentication, permission or service error,
report that specific failure; do not describe every failure as missing access.
An empty result means no relevant result, not a tool outage. Retry only when a
specific recoverable issue justifies it; never loop on authentication failures.

Continue independent work with supplied references, the existing product, or
clearly identified public alternatives where permitted. Label the research gap
and do not invent Mobbin evidence or claim MCP verification. If the user requires
Mobbin-only evidence, pause only the decisions dependent on it. Adding this skill
workflow does not install/configure Mobbin or change credentials, subscriptions
or tool permissions.
