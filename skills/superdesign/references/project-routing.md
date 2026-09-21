# Project routing

Superdesign is the design entry point, not a replacement for every specialist.
Identify the dominant artifact and load the smallest specialist that owns it.
Keep the visual brief and acceptance with Superdesign; keep implementation
details with the specialist.

| Surface or request | Route after Superdesign intake |
|---|---|
| Website, landing page, portfolio, web app UI | `superdesign` frontend and QA references |
| Motion or interaction optimisation | the bundled motion guide, then return findings to Superdesign |
| Stitch `DESIGN.md` or Stitch screen prompt | Stitch reference; use the authorized Stitch integration if generation is requested |
| Screenshot/Figma/source matching | visual QA workflow; use Product Design QA when its build workflow is explicitly active |
| Mobile or native iOS/Android interface | the applicable native/mobile product-design skill; preserve platform HIG/material rules |
| Three.js, WebGL, shaders or spatial 3D | the applicable `threejs-*`, `genjutsu-*` or `scroll-world` skill; isolate canvas concerns |
| Video, Remotion, image generation or media production | the applicable video, Remotion or image skill; Superdesign supplies composition only when the task is also a UI surface |
| Slides, documents, data visualisation or dense analytics | the applicable presentation/document/data skill; do not force marketing-page card rules onto them |
| Backend, database, auth or deployment | the project's engineering/ops skill; Superdesign may review the user-facing surface after implementation |

Do not route based on a single keyword. Route by the deliverable, platform and
dominant risk. If two surfaces are genuinely coupled, name both owners and
define the handoff boundary. Keep one parent acceptance checklist and avoid
parallel edits to the same files.

If no specialist is available, continue with platform-neutral design reasoning,
state the missing capability, and avoid inventing APIs, package names or tool
results. A specialist handoff never grants permission to install packages,
connect accounts, upload assets, publish, deploy or message anyone.

## Handoff record

For work that crosses a specialist boundary, record:

1. Parent brief and affected surface.
2. Specialist skill and exact files or artifact it owns.
3. Inputs supplied and assumptions still open.
4. Acceptance checks and evidence returned.
5. Remaining work and the next owner.

For a small single-surface task, this can be one paragraph in the response.
For cross-session work, use the project's existing handoff or design document.
