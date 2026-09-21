---
name: superdesign
description: Design and build distinctive landing pages, portfolios, websites and product UI; redesign UX, onboarding flows and navigation across web, mobile/native and data-heavy interfaces; create Stitch DESIGN.md specifications; compare reference screenshots with rendered implementations; use Mobbin for new UX; handle purposeful interaction design; and route 3D/media work to the right specialist. Single design entry point for visual direction, responsive layout, specialist handoffs and evidence-based QA.
---

# Superdesign

Turn the brief into a coherent, usable interface and verify the actual result.
Use this as the everyday design entry point. Select the relevant mode internally;
the user does not need to choose another taste skill or load the old versions.

## Read the task

Infer the surface, audience, primary task, brand, references, existing stack,
and requested deliverable. For existing products, inspect nearby components,
tokens and interaction patterns before proposing replacements. Reuse available
project context; ask only when a missing decision materially changes the work.

State a short design read, for example: "A calm product dashboard for repeat
use, preserving the violet brand and emphasizing scanability."

For a brand-new design task (new site, app, screen or flow), or any UX-related
request (including existing-flow audits, navigation, onboarding, forms and
usability improvements), first follow [Mobbin research](references/mobbin.md)
before choosing or changing the UX. A fresh chat, typo fix, mechanical maintenance
or isolated animation timing change is not by itself a new design task.

Before implementation, classify the project surface using [project routing](references/project-routing.md).
Superdesign owns the brief, design contract and final acceptance; specialist
skills own their narrow implementation details. Handoff must name the selected
specialist, the exact scope, dependency and verification evidence.

Choose the mode:

| Request | Load and apply |
|---|---|
| Build or redesign a website, landing page or portfolio | [frontend](references/frontend.md), then [QA](references/visual-qa.md) |
| Dashboard, forms or multi-step product UI | The product section of [frontend](references/frontend.md), then [QA](references/visual-qa.md) |
| Stitch design system or screen instructions | [Stitch](references/stitch.md); a document alone needs no Stitch connection |
| Build, audit, improve, review, plan or name UI motion | Apply the bundled [motion guide](references/motion.md) |
| Match a screenshot, Figma design or existing reference | [QA](references/visual-qa.md) for fidelity; preserve the reference over default taste |
| Critique or audit without implementation | [QA](references/visual-qa.md), critique mode; report findings without unsolicited edits |

Load only relevant references. If an explicitly requested platform workflow is
available, follow its tool/runtime contract for that step. The bundled Product
Design QA helper applies only to its source-versus-rendered build workflow;
its absence does not prevent Superdesign's own implementation review.
Do not load the four old taste skills as additional rulebooks. The user only
needs `$superdesign`: apply the motion guide when motion is in
scope, retaining the parent task and its audit-only or implementation boundary.
For a substantial interactive build or UX improvement, include its Motion Gate
for the affected interactions; choosing to keep them static is a valid result.
Do not treat every general optimisation request as an animation request.

When a more specific project skill is a better owner, keep Superdesign as the
orchestrator and hand off rather than duplicating its instructions. Use the
specialist's current contract for video, 3D, slides, image generation, native
mobile, analytics or production deployment. Never pretend a handoff occurred
without reading the specialist and recording its result.

## Decide the visual direction

Start from user intent, existing identity and source evidence. For a new design,
consider a few materially different compositions, select the best fit, and
explain its reason briefly. Do not simulate scripts, random choices, measurements
or previous-project history. Randomness is not evidence of quality.

Use these optional dials to describe decisions, never as a fixed recipe:

| Context | DESIGN_VARIANCE | MOTION_INTENSITY | VISUAL_DENSITY |
|---|---|---|---|
| Everyday product UI | 3-5 | 1-3 | 5-7 |
| Marketing / portfolio | 6-8 | 3-5 | 3-5 |
| Expressive campaign | 8-9 | 5-7 | 2-4 |
| Existing design to preserve | Match evidence | Match intent and accessibility | Match task |

Values run from 1 to 10: predictable to experimental, still to cinematic,
airy to dense. A high motion value never requires unnecessary animations.
For a small fix, skip the dials and full design document.

Define a compact project design contract before substantial implementation:
typography, semantic colors, spacing, radii, layout rhythm, imagery, theme,
motion purpose and responsive behavior. Save it in the existing design document,
or a project `DESIGN.md` when one is useful. Avoid duplicate token authorities.

## Taste defaults

- Make hierarchy and content do the work. Avoid automatic dark gradient heroes,
  decorative badges, repetitive eyebrow labels, generic three-card sections,
  gratuitous glass, and oversized headlines that bury the primary action.
- Favor a purposeful sans family for modern interfaces. Editorial serif,
  centered composition, purple and warm palettes remain valid when they fit
  the brand. Use existing licensed fonts and local language glyph coverage.
- Start with coherent neutrals and one brand accent. Keep separate semantic
  colors for errors, warnings, success and data; never recolor errors merely
  to enforce a one-accent aesthetic.
- Choose a radius scale with component roles, not identical rounding everywhere.
  Repetition is useful for comparable items; vary composition where section
  purpose changes. Do not replace clear tables with carousels for novelty.
- Use concise, concrete copy. Avoid decorative metadata and em-dash flourishes.
  Preserve accurate quotations and required legal copy. Repeated CTA placement
  is fine; keep labels consistent when the action is the same.
- Use genuine assets and real product captures where they communicate value.
  Text-led design is valid. A seed in a placeholder URL is not semantic image
  search. Inspect imagery rather than assuming it depicts the named subject.
- Separate real claims from visibly labeled demo data. Never fabricate customer
  endorsements, testimonials, availability, product specifications or metrics.

These are defaults, not vetoes over the brief, source target or product system.

## Build and finish

Implement the requested core interactions and relevant loading, empty, error,
success and focus states. Preserve the existing framework and dependencies
unless changing them is part of the task. Check installed versions before use;
verify current official documentation when exact package APIs are needed.

Keep keyboard access, readable content, touch use, responsive reflow and
reduced-motion behavior intact. Choose theme support from the product contract;
do not automatically double scope by adding a second theme.

For builds, run relevant code checks and inspect the rendered result at desktop
and narrow widths plus the key interaction states. Apply the QA module, fix
material problems, and repeat the checks affected by fixes. Distinguish passed
checks, untested areas and actual blockers; never claim visual QA from code alone.

For specs, check completeness and internal consistency without inventing
browser evidence. End with the result or preview, what was verified, and any
material limitation. A skill invocation grants no extra publishing, uploading,
paid generation or Git authorization.
