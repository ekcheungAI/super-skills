#!/usr/bin/env python3
"""Check skill structure, local links, portable files and obvious secret patterns.
This is a package check, not a substitute for a dedicated secret scanner.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
NAMES = {"superadhd", "superpersona", "superdesign", "agency-agents", "superloop"}

def validate():
    errors = []
    skills = ROOT / "skills"
    if {p.name for p in skills.iterdir() if p.is_dir()} != NAMES:
        errors.append("Expected exactly five skill directories")
    for name in sorted(NAMES):
        p = skills / name / "SKILL.md"
        s = p.read_text() if p.exists() else ""
        if not s.startswith(f"---\nname: {name}\ndescription: "):
            errors.append(f"Invalid frontmatter: {p.relative_to(ROOT)}")
    files = []
    for folder in ("skills", "scripts", "tests", "docs", ".github"):
        base = ROOT / folder
        if base.exists():
            files.extend(p for p in base.rglob("*") if p.is_file() and "__pycache__" not in p.parts)
    files.extend(p for p in ROOT.iterdir() if p.is_file() and p.name != ".git")
    patterns = [
        r"-----BEGIN " + r"(?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
        r"gh[pousr]_" + r"[A-Za-z0-9]{30,}",
        r"sk-" + r"[A-Za-z0-9_-]{24,}",
        r"AKIA" + r"[0-9A-Z]{16}",
    ]
    for p in files:
        rel = str(p.relative_to(ROOT))
        if p.is_symlink():
            errors.append(f"Symlink: {rel}")
        try:
            text = p.read_text()
        except UnicodeDecodeError:
            errors.append(f"Non-text file: {rel}")
            continue
        if any(re.search(pattern, text) for pattern in patterns):
            errors.append(f"Possible credential (value withheld): {rel}")
        if p.suffix == ".md":
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
                if target.startswith(("https://", "http://", "#", "mailto:")):
                    continue
                target = target.split("#")[0]
                resolved = (p.parent / target).resolve()
                if not resolved.is_relative_to(ROOT) or not resolved.exists():
                    errors.append(f"Missing/non-portable link: {rel}: {target}")
    return errors, len(files)

if __name__ == "__main__":
    errors, count = validate()
    for error in errors:
        print(error)
    print(f"Checked {count} text files; {len(errors)} issues")
    sys.exit(bool(errors))
