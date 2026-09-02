#!/usr/bin/env python3
"""
Detect when the English docs have drifted from their French source.

Background: docs/ holds one folder per language (docs/fr/, docs/en/). French is
the source of truth - content is written in French first, then translated.
Nothing in the build enforces that the English *content* is a current
translation: an editor can tweak the French and the English copy silently falls
behind. This applies to two kinds of file:

  * PAGES  - docs/fr/<name>.md  translated as  docs/en/<name>.md
  * ASSETS - docs/resources/.../<name>.svg  translated as
             docs/resources/.../<name>-en.svg  (the unsuffixed file is the
             French/source version that docs/fr/ pages reference; the "-en"
             sibling is what docs/en/ pages reference)

translation-sync.json at the repo root records, per file, the hash of the French
source its translation was last based on:

    {
      "pages":  { "warnings.md": "<sha256 of docs/fr/warnings.md>", ... },
      "assets": { "resources/images/serial-protocols/uart-framing.svg": "<sha256>", ... }
    }

A source whose current hash differs from its recorded hash is "out of sync": its
English counterpart may no longer match. The pre-commit hook
(scripts/githooks/pre-commit) runs `--staged` and refuses the commit; the MkDocs
build hook (hooks/check_translations.py) runs `--check` and aborts the build.

Typical workflow after editing French text (or a source .svg):
  1. Update the matching English file so it reflects the new French content.
  2. Run:  python scripts/check_translation_sync.py --accept-all
     (records the new French hashes - your assertion that EN is now caught up)
  3. git add -A && git commit

If a French edit genuinely needs no English change, step 1 is a no-op but you
still run step 2 to acknowledge it.

Commands:
  --staged        Check French sources staged in the index (used by the
                  pre-commit hook). Exit 1 if any are out of sync.
  --check         Check every French source against the working tree. Exit 1 if
                  any are out of sync. Used by the build hook and manual checks.
  --list          Print the sync status of every tracked file. Always exit 0.
  --accept NAME   Record the current French hash for a single page NAME
                  (language-relative, e.g. "step-6-lighting.md"). Repeatable.
  --accept-all    Record the current French hash for every page and every
                  translated asset, and drop entries for files that no longer
                  exist.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = REPO_ROOT / "translation-sync.json"
DOCS_DIR = REPO_ROOT / "docs"
ASSETS_SUBDIR = "resources"
SOURCE_LANG = "fr"
TARGET_LANG = "en"


# --------------------------------------------------------------------------- #
# tracked translation units
# --------------------------------------------------------------------------- #

@dataclass(frozen=True)
class Unit:
    kind: str          # "page" or "asset"
    key: str           # manifest key within manifest[kind + "s"]
    source_rel: str    # French source, path relative to the repo root (posix)
    target_rel: str    # English translation, path relative to the repo root (posix)

    @property
    def manifest_section(self) -> str:
        return self.kind + "s"


def _page_units() -> list[Unit]:
    root = DOCS_DIR / SOURCE_LANG
    units = []
    for path in sorted(root.rglob("*.md")):
        name = path.relative_to(root).as_posix()
        units.append(
            Unit("page", name, f"docs/{SOURCE_LANG}/{name}", f"docs/{TARGET_LANG}/{name}")
        )
    return units


def _asset_units() -> list[Unit]:
    """Every file under docs/resources/ that has a '<stem>-en<suffix>' sibling."""
    root = DOCS_DIR / ASSETS_SUBDIR
    if not root.is_dir():
        return []
    units = []
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        if path.stem.endswith(("-en", "-fr")):
            continue
        translated = path.with_name(f"{path.stem}-{TARGET_LANG}{path.suffix}")
        if not translated.is_file():
            continue
        key = path.relative_to(DOCS_DIR).as_posix()
        units.append(
            Unit("asset", key, path.relative_to(REPO_ROOT).as_posix(),
                 translated.relative_to(REPO_ROOT).as_posix())
        )
    return units


def all_units() -> list[Unit]:
    return _page_units() + _asset_units()


def _staged_units() -> list[Unit]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
        capture_output=True, text=True, cwd=REPO_ROOT, check=True,
    )
    staged = set(result.stdout.splitlines())
    return [u for u in all_units() if u.source_rel in staged]


# --------------------------------------------------------------------------- #
# hashing
# --------------------------------------------------------------------------- #

def _hash_bytes(data: bytes) -> str:
    # Normalize line endings so a CRLF/LF checkout difference never counts as a
    # content change.
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def _worktree_hash(rel: str) -> str | None:
    path = REPO_ROOT / rel
    return _hash_bytes(path.read_bytes()) if path.is_file() else None


def _staged_hash(rel: str) -> str | None:
    result = subprocess.run(["git", "show", f":{rel}"], capture_output=True, cwd=REPO_ROOT)
    return _hash_bytes(result.stdout) if result.returncode == 0 else None


# --------------------------------------------------------------------------- #
# manifest
# --------------------------------------------------------------------------- #

def _load_manifest() -> dict:
    data = {}
    if MANIFEST_PATH.is_file():
        data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    data.setdefault("pages", {})
    data.setdefault("assets", {})
    return data


def _save_manifest(manifest: dict) -> None:
    manifest["pages"] = dict(sorted(manifest["pages"].items()))
    manifest["assets"] = dict(sorted(manifest["assets"].items()))
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


# --------------------------------------------------------------------------- #
# checks
# --------------------------------------------------------------------------- #

def _out_of_sync(units: list[Unit], *, staged: bool) -> list[Unit]:
    manifest = _load_manifest()
    hasher = _staged_hash if staged else _worktree_hash
    stale = []
    for unit in units:
        current = hasher(unit.source_rel)
        if current is None:
            continue
        if manifest[unit.manifest_section].get(unit.key) != current:
            stale.append(unit)
    return stale


def stale_translations(*, staged: bool = False) -> list[Unit]:
    """French sources whose English translation may have fallen behind.

    Public entry point reused by the MkDocs build hook
    (hooks/check_translations.py). With staged=False, checks every tracked file
    against the working tree.
    """
    return _out_of_sync(_staged_units() if staged else all_units(), staged=staged)


def format_stale_report(stale: list[Unit]) -> str:
    bar = "=" * 78
    lines = [
        "",
        bar,
        " TRANSLATION SYNC CHECK FAILED - commit/build stopped on purpose",
        bar,
        "",
        "French is the source of truth for docs/. Each file's English copy is",
        "expected to be a current translation of its French original. The",
        "following French source(s) have changed since their English counterpart",
        "was last confirmed in sync (per translation-sync.json):",
        "",
    ]
    for unit in stale:
        lines.append(f"  * {unit.key}  ({unit.kind})")
        lines.append(f"      source : {unit.source_rel}")
        lines.append(f"      target : {unit.target_rel}   <-- review / update this")
    lines += [
        "",
        "HOW TO FIX THIS:",
        "  1. Update the English file so it reflects the new French content",
        "     (or confirm no change is needed).",
        "  2. Record that the translation is caught up:",
        "         python scripts/check_translation_sync.py --accept-all",
        "  3. Stage translation-sync.json together with your changes and retry.",
        "",
        "  In a genuine emergency a commit can bypass this with --no-verify, but",
        "  the build hook will still fail until the manifest is updated.",
        "",
        bar,
        "",
    ]
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# entry point
# --------------------------------------------------------------------------- #

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--staged", action="store_true", help="check French sources staged in the index")
    group.add_argument("--check", action="store_true", help="check every French source against the working tree")
    group.add_argument("--list", action="store_true", help="print the sync status of every tracked file")
    group.add_argument("--accept", metavar="PAGE", nargs="+", help="record the current French hash for PAGE(s)")
    group.add_argument("--accept-all", action="store_true", help="record the current French hash for every tracked file")
    args = parser.parse_args(argv)

    if args.list:
        manifest = _load_manifest()
        for unit in all_units():
            current = _worktree_hash(unit.source_rel)
            status = "ok" if manifest[unit.manifest_section].get(unit.key) == current else "OUT OF SYNC"
            print(f"  {status:<12} {unit.kind:<6} {unit.key}")
        return 0

    if args.accept or args.accept_all:
        manifest = _load_manifest()
        units = all_units()
        if args.accept_all:
            selected = units
        else:
            by_key = {u.key: u for u in units if u.kind == "page"}
            selected = []
            for name in args.accept:
                if name not in by_key:
                    print(f"error: no such French page: docs/{SOURCE_LANG}/{name}", file=sys.stderr)
                    return 2
                selected.append(by_key[name])
        for unit in selected:
            manifest[unit.manifest_section][unit.key] = _worktree_hash(unit.source_rel)
        if args.accept_all:
            live = {"pages": set(), "assets": set()}
            for u in units:
                live[u.manifest_section].add(u.key)
            for section in ("pages", "assets"):
                for gone in set(manifest[section]) - live[section]:
                    del manifest[section][gone]
        _save_manifest(manifest)
        print(f"Recorded {len(selected)} hash(es) in {MANIFEST_PATH.name}.")
        return 0

    stale = stale_translations(staged=args.staged)
    if stale:
        print(format_stale_report(stale), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
