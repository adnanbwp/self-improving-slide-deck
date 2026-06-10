# Design System

> **Superseded for slide decks (2026-06-10).** All decks are now built on the aha agile
> templating system at `shared/templates/aha-agile/` (brand source of truth:
> `shared/aha-agile-brand/DESIGN.md`). The architecture below applies only when patching
> legacy pre-v2 deck versions (Reveal.js / per-deck theme CSS).

## CSS Architecture

Each deck owns its full theme. The deck's `theme/<slug>.css` file is the single CSS entry point:
- It imports `shared/branding/base.css` (type scale, layout primitives, font imports — never changes per deck)
- It declares the deck's own color tokens (`--bg`, `--accent`, etc.)
- It defines deck-specific components (stat callouts, warning lists, etc.)

HTML files link **only** `shared/lib/reset.css`, `shared/lib/reveal.css`, and `theme/<slug>.css`. They do **not** link `shared/branding/theme-light.css` or `theme-dark.css`.

`shared/branding/theme-light.css` and `theme-dark.css` remain as reference templates. Copy their token block into a new deck's theme file as a starting point, then customize.

**Consequence:** running impeccable on a deck means editing `decks/<slug>/theme/<slug>.css` only. The shared layer is never touched during a design pass.

## Colors

**Strategy**: Committed dark. The surface IS the authority — a well-lit room distracts; a commanding dark ground focuses. One jade accent carries provocation without noise.

**Dark theme (presentation default)**

| Token | Value | Usage |
|---|---|---|
| `--color-bg` | `oklch(12% 0.008 258)` | Slide background |
| `--color-surface` | `oklch(17% 0.008 258)` | Elevated surfaces, callout backgrounds |
| `--color-text-primary` | `oklch(93% 0.007 68)` | Body text, slide titles |
| `--color-text-muted` | `oklch(55% 0.009 258)` | Labels, footers, speaker notes preview |
| `--color-accent` | `oklch(62% 0.14 158)` | Accent rule, highlighted stats, section labels |
| `--color-accent-dim` | `oklch(38% 0.10 158)` | Subtle accent backgrounds |
| `--color-divider` | `oklch(25% 0.008 258)` | Rules, separators, header border |

**Light theme (optional, for printed handouts or bright rooms)**

| Token | Value | Usage |
|---|---|---|
| `--color-bg` | `oklch(98% 0.004 78)` | Slide background |
| `--color-surface` | `oklch(94% 0.006 78)` | Elevated surfaces |
| `--color-text-primary` | `oklch(15% 0.010 258)` | Body text, slide titles |
| `--color-text-muted` | `oklch(48% 0.008 258)` | Labels, footers |
| `--color-accent` | `oklch(40% 0.14 158)` | Accent rule, highlights |
| `--color-accent-dim` | `oklch(90% 0.06 158)` | Subtle accent backgrounds |
| `--color-divider` | `oklch(82% 0.005 78)` | Rules, separators |

**Do not**: use pure `#000` or `#fff`. Every neutral is tinted. Do not add a second accent color per deck — one accent across all slides, always.

## Typography

**Font families**

- **Display** (stats, big claims, slide titles): `Barlow Condensed` — SemiBold 600 for commanding single-slide stats; Regular 400 for claim titles. Has authority at 4rem+ without being a startup font.
- **Body** (body text, labels, speaker notes): `Barlow` — Regular 400 for body; Medium 500 for labels and section headers. Same family as display — unified, committed.

Google Fonts import:
```
https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;700&family=Barlow+Condensed:wght@400;600;700&display=swap
```

**Type scale** (slide-specific — 1920×1080 context)

| Variable | Value | Usage |
|---|---|---|
| `--text-xs` | `0.65rem` | Footer labels, page numbers |
| `--text-sm` | `0.85rem` | Section labels, deck label, speaker notes |
| `--text-base` | `1.1rem` | Body text, bullets |
| `--text-lg` | `1.5rem` | Sub-claims, supporting text |
| `--text-xl` | `2.2rem` | Secondary headings (h3) |
| `--text-2xl` | `3rem` | Slide claim titles (h2) |
| `--text-3xl` | `4rem` | Primary display (h1, big stats) |
| `--text-4xl` | `6rem` | Dominant stat or single-word impact slide |

**Rules**

- Claim titles (h2): Barlow Condensed SemiBold 600. No italic on body slides — italic is reserved for deliberate rhetorical emphasis only.
- Big stats: Barlow Condensed Bold 700 at `--text-3xl` or `--text-4xl`. The number IS the slide.
- Section labels: Barlow Medium 500, tracked wide (`0.14em`), uppercase, `--text-sm`.
- Body: Barlow Regular 400, `--text-base`, line-height 1.55.

**Do not**: use Georgia, Times, or any serif for slide content. The brand is not editorial-typographic. Serif italic as a design move is the first training-data reflex — reject it.

## Elevation

Slides are flat. No drop shadows, no blur, no glass effects. Depth comes from color lightness contrast (`--color-surface` vs `--color-bg`), not from CSS shadows.

Exception: `.stat-callout` and similar emphasis components may use a 1px border in `--color-accent-dim` and a `--color-surface` background. Never a box-shadow.

## Components

**Dominant stat block** (the most important component)
```css
.stat-callout {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: var(--text-3xl);
  font-weight: 700;
  color: var(--color-accent);
  line-height: 1;
  letter-spacing: -0.01em;
}
.stat-label {
  font-family: 'Barlow', sans-serif;
  font-size: var(--text-sm);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: var(--color-text-muted);
  margin-top: 0.5rem;
}
```

**Section label** (above claim titles)
```css
.section-label {
  font-family: 'Barlow', sans-serif;
  font-size: var(--text-xs);
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--color-accent);
  margin-bottom: 0.75rem;
}
```

**Accent rule** (visual separator between header and content)
```css
.slide-rule {
  width: 2rem;
  height: 2px;
  background: var(--color-accent);
  border: none;
  margin: 1.5rem 0;
}
```

## Do / Don't

**Do**
- Let a single big number own the slide. Resist adding context text around it.
- Use `--color-accent` sparingly — one use per slide is enough. Two is the maximum.
- Maintain generous left/right padding (3rem+). Slides are not pages.
- Use Barlow Condensed Bold at `--text-4xl` for maximum-impact single-word or single-stat slides.
- Keep the slide footer (`--text-xs`, `--color-text-muted`) invisible until the audience looks for it.

**Don't**
- No bullets that could instead be three separate slides.
- No decorative dividers, icon rows, or repeated ornamental elements.
- No color gradients anywhere. Flat colors only.
- No light serif italic as a design move. Not on titles, not on pull quotes.
- No background images behind text unless contrast is WCAG AA verified.
- No second accent color per deck. One jade, always.
