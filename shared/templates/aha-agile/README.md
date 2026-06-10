# Aha Agile deck templating system

The production templating system for building — and converting existing decks to — the
**aha agile** brand: a duotone editorial / Swiss-brutalist system (Archivo 900 + Space Mono,
orange/paper/ink fields, paper grain, redaction motifs).

**Brand source of truth:** `shared/aha-agile-brand/` (DESIGN.md, tokens.css, brand guide,
design system, and `aha-agile-deck-template.html` — the 21-layout guideline implementation
this system is derived from).

## Files

| File | Role | Edit per deck? |
|---|---|---|
| `tokens.css` | Brand colour / type / spacing tokens at deck scale. Rebrand every deck by editing this one file. | No |
| `engine.css` | Fixed 1280×720 stage, scaling, grid overview, auto-fading controls. | **Never** |
| `engine.js` | Keyboard nav, hash deep-links (`#7`), grid (G), fullscreen (F). | **Never** |
| `layouts.css` | All slide-type layouts: 21 canonical + 5 production extensions. | No — extend here if a genuinely new type emerges |
| `deck-skeleton.html` | Copy-to-start scaffold for a new deck. | Copy it, then edit the copy |

## Starting a new deck

1. `cp shared/templates/aha-agile/deck-skeleton.html decks/<slug>/versions/v1.0.0/canonical.html`
2. Replace placeholder slides using the catalogue below. One `<section class="slide">` per slide;
   inside it exactly one `<div class="slide-inner f-<field> t-<type>">`.
3. Keep the chrome on every slide: `.tag` (kicker, all-caps), `.pageno`, `.slug` (deck or brand slug).
4. The first slide carries `class="slide active"`.

## The three fields

Every slide sits on exactly one field. Allocation logic ("Field Locking", per DESIGN.md):

- **`f-orange`** — shouts. Title, statements, questions, CTA, vision. Use for the deck's
  highest-stakes beats; if everything shouts, nothing does.
- **`f-paper`** — reads. All content workhorses: content, lists, stat grids, comparisons,
  sources, team.
- **`f-ink`** — breaks. Section dividers, the end slide, occasional quote. Use as
  structural punctuation between acts.

## Slide-type catalogue

Poster types (absolute layout — content is one short statement):

| Class | Type | Key elements | Budget |
|---|---|---|---|
| `t-title` | Title | `.topiclabel`, `h1.display` (add `.brandmark` for the 170px wordmark), `.badge`, `.meta` kv pairs, `.bleed-num` | h1 ≤3 short lines |
| `t-statement` | Statement | `.claim.display` (add `.short` for ≤6 words), optional `.support` line | ≤14 words |
| `t-stat` | Single stat | `.big.display`, `.lab` | number ≤4 chars |
| `t-evidence` | Stat + context | `.col` > optional `.head`, `.big.display`, `.ctx`, `.src` | ctx ≤2 lines |
| `t-quote` | Quote | `.q` (italic mono), `.by` | ≤30 words |
| `t-question` | Question / hook | `.q.display`, optional `.annot` | ≤12 words |
| `t-cta` | Call to action | `.imperative.display`, optional `.support`, `a.btn` | ≤8 words |
| `t-divider` | Section divider | `.partno`, `.accent-rule`, `h2.display`, `.bleed-num` (on `f-ink`) | title ≤4 words |
| `t-image-claim` | Full-bleed image + claim | `.imgblock` (+`<img>`), `.claim` | claim ≤10 words |
| `t-vision` | About / vision | `.eyebrow`, `.vision.display`, `.narr` | vision ≤20 words |
| `t-end` | Closing | `.closing.display`, `.contact`, `.badge` (on `f-ink`) | ≤5 words |

Workhorse types (flow layout inside `.pad` — respect the budgets or content overflows the 720px stage):

| Class | Type | Key elements | Budget |
|---|---|---|---|
| `t-content` | Kicker + headline + body | `.pad` > `h2.head.display`, `.body` (+optional `.cols` > body + `.aside`), `.src` | head ≤2 lines @46px; body ≤5 short blocks |
| `t-stat-grid` | Headline + stat cards | `.pad` > `.head`, optional `.lead`, `.grid.cols-2/3/4` > `.card` (`.num` + `.cap` + optional `.note`), `.src` | 2–4 cards; `.num.long` for >4 chars |
| `t-cards` | Headline + text cards | `.pad` > `.head`, optional `.lead`, `.grid.cols-1/2/3` (+`.dense`) > `.card` (`.k` + `.t` + `.d` + optional `.note`), `.src` | 3–4 cards; ≤7 with `.dense`; `.hot` highlights one |
| `t-figure` | Headline + framed diagram | `.pad` > `.head`, `.fig` > `<img>` (object-fit contain on bone panel) | one diagram; head ≤2 lines @38px |
| `t-list` | Numbered list | `.pad` > `.head.display`, optional `.lead`, `ul` > `li` (`.n` + text, optional `.sub`), optional `.foot` | ≤6 items; ≤4 if using `.sub`; `.labels` widens `.n` for word markers |
| `t-compare` | Split on the seam | two `.half` (each its own field class) > `.lab`, `.val.display` or `.mini-list`, `.desc`, optional `.note`; optional `.seam-head` (add `.has-head` to inner) and `.annot-line` (add `.has-annot`) | ≤6 mini-list items per half (≤4 with head) |
| `t-sources` | Citations | `.pad` > `.head.display`, `ol` > `li` (`.n` + text) | ≤12 entries |
| `t-team-avatars` | Closing credits w/ photos | `.pad` > `.head.display`, `.rows` > `.row` > `.person` (`.av` + img + initials, `.nm`, `.ro`) | rows per `shared/slide-types/team.md` stagger table |
| `t-process` | Steps | `.head.display`, `.steps` > `.step` (`.num`, `.lab`, optional `.sub`) + `.arrow` | 3–5 steps |
| `t-chart` | CSS bar chart | `.head`, `.chart` > `.colb` (`.v`, `.b` w/ inline height %, `.x`) | 3–6 bars |
| `t-timeline` | Timeline | `.head`, `.line`, `.ev` w/ inline `left:%` | 3–5 events |
| `t-toc` | Table of contents | `.head`, `ol` (2 columns) | ≤8 entries |
| `t-split` | Text + half image | `.text` (field class) > `h3`, `p`; `.imgblock` | p ≤4 sentences |
| `t-team` | Team (badge icons) | use `t-team-avatars` when avatar PNGs exist | 3–4 people |
| `t-services` | Offerings grid | `.head`, `.grid` > `.svc` (svg, `.nm`, `.ds`) | 4 cells |
| `t-gallery` | Image grid | `.head`, `.grid` > `.imgblock` | 6 cells |
| `t-about-me` | Presenter bio | `.photo` (imgblock), `.info` (`.nm`, `.ti`, `.bio`, `.tags`) | bio ≤3 sentences |

### Team avatars

Avatar PNGs live at `shared/assets/avatars/<slug>.png` (path from a deck:
`../../../../shared/assets/avatars/<slug>.png`). Markup keeps the initials fallback:

```html
<div class="av presenter"><img src="../../../../shared/assets/avatars/adnan.png" alt="Adnan" onerror="this.style.display='none'">AA</div>
```

`.presenter` (orange ring) goes on Adnan only. Row split by member count follows
`shared/slide-types/team.md`.

## Conversion playbook (existing → aha agile)

Converting a deck is a re-skin, not a rewrite: keep the argument, slide order, and speaker
content; replace each slide's markup with the matching `t-*` layout. Rebrands are a major
version bump (e.g. v1.5.1 → v2.0.0).

1. Copy `deck-skeleton.html` to the new version directory.
2. Walk the old deck slide by slide; map each to a `t-*` type with the tables below.
3. Move the old kicker / section label into `.tag`; renumber `.pageno`. Carry speaker notes
   over verbatim as `<aside class="notes">` inside each `.slide` — the engine hides them but
   they travel with the deck.
4. Apply field allocation: the old deck's "dark = emphasis" slides become `f-orange`
   (shout) or `f-ink` (structural break); content slides become `f-paper`.
5. Enforce the budgets. If old content exceeds a budget, tighten the copy or split the
   slide — never shrink fonts or unlock the layout.
6. Copy real images into the version's `assets/` and drop them in `.imgblock`s.
7. Verify with screenshots (below) before shipping.

### Mapping — hybrid-delivery-style decks (custom engine, `slide--*` classes)

| Old `slide--*` | New `t-*` |
|---|---|
| `cover` | `t-title` |
| `statement` | `t-statement` (f-orange) |
| `question` | `t-question` (f-orange) |
| `divider` | `t-divider` (f-ink) |
| `list` | `t-list` (≤6 items) or `t-content` (prose) |
| `stats` | `t-stat-grid`; a single hero number → `t-stat` / `t-evidence` |
| `compare` | `t-compare` (orange/paper halves) |
| `image` (photo) | `t-image-claim` (full bleed) or `t-split` (half) |
| `image` (diagram) | `t-figure` (framed bone panel keeps diagrams legible) |
| `list` w/ marker+title+body cells | `t-cards` (3–4) or `t-cards` + `.dense` (5–7) |
| `process` | `t-process` |
| `team` | `t-team-avatars` |
| `end` | `t-end` (f-ink) |

### Mapping — Signal/Reveal decks (ai-and-kids style, `<section>` + kicker)

| Old pattern | New `t-*` |
|---|---|
| Title slide (`h1.title-main`) | `t-title` |
| `section.dark` + lone `h2` (statement beat) | `t-statement` (f-orange) |
| About the presenter | `t-about-me` |
| Kicker + `h2` + prose body | `t-content` (f-paper) |
| Kicker + `h2` + stat cards | `t-stat-grid` (f-paper) |
| Three-schools / before-after | `t-compare` |
| Warning signs / action lists | `t-list` |
| Sources | `t-sources` |
| Team slide | `t-team-avatars` |
| Italic-gold `<em>` inside headlines | drop the colour move — emphasis via line-break or `.bar` redaction; the system's voice is the field, not inline colour |

## Verification

Serve the repo root and screenshot any slide by hash (engine supports `#<n>`, 1-based):

```bash
python3 -m http.server 8080 --directory . &
node scripts/screenshot-slide.js "http://<wsl-ip>:8080/decks/<slug>/versions/v<N>/canonical.html#5" screenshots/<slug>/slide-05.png
```

Controls are hidden until the mouse moves, so headless captures are clean. Check every
workhorse slide for overflow (content must clear the `.pageno` row).

## Portable / emailable builds

Same recipe as previous decks: inline the four CSS files + engine.js into the HTML, embed
the two Google font families, downscale avatars (see memory: portable single-file deck,
`decks/hybrid-delivery/hybrid-delivery-v1.5.1-portable.html` as reference).
