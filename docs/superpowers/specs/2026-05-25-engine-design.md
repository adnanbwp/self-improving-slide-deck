# Engine Design Spec
*2026-05-25 — approved in design session*

---

## Scope

This spec covers the full engine design: two workstreams (bootstrap + improvement cycle), the Reveal.js base template design system, shared/ asset structure, PR format, and the first deck topic.

---

## First Deck

**Topic:** AI and Kids

**PoV:** Both over-protective parenting (keeping kids/teens away from AI) and hands-off parenting (letting kids/teens interact with AI freely) are harmful. There is a specific set of mindsets and actions parents and teachers can take today.

**Audiences for v1.0.0:** parents, teachers
**Deferred audience:** teenagers (later cycle)

**Engagement level:** collaborative (default for all bootstrap runs)
**Improvement cycle engagement level:** autonomous (default for all cycles)

**Source note:** existing research in aa2brain relevant to this topic; Pax to mine before bootstrapping.

---

## Workstream Architecture

Two separate workstreams. The improvement cycle always assumes a prior version exists — bootstrap handles first production exclusively.

### WS-004 — Bootstrap (first production)

Triggered once per deck topic.

1. Larry + Adnan lock the PoV → write `pov.md` (`engagement_level: collaborative`, `status: active`, `current_version: v0.0.0`)
2. Pax: deep research → `decks/<slug>/research/YYYY-MM-DD-research-brief-v1.md`
3. Rex: build argument map from Pax's research → argument score
4. **Collaborative checkpoint** — Larry surfaces to Adnan:
   - Pax research brief
   - Rex argument map + argument score
   - If score sufficient (Rex finds no critical gaps and argument supports PoV) → proceed to Coda
   - If score low (Rex flags critical gaps or weak evidence base) → Adnan chooses:
     - (a) Loop back to Pax for tighter research; Rex re-audits
     - (b) PoV falsified → refine PoV and restart, or overturn and archive
5. Coda: produce `versions/v1.0.0/canonical.html` + audience variants (`parents.html`, `teachers.html`)
6. **Humanizer pass** — Coda runs humanizer skill on all slide text and speaker notes before scoring
7. Rex: logic audit → `scorecards/v1.0.0-argument.md`
8. Vera: adversarial pass → `scorecards/v1.0.0-adversarial.md`
9. Aria: persuasion score × 2 audiences → `scorecards/v1.0.0-persuasion-parents.md`, `scorecards/v1.0.0-persuasion-teachers.md`
10. Larry: compile PR (see PR Format section)
11. Adnan: review → merge → tag `v1.0.0` → update `pov.md` `current_version`

### WS-005 — Improvement Cycle

Recurring. Default engagement: autonomous.

**Triggers (any one is sufficient):**
- Weekly cron (default cadence)
- Adnan manual request
- External process signal (future — not yet wired; reserved for automation layer)

**Steps:**

1. Pax: research sweep — new sources, developments since last cycle date
2. **Threshold check:**
   - Below significance threshold → log finding in `reports/`, no cycle triggered
   - Above threshold + AI governance material → surface to Adnan for go-ahead before proceeding
   - Above threshold, non-governance → proceed autonomously
3. Rex: re-audit argument with new research → updated argument score
4. Vera: re-run adversarial pass → updated adversarial score
5. Aria: re-score persuasion for each active audience variant
6. **Score delta check:**
   - Scores flat AND no PoV update warranted → log in `reports/`, no PR
   - Any score changed or PoV update warranted → proceed to Coda
7. Coda: update deck where warranted (new evidence, tighter argument, stronger CTA)
8. **Humanizer pass** — Coda runs humanizer skill on all modified slide text and speaker notes
9. Larry: compile PR (see PR Format section)
10. Adnan: review → merge → version bump → update `pov.md` `current_version`

**Significance threshold (to be defined in WS-005 body):** Pax evaluates new research against: (a) number of independent credible sources, (b) whether findings directly support, challenge, or overturn a claim in the current deck, (c) recency relative to the deck's existing sources.

---

## Reveal.js Base Template — Design System

Two theme variants, same design language. Warm palette, amber accent throughout.

### Theme: Dark (default base)

| Element | Value |
|---|---|
| Background | `#1a1614` (warm charcoal — not pure black, not navy) |
| Body text | `#f5ede3` (warm off-white) |
| Accent | `#c97d2a` (amber) |
| Muted text | `#6b5a47` |
| Display type | Georgia or equivalent serif |
| Body/UI type | System sans (Segoe UI / -apple-system stack) |
| Dividers | `1px solid #c97d2a` |

### Theme: Light (per-deck override, default for AI & Kids)

| Element | Value |
|---|---|
| Background | `#faf7f2` (cream/off-white) |
| Body text | `#1c1917` (rich near-black) |
| Accent | `#b45309` (amber) |
| Muted text | `#78716c` |
| Display type | Georgia or equivalent serif |
| Body/UI type | System sans |

### Anti-AI-slop rules for Coda (template implementation)

- No pure black (`#000`) or pure navy (`#0a0a2e` etc.) backgrounds
- No electric blue or purple accent colours
- No gradient text effects
- No perfectly centred floating-card layouts on every slide
- Slides must use intentional asymmetry or a strong editorial grid — not "centred everything"
- Slide count indicator and deck label in header/footer on every slide

---

## shared/ Asset Structure

```
shared/
  branding/
    base.css          — CSS variables, typography scale, spacing system
    theme-dark.css    — A1: warm charcoal + amber
    theme-light.css   — C: cream + amber
    logo.svg          — Adnan's mark, used in slide header
  lib/
    reveal.js         — single copy, referenced by all decks via relative path
    reveal.css
    reset.css
  templates/
    slide-template.html   — Reveal.js base HTML with correct asset paths pre-wired
```

Per-deck `theme/` folders reference `../../../shared/branding/` and override only deck-specific values. The AI & Kids deck defaults to `theme-light.css`.

HTML files reference assets via relative paths:
- `../../../shared/lib/reveal.js`
- `../../../shared/branding/base.css`
- `../../../shared/branding/theme-light.css` (or `theme-dark.css`)
- `../../theme/<deck-slug>.css`

---

## PR Format

Every improvement cycle and bootstrap PR follows this structure:

```
## Larry's Synthesis
[One paragraph: what changed, why, which specialist findings drove it]

## Score Delta
| Dimension   | Prior (vN) | This (vN+1) | Delta |
|-------------|-----------|-------------|-------|
| Research    | —         | —           | —     |
| Argument    | —         | —           | —     |
| Adversarial | —         | —           | —     |
| Persuasion (parents)   | — | —      | —     |
| Persuasion (teachers)  | — | —      | —     |

## Decisions
[Links to decisions.md entries added this cycle]

## Specialist Reports
- [Rex — Logic Audit vN](link)
- [Vera — Adversarial vN](link)
- [Aria — Persuasion Parents vN](link)
- [Aria — Persuasion Teachers vN](link)
- [Pax — Research Brief vN](link)

## Files Changed
[Standard git diff]
```

**Bootstrap PRs:** same format, but score delta table shows baseline scores only (no prior version to diff against), and includes a PoV confirmation line above the synthesis.

---

## Humanizer Requirement

The humanizer skill is a mandatory step in both workstreams, applied to all deck text (slide content, speaker notes) before scoring and before the PR is compiled. Coda owns this step. It applies on first production and on every cycle where slides are updated.

---

## Decisions Captured

- **Separate bootstrap + improvement cycle workstreams** — clean separation; improvement cycle always assumes a prior version exists.
- **Collaborative default for bootstrap, autonomous default for improvement cycles** — first deck gets Adnan's input before Coda commits to a direction; cycles run without interruption by default.
- **Rex argument score as collaborative checkpoint gate** — low score sends the deck back to Pax or triggers PoV falsification, not straight to Coda.
- **Significance threshold gates Pax's research trigger** — prevents noisy cycles on minor new sources.
- **AI governance research surfaces to Adnan regardless of threshold** — governance material requires human go-ahead.
- **Score delta check before Coda** — flat scores with no PoV change = no PR, no noise.
- **Dark theme: A1 (editorial dark, warm charcoal + amber)** — avoids AI-generated dark theme tells; warm palette not cold/tech.
- **Light theme: C (cream + amber)** — same design language as dark, coherent pair.
- **AI & Kids deck defaults to light theme** — appropriate for parenting/education audience.
- **Humanizer as mandatory pipeline step** — removes AI writing patterns from all deck text before it ships.
- **Anti-AI-slop design rules encoded in template spec** — Coda has explicit constraints to prevent generated-looking slides.
