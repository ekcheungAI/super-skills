# Stitch design specification

Translate the selected design contract into a semantic `DESIGN.md` for screen
generation. Explain visual intent alongside exact tokens and component behavior.
Writing this file requires no Stitch account or tool connection. Generating
screens requires an available authorized integration; report the distinction.

For an existing product, extract its system instead of imposing old taste
defaults. Preserve established accents, typography and navigation. For a new
product, infer a coherent direction from the brief and name assumptions.

Use this document shape, adapting depth to the project:

1. **Purpose and atmosphere:** audience, primary task, surface type, mood and
   density. Describe the composition in understandable visual language.
2. **Color roles:** semantic token, descriptive name, concrete value, foreground
   pairing and use. Separate brand accents from semantic feedback colors.
3. **Typography:** available family and fallback, weights, size/line-height scale,
   letter spacing and language coverage. Describe the intended hierarchy.
4. **Layout and responsiveness:** containers, grid, spacing, key breakpoints,
   reflow, navigation changes and image crop behavior. State reading order.
5. **Components and states:** button roles, radius scale, borders, elevation,
   inputs, navigation and product-specific components. Specify hover/focus,
   loading, empty, error, disabled and success states where applicable.
6. **Motion and accessibility:** purpose and approximate timing, keyboard/touch
   behavior and reduced-motion alternatives. No mandatory perpetual animation.
7. **Assets and content:** real asset references, slot sizes, crop, copy and
   visibly labeled placeholders. Record unavailable assets without inventing them.
8. **Constraints and acceptance:** brand-specific patterns to preserve/avoid,
   supported themes and states, and what the resulting screens must demonstrate.

Use concrete values once chosen, e.g. "panel corners 12px; compact controls
8px", instead of untranslated utility classes. Document a justified two-column
mobile table if needed; do not demand single-column collapse for every surface.
Check consistency between component descriptions, tokens and examples.

When screen generation is requested and authorized, send only relevant context
through the available tool, inspect the actual returned screens, then refine
observed mismatches. Do not claim `DESIGN.md` alone guarantees generator fidelity,
working interaction code, or accessibility. A generated source screen can become
the target for implementation comparison using the QA module.
