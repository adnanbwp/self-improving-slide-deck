# Signal

**Aesthetic register:** Editorial / Magazine-authority
**Source:** `shared/design-library/_source/templates/signal/`

## Visual character
Signal is a literary editorial system modeled on long-form intelligence briefings and quarterly magazine reviews. It runs a dual-surface model: deep navy (`#1C2644`) and warm aged cream (`#F0ECE3`), with a single antique-gold accent (`#C8A870`) that appears only on rules, italic-emphasis inside headlines, and statistical numerals. Source Serif 4 carries every headline — the system's signature move is mixing roman and italic mid-sentence, with the italic phrase rendered in gold. DM Sans steps back for body text; IBM Plex Mono carries every timestamp, kicker, chrome label, and stat note. A near-invisible 80px grid texture overlays every dark slide at 3% white opacity as a visual fingerprint. The mood is sober, restrained, and aristocratic — a deck that does not need to shout.

## Strengths
- The roman/italic gold mid-sentence emphasis in Source Serif 4 headlines is a high-distinctiveness typographic move that readers recognize across multiple slides as a consistent editorial voice.
- The dual-surface (navy / cream) model allows adjacent slides to alternate tone without explanation, providing visual rhythm in long decks.
- The editorial and dense layout patterns handle complex mixed-content slides (date logs + stat grids, two-column analysis) with genuine magazine-like composure.
- Hairline-only depth (no shadows, no elevation) keeps the system legible across any display brightness without calibration issues.

## Weaknesses
- The italic-gold-serif signature treatment is lost entirely on dark backgrounds where the gold accent must be replaced by the design system's jade green — the roman/italic mid-sentence moment still works, but the distinctive warm-gold warmth is gone.
- Source Serif 4 + DM Sans + IBM Plex Mono is a three-family stack requiring careful font loading; if any family fails, the editorial voice collapses to Georgia/system-ui fallbacks.

## Best-fit slide types
Statement, Quote, About Me, About / Vision, Split (text + image), Section Divider

## Known adaptations
- **Chart / Graph:** Editorial layout needs explicit chart container added; source has no native data visualisation pattern. Use a CSS-only bar chart within the editorial frame.
- **Stat:** Scale the number to fill the editorial column — resist adding decorative rules around it.

## Dark theme notes
The source template is already dark-native (navy background) on most slides, so the dark theme adaptation was the more natural direction.

- **Background:** The source navy (`#1C2644`) is close to the design system `--bg`; replaced with `var(--bg)` for consistency.
- **Gold accent replaced:** `#C8A870` antique gold → `var(--accent)` jade green (`oklch(62% 0.14 158)`). The italic-serif emphasis and kicker roles are preserved, but the warm antique warmth shifts to a cooler jade register.
- **Text warm-white preserved:** Source `#E2DCD0` warm off-white maps directly to `var(--text-primary)` (`oklch(93% 0.007 68)`).
- **Muted text:** Source `#8A96A8` muted blue-grey → `var(--text-muted)`.
- **Borders:** Source `#2E3D5C` navy border → `var(--divider)`.
- **Surface for elevated panels:** Source `#232F55` navy-alt → `var(--surface)`.
- **Fonts swapped to design system standard:** Source Serif 4 / DM Sans / IBM Plex Mono → Barlow Condensed (display) and Barlow (body/labels), preserving the weight hierarchy (heavy display, lighter body) within the available font stack. The italic-gold `<em>` treatment is retained using Barlow italic in `var(--accent)`.
- **Grid texture retained:** The 80px near-invisible grid overlay is kept on the dark slide, recolored to use `var(--accent)` at ~3% opacity.
- **Statement slide:** Chrome bars suppressed — statement layout uses no top/bottom chrome, letting the headline breathe edge-to-edge with only the kicker + short rule above it.
