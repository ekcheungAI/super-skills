# Super Skills

Five practical workflows for working with an AI assistant. Start with a messy idea,
review it from useful perspectives, design the result, bring in a specialist, and
improve it in bounded rounds.

[繁體中文入門](docs/QUICKSTART.zh-HK.md) · [Security and scope](SECURITY.md) · [Attribution](THIRD_PARTY_NOTICES.md)

## Download

**[Download ZIP](https://github.com/ekcheungAI/super-skills/archive/refs/heads/main.zip)**,
then extract it, or clone:

```bash
git clone https://github.com/ekcheungAI/super-skills.git
cd super-skills
```

| Skill | What it helps with | Example prompt |
|---|---|---|
| [superadhd](skills/superadhd/SKILL.md) | Clarify messy thoughts and choose the next useful action | “Use superadhd to help me organize my final project ideas.” |
| [superpersona](skills/superpersona/SKILL.md) | Review a concept or flow with simulated user perspectives | “Use superpersona fast to review this course signup flow.” |
| [superdesign](skills/superdesign/SKILL.md) | Plan, build and verify an interface | “Use superdesign to improve this student club homepage.” |
| [agency-agents](skills/agency-agents/SKILL.md) | Apply one of 12 specialist roles | “Use agency-agents with the code-reviewer role on this diff.” |
| [superloop](skills/superloop/SKILL.md) | Plan or run bounded repeated work | “Use superloop to improve this draft for at most 3 rounds.” |

## Get updates

From your cloned folder, run:

```bash
git pull --ff-only
```

Keep personal edits in your own project. If you installed copies of the skills,
review and update those copies after pulling; the installer never overwrites them.

## Start without installing

Open this folder in your coding assistant. Ask it to read the selected
`skills/<name>/SKILL.md` and the references that skill requests, then give it your
task. This works without relying on a particular automatic skill-discovery feature.
For a chat-only assistant, provide the skill file and relevant reference files;
it can reason about supplied material but cannot verify tools or files it cannot access.

## Optional installation

Requires Python 3.10 or newer. Find the **skills directory supported by your installed
assistant/version**. Copy each whole folder under `skills/` there, keeping its
`SKILL.md`, references and licenses together. These are skill folders, not native
subagent configuration files. Do not put them in a runtime's agent-config directory.

The optional installer accepts your chosen destination explicitly. For example,
a project-local destination (only if your runtime supports `.agents/skills`):

```bash
python3 scripts/install.py --dest .agents/skills
python3 scripts/install.py --dest .agents/skills --apply
```

The first command previews; the second copies. Existing same-name folders or
symlinks stop the entire install before any files are copied. Review conflicts
manually; there is no force-overwrite option. Installation changes no runtime
settings, credentials, hooks or permissions and makes no network requests.
Reload your assistant's skill discovery or start a fresh session, then ask it to
identify the loaded skill file. Automatic discovery varies by runtime/version;
the explicit read-file method above remains the fallback. To uninstall, remove
only the five folders you copied, after saving any changes you made to them.

## A classroom exercise

Use a fictional student-club event page. Do not supply classmates' personal data.

1. **Clarify:** use superadhd to define the audience, goal and one-page brief.
2. **Review:** use superpersona with 3 personas and 1 loop; ask for assumptions
   and friction, clearly labeled as simulated.
3. **Design:** use superdesign to implement an accessible signup page using fake data.
4. **Check:** use agency-agents with reality-checker to exercise the page if browser
   tools are available, otherwise report what remains unverified.
5. **Improve:** use superloop for at most 2 rounds against the same acceptance criteria.

A persona simulation is not user research. A role is an instruction, not a new
permission or an independently running agent. A loop prompt is not a scheduler.

## What is included

The four Super skills retain their detailed workflow and local reference guides.
Agency Agents is a curated student adaptation with 12 role profiles, not the full
upstream repository or its runtime integrations. Motion and loop execution have
self-contained student guides. External MiroFish setup, private evaluation logs,
internal project wiring and personal configuration are excluded.

No API keys or additional provider setup are needed by these files or installer.
You still need your own AI assistant and any account it requires; its normal usage
limits/costs apply. Optional tools such as browsers, Mobbin, Stitch or delegation
are not installed or guaranteed. Report unavailable capabilities honestly and use
the documented fallback. Do not upload private material to external services
without authorization.

## Contributing and checks

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests
```

Use synthetic examples. Check changes with a dedicated secret scanner before
publishing, including Git history. The built-in validator is only a first check.
Package structure and installer behavior are tested; no claim is made that every
AI runtime or live model has been tested with this edition.

MIT licensed; retain the bundled Agency Agents license when redistributing.
