"""
Expand a `!!! lightbox` block into the click-to-zoom lightbox markup (see
docs/style.css and docs/lightbox.js for the CSS/JS half of this component),
so a page can write a short list of images instead of hand-writing raw HTML.

Usage in a .md file, styled after the built-in `!!! admonition` blocks:

    !!! lightbox
        ![Caption for the first image](../resources/images/foo/a.png)
        ![Caption for the second image](../resources/images/foo/b.png)

Like any other admonition, `!!! lightbox` can itself be nested inside
another indentation-based block (a `??? note` details block, a list item,
a tab, ...) - just indent the whole block, marker included, one level
further in.

Each indented line must be a single Markdown image. Its alt text becomes
both the rendered <img>'s alt attribute and the visible caption under it
(small in the thumbnail, normal-sized once zoomed - see style.css). Each
image also gets a data-lightbox-group/-index pair (one group per `!!!
lightbox` block, in source order) so lightbox.js can cycle left/right
through just that block's images with the arrow keys while one is open -
and, whenever a block has more than one image, a pair of on-screen
prev/next arrow buttons that do the same thing on click.

Why this needs a hook instead of just writing the HTML inline: a hand-written
raw <a>/<div class="lightbox-overlay"> block works, but two things about it
are unpleasant enough to be worth automating away:

  1. Python-Markdown's raw-HTML-block detection only recognizes a handful of
     block-level tags (div, p, ...) - NOT <a>/<span> - so a multi-line inline
     tag with nested block content (figure/figcaption) gets its content
     mangled by the markdown parser even with markdown="0". Every element in
     the hand-written version has to be one of the recognized block tags,
     which is a non-obvious trap (see git history on docs/fr/step-6-lighting.md
     for what that mangling actually looks like).
  2. A raw HTML <img src="..."> is copied verbatim into the page - MkDocs
     never rewrites it - so its path has to already be relative to the
     *built page's* location (which, under mkdocs-static-i18n's folder
     layout with use_directory_urls, is one directory deeper than the
     source .md file), instead of the source-relative path every other
     image in the docs uses. That mismatch is exactly the kind of thing
     that builds clean and 404s at runtime.

Running as on_page_markdown (before the markdown conversion) sidesteps both:
we emit the final HTML ourselves (so we control which tags get used), and we
resolve each image path the same way MkDocs' own relative-link rewriting
does - by looking it up in the Files collection and asking for its URL
relative to the current page - so authors just write the path the way they
would for a normal Markdown image.
"""

import hashlib
import html
import posixpath
import re

from mkdocs.exceptions import PluginError

_START_RE = re.compile(r"^(?P<indent>[ \t]*)!!!\s+lightbox\s*$")
_IMAGE_RE = re.compile(r"^!\[(?P<alt>[^\]]*)\]\((?P<src>[^)\s]+)\)$")


def _nav_labels(page) -> tuple:
    # Only two locales exist (docs/en/, docs/fr/ - see hooks/check_translations.py),
    # so a plain lookup on the page's own locale folder is enough; no need to
    # go through the i18n plugin's config for just an aria-label string.
    locale = page.file.src_uri.split("/", 1)[0]
    if locale == "en":
        return "Previous image", "Next image"
    return "Image précédente", "Image suivante"


def _slug(src: str) -> str:
    # A stable id derived from the source path, not a page-scoped counter -
    # so it stays the same across edits/reorders and is guaranteed unique
    # per distinct image.
    return "lightbox-" + hashlib.sha1(src.encode("utf-8")).hexdigest()[:10]


def _resolve_src(raw_src: str, page, files) -> str:
    if raw_src.startswith(("http://", "https://", "/")):
        return raw_src

    # Mirrors mkdocs.structure.pages._RelativePathTreeprocessor._target_uri:
    # resolve relative to the *source* file's directory, then look the
    # result up in the Files collection to get its real (possibly
    # locale-deduped, see hooks/dedupe_static_resources.py) destination.
    page_dir = posixpath.dirname(page.file.src_uri)
    target_uri = posixpath.normpath(posixpath.join(page_dir, raw_src))
    target_file = files.get_file_from_path(target_uri)
    if target_file is None:
        raise PluginError(
            f"!!! lightbox in {page.file.src_uri}: image {raw_src!r} "
            f"(resolved to docs/{target_uri}) does not exist."
        )
    return target_file.url_relative_to(page.file)


def _render(body_lines: list, page, files, group_id: str) -> str:
    images = []
    for line in body_lines:
        match = _IMAGE_RE.match(line)
        if not match:
            raise PluginError(
                f"!!! lightbox in {page.file.src_uri}: expected a single "
                f"Markdown image per line, got {line!r}."
            )
        images.append((match.group("src"), match.group("alt")))

    # Only worth showing prev/next arrows (and wiring them up) when there's
    # actually something to navigate to.
    nav_html = ""
    if len(images) > 1:
        prev_label, next_label = _nav_labels(page)
        nav_html = (
            f'<button type="button" class="lightbox-nav lightbox-nav-prev" '
            f'aria-label="{html.escape(prev_label)}">&#8249;</button>'
            f'<button type="button" class="lightbox-nav lightbox-nav-next" '
            f'aria-label="{html.escape(next_label)}">&#8250;</button>'
        )

    thumbs = []
    overlays = []
    for index, (raw_src, alt) in enumerate(images):
        src = html.escape(_resolve_src(raw_src, page, files))
        caption = html.escape(alt)
        uid = _slug(raw_src)
        # data-lightbox-group/-index let lightbox.js find this image's
        # siblings (and their order) to answer "what's next/previous" for
        # the left/right arrow-key navigation, without needing every image
        # on the page to share one single sequence.
        thumbs.append(
            f'<a href="#{uid}" class="lightbox-thumb" '
            f'data-lightbox-group="{group_id}" data-lightbox-index="{index}">'
            f"<figure><img src=\"{src}\" alt=\"{caption}\">"
            f"<figcaption>{caption}</figcaption></figure></a>"
        )
        overlays.append(
            f'<div class="lightbox-overlay" markdown="0" id="{uid}" '
            f'data-lightbox-group="{group_id}" data-lightbox-index="{index}">'
            + nav_html
            + f"<figure><img src=\"{src}\" alt=\"{caption}\">"
            f"<figcaption>{caption}</figcaption></figure></div>"
        )

    return (
        '<div class="lightbox-row" markdown="0">' + "".join(thumbs) + "</div>\n"
        + "\n".join(overlays)
    )


def on_page_markdown(markdown, page, config, files, **kwargs):
    lines = markdown.split("\n")
    out = []
    i = 0
    group_count = 0
    while i < len(lines):
        line = lines[i]
        start_match = _START_RE.match(line)
        if not start_match:
            out.append(line)
            i += 1
            continue

        # `!!! lightbox` can itself be nested inside another indentation-based
        # block (a "??? note" details block, a list item, a tab, ...), same
        # as any other admonition. Whatever indentation the marker itself
        # carries is exactly the indentation its *content* needs to keep
        # being considered part of that enclosing block - one further level
        # (4 spaces) in, per the usual Markdown nesting convention.
        indent = start_match.group("indent")
        content_prefix = indent + "    "

        i += 1
        body = []
        while i < len(lines) and (lines[i].strip() == "" or lines[i].startswith(content_prefix)):
            if lines[i].strip():
                body.append(lines[i].strip())
            i += 1

        if not body:
            raise PluginError(
                f"!!! lightbox in {page.file.src_uri}: block has no "
                f"indented images under it."
            )
        rendered = _render(body, page, files, f"lightbox-group-{group_count}")
        # Re-apply the marker's own indentation to every output line, so the
        # substitution still reads as content of whatever it's nested under
        # (if anything) once Markdown re-parses it.
        out.append("\n".join(indent + rendered_line for rendered_line in rendered.split("\n")))
        group_count += 1

    return "\n".join(out)
