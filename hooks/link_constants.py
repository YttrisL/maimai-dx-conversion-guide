"""
Let a Markdown page reference an external URL - or any other short piece of
text worth keeping in exactly one place - by name, instead of retyping it
wherever it's needed.

Background: this project links to a handful of external resources (a
Discord invite, a manufacturer's docs site, ...) from more than one page.
Nothing stops one of those copies from silently going stale relative to the
others when the target changes (an invite link expiring and getting
reissued, a manufacturer restructuring their site), and nothing catches a
typo'd URL either.

Constants live in `link-constants.yml` at the repo root, one YAML mapping of
UPPER_SNAKE_CASE name -> value:

    DISCORD_HANDEVICE: https://discord.gg/xABCFMWmTK

and are referenced from any .md page (either language - a constant is
shared across docs/fr/ and docs/en/, which is the point: the *place the
link points to* doesn't change between translations) as `{{NAME}}`, e.g.:

    [Sur le discord HanDevice]({{DISCORD_HANDEVICE}})

Substitution runs as on_page_markdown (before the Markdown conversion, same
stage as hooks/lightbox.py), skipping fenced code blocks and inline code
spans so a page that ever needs to show literal `{{...}}` syntax as an
example (documenting Jinja templates, for instance) isn't corrupted.

Only text shaped like a constant reference (`{{`, an UPPER_SNAKE_CASE name -
the same convention the file's own keys are required to follow - then `}}`,
no space-separated words or lowercase in between) is treated as one; any
other use of doubled braces passes through untouched. A reference in that
shape naming a constant that doesn't exist in link-constants.yml fails the
build (same strict-by-default philosophy as hooks/check_translations.py)
rather than silently shipping a page with a literal, unresolved "{{TYPO}}"
in it.
"""

import re
from pathlib import Path

import yaml
from mkdocs.exceptions import PluginError

_CONSTANTS_PATH = Path(__file__).resolve().parent.parent / "link-constants.yml"

_NAME_RE = r"[A-Z][A-Z0-9_]*"
_NAME_ONLY_RE = re.compile(rf"^{_NAME_RE}$")
_REFERENCE_RE = re.compile(r"\{\{\s*(" + _NAME_RE + r")\s*\}\}")

# Inline code spans (`...` / ``...``) - substitution must skip over these,
# same reasoning as skipping fenced code blocks below, one level down.
_INLINE_CODE_RE = re.compile(r"(``.*?``|`.*?`)")

# A fenced-code-block delimiter: 3+ backticks or 3+ tildes, optionally
# indented (list items, admonitions, ...). Matching on the fence *character*
# rather than the exact run length is an approximation of CommonMark's real
# "closing fence must be >= opening fence length" rule, but is enough for
# how this project actually writes fences.
_FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")

_constants = None


def _load_constants() -> dict:
    if not _CONSTANTS_PATH.is_file():
        raise PluginError(
            f"link_constants hook: {_CONSTANTS_PATH} does not exist. Create "
            f"it (a YAML mapping of NAME: value), or remove hooks/link_constants.py "
            f"from mkdocs.yml's `hooks` list if it's no longer wanted."
        )
    with open(_CONSTANTS_PATH, encoding="utf-8") as f:
        raw = yaml.safe_load(f) or {}
    if not isinstance(raw, dict):
        raise PluginError(f"link_constants hook: {_CONSTANTS_PATH} must contain a YAML mapping.")
    for name, value in raw.items():
        if not isinstance(name, str) or not _NAME_ONLY_RE.match(name):
            raise PluginError(
                f"link_constants hook: {_CONSTANTS_PATH} defines {name!r}, which "
                f"isn't a valid constant name - names must be UPPER_SNAKE_CASE "
                f"(e.g. 'DISCORD_HANDEVICE')."
            )
        if not isinstance(value, str):
            raise PluginError(
                f"link_constants hook: {_CONSTANTS_PATH}: {name} must be a plain "
                f"string value, got {value!r}."
            )
    return raw


def on_config(config, **kwargs):
    # Reloaded on every `mkdocs serve` rebuild (on_config re-runs), so an
    # edit to link-constants.yml is picked up without restarting the server.
    global _constants
    _constants = _load_constants()
    return config


def _substitute_outside_code_spans(line: str, page) -> str:
    def repl(match: re.Match) -> str:
        name = match.group(1)
        if name not in _constants:
            raise PluginError(
                f"{page.file.src_uri}: '{{{{{name}}}}}' does not match any "
                f"constant defined in {_CONSTANTS_PATH.name}. Fix the typo, or "
                f"add {name} there."
            )
        return _constants[name]

    # re.split with a capturing group interleaves the delimiters (the code
    # spans themselves) back into the result at the odd indices - leave
    # those alone and only run the substitution on the even (non-code) ones.
    parts = _INLINE_CODE_RE.split(line)
    return "".join(
        part if i % 2 else _REFERENCE_RE.sub(repl, part) for i, part in enumerate(parts)
    )


def on_page_markdown(markdown, page, **kwargs):
    out = []
    in_fence = False
    fence_char = None
    for line in markdown.split("\n"):
        fence_match = _FENCE_RE.match(line)
        if fence_match:
            char = fence_match.group(1)[0]
            if not in_fence:
                in_fence, fence_char = True, char
            elif char == fence_char:
                in_fence, fence_char = False, None
            out.append(line)
            continue
        out.append(line if in_fence else _substitute_outside_code_spans(line, page))
    return "\n".join(out)
