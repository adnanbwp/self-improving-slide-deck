# WS-006 — Slide Plan & Design Selection

- **Type:** Workstream — called by WS-004 (Step 5) and WS-005 (Step 5) before Coda writes any HTML
- **Owners:** Aria (narrative spine), Coda (Pass 1), Larry (review gates), Iris (design proposal), Adnan (approvals)
- **References:** [[docs/superpowers/specs/2026-05-26-slide-plan-design-selection-design]], [[shared/slide-vocabulary]], [[shared/design-library/INDEX]], [[GL-001-file-naming-conventions]]
- **Trigger:** Called from WS-004 Step 5 and WS-005 Step 5. Never triggered standalone.

---

## Purpose

Resolve four decisions before Coda writes a single slide:
0. What story is the argument told through — which arc, hook, and beats? (the **narrative spine**, Aria via `/tactics` SHAPE)
1. What is the purpose and narrative role of each slide? (each slide maps to a beat in the spine)
2. What type of slide best conveys that message?
3. How does each slide map onto the brand templating system's layouts?

**Brand default (from 2026-06-10):** every deck uses the **aha agile templating system** at `shared/templates/aha-agile/` (brand source of truth: `shared/aha-agile-brand/`). The three-candidate design-library selection only runs when Adnan explicitly requests an off-brand deck; otherwise Step 3 is a layout-mapping proposal against the brand system and Step 4 is skipped.

Exits with an approved slide plan, `design_template: aha-agile` recorded in `pov.md`, and Iris's per-slide layout mapping + Coda tips ready for Coda Pass 2.

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
| `prior_narrative_spine` | Path to prior version's narrative spine (WS-005 only; omit for WS-004) |

---

## Outputs

| Artifact | Path |
|---|---|
| Narrative spine | `decks/<slug>/reports/YYYY-MM-DD-narrative-spine-vN.md` |
| Slide plan | `decks/<slug>/reports/YYYY-MM-DD-slide-plan-vN.md` |
| Design proposal | `decks/<slug>/reports/YYYY-MM-DD-design-proposal-vN.md` |
| Chosen template | Recorded in `decks/<slug>/pov.md` under `design_template` |

---

## Carry-forward rule (WS-005 only)

When called from an improvement cycle, Coda Pass 1 starts from the prior slide plan and updates only rows where new evidence warrants a change. A slide warrants an update when the new research: (a) contradicts its `content_summary`, (b) introduces stronger evidence for its `purpose`, or (c) changes the narrative reason for its position in the argument.

The narrative spine carries forward from the prior version — Aria keeps the same arc and hook unless new evidence or a PoV change breaks it, or the prior version's narrative scorecard flagged an arc-level FAIL. A changed arc reorders the slide plan and is not a carry-forward delta.

The design template carries forward from `pov.md` unless Adnan explicitly requests a redesign, in which case Step 3 (Iris proposal) runs in full.

**Ceremony reduction:** If Coda's delta produces zero `type` changes and zero `purpose` changes, Larry may surface the slide plan as FYI and proceed without requiring explicit approval unless Adnan requests a review.

---

## Choreography

### Step 0 — Narrative Spine (Aria, `/tactics` SHAPE)

Larry briefs Aria:

> "Shape the narrative spine for the `<topic>` deck. Read the PoV at `<pov_path>`, the argument map at `<argument_map>`, and the research brief at `<research_brief>`. Run the `/tactics` skill in Shape mode with the deck's objective (PoV + engagement level + audience). Return the family + recipe, ONE chosen arc, a hook approach with an example opening line, and the beat scaffold. File it at `decks/<slug>/reports/YYYY-MM-DD-narrative-spine-vN.md`."
>
> For WS-005 calls, add: "The prior spine is at `<prior_narrative_spine>`. Keep the same arc unless the new evidence or a PoV change breaks it; if you change the arc, say why."

Aria output: narrative spine filed at the specified path. This is structural guidance for Coda, not slide content — producing it does not make Aria a self-marker at the narrative scoring gate.

**Hard gate:** WS-006 does not proceed to Step 1 until the arc and hook are chosen. Larry may surface the spine to Adnan as FYI; the arc choice is Aria's to make from the objective.

### Step 1 — Slide Plan (Coda Pass 1)

Larry briefs Coda:

> "Produce a slide plan — no HTML — for the `<topic>` deck. Read the narrative spine at `decks/<slug>/reports/YYYY-MM-DD-narrative-spine-vN.md`, the argument map at `<argument_map>`, and the research brief at `<research_brief>`. Order the deck along the spine's beats. For each slide, produce a row with: slide number, purpose (one sentence), narrative_reason (**which beat of the spine this slide serves and why it sits here**), type (one of the 21 types from `shared/slide-vocabulary.md` — use `UNCLASSIFIED` if no type fits, with a one-sentence explanation), and content_summary (one-line summary of actual content). File the plan at `decks/<slug>/reports/YYYY-MM-DD-slide-plan-vN.md`."
>
> For WS-005 calls, add: "Start from the prior slide plan at `<prior_slide_plan>`. Update only rows where new evidence warrants a change per the carry-forward rule in WS-006."

Coda output: slide plan filed at the specified path.

### Step 2 — Slide Plan Review (Larry → Adnan)

Larry runs a vocabulary compliance check before surfacing: every `type` value must match one of the 21 entries in `shared/slide-vocabulary.md`. Any `UNCLASSIFIED` slide is flagged explicitly with Coda's explanation.

Larry surfaces the slide plan to Adnan. Adnan can: approve, request changes, resolve UNCLASSIFIED slides, or collapse/merge slides. Larry re-briefs Coda if changes are needed.

**Hard gate:** WS-006 does not proceed to Step 3 until the slide plan is approved and all type values are resolved.

**WS-005 shortcut:** If the delta has zero `type` and zero `purpose` changes, Larry surfaces as FYI and proceeds without requiring explicit approval, unless Adnan requests a review.

### Step 3 — Layout Mapping Proposal (Iris) — brand default

Larry briefs Iris:

> "Read the approved slide plan at `decks/<slug>/reports/YYYY-MM-DD-slide-plan-vN.md`, the brand templating system README at `shared/templates/aha-agile/README.md` (slide-type catalogue, content budgets, field rules), and the PoV at `decks/<slug>/pov.md` for topic, audience(s), and tone.
>
> Produce a design proposal at `decks/<slug>/reports/YYYY-MM-DD-design-proposal-vN.md` with:
> - **Section 1:** Field allocation for the deck — which slides shout (`f-orange`), which read (`f-paper`), which break (`f-ink`), with a one-paragraph rationale for the rhythm across the deck arc.
> - **Section 2:** A per-slide table with one row per slide: slide number, purpose, narrative reason, type (from the slide plan), the chosen `t-*` layout from the catalogue, the field class, and a budget check (does the planned content fit the layout's documented budget? If not, the Coda tip must say what to tighten or split). A Coda tip is required wherever the budget check fails or a production extension (`t-content`, `t-cards`, `t-figure`, `t-stat-grid`) needs non-obvious composition."

**Off-brand exception:** Only when Adnan explicitly requests a non-brand deck, run the legacy three-candidate selection against `shared/design-library/INDEX.md` (criteria: slide-type coverage, aesthetic register fit, audience resonance; canonical-vs-adaptation paragraphs per candidate; minimum library floor of 3 annotated entries) and then run Step 4.

### Step 4 — Template Pick (Larry → Adnan) — off-brand decks only

Skipped on the brand default — Larry records `design_template: aha-agile` in `decks/<slug>/pov.md` without a pick. For an off-brand deck, Adnan selects one of the three options and Larry records the choice in `pov.md` and the rationale in `decks/<slug>/decisions.md`.

**Template lock protocol:**

| Condition | Action |
|---|---|
| Pass 2 not yet started | Change template freely — update `pov.md`, re-extract Coda tips, re-brief Coda |
| Pass 2 in progress, fewer than half the slides written | Full restart — discard in-progress HTML, update `pov.md`, re-brief Coda |
| Pass 2 in progress, more than half the slides written | Larry surfaces cost tradeoff to Adnan. Default: complete Pass 2 with current template; address redesign in next improvement cycle |

### Step 5 — Hand off to Coda Pass 2

Larry briefs Coda with:
- Approved slide plan path
- The brand system paths: `shared/templates/aha-agile/` (start every deck from `deck-skeleton.html`; `README.md` budgets and field rules are binding)
- All Coda tips extracted from the design proposal, keyed by slide number
- **Budget constraint (mandatory boilerplate):** "Respect the content budgets in `shared/templates/aha-agile/README.md`. If content exceeds a layout's budget, tighten the copy or split the slide — never shrink fonts, never restyle `engine.css` selectors, never unlock a layout. Speaker notes go in `<aside class="notes">` inside each `.slide` (the engine hides them)."
- **(Legacy Reveal.js decks only, e.g. patching a pre-v2 version):** "Do not modify `display` or add `overflow: hidden` to `.reveal .slides section` in CSS. If flex layout is needed on sections, set `display: 'flex'` in `Reveal.initialize()` config."

Coda writes each slide against its row in the slide plan, on the layout and field assigned in the design proposal. Slides with a Coda tip must honour that tip.

WS-006 is complete. Control returns to WS-004 Step 5a or WS-005 Step 5a.
