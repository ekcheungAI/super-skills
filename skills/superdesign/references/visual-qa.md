# Design review and visual QA

Choose the review type before making a claim:

- **Critique:** inspect the existing surface and assess it against the audience
  and task. No external source target is required. Report prioritized findings;
  do not automatically redesign an audit-only request.
- **Implementation review:** inspect a rendered build against its brief and
  design contract, including interactions and responsive behavior.
- **Fidelity comparison:** inspect both a source visual target and a rendered
  implementation in a matched state. Both are required for a fidelity pass.

Code, file paths, a build pass, or an unviewed screenshot do not establish visual
quality. If rendering or source access is unavailable, state the exact missing
evidence, continue independent checks, and leave the affected review blocked.
Do not invent a source target just to satisfy the gate.

## Evidence loop

1. Open the actual source and implementation for fidelity work. Match route,
   content, theme, viewport, interaction/auth state, crop and device density.
2. Capture the content region. Remove browser chrome or device frames unless
   present in the source. Record CSS dimensions, pixel dimensions and density.
3. Present both images together in a single comparison input. Normalize copies
   without altering source evidence and record any resizing/cropping. Separate
   sequential image views are not a side-by-side comparison.
4. Review the whole composition, then matched crops when details are unreadable.
   Do not file differences caused solely by incompatible crops or pixel density.
5. Record actionable findings, fix in-scope build defects, capture the revised
   state and compare again. A source edit is not post-fix evidence.

For critique and implementation review, use the same inspection/fix discipline
but identify the brief or product goal as the criterion instead of claiming
pixel fidelity. Use browser tools permitted by the runtime and user preference.
Never label unexecuted interaction checks as passed.

## Review surfaces

Explicitly inspect each applicable surface:

- **Typography:** loaded font versus fallback, weight, size, line height,
  tracking, wrapping, truncation, descender clearance and small-text readability.
- **Layout:** region proportions, alignment, rhythm, gaps, grids, radii,
  elevation, persistent controls, mobile reflow and overflow.
- **Color:** token consistency, foreground/background contrast, image overlays,
  supported themes, focus indication and semantic status distinctions.
- **Assets:** correct subject/logo, crop, resolution, transparency, distortion
  and fidelity. Code-drawn stand-ins do not match real reference imagery.
- **Content:** exact source copy when cloning, grammatical clarity, action
  labels, truthful claims, missing content and visible demo-data labeling.
- **Behavior:** core navigation, forms, menus, dialogs, keyboard focus, relevant
  loading/error/empty states, touch use and reduced-motion behavior.

Distinguish objective mismatches from taste preferences and intentional approved
deviations. A reference can itself have usability problems; record those
separately rather than silently changing the target.

## Findings and completion

Use P0 for unusable core flows or severe failures, P1 for major mismatch or
regression, P2 for material wrapping/proportion/overflow/state/polish defects,
and P3 for optional minor refinements. For each finding give location, source
versus actual evidence, impact and a concrete fix.

For a substantial build or fidelity handoff, save project-root `design-qa.md`
with review type, source/brief pointer, screenshot paths, viewport/density/state,
full-view and focused comparison evidence (or why crops were unnecessary),
findings, interaction and console checks, limitations, and iteration history.
Keep earlier findings, fixes and post-fix captures traceable.

Set `final result: passed` only when required evidence exists and no actionable
P0/P1/P2 issues remain. Otherwise use `final result: blocked` with the exact gap.
P3 refinements may remain. A first comparison can pass without forced edits;
after a material fix, a new comparison is required.

For quick critiques, report findings directly; a persistent report is optional.
If the separately installed Product Design workflow is explicitly in use,
follow its own current QA contract and template/runtime checks as well.
