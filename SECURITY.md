# Security and privacy

This repository is a curated, text-only student edition with fresh Git history.
It excludes private chat/evaluation logs, runtime configuration, account files,
API credentials, internal endpoints and personal workspace paths.
The installer copies the five skill folders only; it makes no network calls,
loads no credentials and does not change assistant configuration.

Before each publication:

- Review every added file and local link, including generated documentation.
- Run the package validator and installer tests.
- Scan the complete candidate tree and Git history with a dedicated secret scanner.
- Inspect matches without printing any secret value. Remove sensitive material
  before committing; deleting it from the latest version alone does not clean history.
- Check commit author metadata and archive contents for personal information.

Automated scans cannot prove the absence of all sensitive information. Do not put
real student/customer data in examples or commit environment files. If you find a
suspected credential, do not paste it into a public issue; notify the maintainer
privately through an already known channel and identify the file/location only.
