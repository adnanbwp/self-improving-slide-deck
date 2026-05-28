# WS-006 — Slide Plan & Design Selection

- **Type:** Workstream — called by WS-004 (Step 5) and WS-005 (Step 5) before Coda writes any HTML
- **Owners:** Coda (Pass 1), Larry (review gates), Iris (design proposal), Adnan (approvals)
- **References:** [[docs/superpowers/specs/2026-05-26-slide-plan-design-selection-design]], [[shared/slide-vocabulary]], [[shared/design-library/INDEX]], [[GL-001-file-naming-conventions]]
- **Trigger:** Called from WS-004 Step 5 and WS-005 Step 5. Never triggered standalone.

---

## Purpose

Resolve three decisions before Coda writes a single slide:
1. What is the purpose and narrative role of each slide?
2. What type of slide best conveys that message?
3. What visual design language should the deck use?

Exits with an approved slide plan, a chosen template recorded in `pov.md`, and Iris's Coda tips ready for Coda Pass 2.

---

## Inputs

| Field | Description |
|---|---|
| `slug` | Deck folder name |
| `argument_map` | Path to Rex's argument map |
| `research_brief` | Path to Pax's research brief |
| `pov_path` | `decks/<slug>/pov.md` |
| `audiences` | List of audience variants |
| `prior_slide_plan` | Path to prior version's slide plan (WS-005 only; omit for WS-004) |

---

## Outputs

| Artifact | Path |
|---|---|
| Slide plan | `decks/<slug>/reports/YYYY-MM-DD-slide-plan-vN.md` |
| Design proposal | `decks/<slug>/reports/YYYY-MM-DD-design-proposal-vN.md` |
| Chosen template | Recorded in `decks/<slug>/pov.md` under `design_template` |

---

## Carry-forward rule (WS-005 only)

When called from an improvement cycle, Coda Pass 1 starts from the prior slide plan and updates only rows where new evidence warrants a change. A slide warrants an update when the new research: (a) contradicts its `content_summary`, (b) introduces stronger evidence for its `purpose`, or (c) changes the narrative reason for its position in the argument.

The design template carries forward from `pov.md` unless Adnan explicitly requests a redesign, in which case Step 3 (Iris proposal) runs in full.

**Ceremony reduction:** If Coda's delta produces zero `type` changes and zero `purpose` changes, Larry may surface the slide plan as FYI and proceed without requiring explicit approval unless Adnan requests a review.

---

## Choreography

### Step 1 — Slide Plan (Coda Pass 1)

Larry briefs Coda:

> "Produce a slide plan — no HTML — for the `<topic>` deck. Read the argument map at `<argument_map>` and the research brief at `<research_brief>`. For each slide, produce a row with: slide number, purpose (one sentence), narrative_reason (why this slide sits here in the argument flow), type (one of the 21 types from `shared/slide-vocabulary.md` — use `UNCLASSIFIED` if no type fits, with a one-sentence explanation), and content_summary (one-line summary of actual content). File the plan at `decks/<slug>/reports/YYYY-MM-DD-slide-plan-vN.md`."
>
> For WS-005 calls, add: "Start from the prior slide plan at `<prior_slide_plan>`. Update only rows where new evidence warrants a change per the carry-forward rule in WS-006."

Coda output: slide plan filed at the specified path.

### Step 2 — Slide Plan Review (Larry → Adnan)

Larry runs a vocabulary compliance check before surfacing: every `type` value must match one of the 21 entries in `shared/slide-vocabulary.md`. Any `UNCLASSIFIED` slide is flagged explicitly with Coda's explanation.

Larry surfaces the slide plan to Adnan. Adnan can: approve, request changes, resolve UNCLASSIFIED slides, or collapse/merge slides. Larry re-briefs Coda if changes are needed.

**Hard gate:** WS-006 does not proceed to Step 3 until the slide plan is approved and all type values are resolved.

**WS-005 shortcut:** If the delta has zero `type` and zero `purpose` changes, Larry surfaces as FYI and proceeds without requiring explicit approval, unless Adnan requests a review.

### Step 3 — Design Proposal (Iris)

Larry briefs Iris:

> "Read the approved slide plan at `decks/<slug>/reports/YYYY-MM-DD-slide-plan-vN.md`, the design library index at `shared/design-library/INDEX.md`, and the raw source at `shared/design-library/_source/<slug>/design.md` and `template.html` for each candidate (the annotated README is a reference only — the source files are canonical). Read the PoV at `decks/<slug>/pov.md` for topic, audience(s), and tone. Select three template candidates using ranked criteria: (1) slide-type coverage — does the template have native patterns for the majority of types in this deck's slide plan?, (2) aesthetic register fit — does the template's visual register match the deck's PoV tone and audience?, (3) audience resonance — which candidate best holds attention and builds trust with the specific audience(s)?
>
> Produce a design proposal at `decks/<slug>/reports/YYYY-MM-DD-design-proposal-vN.md` with:
> - **Section 1:** Three template options with deck-level rationale (strengths, weaknesses, risks for this specific deck and audience). For each candidate, include a **Canonical vs. adaptation** paragraph that names: what colors, fonts, and structural patterns the canonical template uses; what the design system substitutes; and what is lost in that substitution. If a template's defining characteristic (e.g. Signal's antique gold accent, dual-surface model, or Source Serif 4 italic) is being replaced by design-system equivalents, name it explicitly so Adnan can decide whether to accept the substitution or apply the template canonically.
> - **Section 2:** A per-slide table with one row per slide: slide number, purpose, narrative reason, type (from the slide plan), and a fit assessment for each of the three options using: Very strong (native pattern exists in sample.html — no structural adaptation needed) / Strong (minor CSS adjustment needed) / Moderate (structural adaptation required). A Coda tip is required on every Moderate cell. Coda tips on Strong or Very strong cells are optional — add only where a non-obvious enhancement exists."

**Minimum library floor:** If `shared/design-library/INDEX.md` has fewer than 3 annotated entries, Iris produces a partial proposal labelled "Partial proposal — N of 3 options available" and Larry surfaces this to Adnan with the option to wait for full annotation or proceed.

### Step 4 — Template Pick (Larry → Adnan)

Larry surfaces the design proposal. Adnan selects one of the three options. Larry:
- Records the choice: `design_template: <template-slug>` in `decks/<slug>/pov.md`
- Logs the selection rationale in `decks/<slug>/decisions.md`

**Template lock protocol:**

| Condition | Action |
|---|---|
| Pass 2 not yet started | Change template freely — update `pov.md`, re-extract Coda tips, re-brief Coda |
| Pass 2 in progress, fewer than half the slides written | Full restart — discard in-progress HTML, update `pov.md`, re-brief Coda |
| Pass 2 in progress, more than half the slides written | Larry surfaces cost tradeoff to Adnan. Default: complete Pass 2 with current template; address redesign in next improvement cycle |

### Step 5 — Hand off to Coda Pass 2

Larry briefs Coda with:
- Approved slide plan path
- Chosen template name and library path (`shared/design-library/<template-slug>/`)
- Raw source path (`shared/design-library/_source/`) for patterns not yet in annotated entry
- All Coda tips extracted from the design proposal, keyed by slide number
- **Reveal.js constraint (mandatory boilerplate for all Reveal.js decks):** "Do not modify `display` or add `overflow: hidden` to `.reveal .slides section` in CSS. If flex layout is needed on sections, set `display: 'flex'` in `Reveal.initialize()` config — Reveal manages section display via inline styles and CSS overrides break slide navigation. Do not add any section-level CSS that could interfere with Reveal.js's transform-based slide management."

Coda writes each slide against its row in the slide plan. The chosen template's `sample.html` and `README.md` are the visual reference. Slides with a Coda tip must honour that tip.

WS-006 is complete. Control returns to WS-004 Step 5a or WS-005 Step 5a.
