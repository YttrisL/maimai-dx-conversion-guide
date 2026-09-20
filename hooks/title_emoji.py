"""
Replace the literal Unicode emoji at the start of each page's H1 title -
and, wherever that same title text is echoed elsewhere on the page (the nav
sidebar, the footer's next/previous links, mobile header, breadcrumbs) - with
a bundled Microsoft Fluent Emoji (Flat style, MIT-licensed) SVG, so every
reader sees the same Windows-11-style glyph regardless of their own OS/browser
or font metrics (Windows in particular tends to render an emoji glyph
noticeably off-centre relative to adjacent text).

Background: every page's H1 opens with a plain Unicode emoji character typed
directly into the Markdown (e.g. "# \U0001F6E0️ Step 1: ..."). Unlike
":shortcode:" emoji, `pymdownx.emoji` (see mkdocs.yml) only matches the
`:name:` syntax - a raw Unicode character passes through untouched and gets
rendered by whatever emoji font the *reader's* OS/browser happens to ship
(Segoe UI Emoji on Windows, Apple Color Emoji on iOS/macOS, Noto on Android,
...), so the same page looks different to every reader. Swapping in a bundled
image sidesteps that entirely.

The image assets live under docs/resources/images/emoji/ (one SVG per title
emoji, downloaded from https://github.com/microsoft/fluentui-emoji, Flat
variant) and are named after their emoji, not their page, since a couple of
these could plausibly be reused - see _EMOJI_ASSET below to add more.

Two passes, at two different build stages:

1. on_page_markdown (same stage as hooks/lightbox.py) swaps the emoji in the
   page's own H1. The <img> we emit here is raw HTML, which MkDocs copies
   into the page verbatim without rewriting its src, so - for the same
   reason lightbox.py resolves image paths through the Files collection
   instead of a hardcoded relative path - the path has to already be correct
   for the *built* page's location (which, under mkdocs-static-i18n's folder
   layout with use_directory_urls, sits one directory deeper than the source
   .md file). Its `alt` carries the original emoji character rather than
   being purely decorative: MkDocs' own title-extraction (used for the nav
   sidebar, the browser tab title, breadcrumbs, ...) substitutes an <img>'s
   `alt` text back in wherever it pulls a heading's plain-text title from
   (see mkdocs.utils.rendering._extract_alt_texts) - an empty alt would
   silently drop the emoji from all of those instead of just standardizing
   its look on the page's own H1.

2. on_post_page runs on every page's fully-rendered HTML, once nav, footer
   links, breadcrumbs, and the mobile header have all been assembled from
   page titles as plain text (Material's nav template renders
   `{{ nav_item.title }}` as escaped text, so an <img> can't be injected any
   earlier than this). It finds every remaining occurrence of a mapped emoji
   sitting at the start of a text node (immediately after a `>`) and swaps it
   for the same bundled image. Restricted to text nodes specifically (not
   inside a tag's attributes, e.g. the `alt="..."` this hook itself just
   wrote) by requiring the character right before the emoji to be `>`, and
   restricted to <body> so it can never reach into <head> and mangle the one
   place an <img> truly cannot go: the plain-text <title> element (the
   browser tab title has no markup of its own to override, so it's the one
   place still left showing the reader's native OS emoji font).
"""

import re
import posixpath

from mkdocs.exceptions import PluginError

# Unicode emoji (as they appear in a title) -> asset basename under
# docs/resources/images/emoji/. Add an entry here (and the matching SVG)
# before using a new emoji in a page title.
_EMOJI_ASSET = {
    "\U0001F6E0️": "hammer-and-wrench",   # Step 1
    "\U0001F4FA": "television",                # Step 2
    "\U0001F579️": "joystick",                    # Step 3
    "\U0001F4B3": "credit-card",                # Step 4
    "\U0001F3A7": "headphone",                  # Step 5
    "\U0001F4A1": "light-bulb",                 # Step 6
    "\U0001F4F7": "camera",                     # Step 7
    "\U000026A0️": "warning",              # warnings.md
    "\U0001F6D2": "shopping-cart",              # equipment.md
    "☑️": "check-box-with-check",     # equipment-checklist.md
    "\U0001F4D6": "open-book",                  # glossary.md
    "\U0001F4E6": "package",                    # secondhand-market.md
    "\U0001F393": "graduation-cap",             # understanding-serial-protocols.md
    "\U0001F3E0": "house",                      # index.md
    "\U0001F389": "party-popper",               # conclusion.md
    "\U0001F4DA": "books",                      # official-manuals.md
    "\U0001F5A8️": "printer",                    # spiralglide-resources.md, wiring-diagrams.md
    "\U0001F517": "link",                       # useful-links.md
}

# Longest-first so a multi-codepoint emoji (base + U+FE0F variation
# selector) isn't matched by its base character alone.
_EMOJI_RE = re.compile(
    "|".join(re.escape(e) for e in sorted(_EMOJI_ASSET, key=len, reverse=True))
)

_TITLE_RE = re.compile(r"^(?P<hashes>#\s+)(?P<emoji>\S+)(?P<rest>\s.*)$")

# A mapped emoji sitting right at the start of a text node: the `>` of
# whatever tag precedes it (a <span>, a <title>, ...), then whitespace (nav
# labels have some, e.g. Material's `<span class="md-ellipsis">\n  🔘 3 -
# ...`), then the emoji itself. Requiring the `>` immediately before rules
# out matching inside an attribute value (e.g. `alt="🔘"`, preceded by `="`).
_BODY_EMOJI_RE = re.compile(r"(>\s*)(" + _EMOJI_RE.pattern + r")")

_ASSETS_DIR = "resources/images/emoji"

# Populated by on_files, consumed by on_post_page - see module docstring for
# why the image-swap can't happen any earlier than on_post_page for anything
# other than the page's own H1, but on_post_page isn't handed the Files
# collection MkDocs needs for `_resolve_src`, so it's cached here instead.
_files = None


def _resolve_src(asset_name: str, page, files) -> str:
    target_uri = posixpath.join(_ASSETS_DIR, f"{asset_name}.svg")
    target_file = files.get_file_from_path(target_uri)
    if target_file is None:
        raise PluginError(
            f"title_emoji: asset {target_uri!r} referenced by "
            f"{page.file.src_uri} does not exist."
        )
    return target_file.url_relative_to(page.file)


def on_files(files, config, **kwargs):
    global _files
    _files = files
    return files


def on_page_markdown(markdown, page, config, files, **kwargs):
    lines = markdown.split("\n")
    for i, line in enumerate(lines):
        match = _TITLE_RE.match(line)
        if not match:
            continue

        emoji_match = _EMOJI_RE.fullmatch(match.group("emoji"))
        if not emoji_match:
            continue

        emoji = emoji_match.group(0)
        asset_name = _EMOJI_ASSET[emoji]
        src = _resolve_src(asset_name, page, files)
        # `alt` carries the original emoji character, not a description - see
        # the module docstring: it's what MkDocs' own title-extraction (and,
        # transitively, the <title> tag's text) shows instead of nothing.
        img = f'<img class="emoji-icon" src="{src}" alt="{emoji}">'
        lines[i] = match.group("hashes") + img + match.group("rest")
        # Only the page's H1 (its title) gets this treatment here; every
        # other occurrence of a title's emoji is handled by on_post_page.
        break

    return "\n".join(lines)


def on_post_page(output, page, config, **kwargs):
    body_start = output.find("<body")
    if body_start == -1:
        return output  # not a full HTML document (shouldn't happen) - leave it alone

    def _replace(match: re.Match) -> str:
        prefix, emoji = match.group(1), match.group(2)
        asset_name = _EMOJI_ASSET[emoji]
        src = _resolve_src(asset_name, page, _files)
        return f'{prefix}<img class="emoji-icon" src="{src}" alt="{emoji}">'

    head, body = output[:body_start], output[body_start:]
    return head + _BODY_EMOJI_RE.sub(_replace, body)
