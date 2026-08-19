"""
Keep the shared, non-localized assets under docs/resources/ (wiring diagram
images, official manual PDFs, ...) as a single copy in the built site,
instead of mkdocs-static-i18n's default behaviour of also copying them into
every non-default locale's output subdirectory.

Background: with `docs_structure: folder`, mkdocs-static-i18n builds each
locale as an otherwise self-contained subtree (site/, site/fr/, ...). Any
file that lives in docs_dir but OUTSIDE a language folder - like everything
under docs/resources/ - isn't "owned" by any locale, so on every non-default
locale's build pass mkdocs-static-i18n re-namespaces its destination path
under that locale's prefix (docs/resources/images/foo.jpg ends up written to
BOTH site/resources/images/foo.jpg AND site/fr/resources/images/foo.jpg) so
that locale's pages can link to it with a plain relative path. With N
configured languages the same file physically exists N times in the built
site, which is wasteful for the multi-megabyte diagrams/manuals this project
hosts under resources/.

First attempt at this was to strip these files out of the Files collection
entirely and reference them with root-absolute "/resources/..." links.
That worked for the built site, but had two costs it turns out matter:
  a) mkdocs no longer knew about the files at all, so its own link
     validation (unrecognized_links / strict mode) stopped covering them -
     a typo'd path would build clean and 404 silently.
  b) a root-absolute link resolves differently when the .md file is viewed
     as plain markdown in Gitea's own repo browser: Gitea treats a leading
     "/" as relative to the REPO root, so "/resources/foo.jpg" resolves to
     "<repo>/resources/foo.jpg" - but the file actually lives one directory
     down, at "<repo>/docs/resources/foo.jpg" (docs/ is mkdocs's docs_dir,
     not the repo root) - so the image looked broken in Gitea even though
     it rendered fine on the built site.

Instead, we let the file stay in the Files collection (so mkdocs keeps
doing its normal link resolution/rewriting AND its normal validation for
it) and simply force its computed destination back to the same un-prefixed
path on every locale pass, undoing mkdocs-static-i18n's per-locale
namespacing. Runs as on_files, AFTER mkdocs-static-i18n's own on_files
(priority -100) has already (re)computed each file's per-locale
destination, so there's something to override.

Because the file is a normal, tracked doc-dir asset again, pages should
reference it with an ordinary relative link written the way it actually
sits on disk - e.g. "../resources/images/foo.jpg" from
docs/fr/some-page.md - NOT a root-absolute "/resources/..." link. That
resolves correctly both in the built site (mkdocs rewrites it relative to
the page's real, de-duplicated output location) and in Gitea's raw file
view (plain relative links resolve against the file's real repo location
the same way everywhere), and a typo'd path is caught by mkdocs's own
`unrecognized_links` validation - escalated to a hard build failure by
`strict: true` in mkdocs.yml - same as any other doc link.
"""

import os
from pathlib import Path

from mkdocs.plugins import event_priority

RESOURCES_DIR_NAME = "resources"


@event_priority(-150)  # after mkdocs-static-i18n's on_files (-100)
def on_files(files, config, **kwargs):
    docs_dir = Path(config["docs_dir"]).resolve()
    resources_root = docs_dir / RESOURCES_DIR_NAME
    site_dir = config["site_dir"]
    use_directory_urls = config["use_directory_urls"]

    for file in files:
        src_path = Path(file.abs_src_path).resolve()
        if src_path != resources_root and resources_root not in src_path.parents:
            continue

        # canonical, locale-less destination: same path relative to docs_dir
        # as the source file itself, regardless of which locale pass this is
        canonical_dest = src_path.relative_to(docs_dir).as_posix()
        if file.dest_path == canonical_dest:
            continue  # already canonical (the default-language pass)

        file.dest_path = canonical_dest
        file.abs_dest_path = os.path.normpath(os.path.join(site_dir, file.dest_path))
        file.url = file._get_url(use_directory_urls)

    return files
