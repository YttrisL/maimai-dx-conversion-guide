"""
Mirror the site's single sitemap.xml into every generated page directory.

Background: mkdocs-material's client-side JS resolves hreflang/language
"alternate" links (injected by mkdocs-static-i18n's reconfigure_material
option) by fetching "sitemap.xml" *relative to each alternate page's own
directory* rather than from the site root — e.g. on /fr/step-1-pc-alls/ it
requests /fr/step-1-pc-alls/sitemap.xml. mkdocs-static-i18n, however, only
ever writes ONE combined sitemap.xml at the true site root, so those
per-directory fetches always 404 (mkdocs-material fails soft on this, so
nothing actually breaks — it's just noisy 404s in the server/build log).

This hook runs after the build (and after mkdocs-static-i18n has finished
building every locale and finalized the combined sitemap.xml) and copies
that root sitemap.xml into every output directory that contains a page, so
the relative fetch succeeds wherever it's made from.
"""

import os

from mkdocs.plugins import event_priority


@event_priority(-200)  # after mkdocs-static-i18n's on_post_build (-100),
# which nested-builds every locale and only finalizes the combined
# sitemap.xml once all of those finish.
def on_post_build(config, **kwargs):
    site_dir = config["site_dir"]
    root_sitemap = os.path.join(site_dir, "sitemap.xml")
    if not os.path.isfile(root_sitemap):
        return

    with open(root_sitemap, "rb") as f:
        sitemap_bytes = f.read()

    for dirpath, _dirnames, filenames in os.walk(site_dir):
        if dirpath == site_dir:
            continue  # root already has the real sitemap.xml
        if "index.html" not in filenames:
            continue  # not a page output directory (e.g. assets/)
        with open(os.path.join(dirpath, "sitemap.xml"), "wb") as f:
            f.write(sitemap_bytes)
