# Cartesian

**Aesthetic register:** Classical analytical / Architectural editorial
**Source:** `shared/design-library/_source/templates/cartesian/`

## Visual character
Cartesian is a warm-stone editorial system built on a sandy linen background (`#ede8e0`) with warm taupe accent (`#8a8178`) and muted sand dividers (`#b8b0a4`). Playfair Display (serif, weight 400/600/700) carries all headlines and numerals; Inter (sans, weight 300–600) carries all body, labels, and data captions. The signature decoration is a large geometric circle — drawn in the muted sand line colour at 40–50% opacity — floating in the upper-right corner of every slide as a background element. The overall mood is an architectural studio or finance-adjacent consultant report: precise, warm, classically beautiful but never ornate.

## Strengths
- The large background circle is a strong visual anchor that creates depth without competing with content — it reads as structural, not decorative.
- The Playfair Display / Inter pairing is one of the most reliable editorial font pairs available: the serif headline system carries authority; Inter body recedes cleanly.
- The warm taupe accent is naturally versatile — it reads as subtle emphasis on data labels and as a strong identity mark on category numbers, without ever feeling loud.
- Bar charts and agenda lists use Playfair numerals as anchors, making data sequences feel as deliberate as chapter headings.

## Weaknesses
- The sandy linen palette sits in a neutral zone that can read as "generic premium" if the content itself is not distinctive — the template does not project strong personality.
- Geometric circle decorations are fixed-position overlays; on dense data slides the circle competes with chart elements in the upper-right quadrant.
- Playfair Display at weight 400 requires generous size to read well — at sub-24px the classic letterforms become congested on projection.

## Best-fit slide types
Chart / Graph, Timeline, Comparison, Process / Steps, Table of Contents, Evidence

## Known adaptations
- **Chart/Graph:** Use Playfair numerals for axis values and bar labels; Inter for axis titles. The geo-circle should be suppressed or moved off-slide on chart slides to avoid overlap.
- **Comparison:** Two-column layout with a thin sand-coloured vertical divider. Playfair for category names; Inter for comparative text.
- **Timeline:** Horizontal timeline with Playfair Display for year markers; Inter for event descriptions. Muted taupe dots as timeline nodes.
- **Process/Steps:** Number each step in Playfair Display at large size in the warm taupe accent colour; body in Inter at normal weight.

## Dark theme notes
The source template is a strict light (warm linen + taupe) system with no dark mode. Adapting to the dark theme required:

- **Background replaced:** `#ede8e0` warm linen → `var(--bg)` near-black (`oklch(12% 0.008 258)`).
- **Secondary background:** `#e2dbd1` → `var(--surface)` (`oklch(17% 0.008 258)`).
- **Primary text:** `#1a1a1a` → `var(--text-primary)` (`oklch(93% 0.007 68)`).
- **Secondary text:** `#5a5a5a` → `var(--text-muted)` (`oklch(55% 0.009 258)`).
- **Accent (taupe) → jade:** `#8a8178` warm taupe → `var(--accent)` (`oklch(62% 0.14 158)`). This is a register shift: the warm analytical taupe becomes jade on the dark theme. The structural role is preserved (category numbers, bar labels, navigation), but the warmth is lost.
- **Divider lines:** `#b8b0a4` sand → `var(--divider)` (`oklch(25% 0.008 258)`) for agenda separators and chart baselines.
- **Geo-circle decoration:** Opacity reduced from 0.4–0.5 to 0.08 against dark background; stroke colour mapped to `var(--divider)` so it reads as a subtle ghost rather than a dominant shape.
