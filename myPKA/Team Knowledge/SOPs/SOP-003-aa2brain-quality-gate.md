# SOP-003 — aa2brain Quality Gate

- **Owner:** Silas
- **Triggered by:** Pax completing a synthesis brief that has lasting value; any specialist proposing a write to aa2brain
- **Hard rule:** nothing is written to aa2brain until this gate passes. No exceptions.
- **References:** aa2brain `SCHEMA.md` at `/mnt/c/Users/adnan/Google Drive/aa2brain/SCHEMA.md`

---

## Purpose

Protect aa2brain's schema integrity from engine output that is malformed, off-domain, or inadequately sourced. The engine is a consumer of aa2brain (read) and a contributor (write) — but only after passing this gate.

---

## Step 1 — Domain relevance check

aa2brain's domain is: *Aha! Moments in Agility — Designing human + agent teams that actually work.*

Before any other check, Silas determines: **is this content relevant to aa2brain?**

Content is relevant if it maps to at least one domain tag:

| Tag | Domain |
|---|---|
| `agility` | Agile practices, frameworks, ceremonies, values, principles |
| `agents-ai` | AI agents, LLMs, agentic systems, tool use, orchestration |
| `hybrid-teams` | Human+AI team composition, roles, handoffs, collaboration |
| `delivery` | Token economics, cost governance, velocity, sustainability |
| `practitioners` | Specific people and their frameworks in the field |

**If no domain tag applies: STOP. Do not proceed. Return to Pax with the reason.**

Engine research on topics outside this domain (e.g. slide design theory, presentation rhetoric, general persuasion science) does not belong in aa2brain. It stays in `decks/<topic>/research/` only.

---

## Step 2 — Type and directory determination

Silas determines the correct type and target directory:

| Type | Directory | When to use |
|---|---|---|
| `entity` | `entities/` | Named, discrete things: frameworks, tools, people, organisations |
| `concept` | `concepts/` | Ideas and abstractions that span entities |
| `comparison` | `comparisons/` | Explicit X vs Y with the comparison itself as the insight |
| `query` | `queries/` | Filed synthesis result answering a specific research question |
| Source material | `raw/articles/` | Immutable source material — never edited after creation |

If the proposed type or directory does not match, Silas corrects it before validation continues.

---

## Step 3 — Frontmatter validation

Every page except `raw/` must have valid frontmatter. Check each field:

```yaml
---
title: <descriptive title>              # required — non-empty string
created: YYYY-MM-DD                     # required — valid date
updated: YYYY-MM-DD                     # required — valid date, >= created
type: entity | concept | comparison | query  # required — must match directory
tags: [domain-tag, pillar-tag, ...]     # required — see tag rules below
sources:
  - ^[raw/articles/source-slug.md]      # required for non-raw — at least one
confidence: high | medium | low         # required — must be one of these three
contested: true                         # only when applicable
---
```

**Tag rules:**
- At least one domain tag required (`agility`, `agents-ai`, `hybrid-teams`, `delivery`, `practitioners`)
- At most one pillar tag (`pillar-1`, `pillar-2`, `pillar-3`) — add a second only if genuinely cross-pillar
- Epistemic tag if applicable (`contested`, `settled`, `emerging`)
- Editorial tags optional (`angle-candidate`, `evergreen`, `dated`, `adnan-perspective`)

**Confidence guidance:**
- `high` — multiple independent sources agree
- `medium` — one strong source, or multiple with minor variance
- `low` — single source, very new, or practitioner claim without evidence base

If `confidence: low` and the content makes significant claims, Silas flags this to Pax for additional sourcing before writing.

---

## Step 4 — Filename convention check

Filename must be `kebab-case.md` with no spaces, capitals, or special characters.

| Type | Convention | Example |
|---|---|---|
| entity | `entity-name.md` | `jeff-sutherland.md` |
| concept | `concept-description.md` | `token-budget-as-sprint-capacity.md` |
| comparison | `thing-a-vs-thing-b.md` | `continuous-vs-gate-oversight.md` |
| query | `question-slug-YYYY-MM-DD.md` | `ai-dor-best-practices-2026-05-19.md` |
| raw | `source-slug.md` | `ethan-mollick-ai-teammate-2024.md` |

If the proposed filename does not conform, Silas corrects it.

---

## Step 5 — Wikilink minimum check

Every page except `raw/` must have at least 2 outbound `[[wikilinks]]` to existing pages in aa2brain.

Silas checks:
1. Are there at least 2 wikilinks in the body?
2. Do the linked pages actually exist in aa2brain?

If wikilinks are missing or broken, Silas returns the content to Pax with a list of suggested link targets.

---

## Step 6 — Source traceability check

For non-raw pages, every significant claim must be traceable to a source. Check:
- `sources:` frontmatter field lists at least one `raw/` page
- That raw page exists in aa2brain (or is being written in the same batch)
- Key claims in the body cite these sources

If sources are missing, Silas returns the content to Pax.

---

## Step 7 — Write and log

If all checks pass:

1. Write the file to its target directory in aa2brain
2. Append to `log.md` (append-only, never edit):
   ```
   [YYYY-MM-DDTHH:MM:SSZ] ingest: <source-slug> → <type>/<page-slug>
   ```
3. Return to Larry: file path written, log entry appended, any flags raised during validation.

---

## Validation summary output (return to Larry)

```
Status: PASS | FAIL | PASS WITH FLAGS
File: <target-path>
Type: <entity|concept|comparison|query|raw>
Domain tags: <list>
Issues resolved: <list or "none">
Flags: <list or "none">
Log entry: <appended line>
```

---

## Common failure modes

- **Off-domain content** — engine research on non-aa2brain topics routed here by mistake. Return to deck's `research/` folder.
- **Missing warrant in sources** — content references a claim without a raw/ source existing yet. Write the raw source first, then the derived note.
- **Confidence mismatch** — content rated `high` confidence from a single source. Downgrade or return to Pax for triangulation.
- **Wikilink targets don't exist** — proposed links reference pages not yet in aa2brain. Either create the linked pages in the same batch, or replace with links to existing pages.
