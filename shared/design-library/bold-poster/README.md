# Bold Poster

**Aesthetic register:** Brutalist editorial / High-impact print poster
**Source:** `shared/design-library/_source/templates/bold-poster/`

## Visual character
Bold Poster is a white-canvas, fire-engine-red-accent system built around three typefaces with radically different voices: Shrikhand (display, decorative weight only) for all large numerals and headline statements; Libre Baskerville (serif, weight 400/700) for body and citation text; Space Grotesk (sans, weight 400–700) for chrome labels and all-caps section tags. The signature motif is the Shrikhand numeral at extreme scale — the primary stat on a stat slide reaches 200–320px and is intentionally rotated between -6° and +2° as if printed by an imprecise letterpress. A 5px red bottom progress bar chrome runs across the base of every slide. The overall mood is a 1970s poster — confrontational, physical, and unignorable.

## Strengths
- Shrikhand at extreme scale creates immediate visual dominance that no other template in the library can match — the stat IS the slide.
- The white + red two-colour constraint maps cleanly to high-contrast environments (large auditoriums, direct sun projection) where colour fidelity degrades.
- The three-font system (Shrikhand display / Libre Baskerville serif / Space Grotesk sans) creates a strong three-tier hierarchy: shouted → authoritative → indexed.
- The deliberate rotation of display numerals is a structural choice, not decoration — it prevents the extreme type scale from reading as an error.

## Weaknesses
- Shrikhand is a single-weight decorative typeface with no body weight — all body text must use Libre Baskerville or Space Grotesk, making mixed-content slides more complex to lay out.
- The template has no native dark mode. The white canvas is structural — on a dark background Shrikhand loses its typographic gravity and becomes disconnected.
- The extreme type scale means a stat slide can hold only one number at display size — multi-stat slides require a smaller grid system that competes with the poster aesthetic.
- The rotation motif is difficult to control at other scales: rotating body-text paragraphs would be unreadable; only display elements can carry the effect.

## Best-fit slide types
Stat, Statement, Title

## Known adaptations
- **Stat:** Place the Shrikhand numeral at 200px+ rotated -6°. Below the numeral: Space Grotesk uppercase label for the descriptor. Libre Baskerville for the context sentence.
- **Statement:** Full-width Shrikhand headline at 64–90px, no rotation. Libre Baskerville citation or sub-statement below.
- **Title:** Hero pattern: three stacked lines of Shrikhand — first two lines in near-black, middle line in red, optional third line near-black with slight positive rotation. Space Grotesk tagline anchored bottom-right.

## Dark theme notes
The source template is a strict light (white canvas + red accent) system. Adapting to the dark theme required:

- **Background replaced:** `#FFFFFF` white → `var(--bg)` near-black (`oklch(12% 0.008 258)`).
- **Light surface:** `#F5F2EF` off-white → `var(--surface)` (`oklch(17% 0.008 258)`).
- **Primary text:** `#1C1410` near-black → `var(--text-primary)` (`oklch(93% 0.007 68)`).
- **Red accent replaced with jade:** `#D8000F` fire-engine red → `var(--accent)` (`oklch(62% 0.14 158)`). This is a significant identity shift — the confrontational red-on-white drama is replaced by jade-on-near-black, which is quieter and more editorial. The rotated numeral retains its structural role but loses its poster aggression.
- **Progress bar (nav chrome):** Red bottom bar → `var(--accent)` jade. The structural bar remains but the colour personality changes.
- **Borders on financial/grid slides:** `2px solid #1C1410` near-black → `var(--divider)` to prevent harsh contrast.
- **Identity concern:** Bold Poster's visual identity is fundamentally bound to white + red — the dark theme adaptation is a meaningful register change, not a simple colour swap.
