/*
 * Click-to-zoom lightbox for `.lightbox-thumb` / `.lightbox-overlay` pairs
 * (see style.css for the accompanying styles and usage example). Generic
 * and page-agnostic: works for however many lightbox instances a page adds,
 * each identified by its own unique id.
 *
 * Markup contract:
 *   <a href="#my-id" class="lightbox-thumb"
 *      data-lightbox-group="g" data-lightbox-index="0"><img ...></a>
 *   <div class="lightbox-overlay" id="my-id"
 *        data-lightbox-group="g" data-lightbox-index="0"><img ...></div>
 *
 * data-lightbox-group/-index are what the left/right arrow keys (and the
 * .lightbox-nav-prev/-next on-screen buttons, when present) use to find
 * "next"/"previous" while an overlay is open: every image meant to be
 * navigable as one set shares the same group value, ordered by index (see
 * hooks/lightbox.py, which assigns one group per `!!! lightbox` block - so
 * arrow-key navigation stays scoped to the block the reader zoomed into,
 * not every image on the page). Both attributes are optional; without them
 * an overlay just isn't reachable by arrow keys or nav buttons.
 *
 * The overlay is a <div>, not a link: Python-Markdown's raw-HTML-block
 * detection only recognizes a handful of block-level tags (div, p, ...),
 * not <a>, so an anchor spanning multiple lines with nested block content
 * (figure/figcaption) gets its content mangled by the markdown parser even
 * with markdown="0" - see mkdocs.yml's md_in_html extension. The thumbnail
 * link's href="#my-id" doubles as a no-JS fallback via the :target rule in
 * style.css (opens the overlay; closing it then needs the browser's Back
 * button, since there's no close link without JS). With JS available we
 * intercept the thumbnail click and toggle a class instead of following the
 * link, so the hash never changes and opening/closing never scrolls the
 * page.
 */
(function () {
  "use strict";

  function openOverlay(overlay) {
    document.querySelectorAll(".lightbox-overlay.lightbox-open").forEach(
      function (other) {
        if (other !== overlay) other.classList.remove("lightbox-open");
      }
    );
    overlay.classList.add("lightbox-open");
  }

  function closeAll() {
    document.querySelectorAll(".lightbox-overlay.lightbox-open").forEach(
      function (overlay) {
        overlay.classList.remove("lightbox-open");
      }
    );
  }

  function navigate(direction) {
    var current = document.querySelector(".lightbox-overlay.lightbox-open");
    var group = current && current.getAttribute("data-lightbox-group");
    if (!group) return;

    var siblings = Array.prototype.slice
      .call(document.querySelectorAll('.lightbox-overlay[data-lightbox-group="' + group + '"]'))
      .sort(function (a, b) {
        return Number(a.getAttribute("data-lightbox-index")) - Number(b.getAttribute("data-lightbox-index"));
      });
    if (siblings.length < 2) return;

    var currentIndex = siblings.indexOf(current);
    var nextIndex = (currentIndex + direction + siblings.length) % siblings.length;
    openOverlay(siblings[nextIndex]);
  }

  document.addEventListener("click", function (event) {
    var thumb = event.target.closest(".lightbox-thumb");
    if (thumb) {
      var id = (thumb.getAttribute("href") || "").slice(1);
      var overlay = id && document.getElementById(id);
      if (overlay) {
        event.preventDefault();
        openOverlay(overlay);
      }
      return;
    }

    var navButton = event.target.closest(".lightbox-nav");
    if (navButton) {
      event.preventDefault();
      navigate(navButton.classList.contains("lightbox-nav-next") ? 1 : -1);
      return;
    }

    var openedOverlay = event.target.closest(".lightbox-overlay");
    if (openedOverlay) {
      // A caption can contain its own real link (e.g. an image source
      // attribution - see hooks/lightbox.py) - let clicks on that link
      // navigate normally instead of treating them as "click anywhere
      // to close".
      var captionLink = event.target.closest("a");
      if (captionLink && openedOverlay.contains(captionLink)) {
        return;
      }
      event.preventDefault();
      openedOverlay.classList.remove("lightbox-open");
    }
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      closeAll();
    } else if (event.key === "ArrowRight") {
      navigate(1);
    } else if (event.key === "ArrowLeft") {
      navigate(-1);
    }
  });
})();
