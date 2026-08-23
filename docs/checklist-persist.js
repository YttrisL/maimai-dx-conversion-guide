/*
 * Persists the checked/unchecked state of task-list checkboxes
 * (see pymdownx.tasklist, clickable_checkbox: true) to localStorage, so a
 * checklist a reader is ticking off survives a page reload.
 *
 * State is scoped per page (window.location.pathname) and keyed by each
 * item's own text, not its position in the list - so reordering items in
 * the markdown doesn't scramble a reader's saved progress. Editing an
 * item's wording is treated as a new item (its old saved state is simply
 * abandoned), which is an acceptable tradeoff for a static site with no
 * backend to migrate state.
 */
(function () {
  "use strict";

  function storageKey() {
    return "checklist:" + window.location.pathname;
  }

  function itemText(checkbox) {
    var item = checkbox.closest(".task-list-item");
    if (!item) return null;
    var clone = item.cloneNode(true);
    var control = clone.querySelector(".task-list-control");
    if (control) control.remove();
    return clone.textContent.trim();
  }

  function readState(key) {
    try {
      return JSON.parse(localStorage.getItem(key) || "{}");
    } catch (e) {
      return {};
    }
  }

  function init() {
    var checkboxes = document.querySelectorAll(
      ".task-list-control > input[type='checkbox']"
    );
    if (!checkboxes.length) return;

    var key = storageKey();
    var saved = readState(key);

    checkboxes.forEach(function (checkbox) {
      var id = itemText(checkbox);
      if (id && saved[id]) {
        checkbox.checked = true;
      }

      checkbox.addEventListener("change", function () {
        if (!id) return;
        var state = readState(key);
        if (checkbox.checked) {
          state[id] = true;
        } else {
          delete state[id];
        }
        localStorage.setItem(key, JSON.stringify(state));
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
