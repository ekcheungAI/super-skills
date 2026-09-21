---
name: agency-agents
description: Select a specialist role for product planning, UX, UI, architecture, code review, security review, verification, documentation or repository hygiene. Use when the user asks for agency-agents or a named specialist. Roles add perspective, not permissions.
---

# Agency Agents — student selection

This is a portable selection of 12 adapted or original roles, not the complete
upstream Agency Agents repository. Eleven profiles cite upstream inspirations;
Repo Steward is original. Upstream: https://github.com/msitarzewski/agency-agents
at `ad9264e309bd5e5422c04784372d7841b1e5d604`, MIT; see
[upstream license](UPSTREAM-LICENSE).

Choose the requested role, or recommend the smallest relevant role for the goal.
Read its profile before applying it. For unclear goals use `superadhd`; for
simulated user perspectives use `superpersona`; for a design build use `superdesign`.

| Role | Instructions | Focus |
|---|---|---|
| `product-manager` | [Profile](references/product-manager.md) | Product Manager |
| `ux-researcher` | [Profile](references/ux-researcher.md) | UX Researcher |
| `ui-designer` | [Profile](references/ui-designer.md) | UI Designer |
| `ui-finish-gate-reviewer` | [Profile](references/ui-finish-gate-reviewer.md) | UI Finish-Gate Reviewer |
| `software-architect` | [Profile](references/software-architect.md) | Software Architect |
| `workflow-architect` | [Profile](references/workflow-architect.md) | Workflow Architect |
| `codebase-onboarding-engineer` | [Profile](references/codebase-onboarding-engineer.md) | Codebase Onboarding Engineer |
| `code-reviewer` | [Profile](references/code-reviewer.md) | Code Reviewer |
| `ai-code-security-auditor` | [Profile](references/ai-code-security-auditor.md) | AI Code Security Auditor |
| `reality-checker` | [Profile](references/reality-checker.md) | Reality Checker |
| `repo-steward` | [Profile](references/repo-steward.md) | Repo Steward |
| `technical-writer` | [Profile](references/technical-writer.md) | Technical Writer |

Give the role the goal, input evidence, allowed files, forbidden actions, output
and acceptance criteria. Use a native subagent only when supported and authorized;
otherwise apply the role in the current conversation and disclose that no separate
agent ran. Limit delegated workers to depth one and disjoint ownership. Follow
the runtime's completion/cleanup protocol. The parent verifies findings and owns
integration. These profiles install no tools, accounts, models or permissions.
An advisory review never grants permission to edit, publish or deploy.
