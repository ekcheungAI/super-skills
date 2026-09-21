#!/usr/bin/env python3
"""Copy the five self-contained skills without touching runtime configuration."""
import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
NAMES = ("superadhd", "superpersona", "superdesign", "agency-agents", "superloop")

def install(destination, apply=False):
    dest = Path(destination).expanduser().absolute()
    sources = [ROOT / "skills" / name for name in NAMES]
    # Check every destination before creating anything. Never overwrite a skill.
    for source in sources:
        target = dest / source.name
        if target.exists() or target.is_symlink():
            raise ValueError(f"Already exists; review manually: {target}")
        if not (source / "SKILL.md").is_file():
            raise ValueError(f"Missing skill: {source.name}")
        if any(p.is_symlink() for p in source.rglob("*")):
            raise ValueError(f"Symlink in source: {source.name}")
    for source in sources:
        print(f"{'Copy' if apply else 'Would copy'} {source.name} -> {dest / source.name}")
    if apply:
        dest.mkdir(parents=True, exist_ok=True)
        for source in sources:
            shutil.copytree(source, dest / source.name)
    return len(sources)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", required=True, help="Your runtime's skills directory")
    parser.add_argument("--apply", action="store_true", help="Copy; default is dry-run")
    args = parser.parse_args()
    try:
        install(args.dest, args.apply)
    except (ValueError, OSError) as error:
        parser.exit(1, f"Install stopped: {error}\n")

if __name__ == "__main__":
    main()
