# WS-004 — Bootstrap Deck (First Production)

- **Type:** Workstream — multi-agent composition. Produces a deck's v1.0.0 from scratch.
- **Owners:** Larry (orchestration), Pax (research), Rex (argument), Coda (production), Vera (adversarial), Aria (persuasion)
- **References:** [[docs/deck-folder-spec]], [[docs/engine-decisions]], [[docs/superpowers/specs/2026-05-25-engine-design]], [[GL-001-file-naming-conventions]], [[myPKA/Team Knowledge/Templates/decisions-template]], [[WS-006-slide-plan-design-selection]]
- **Trigger:** Once per deck topic, initiated by Larry + Adnan when a new spiky PoV is ready to research and produce.

---

## Purpose

Produce v1.0.0 of a new deck: lock the PoV, research it, map the argument, gate on quality, produce audience-specific HTML slides, score them on four dimensions, and submit a PR for Adnan's review.

This workstream runs once per topic. From v1.1.0 onwards, improvement cycles run via [[WS-005-improvement-cycle]].

---

## Inputs

| Field | Description |
|---|---|
| `topic` | Deck subject (e.g. "AI and Kids") |
| `slug` | Kebab-case folder name (e.g. `ai-and-kids`) |
| `pov_draft` | Adnan's initial spiky PoV — one sentence, falsifiable |
| `audiences` | List of audience variants for v1.0.0 (e.g. `parents`, `teachers`) |
| `theme` | `light` or `dark` — which base theme Coda applies |
| `engagement_level` | Defaults to `collaborative` unless Adnan specifies otherwise |

---

## Outputs

| Artifact | Path |
|---|---|
| PoV file | `decks/<slug>/pov.md` |
| Decisions log | `decks/<slug>/decisions.md` |
| Research brief | `decks/<slug>/research/YYYY-MM-DD-research-brief-v1.md` |
| Argument map | `decks/<slug>/reports/YYYY-MM-DD-argument-map-v1.md` |
| Canonical deck | `decks/<slug>/versions/v1.0.0/canonical.html` |
| Audience variants | `decks/<slug>/versions/v1.0.0/<audience>.html` × N |
| Argument scorecard | `decks/<slug>/scorecards/v1.0.0-argument.md` |
| Adversarial scorecard | `decks/<slug>/scorecards/v1.0.0-adversarial.md` |
| Persuasion scorecards | `decks/<slug>/scorecards/v1.0.0-persuasion-<audience>.md` × N |
| GitHub PR | — |

---

## Choreography

### Step 1 — PoV Lock (Larry + Adnan)

Larry reviews the draft PoV against three criteria:
1. **Falsifiable** — can evidence overturn it?
2. **Controversial** — would a reasonable person disagree?
3. **Specific** — a concrete claim, not a vague opinion

If the PoV passes all three: Larry writes `pov.md` and creates the deck folder structure (below). If not: Larry proposes refinements; Adnan approves before continuing.

**Write `decks/<slug>/pov.md`:**
```yaml
---
topic: <topic>
pov: <one-sentence spiky claim>
engagement_level: collaborative
current_version: v0.0.0
status: active
---
```

**Create deck folder structure:**
```
decks/<slug>/
  pov.md
  decisions.md            ← copy from myPKA/Team Knowledge/Templates/decisions-template.md, update header
  theme/
    <slug>.css            ← empty file; Coda populates with deck-specific overrides
  research/
  versions/
  scorecards/
  reports/
```

### Step 2 — Research (Pax)

Larry briefs Pax:

> "Research the following PoV for the `<topic>` deck: `<pov>`. Mine aa2brain first — look for existing notes, articles, and derived concepts relevant to this claim. Then search external sources. Cross-verify all significant claims across two or more independent credible sources. Produce a structured research brief at `decks/<slug>/research/YYYY-MM-DD-research-brief-v1.md`. Structure it as: (1) supporting evidence with source citations, (2) credible counter-evidence, (3) source quality flags. Audience variants for this deck: `<audiences>`."

Pax output: research brief filed at the specified path.

### Step 3 — Argument Map (Rex)

Larry briefs Rex:

> "Read Pax's research brief at `decks/<slug>/research/YYYY-MM-DD-research-brief-v1.md` and the PoV in `decks/<slug>/pov.md`. Build an argument map: identify the core claim, the supporting warrants, the evidence behind each warrant, logical gaps (missing steps, unstated assumptions), and any non-sequiturs. Assign an argument score (1–10). File your report at `decks/<slug>/reports/YYYY-MM-DD-argument-map-v1.md`."

Rex output: argument map + argument score.

### Step 4 — Collaborative Checkpoint (Larry → Adnan)

Larry surfaces to Adnan:
- Link: `decks/<slug>/research/YYYY-MM-DD-research-brief-v1.md`
- Link: `decks/<slug>/reports/YYYY-MM-DD-argument-map-v1.md`
- Rex's argument score

**Decision gate:**

| Condition | Action |
|---|---|
| Score sufficient (Rex finds no critical gaps; argument supports PoV) | Proceed to Step 5 |
| Score low (Rex flags critical gaps or weak evidence) | Adnan chooses: (a) or (b) below |

- **(a) Tighten:** Return to Pax (Step 2) with Rex's specific gaps flagged. Pax supplements research. Rex re-audits. Repeat until score is sufficient.
- **(b) PoV falsified:** Larry + Adnan decide: refine the PoV and restart at Step 1, or set `pov.md` `status: overturned` and archive the deck. Larry logs the falsification decision in `decisions.md`.

### Step 5 — Slide Plan & Design Selection (WS-006)

Larry runs [[WS-006-slide-plan-design-selection]] with inputs:
- `slug`: `<slug>`
- `argument_map`: `decks/<slug>/reports/YYYY-MM-DD-argument-map-v1.md`
- `research_brief`: `decks/<slug>/research/YYYY-MM-DD-research-brief-v1.md`
- `pov_path`: `decks/<slug>/pov.md`
- `audiences`: `<audiences>`

WS-006 exits with an approved slide plan, a chosen template recorded in `pov.md`, and Iris's Coda tips. Proceed to Step 5a.

### Step 5a — Deck Production (Coda Pass 2)

Larry briefs Coda:

> "Produce `decks/<slug>/versions/v1.0.0/canonical.html` and audience variants `<audiences>`. Approved slide plan: `decks/<slug>/reports/YYYY-MM-DD-slide-plan-v1.md`. Chosen template: read `design_template` from `decks/<slug>/pov.md` and use `shared/design-library/<template>/sample.html` and `README.md` as your visual reference. Raw source: `shared/design-library/_source/`. Write each slide against its row in the slide plan — type, purpose, and content_summary are the brief for that slide. Honour all Coda tips from the design proposal. After producing HTML, run the humanizer skill on all slide text and speaker notes."

Coda output: `versions/v1.0.0/canonical.html` + `versions/v1.0.0/<audience>.html` × N.

### Step 5b — Image Brief (Iris)

Larry briefs [[Iris]] with links to the HTML files produced in Step 5, the research brief, and the argument map. Iris produces `decks/<slug>/image-briefs/YYYY-MM-DD-image-brief-v1.md` — one structured entry per slide that benefits from an image, each with prompt, model recommendation, aspect ratio, style direction, and negative constraints. Mack executes the brief via `scripts/generate-image.py`. Coda wires the generated image paths into the HTML files.

### Step 6 — Humanizer Pass + Screenshot Verification (Coda)

**Hard gate — Larry verifies before Step 7 proceeds.**

Coda runs the humanizer skill on all text content (slide body, speaker notes) in every HTML file. Then takes a screenshot of every slide using `scripts/screenshot-slide.js` and checks:
- No slide clips content at 1280×720
- Every slide has one dominant visual focal point (large stat, single phrase, or image)
- No slide exceeds ~30 words of body text

Coda files a brief layout report to Larry: any clipping, any verbosity violations, any slides without a focal point. Larry reviews and either approves (proceed to Step 7) or returns to Coda for fixes. This step is not complete until Larry's explicit approval.

### Step 7 — Scoring (Rex, Vera, Aria — parallel)

Larry briefs all three specialists in the same message:

**Rex brief:** "Logic-audit `decks/<slug>/versions/v1.0.0/canonical.html`. Evaluate argument coherence, gap coverage, and warrant strength against your argument map from `reports/YYYY-MM-DD-argument-map-v1.md`. File scorecard at `decks/<slug>/scorecards/v1.0.0-argument.md`."

**Vera brief:** "Adversarial pass on the PoV in `decks/<slug>/pov.md` and the deck at `decks/<slug>/versions/v1.0.0/canonical.html`. Mount the strongest available counter-arguments. Evaluate how well the deck responds. File scorecard at `decks/<slug>/scorecards/v1.0.0-adversarial.md`."

**Aria brief (one per audience):** "Score the persuasion quality of `decks/<slug>/versions/v1.0.0/<audience>.html` for a `<audience>` audience. Evaluate: emotional resonance, narrative clarity, and CTA strength for this specific audience. File scorecard at `decks/<slug>/scorecards/v1.0.0-persuasion-<audience>.md`."

### Step 8 — PR Compilation (Larry)

Larry compiles a GitHub PR following the PR format in [[docs/superpowers/specs/2026-05-25-engine-design]].

For bootstrap PRs:
- Add a PoV confirmation line above the synthesis: `**PoV:** <pov>`
- Score delta table shows baseline scores only — label the "Prior" column as "—" (no prior version exists)
- Link all specialist reports and scorecards

### Step 9 — Review and Merge (Adnan)

Adnan reviews PR → merges → Larry tags `v1.0.0` in git and updates `pov.md`:

```yaml
current_version: v1.0.0
```

---

## Significance Thresholds (carried from WS-005)

The bootstrap workstream does not use a significance threshold — all research is in scope for v1.0.0. Thresholds apply only to improvement cycles. See [[WS-005-improvement-cycle]].
