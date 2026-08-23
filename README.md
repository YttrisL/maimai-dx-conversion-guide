# maimai FiNALE → DX Upgrade Guide

This repo hosts a step-by-step hardware guide for converting a **maimai
FiNALE** arcade cabinet into a working **maimai DX** cabinet — a project the
community calls "DxNALE". It covers everything from sourcing the right
equipment, to wiring, the touchscreen, the I/O board, the Aime reader, proxy
compatibility, audio, lighting, and cameras, in an order meant to be
followed start to finish by someone who isn't an electronics engineer.

The guide's guiding principle is **total software fidelity**: the goal is
never to modify the game's own software, but to make the hardware
adaptation invisible to it, so the resulting cabinet stays compatible with
the way most private maimai DX servers expect a genuine cabinet to behave.

## Building, running, or publishing this site

If you need to set up MkDocs locally, preview changes as you write, or build/publish
the static site, that's all covered separately in [DEVELOPMENT.md](DEVELOPMENT.md).

---

## A note on AI involvement

Claude (Anthropic) was used to help set up the MkDocs infrastructure for this
repo, and to assist with proofreading — fixing spelling and grammar,
rewording awkward turns of phrase — and with translating pages. 
Claude was **not** used to draft or generate the guide's
actual content from scratch: every `.md` file's substance — the steps, the
explanations, the technical knowledge — is human-written. AI here played an
editing and translation role, not an authoring one.
