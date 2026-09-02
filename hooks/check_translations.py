"""
Enforce translation integrity across all configured languages.

Two separate checks, both aborting the build with a hard PluginError:

1. COVERAGE. docs/ is organized as one subfolder per language code
   (docs/en/, docs/fr/, ...) per mkdocs-static-i18n's `docs_structure: folder`
   convention. Every markdown page that exists under one language folder is
   expected to have a same-named counterpart under every other configured
   language folder (e.g. docs/en/info.md <-> docs/fr/info.md). Nothing in
   mkdocs-static-i18n itself enforces that, so a page can silently go
   untranslated (or a translated file can silently drift out of the nav due to
   a typo'd filename) without anyone noticing until a reader hits a 404 or an
   unexpected fallback.

2. FRESHNESS. Even when every page exists in every language, an English page
   can fall behind edits to its French source (French is the source of truth).
   translation-sync.json at the repo root records the hash of the French source
   each English page was last translated from; scripts/check_translation_sync.py
   compares. A commit that changes docs/fr/*.md is blocked locally by
   scripts/githooks/pre-commit, and this hook is the backstop for anything that
   slips past it (--no-verify, a clone without the hook installed).

This hook runs early (default priority, before mkdocs-static-i18n's own
on_files at priority -100) so it sees the raw, un-reconfigured file list
straight out of docs_dir - each file's src_uri is still "en/info.md" /
"fr/info.md" etc. It cross-checks every language's page set and raises a
hard PluginError (which aborts the build unconditionally, independent of
`mkdocs build --strict`) listing every gap found, if any.
"""

import sys
from collections import defaultdict
from pathlib import Path, PurePosixPath

from mkdocs.exceptions import PluginError
from mkdocs.plugins import get_plugin_logger

# scripts/ is not an installable package; add it to the path so the freshness
# check has a single implementation shared with the pre-commit hook.
_SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from check_translation_sync import format_stale_report, stale_translations  # noqa: E402

log = get_plugin_logger(__name__)


def on_files(files, config, **kwargs):
    i18n_plugin = config.plugins.get("i18n")
    if i18n_plugin is None:
        return files  # i18n plugin not configured, nothing to check

    if i18n_plugin.config.docs_structure != "folder":
        return files  # this check only makes sense for the folder layout

    languages = [lang.locale for lang in i18n_plugin.config.languages]
    if len(languages) < 2:
        return files  # nothing to cross-check against

    # normalized (language-relative) page path -> set of languages that have it
    pages_by_language: dict[str, set] = defaultdict(set)

    for file in files:
        if not file.is_documentation_page():
            continue
        parts = PurePosixPath(file.src_uri).parts
        if not parts or parts[0] not in languages:
            continue  # shared/non-localized file living outside a language folder
        relative_path = PurePosixPath(*parts[1:]).as_posix()
        pages_by_language[relative_path].add(parts[0])

    missing = {
        page: sorted(set(languages) - present)
        for page, present in pages_by_language.items()
        if set(languages) - present
    }

    if missing:
        raise PluginError(_format_missing_translations_message(missing, pages_by_language, languages))

    log.info(f"Translation coverage check passed for languages: {', '.join(languages)}")

    # Every page exists in every language; now check that the English copies
    # (pages and translated .svg assets) are current translations of their
    # French source.
    stale = stale_translations()
    if stale:
        raise PluginError(format_stale_report(stale))

    log.info("Translation freshness check passed (docs/en is in sync with docs/fr)")
    return files


def _format_missing_translations_message(missing, pages_by_language, languages) -> str:
    """
    Build a deliberately over-explained error message. This is shown verbatim
    (mkdocs.exceptions.PluginError aborts the build and prints it as-is), so
    it needs to make sense to someone who has never heard of this hook,
    mkdocs-static-i18n, or the folder-per-language convention before.
    """
    bar = "=" * 78
    lines = [
        "",
        bar,
        " TRANSLATION CHECK FAILED - the build was stopped on purpose",
        bar,
        "",
        "This project requires EVERY page (every .md file) to exist in EVERY",
        f"configured language folder under docs/. Configured languages: {', '.join(languages)}.",
        "That means: if a page exists as docs/<lang>/some-page.md for one",
        "language, the exact same filename 'some-page.md' must also exist under",
        "docs/<other-lang>/ for every other language, even if it's a rough or",
        "unfinished translation. There is no such thing as an 'English-only' or",
        "'French-only' page in this project.",
        "",
        f"Found {len(missing)} page(s) that break this rule:",
    ]

    for i, (page, missing_langs) in enumerate(sorted(missing.items()), start=1):
        present_langs = sorted(pages_by_language[page])
        lines.append("")
        lines.append(f"{i}) '{page}'")
        for lang in present_langs:
            lines.append(f"     [OK]      docs/{lang}/{page}   (exists)")
        for lang in missing_langs:
            lines.append(f"     [MISSING] docs/{lang}/{page}   <-- you need to create this file")

    lines += [
        "",
        "HOW TO FIX THIS:",
        "  For each '[MISSING]' line above, create a new file at that exact path",
        "  (same filename, just placed inside the other language's folder), and",
        "  fill it in with a translation of the corresponding '[OK]' file's",
        "  content. Once a matching file exists in every language folder for",
        "  every page, the build will succeed.",
        "",
        "  Example: if docs/fr/glossary.md exists but docs/en/glossary.md does",
        "  not, copy docs/fr/glossary.md to docs/en/glossary.md and translate it",
        "  to English (or vice-versa).",
        "",
        bar,
        "",
    ]
    return "\n".join(lines)
