# Development guide

This document walks you through getting the documentation site running on
your own machine from a completely clean install - no prior MkDocs
experience assumed. If you're just here to read the guide, you don't need
any of this: head back to the [README](README.md).

This repo's site is built with [MkDocs](https://www.mkdocs.org/) and the
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.
You write plain Markdown files in the `docs/` folder, and MkDocs turns them
into a full static website (search, navigation, dark mode, etc. included for
free).

---

## 1. What you need installed

You need two things: **Git** (to get the code) and **Python** (to run
MkDocs). If you already have both, skip to [section 2](#2-get-the-code).

### Git

- **Windows:** download and run the installer from
  [git-scm.com/downloads](https://git-scm.com/downloads). Default options are
  fine.
- **macOS:** install [Xcode Command Line Tools](https://developer.apple.com/xcode/resources/)
  (`xcode-select --install` in Terminal), or install via [Homebrew](https://brew.sh/):
  `brew install git`.
- **Linux:** `sudo apt install git` (Debian/Ubuntu) or your distro's
  equivalent.

Verify it worked by opening a terminal (PowerShell on Windows, Terminal on
macOS/Linux) and running:

```bash
git --version
```

### Python

MkDocs needs **Python 3.9 or newer**.

- **Windows:** download the latest installer from
  [python.org/downloads](https://www.python.org/downloads/). On the first
  install screen, **make sure you tick "Add python.exe to PATH"** before
  clicking Install - this is the single most common thing people forget, and
  without it none of the commands below will work.
- **macOS:** `brew install python` (Homebrew), or the installer from
  python.org.
- **Linux:** Python 3 usually comes preinstalled; if not,
  `sudo apt install python3 python3-pip python3-venv`.

Verify it worked:

```bash
python --version
```

(On macOS/Linux this command is sometimes `python3` instead of `python` -
if `python --version` says "command not found", try `python3 --version`.)

---

## 2. Get the code

Clone the repo (swap in the actual repo URL) and move into the folder:

```bash
git clone <your-gitea-repo-url>
cd maimai-dx-guide
```

If you already downloaded this as a zip instead of cloning, just open a
terminal inside the unzipped folder and skip the `git clone` step - though
note you'll want a real `git clone` eventually if you intend to push changes
back.

---

## 3. Set up a virtual environment

A **virtual environment** ("venv") keeps this project's Python packages
separate from anything else on your system, so you don't end up with version
conflicts between different projects. You only need to create it once.

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

You'll know it worked because your terminal prompt now starts with
`(.venv)`. You'll need to run the `activate` line again every time you open
a *new* terminal window to work on this project - it doesn't persist
automatically.

> **Note:** the `.venv` folder is intentionally excluded from git (see
> `.gitignore`) - every contributor creates their own locally, it never gets
> committed.

---

## 4. Install the project's dependencies

With the venv active, install everything the site needs:

```bash
pip install -r requirements.txt
```

This pulls in `mkdocs-material` and a couple of small plugins. It only
downloads a few megabytes and takes well under a minute.

---

## 5. Run the site locally

```bash
mkdocs serve
```

You'll see log output ending in something like:

```
INFO    -  Serving on http://127.0.0.1:8000/
```

Open that address in your browser - you now have the site running locally.

The best part: **leave this command running** and edit any `.md` file in
`docs/`. The moment you save, the browser tab auto-refreshes with your
changes. This is the fastest way to write and preview content.

Stop the server anytime with `Ctrl+C` in the terminal.

---

## 6. Making changes

- **Page content** lives in `docs/*.md` - plain Markdown files. Add a new
  file for a new page.
- **Navigation / page order** is controlled by the `nav:` section in
  `mkdocs.yml` at the repo root. If you add a new `.md` file and it isn't
  showing up in the sidebar, this is why - add it to the list there.
- **Site-wide settings** (title, theme colors, plugins, repo links, etc.)
  are also in `mkdocs.yml`.

---

## 7. Building the static site (no live server)

When you want the actual static HTML/CSS/JS files - e.g. to upload
somewhere yourself, inspect the output, or just confirm it builds cleanly -
run:

```bash
mkdocs build
```

This generates a full static copy of the site in a new `site/` folder. You
could open `site/index.html` directly in a browser, or upload the entire
`site/` folder's contents to any static web host or FTP server. This folder
is also excluded from git (it's a build artifact, regenerated fresh every
time) - never edit files inside it directly, your changes would be
overwritten on the next build.

> In this repo, this exact `mkdocs build` step already happens
> automatically via a CI pipeline (`.gitea/workflows/deploy.yml`) every time
> a change is pushed to `main`, followed by an automatic upload to the live
> site. You generally won't need to run `mkdocs build` by hand unless you're
> troubleshooting something locally first - `mkdocs serve` covers everyday
> editing.

---

## 8. Troubleshooting

**`mkdocs: command not found` / `'mkdocs' is not recognized`**\
Your virtual environment isn't active. Re-run the `activate` command from
[section 3](#3-set-up-a-virtual-environment) - you need to do this in every
new terminal window.

**A `git-revision-date-localized` / `InvalidGitRepositoryError` error on
build**\
This plugin shows each page's real "last updated" date, which it reads from
git history. It needs you to have actually run `git clone` (or at least
`git init` + one commit) - if you're working from a loose folder that was
never a git repo, this is why. It's configured to fall back gracefully to
the build date otherwise, so this shouldn't hard-crash, but a real git
history gives more accurate dates.

**Still stuck?**\
Check the terminal output - MkDocs errors are usually specific about which
file and line caused the problem. Feel free to paste the error into an issue
or ask whoever maintains this repo.
