# Deck Folder Specification
*Version 0.2 — 2026-05-25 — updated after Attack 5 scored review*

---

## Engine root structure

```
[engine root]
  shared/
    branding/
      base.css              — shared branding across all decks
      logo.svg              — (and other shared brand assets)
    templates/
      slide-template.html   — Reveal.js base template
  decks/
    <topic-slug>/           — one folder per deck topic
  docs/                     — engine documentation
  myPKA/                    — team orchestration layer
```

`shared/` is the single home for all assets that span decks. Per-deck visual identity overrides live inside the deck at `decks/<topic-slug>/theme/`.

---

## Per-deck folder structure

```
decks/
  <topic-slug>/
    pov.md                  — deck identity: PoV, engagement_level, status, version
    decisions.md            — persistent decision memory (see decisions-template)
    theme/                  — per-deck CSS/visual identity overrides (references shared/branding/)
    research/               — Pax's synthesis briefs for this topic
    versions/
      v1.0.0/
        canonical.html      — base version, no audience-specific adaptation
        parents.html        — audience variant
        teachers.html       — audience variant
      v1.1.0/
        ...
    scorecards/
      v1.0.0-research.md
      v1.0.0-argument.md
      v1.0.0-narrative.md
      v1.0.0-adversarial.md
      v1.0.0-persuasion-parents.md
      v1.0.0-persuasion-teachers.md
    reports/                — specialist deliverables for this deck
      YYYY-MM-DD-narrative-spine-v1.md
      YYYY-MM-DD-logic-audit-v1.md
      YYYY-MM-DD-adversarial-v1.md
      YYYY-MM-DD-persuasion-parents-v1.md
```

---

## pov.md fields (required)

```yaml
---
topic: [deck topic]
pov: [the spiky point of view — one sentence, falsifiable]
engagement_level: autonomous | collaborative | co-author
current_version: v0.0.0
status: active | archived | overturned
overturned_by: [link to replacement deck or PoV, only when status is overturned]
---
```

**status behaviour in improvement cycles:**
- `active` — improvement cycle runs normally
- `archived` — improvement cycle skips unless manually triggered by Adnan
- `overturned` — improvement cycle skips permanently; deck remains as historical record; `overturned_by` links to the replacement

`engagement_level` controls the cycle:
- `autonomous` — engine runs a full cycle and submits a PR without checking in first
- `collaborative` — engine runs research and scoring, then checks with Adnan before producing the PR
- `co-author` — Adnan is involved at each step; no cycle phase runs without his input

---

## versions/ convention

Audience variants are nested inside the version folder:

```
versions/v1.2.0/
  canonical.html        — the argument-only base, no audience framing applied
  parents.html
  teachers.html
  teenagers.html
```

`canonical.html` is required for every version. Audience variants are optional and per-audience.

All HTML files reference `../../../shared/branding/base.css` and `../../theme/<deck-slug>.css` for styling. The Reveal.js library is referenced from `shared/` as well, so the engine does not duplicate it per deck.

---

## scorecards/ naming convention

Scorecards are keyed by version and (where applicable) audience:

| Scorecard | Filename pattern | Audience-specific? |
|---|---|---|
| Research | `v<N>-research.md` | No — Pax scores the research base |
| Argument | `v<N>-argument.md` | No — Rex audits the canonical argument |
| Narrative | `v<N>-narrative.md` | No — Aria critiques the canonical story (arc is deck-wide) |
| Adversarial | `v<N>-adversarial.md` | No — Vera attacks the PoV itself |
| Persuasion | `v<N>-persuasion-<audience-slug>.md` | Yes — one per audience variant |

Example: `scorecards/v1.2.0-persuasion-parents.md`

---

## reports/ (formerly deliverables/)

Specialist working documents for this deck: logic audit reports, adversarial review documents, persuasion scorecards, Pax research briefs specific to this topic.

Named: `YYYY-MM-DD-<type>-v<N>.md` (e.g. `2026-05-25-logic-audit-v1.md`)

**Note:** this folder is named `reports/` to avoid collision with `myPKA/Deliverables/`, which is the system-wide drop zone for team deliverables (hire research, cross-team work). Specialist contracts that reference "Deliverables/" for deck-specific work should use `decks/<topic-slug>/reports/` as the explicit path.

---

## decisions.md

Template: `myPKA/Team Knowledge/Templates/decisions-template.md`

Each specialist logs their own decisions; entries are included in the cycle PR. Vera and Pax read `decisions.md` before every pass. See [[docs/deck-folder-spec]] for re-litigation rules.

---

## HTML framework

**Reveal.js.** Git-native HTML+CSS output, no mandatory build step, audience variants via CSS swap (`<link>` tag), speaker notes, fullscreen, offline operation. The Deck Author owns the Reveal.js implementation. See `docs/engine-decisions.md` for the decision record.

---

## Disagreement protocol

When Rex, Vera, Aria, or Pax reach conflicting findings (e.g. Rex finds a gap Pax says is evidenced), Larry documents both positions in the PR summary. Adnan resolves via PR review. Larry does not make content calls.

---

## PR legibility

Every PR includes a **Larry synthesis** at the top: one paragraph covering what changed, why, and which specialist findings drove it. Specialist reports are linked but not inlined. Adnan reads the synthesis; opens specialist reports only when a finding needs scrutiny.
