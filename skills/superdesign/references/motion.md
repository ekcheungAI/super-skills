# Motion guide

Use motion to explain a state change, preserve spatial context or provide useful
feedback. First identify purpose, frequency, user context and rendering cost.
A static result is valid. Audit requests remain read-only.

1. Inspect existing behavior and the installed framework before changing it.
2. Prefer existing CSS or platform primitives for simple transitions; add a library
   only when the task needs it and its maintenance cost is justified.
3. Keep frequent actions quick and interruptible. Avoid waiting for decorative
   sequences before the user can interact. Do not animate essential text endlessly.
4. Preserve focus and keyboard operation. Honor reduced-motion preferences and
   provide an equivalent static state. Motion must not be the only status signal.
5. Prefer transform and opacity when appropriate; inspect actual rendering before
   making performance claims. Do not assume a property guarantees smoothness.
6. Exercise open, close, rapid repeated input, cancellation and resize. Check narrow
   and wide screens and reduced motion. A screenshot alone does not verify motion.

Record the interaction, purpose, states, implementation and observed verification.
Report untested conditions. No external motion skill or paid tool is required.
