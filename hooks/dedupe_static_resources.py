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

Since these assets are intentionally not localized, we instead:
  1. (on_files, default priority - runs before mkdocs-static-i18n's own
     on_files at priority -100, same as check_translations.py) drop every
     docs/resources/... file from the Files collection entirely, so
     mkdocs-static-i18n never sees it and never duplicates it.
  2. (on_post_build, after mkdocs-static-i18n's on_post_build at -100, same
     spot as copy_sitemap.py) copy docs/resources/ into the site root
     exactly once, directly, bypassing mkdocs entirely.

Because step 1 removes these files from mkdocs's own bookkeeping, pages must
reference them with a root-absolute link (e.g. "/resources/images/foo.jpg",
NOT "resources/images/foo.jpg") - mkdocs can no longer resolve/rewrite a
relative link to a file it doesn't know about. Root-absolute links are
validated under the separate `validation.links.absolute_links` setting
(left at its default 'info' in mkdocs.yml) rather than `unrecognized_links`,
so they don't trip `strict: true`.
"""

import shutil
from pathlib import Path

from mkdocs.plugins import event_priority

RESOURCES_DIR_NAME = "resources"


def on_files(files, config, **kwargs):
    resources_root = (Path(config["docs_dir"]) / RESOURCES_DIR_NAME).resolve()

    for file in list(files):
        src_path = Path(file.abs_src_path).resolve()
        if src_path == resources_root or resources_root in src_path.parents:
            files.remove(file)

    return files


@event_priority(-200)  # after mkdocs-static-i18n's on_post_build (-100)
def on_post_build(config, **kwargs):
    src = Path(config["docs_dir"]) / RESOURCES_DIR_NAME
    if not src.is_dir():
        return
    shutil.copytree(src, Path(config["site_dir"]) / RESOURCES_DIR_NAME, dirs_exist_ok=True)
