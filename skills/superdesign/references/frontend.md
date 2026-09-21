# Frontend composition and implementation

## Preserve or redesign

Detect new build, targeted improvement, or explicitly requested visual overhaul.
Inspect the existing render, content, brand tokens, routes and component system.
Preserve working navigation, analytics contracts, URLs, form field identifiers,
legal copy and accessible behavior unless the task authorizes changing them.
Do not infer a complete rebuild from "make this look better".

Improve hierarchy, typography, spacing and consistency before replacing entire
sections. Source matching takes precedence over stylistic novelty.

## Marketing and portfolios

Give each section a job: value proposition, explanation, evidence, comparison
or action. AIDA is an optional narrative aid, not a required page structure.
Design around real content and assets rather than filling a fixed template.

- Compose headline width, font size, image proportions and CTA together.
  Aim for a quickly readable desktop hero, commonly two or three headline
  lines, while allowing long translations, zoom and short viewports to reflow.
  Never clip text or shrink it below readability to satisfy a line count.
- Keep navigation compact and stable. Switch to a usable menu before links
  collide; implement opening, closing, keyboard operation and focus behavior.
- Make the primary action clear. Add a secondary action only if it serves a
  distinct user need. Repeat the same action where helpful with consistent text.
- Place real evidence where it resolves doubt. Trust logos may accompany the
  hero when useful; they require a genuine relationship, not brand decoration.
- Use cards for meaningful grouping or interaction. Use open layouts, rows,
  comparisons and grids when they fit better. Vary section rhythm deliberately,
  without forcing every section to have a unique layout.
- Plan bento cells from the actual item count. Verify spans at each breakpoint.
  Do not use dense auto-placement if it changes visual order relative to reading
  or keyboard order. Intentional whitespace differs from an accidental gap.
- Use progressive disclosure for secondary detail without hiding essential
  product information. Tables remain appropriate for comparisons and specs.

## Product UI

Prioritize task completion, learnability and repeated use over cinematic layout.
Keep established components, navigation, semantic states and design-system
conventions. An enterprise-looking brief alone is not reason to install a large
official component library. Use official systems when the platform requires one
or the project has deliberately selected it.

For relevant surfaces, handle validation, submitting, success, failure/retry,
empty/filter-zero results, disabled states and destructive confirmation.
Forms need persistent labels and associated helper/error messages. Tables need
readable headers and usable sorting/filtering when those actions are in scope.
Dense data may scroll within a labeled region; persistent controls must remain
reachable. Mobile layouts may retain useful columns rather than forcing every
surface into a single-column marketing layout.

Do not require monospace for every number. Use tabular figures for numerical
alignment where useful. Semantic status colors remain distinct from brand color.

## Engineering choices

- Reuse the existing framework, styling approach and component library. Use
  server/client boundaries only where that framework supports them. Keep browser
  interaction code in appropriate client components; avoid broad client wrappers.
- Check package manifests and the lockfile before adding imports. Follow the
  project's package manager and installed versions; avoid silent major upgrades.
- Use semantic HTML, proper links/buttons, visible focus and meaningful names.
  Match the current icon family. Prefer library glyphs to ad hoc icon paths;
  custom brand art is valid when deliberately sourced or requested.
- Use fluid sizing and explicit breakpoint behavior. Choose `svh`, `dvh`, or
  natural content height according to stability needs; a full-height hero is
  optional. Fix overflow at its cause rather than hiding it at the page root.
- Reserve image/media dimensions, use responsive sources, and prioritize only
  the actual critical asset. Load fonts with fallbacks and check accented and
  CJK text, descenders and actual wrap behavior in the browser.
- Use semantic color variables and component tokens. Honor required themes;
  preserve hierarchy and contrast in every supported theme.
- Use project assets first. Image generation is an optional asset workflow with
  the existing cost/upload authorization boundaries. Label mock product imagery
  as concept material and never present it as a real product screenshot.

Avoid rendering a fake screenshot from decorative rectangles. A functioning
component demo is appropriate and should be tested as UI. Do not substitute
invented logos or handmade approximations for assets in a fidelity target.

## Acceptance

Verify real narrow and wide viewports, typography at zoom, keyboard flow, primary
actions, form states, missing assets, and relevant console errors. Run targeted
build/lint/tests according to the change. Performance measurements, if reported,
must come from an actual run with conditions stated; do not equate a laboratory
score with observed field performance. Use the QA reference for visual evidence.
