# Cobalt Grid

**Aesthetic register:** Structured / Data-authority
**Source:** `shared/design-library/_source/templates/cobalt-grid/`

## Visual character
Cobalt Grid is a two-color risograph editorial system built on a warm cream paper canvas (`#F0EBDE`) with a single electric cobalt ink (`#1F2BE0`). A permanent graph-paper grid at 10% cobalt opacity underlies every slide and cannot be suppressed — it is the canvas tone, not decoration. Every slide is framed by top and bottom 1.5px cobalt hairlines. Newsreader (a literary serif at weight 400 only) carries every headline and stat numeral; Hanken Grotesk (uppercase, tracked) carries every label; DM Mono carries all chrome. The signature decorative element is a stair-stepped vertical scanline column (pixel-glitch) anchored to the right edge of declarative slides, paired with a small 8×8 QR-style mosaic patch. The overall mood is a Japanese trend-report monograph: precise, measured, two-color, and quiet.

## Strengths
- The permanent graph-paper grid creates an immediately recognizable canvas tone that unifies every slide type without requiring per-slide effort.
- The three-font system (Newsreader serif / Hanken Grotesk sans / DM Mono) establishes a strict serif=statement, sans=body, mono=chrome hierarchy that reads as authoritative at every scale.
- The pixel-stack bar chart echoes the pixel-glitch decoration, making data visualization feel native rather than bolted on.
- The two-color constraint is a strength in presentation contexts: high contrast, print-friendly, and immune to off-brand color drift.
- Dense ledger and index layouts (2-column grid, 5-column table) handle information-heavy slides without visual noise.

## Weaknesses
- The strict two-color cream+cobalt identity has no native dark-mode register — adapting to a dark background requires replacing the entire surface logic.
- Newsreader at weight 400 relies entirely on size for hierarchy; at smaller display sizes the type can read as insufficiently authoritative compared to heavier serif designs.
- The pixel-glitch decoration is hand-authored SVG per usage — there is no generative component, making it time-consuming to customize stair-step patterns.

## Best-fit slide types
Evidence, Stat, Chart / Graph, Comparison, Table of Contents, Process / Steps

## Known adaptations
- **Question / Hook:** Break the grid entirely — centre the question with no column structure. Use whitespace as the dominant design element.
- **Statement:** Optionally break grid for maximum impact; column framing also works if the claim is data-adjacent.

## Dark theme notes
The source template is strictly a light (cream paper + cobalt ink) system with no dark mode. Adapting to the dark theme required the following changes:

- **Background replaced:** `#F0EBDE` cream paper → `var(--bg)` near-black (`oklch(12% 0.008 258)`).
- **Surface for stat area:** `var(--surface)` (`oklch(17% 0.008 258)`) used for the stat column background to maintain the column structure.
- **All cobalt ink replaced with design system tokens:** Cobalt (`#1F2BE0`) headlines, body, borders, and hairlines → `var(--text-primary)` (`oklch(93% 0.007 68)`) for text; `var(--accent)` (`oklch(62% 0.14 158)`) for the stat numeral and accent rules; `var(--divider)` (`oklch(25% 0.008 258)`) for structural borders and row dividers.
- **Graph-paper grid recolored:** The `::before` grid uses `rgba` of `--accent` at 5% opacity instead of cobalt at 10% — visible enough to signal "Cobalt Grid" while not competing with light text on dark background.
- **Pixel-glitch column recolored:** SVG scanlines changed from cobalt `#1F2BE0` to `var(--accent)` jade green to maintain the decorative column in the dark register.
- **Fonts swapped to design system standard:** Newsreader/Hanken Grotesk/DM Mono → Barlow Condensed (display/stats) and Barlow (body/labels), maintaining the heavy display vs. body weight contrast with the available font stack.
- **Hairlines dimmed:** 1.5px cobalt hairlines → 1px `var(--divider)` lines to avoid overpowering the dark background.
