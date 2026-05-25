# Engine Infrastructure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the self-improving slide deck engine infrastructure: shared Reveal.js assets and CSS design system, two workstream documents (WS-004 bootstrap, WS-005 improvement cycle), and the AI & Kids first-deck scaffold.

**Architecture:** Three independent phases. Phase 1 builds the shared asset layer all decks reference. Phase 2 writes the workstream documents that define how the engine operates. Phase 3 scaffolds the first deck so WS-004 can be run immediately after.

**Tech Stack:** Reveal.js 5.1.0 (no build step), CSS custom properties, plain HTML, markdown (myPKA workstream format).

---

## Phase 1: Shared Infrastructure

### Task 1: Create shared/ directory scaffold and download Reveal.js

**Files:**
- Create: `shared/branding/` (directory)
- Create: `shared/lib/` (directory)
- Create: `shared/templates/` (directory)
- Create: `shared/lib/reveal.js`
- Create: `shared/lib/reveal.css`
- Create: `shared/lib/reset.css`

- [ ] **Step 1: Create directories**

```bash
mkdir -p shared/branding shared/lib shared/templates
```

Expected: no output, no error.

- [ ] **Step 2: Verify directories exist**

```bash
ls shared/
```

Expected output:
```
branding  lib  templates
```

- [ ] **Step 3: Download Reveal.js library files**

```bash
curl -s -o shared/lib/reveal.js https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/reveal.js
curl -s -o shared/lib/reveal.css https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/reveal.css
curl -s -o shared/lib/reset.css https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/reset.css
```

- [ ] **Step 4: Verify downloads are non-empty**

```bash
wc -c shared/lib/reveal.js shared/lib/reveal.css shared/lib/reset.css
```

Expected: all three files over 1000 bytes. If any is 0 bytes or shows an HTML error page, re-run the curl for that file.

- [ ] **Step 5: Commit**

```bash
git add shared/
git commit -m "feat: scaffold shared/ and download Reveal.js 5.1.0"
```

---

### Task 2: Write shared/branding/base.css

**Files:**
- Create: `shared/branding/base.css`

- [ ] **Step 1: Write base.css**

```css
/* ==========================================================
   base.css — shared variables, type scale, layout primitives
   Imported by theme-dark.css and theme-light.css.
   ========================================================== */

:root {
  /* Font families */
  --font-display: Georgia, 'Times New Roman', serif;
  --font-body: -apple-system, 'Segoe UI', system-ui, sans-serif;

  /* Type scale */
  --text-xs:   0.65rem;
  --text-sm:   0.85rem;
  --text-base: 1.1rem;
  --text-lg:   1.5rem;
  --text-xl:   2.2rem;
  --text-2xl:  3rem;
  --text-3xl:  4rem;

  /* Tracking */
  --tracking-wide:   0.06em;
  --tracking-widest: 0.18em;

  /* Leading */
  --leading-tight:  1.15;
  --leading-normal: 1.5;
}

/* --- Reveal base overrides -------------------------------- */

.reveal {
  font-family: var(--font-body);
  font-size: 1rem;
  line-height: var(--leading-normal);
}

.reveal h1 {
  font-family: var(--font-display);
  font-size: var(--text-3xl);
  font-weight: 400;
  font-style: italic;
  line-height: var(--leading-tight);
  margin: 0 0 1.5rem;
  text-transform: none;
  letter-spacing: normal;
}

.reveal h2 {
  font-family: var(--font-display);
  font-size: var(--text-2xl);
  font-weight: 400;
  font-style: italic;
  line-height: var(--leading-tight);
  margin: 0 0 1.2rem;
  text-transform: none;
  letter-spacing: normal;
}

.reveal h3 {
  font-family: var(--font-body);
  font-size: var(--text-xl);
  font-weight: 700;
  line-height: var(--leading-tight);
  margin: 0 0 1rem;
  text-transform: none;
  letter-spacing: normal;
}

.reveal p {
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  margin: 0 0 1rem;
}

.reveal ul,
.reveal ol {
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  margin: 0 0 1rem 1.5rem;
}

.reveal li {
  margin-bottom: 0.5rem;
}

/* --- Slide layout primitives ------------------------------ */

/* Every slide is left-aligned, no Reveal centering */
.reveal section {
  text-align: left;
  padding: 3rem 3.5rem 4.5rem;
  box-sizing: border-box;
  height: 100%;
  position: relative;
  top: auto;
}

/* Header: deck label left, author right — separated by accent rule */
.slide-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding-bottom: 0.75rem;
  margin-bottom: 2.5rem;
}

/* Footer: slide number left, deck label right */
.slide-footer {
  position: absolute;
  bottom: 2rem;
  left: 3.5rem;
  right: 3.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Editorial grid: 3 content columns, 1 margin column */
.slide-grid {
  display: grid;
  grid-template-columns: 3fr 1fr;
  gap: 3rem;
  align-items: start;
}

/* --- Text classes ----------------------------------------- */

.section-label {
  font-family: var(--font-body);
  font-size: var(--text-xs);
  font-weight: 700;
  letter-spacing: var(--tracking-widest);
  text-transform: uppercase;
  margin: 0 0 0.75rem;
  display: block;
}

.deck-label {
  font-family: var(--font-body);
  font-size: var(--text-xs);
  letter-spacing: var(--tracking-widest);
  text-transform: uppercase;
}

.page-num {
  font-family: var(--font-body);
  font-size: var(--text-xs);
  letter-spacing: var(--tracking-wide);
}

/* Horizontal rule between header and content */
.slide-rule {
  width: 2rem;
  height: 1px;
  margin: 1.5rem 0;
  border: none;
}
```

- [ ] **Step 2: Commit**

```bash
git add shared/branding/base.css
git commit -m "feat: add shared branding base.css"
```

---

### Task 3: Write theme-dark.css and theme-light.css

**Files:**
- Create: `shared/branding/theme-dark.css`
- Create: `shared/branding/theme-light.css`

- [ ] **Step 1: Write theme-dark.css**

```css
/* ==========================================================
   theme-dark.css — Editorial Dark (A1)
   Warm charcoal base (#1a1614), amber accent (#c97d2a).
   Default theme for most decks.
   ========================================================== */
@import './base.css';

:root {
  --bg:           #1a1614;
  --text-primary: #f5ede3;
  --text-muted:   #6b5a47;
  --accent:       #c97d2a;
  --divider:      rgba(201, 125, 42, 0.35);
}

.reveal-viewport { background: var(--bg); }

.reveal                     { color: var(--text-primary); }
.reveal h1, .reveal h2      { color: var(--text-primary); }
.reveal h3                  { color: var(--text-primary); }
.reveal p, .reveal li       { color: var(--text-primary); }

.section-label              { color: var(--accent); }
.deck-label                 { color: var(--text-muted); }
.page-num                   { color: var(--text-muted); }
.slide-rule                 { background: var(--accent); }

.slide-header               { border-bottom: 1px solid var(--divider); }

.reveal a                   { color: var(--accent); text-decoration: underline; }
.reveal a:hover             { opacity: 0.8; }
```

- [ ] **Step 2: Write theme-light.css**

```css
/* ==========================================================
   theme-light.css — Warm Light (C)
   Cream base (#faf7f2), amber accent (#b45309).
   Default theme for AI & Kids deck.
   ========================================================== */
@import './base.css';

:root {
  --bg:           #faf7f2;
  --text-primary: #1c1917;
  --text-muted:   #78716c;
  --accent:       #b45309;
  --divider:      rgba(180, 83, 9, 0.25);
}

.reveal-viewport { background: var(--bg); }

.reveal                     { color: var(--text-primary); }
.reveal h1, .reveal h2      { color: var(--text-primary); }
.reveal h3                  { color: var(--text-primary); }
.reveal p, .reveal li       { color: var(--text-primary); }

.section-label              { color: var(--accent); }
.deck-label                 { color: var(--text-muted); }
.page-num                   { color: var(--text-muted); }
.slide-rule                 { background: var(--accent); }

.slide-header               { border-bottom: 1px solid var(--divider); }

.reveal a                   { color: var(--accent); text-decoration: underline; }
.reveal a:hover             { opacity: 0.8; }
```

- [ ] **Step 3: Commit**

```bash
git add shared/branding/theme-dark.css shared/branding/theme-light.css
git commit -m "feat: add dark and light theme CSS"
```

---

### Task 4: Write slide-template.html and smoke test

**Files:**
- Create: `shared/templates/slide-template.html`
- Create (temp): `shared/templates/smoke-test.html` — delete after verification

The template uses paths correct for its deployed location at `decks/<slug>/versions/v<N>/`. The smoke test uses sibling paths (`../lib/`, `../branding/`) so it can be served directly from `shared/`.

- [ ] **Step 1: Write slide-template.html**

This is the file Coda copies to `decks/<slug>/versions/v<N>/canonical.html` and adapts. Paths are written for the deployed location.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DECK_TITLE — AUTHOR_NAME</title>

  <!--
    PATH NOTE: This template is deployed at decks/<slug>/versions/v<N>/canonical.html
    All paths below are relative to that deployed location.
    shared/ lives three levels up: ../../../shared/
  -->
  <link rel="stylesheet" href="../../../shared/lib/reset.css">
  <link rel="stylesheet" href="../../../shared/lib/reveal.css">

  <!-- Theme: swap theme-light.css for theme-dark.css per deck -->
  <link rel="stylesheet" href="../../../shared/branding/theme-light.css">

  <!-- Per-deck overrides (empty file on first production; Coda adds deck-specific values) -->
  <link rel="stylesheet" href="../../theme/DECK_SLUG.css">
</head>
<body>

<div class="reveal">
  <div class="slides">

    <!-- ═══════════════════════════════════════════════
         TITLE SLIDE
         ═══════════════════════════════════════════════ -->
    <section>
      <div class="slide-header">
        <span class="deck-label">DECK_LABEL</span>
        <span class="deck-label">AUTHOR_NAME</span>
      </div>

      <span class="section-label">FRAMING_PHRASE</span>
      <h1>DECK_TITLE</h1>
      <hr class="slide-rule">

      <div class="slide-footer">
        <span class="page-num">1</span>
        <span class="deck-label">DECK_LABEL</span>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════
         CONTENT SLIDE — single column
         ═══════════════════════════════════════════════ -->
    <section>
      <div class="slide-header">
        <span class="deck-label">SECTION_NAME</span>
        <span class="deck-label">AUTHOR_NAME</span>
      </div>

      <span class="section-label">SECTION_NAME</span>
      <h2>SLIDE_TITLE</h2>
      <p>SLIDE_BODY</p>

      <div class="slide-footer">
        <span class="page-num">N</span>
        <span class="deck-label">DECK_LABEL</span>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════
         CONTENT SLIDE — editorial grid (content + margin)
         ═══════════════════════════════════════════════ -->
    <section>
      <div class="slide-header">
        <span class="deck-label">SECTION_NAME</span>
        <span class="deck-label">AUTHOR_NAME</span>
      </div>

      <div class="slide-grid">
        <div>
          <span class="section-label">SECTION_NAME</span>
          <h2>SLIDE_TITLE</h2>
          <p>SLIDE_BODY</p>
        </div>
        <div>
          <!-- Margin column: pull quote, stat, or source citation -->
          <p style="font-size: var(--text-sm); color: var(--text-muted); font-style: italic;">MARGIN_NOTE</p>
        </div>
      </div>

      <div class="slide-footer">
        <span class="page-num">N</span>
        <span class="deck-label">DECK_LABEL</span>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════
         REFERENCE SLIDE — for live deep-dive
         ═══════════════════════════════════════════════ -->
    <section>
      <div class="slide-header">
        <span class="deck-label">Reference</span>
        <span class="deck-label">AUTHOR_NAME</span>
      </div>

      <span class="section-label">Reference</span>
      <h3>SOURCE_TITLE</h3>
      <p>SOURCE_SUMMARY</p>
      <p style="font-size: var(--text-sm); color: var(--text-muted);">SOURCE_CITATION</p>

      <div class="slide-footer">
        <span class="page-num">R</span>
        <span class="deck-label">DECK_LABEL</span>
      </div>
    </section>

  </div>
</div>

<script src="../../../shared/lib/reveal.js"></script>
<script>
  Reveal.initialize({
    hash: true,
    controls: true,
    progress: false,
    center: false,
    slideNumber: false,
    transition: 'none',
    transitionSpeed: 'fast',
  });
</script>
</body>
</html>
```

- [ ] **Step 2: Write smoke-test.html (temp — delete after step 4)**

This file uses sibling paths so it can be served from `shared/` directly:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Smoke Test</title>
  <link rel="stylesheet" href="../lib/reset.css">
  <link rel="stylesheet" href="../lib/reveal.css">
  <link rel="stylesheet" href="../branding/theme-light.css">
</head>
<body>
<div class="reveal">
  <div class="slides">
    <section>
      <div class="slide-header">
        <span class="deck-label">Smoke Test</span>
        <span class="deck-label">Adnan Ali</span>
      </div>
      <span class="section-label">Verification</span>
      <h1>Template renders correctly.</h1>
      <hr class="slide-rule">
      <p>Cream background. Amber accent on section label. Italic serif h1. Left-aligned.</p>
      <div class="slide-footer">
        <span class="page-num">1</span>
        <span class="deck-label">Smoke Test</span>
      </div>
    </section>
    <section>
      <div class="slide-header">
        <span class="deck-label">Dark Theme</span>
        <span class="deck-label">Adnan Ali</span>
      </div>
      <span class="section-label">Second slide</span>
      <h2>Editorial grid slide.</h2>
      <div class="slide-grid">
        <div>
          <p>Main content column — three-quarter width.</p>
        </div>
        <div>
          <p style="font-size: var(--text-sm); color: var(--text-muted); font-style: italic;">Margin note here.</p>
        </div>
      </div>
      <div class="slide-footer">
        <span class="page-num">2</span>
        <span class="deck-label">Smoke Test</span>
      </div>
    </section>
  </div>
</div>
<script src="../lib/reveal.js"></script>
<script>
  Reveal.initialize({ hash: true, controls: true, progress: false, center: false, transition: 'none' });
</script>
</body>
</html>
```

- [ ] **Step 3: Serve and verify**

```bash
cd shared/templates && python3 -m http.server 8001
```

Open `http://localhost:8001/smoke-test.html` in a browser.

Verify:
- Slide 1: cream background (`#faf7f2`), amber section label, italic Georgia h1, left-aligned text, slide number and deck label in footer
- Slide 2: two-column grid layout, muted margin note
- Arrow keys navigate between slides
- No console errors

Kill the server with Ctrl+C when done.

- [ ] **Step 4: Delete smoke test and commit**

```bash
rm shared/templates/smoke-test.html
cd ../..  # back to project root
git add shared/templates/slide-template.html
git commit -m "feat: add Reveal.js slide template"
```

---

### Task 5: Create logo placeholder

**Files:**
- Create: `shared/branding/logo.svg`

- [ ] **Step 1: Write placeholder logo**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 32" width="120" height="32">
  <!-- Placeholder: replace with Adnan's actual mark -->
  <text x="0" y="24" font-family="Georgia, serif" font-size="20" font-style="italic" fill="currentColor">AA</text>
</svg>
```

- [ ] **Step 2: Commit**

```bash
git add shared/branding/logo.svg
git commit -m "feat: add logo placeholder (replace with actual mark)"
```

---

## Phase 2: Workstream Documents

### Task 6: Write WS-004 bootstrap workstream

**Files:**
- Create: `myPKA/Team Knowledge/Workstreams/WS-004-bootstrap-deck.md`

- [ ] **Step 1: Write WS-004-bootstrap-deck.md**

```markdown
# WS-004 — Bootstrap Deck (First Production)

- **Type:** Workstream — multi-agent composition. Produces a deck's v1.0.0 from scratch.
- **Owners:** Larry (orchestration), Pax (research), Rex (argument), Coda (production), Vera (adversarial), Aria (persuasion)
- **References:** [[docs/deck-folder-spec]], [[docs/engine-decisions]], [[docs/superpowers/specs/2026-05-25-engine-design]], [[GL-001-file-naming-conventions]], [[myPKA/Team Knowledge/Templates/decisions-template]]
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

### Step 5 — Deck Production (Coda)

Larry briefs Coda:

> "Produce `decks/<slug>/versions/v1.0.0/canonical.html` and audience variants `<audiences>` using the base template at `shared/templates/slide-template.html`. Apply `theme-<light|dark>.css`. Research brief: `decks/<slug>/research/YYYY-MM-DD-research-brief-v1.md`. Argument map: `decks/<slug>/reports/YYYY-MM-DD-argument-map-v1.md`. PoV: `decks/<slug>/pov.md`. Create `decks/<slug>/versions/v1.0.0/` folder if it does not exist. Audience variants share the same argument and evidence base — adapt narrative framing, language, examples, and CTA without altering evidence. After producing HTML, run the humanizer skill on all slide text and speaker notes before handing off."

Coda output: `versions/v1.0.0/canonical.html` + `versions/v1.0.0/<audience>.html` × N.

### Step 6 — Humanizer Pass (Coda)

Coda runs the humanizer skill on all text content (slide body, speaker notes) in every HTML file produced in Step 5. This step is complete when the humanizer skill reports no remaining AI-writing patterns.

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
```

- [ ] **Step 2: Verify required sections are present**

```bash
grep -c "## " myPKA/Team\ Knowledge/Workstreams/WS-004-bootstrap-deck.md
```

Expected: 6 or more (Purpose, Inputs, Outputs, Choreography, and sub-steps).

- [ ] **Step 3: Commit**

```bash
git add "myPKA/Team Knowledge/Workstreams/WS-004-bootstrap-deck.md"
git commit -m "feat: add WS-004 bootstrap deck workstream"
```

---

### Task 7: Write WS-005 improvement cycle workstream

**Files:**
- Create: `myPKA/Team Knowledge/Workstreams/WS-005-improvement-cycle.md`

- [ ] **Step 1: Write WS-005-improvement-cycle.md**

```markdown
# WS-005 — Improvement Cycle

- **Type:** Workstream — recurring multi-agent composition. Runs on every active deck whenever a trigger fires.
- **Owners:** Larry (orchestration), Pax (research sweep), Rex (argument re-audit), Vera (adversarial re-pass), Aria (persuasion re-score), Coda (deck update)
- **References:** [[docs/deck-folder-spec]], [[docs/superpowers/specs/2026-05-25-engine-design]], [[WS-004-bootstrap-deck]]
- **Trigger:** Weekly cron (default), Adnan manual request, or external process signal (future). Skips decks with `status: archived` or `status: overturned`.

---

## Purpose

Improve an existing deck version using new research, updated argument analysis, and re-scored outputs. Produces a new version (e.g. v1.0.0 → v1.1.0) only when improvement is warranted. Does not produce a PR if scores are flat and no PoV update is needed.

---

## Inputs

| Field | Description |
|---|---|
| `slug` | Deck folder name (e.g. `ai-and-kids`) |
| `current_version` | Read from `decks/<slug>/pov.md` |
| `trigger_type` | `scheduled` \| `manual` \| `external` |
| `engagement_level` | Read from `decks/<slug>/pov.md` — defaults to `autonomous` |

---

## Significance Threshold

Pax evaluates new research against three criteria. All three must be considered together:

1. **Source count** — at least one new independent credible source not present in the prior research brief
2. **Claim impact** — the new finding directly supports, challenges, or could overturn a specific claim in the current deck (not just tangentially related)
3. **Recency** — published or updated after the date of the prior research brief

**Below threshold:** one new source, weakly related to claims, or not more recent than existing sources. Log in `reports/` and stop — no cycle triggered.

**Above threshold:** two or more new independent sources with direct claim impact, or one highly credible source (e.g. peer-reviewed, major institution) with strong claim impact.

**Special rule — AI governance material:** Any finding that directly affects the engine's own governance principles (as documented in aa2brain) surfaces to Adnan for explicit go-ahead regardless of threshold level.

---

## Choreography

### Step 1 — Research Sweep (Pax)

Larry briefs Pax:

> "Research sweep for the `<topic>` deck (current version: `<current_version>`). Prior research brief: `decks/<slug>/research/YYYY-MM-DD-research-brief-vN.md`. Find: (1) new sources published or updated since that brief's date, (2) new developments relevant to the PoV in `decks/<slug>/pov.md`. Assess against the significance threshold in [[WS-005-improvement-cycle]]. Report your finding: threshold met or not, with evidence. If met, provide a new supplementary brief."

### Step 2 — Threshold Check (Larry)

| Condition | Action |
|---|---|
| Below threshold | Larry logs finding in `decks/<slug>/reports/YYYY-MM-DD-research-sweep-vN.md`. Cycle stops. |
| Above threshold + AI governance material | Larry surfaces to Adnan with Pax's finding. Wait for go-ahead before proceeding. |
| Above threshold, non-governance | Proceed autonomously to Step 3. |

### Step 3 — Re-audit (Rex, Vera, Aria — parallel)

Larry briefs all three in the same message, with links to Pax's new research and the current deck version.

**Rex brief:** "Re-audit the argument in `decks/<slug>/versions/<current_version>/canonical.html` against Pax's new research brief `decks/<slug>/research/YYYY-MM-DD-research-brief-vN.md`. Has the new evidence strengthened, weakened, or changed any claims? Updated argument score. File at `decks/<slug>/scorecards/<next_version>-argument.md`."

**Vera brief:** "Re-run adversarial pass on `decks/<slug>/versions/<current_version>/canonical.html` incorporating any new counter-evidence from Pax's research brief. Has the deck's resilience improved or weakened? Updated adversarial score. File at `decks/<slug>/scorecards/<next_version>-adversarial.md`."

**Aria brief (one per active audience):** "Re-score persuasion for `decks/<slug>/versions/<current_version>/<audience>.html` for a `<audience>` audience. Note any changes in emotional resonance, narrative clarity, or CTA strength relative to the prior persuasion scorecard. File at `decks/<slug>/scorecards/<next_version>-persuasion-<audience>.md`."

### Step 4 — Score Delta Check (Larry)

Larry compares all new scorecards against the prior version's scorecards.

| Condition | Action |
|---|---|
| All scores flat AND no PoV update warranted | Log in `reports/`. Cycle stops — no PR. |
| Any score changed OR PoV update warranted | Proceed to Step 5. |

### Step 5 — Deck Update (Coda)

Larry briefs Coda:

> "Update `decks/<slug>/versions/<current_version>/` to produce `decks/<slug>/versions/<next_version>/`. New research: `decks/<slug>/research/YYYY-MM-DD-research-brief-vN.md`. Score changes: [summary from Larry]. Update only what the new evidence warrants — do not rewrite slides that have not changed. Produce canonical.html and all active audience variants. After producing HTML, run the humanizer skill on all modified slide text and speaker notes."

### Step 6 — Humanizer Pass (Coda)

Coda runs the humanizer skill on all modified text content in the updated HTML files. This step is complete when no remaining AI-writing patterns are flagged.

### Step 7 — PR Compilation (Larry)

Larry compiles a GitHub PR following the PR format in [[docs/superpowers/specs/2026-05-25-engine-design]].

Score delta table compares `<current_version>` → `<next_version>` across all four dimensions.

### Step 8 — Review and Merge (Adnan)

Adnan reviews PR → merges → Larry updates `pov.md`:

```yaml
current_version: <next_version>
```

---

## Version Bumping Convention

| Change type | Bump |
|---|---|
| New evidence strengthens or refines existing claims | `v1.0.0 → v1.1.0` (minor) |
| PoV refined (still same core claim, tighter framing) | `v1.1.0 → v1.2.0` (minor) |
| PoV significantly changed (still same topic, different claim) | `v1.2.0 → v2.0.0` (major) |
| New audience variant added | `v1.0.0 → v1.1.0` (minor) |
```

- [ ] **Step 2: Verify required sections are present**

```bash
grep -c "## " myPKA/Team\ Knowledge/Workstreams/WS-005-improvement-cycle.md
```

Expected: 5 or more (Purpose, Inputs, Significance Threshold, Choreography, Version Bumping).

- [ ] **Step 3: Commit**

```bash
git add "myPKA/Team Knowledge/Workstreams/WS-005-improvement-cycle.md"
git commit -m "feat: add WS-005 improvement cycle workstream"
```

---

## Phase 3: First Deck Scaffold

### Task 8: Scaffold decks/ai-and-kids/ and write pov.md

**Files:**
- Create: `decks/ai-and-kids/pov.md`
- Create: `decks/ai-and-kids/decisions.md`
- Create: `decks/ai-and-kids/theme/ai-and-kids.css`
- Create: `decks/ai-and-kids/research/` (directory)
- Create: `decks/ai-and-kids/versions/` (directory)
- Create: `decks/ai-and-kids/scorecards/` (directory)
- Create: `decks/ai-and-kids/reports/` (directory)

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p decks/ai-and-kids/theme \
         decks/ai-and-kids/research \
         decks/ai-and-kids/versions \
         decks/ai-and-kids/scorecards \
         decks/ai-and-kids/reports
```

- [ ] **Step 2: Write pov.md**

```yaml
---
topic: AI and Kids
pov: "Both over-protective parenting (keeping kids and teens away from AI) and hands-off parenting (letting kids and teens interact with AI freely) are harmful; parents and teachers have specific mindsets and actions available today that chart the right course."
engagement_level: collaborative
current_version: v0.0.0
status: active
audiences:
  - parents
  - teachers
theme: light
---
```

- [ ] **Step 3: Write decisions.md (from template)**

Copy the decisions template and set the deck header:

```markdown
# Decisions Log — AI and Kids

Persistent memory for this deck across all improvement cycles. **Vera reads this before every adversarial pass. Pax reads this before every research sweep.** Specialists do not re-litigate a Closed decision without citing new evidence — if new evidence surfaces, flag it to Larry rather than silently opening the decision again.

Each entry is written by the specialist who owns the decision and is included in the PR for the cycle in which the decision was made. The PR is the review layer — Adnan reviews and approves both the content change and the decision log entry together.

---

<!-- Add new entries above this line, newest first -->
```

- [ ] **Step 4: Write theme/ai-and-kids.css (empty override file)**

```css
/* ai-and-kids.css — per-deck theme overrides
   Base: theme-light.css (cream + amber)
   Add deck-specific overrides below as needed.
   ================================================ */
```

- [ ] **Step 5: Verify structure**

```bash
find decks/ai-and-kids -type f | sort
```

Expected:
```
decks/ai-and-kids/decisions.md
decks/ai-and-kids/pov.md
decks/ai-and-kids/theme/ai-and-kids.css
```

Directories `research/`, `versions/`, `scorecards/`, `reports/` will be empty (no files yet — populated when WS-004 runs).

- [ ] **Step 6: Verify pov.md has all required fields**

```bash
grep -E "^(topic|pov|engagement_level|current_version|status|audiences|theme):" decks/ai-and-kids/pov.md
```

Expected: 7 lines, one per field.

- [ ] **Step 7: Smoke test — open deck template in browser**

To verify the full asset path chain works from a real deck location, copy the template into the deck and serve:

```bash
mkdir -p decks/ai-and-kids/versions/v0.0.0
cp shared/templates/slide-template.html decks/ai-and-kids/versions/v0.0.0/canonical.html
python3 -m http.server 8001
```

Open `http://localhost:8001/decks/ai-and-kids/versions/v0.0.0/canonical.html` in browser.

Verify:
- Cream background (light theme loading correctly)
- Amber accent colour on section labels
- Italic serif h1
- Slide navigation works
- No 404 errors in browser console for CSS or JS files

Kill server with Ctrl+C. Remove the test file:

```bash
rm decks/ai-and-kids/versions/v0.0.0/canonical.html
rmdir decks/ai-and-kids/versions/v0.0.0
```

- [ ] **Step 8: Commit**

```bash
git add decks/
git commit -m "feat: scaffold ai-and-kids deck — ready for WS-004"
```

---

### Task 9: Register WS-004 and WS-005 in Workstreams INDEX

**Files:**
- Modify: `myPKA/Team Knowledge/Workstreams/INDEX.md`

- [ ] **Step 1: Add WS-004 and WS-005 rows to the Active Workstreams table**

Find the line:
```
| WS-003 | [[WS-003-install-an-expansion]] | ...
```

Add immediately after it:

```markdown
| WS-004 | [[WS-004-bootstrap-deck]] | Larry + Pax + Rex + Coda + Vera + Aria | How a new deck topic goes from a draft PoV to a fully scored v1.0.0: PoV lock → research → argument map → collaborative checkpoint → Coda production → humanizer pass → scoring → PR. Runs once per topic. References [[docs/deck-folder-spec]], [[docs/superpowers/specs/2026-05-25-engine-design]]. |
| WS-005 | [[WS-005-improvement-cycle]] | Larry + Pax + Rex + Vera + Aria + Coda | How an existing deck is improved on a weekly cadence or on trigger: research sweep → threshold check → re-scoring → score delta check → Coda update → humanizer pass → PR. Skips decks with `status: archived` or `status: overturned`. References [[WS-004-bootstrap-deck]], [[docs/superpowers/specs/2026-05-25-engine-design]]. |
```

- [ ] **Step 2: Commit**

```bash
git add "myPKA/Team Knowledge/Workstreams/INDEX.md"
git commit -m "docs: register WS-004 and WS-005 in Workstreams INDEX"
```

---

## Done When

- [ ] `shared/` directory exists with `lib/`, `branding/`, `templates/` populated
- [ ] Reveal.js files in `shared/lib/` are non-empty
- [ ] `theme-dark.css` and `theme-light.css` use correct hex values from the design spec
- [ ] `slide-template.html` asset paths resolve correctly from `decks/<slug>/versions/v<N>/`
- [ ] WS-004 and WS-005 documents exist in `myPKA/Team Knowledge/Workstreams/`
- [ ] WS-004 references significance threshold → [[WS-005]]
- [ ] WS-005 defines significance threshold with three explicit criteria
- [ ] `decks/ai-and-kids/pov.md` has all seven required fields
- [ ] Team Knowledge INDEX updated with WS-004 and WS-005
