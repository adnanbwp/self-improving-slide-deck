# Monochrome

**Aesthetic register:** Archival / Research-grade editorial
**Source:** `shared/design-library/_source/templates/monochrome/`

## Visual character
Monochrome (sourced as "Ivory Ledger") is a black-ink-on-cream-paper system: every slide uses a warm cream canvas (`#fafadf`) with near-black ink (`#1a1a16`) and absolutely no accent colour — even the accent token collapses to black. The font stack is Jost (geometric sans, weights 200–600) for all display and body text, JetBrains Mono for chrome labels and sidebar metadata, and Lora italic serif for insight card titles and pull quotes. The signature structural element is a thin vertical hairline rule running down the left gutter with rotated mono labels reading bottom-to-top — a sidebar annotation column that gives every slide a research-notebook feeling. The overall mood is a high-end academic monograph: generous whitespace, ultra-light weight type, and a strict two-value (black + cream) palette.

## Strengths
- The ultra-light Jost weight (200–300) at large scale creates maximum airiness without sacrificing legibility — the page breathes even on dense data slides.
- The sidebar annotation column (thin left-gutter rule + rotated mono labels) is a distinctive identity mark that works across every slide type without competing with content.
- The strict monochrome constraint makes this the most context-neutral template in the library — slides read as credible and unbiased regardless of content domain.
- The Jost + Lora contrast (geometric sans vs. literary serif) provides a built-in pull-quote register that feels scholarly rather than decorative.

## Weaknesses
- The cream+black palette has no native dark-mode register — adapting to a dark background requires replacing the entire surface logic and abandons the "cream paper" identity.
- Ultra-light type weights (Jost 200) can render poorly on lower-quality projection hardware where sub-pixel rendering is unavailable.
- No accent colour means emphasis must be carried entirely by size and weight — large slides with multiple levels of hierarchy require careful weight orchestration.

## Best-fit slide types
Evidence, Quote, About/Vision, Timeline, Process/Steps, Table of Contents, Statement, Title

## Known adaptations
- **Evidence:** Place the dominant stat in Jost 200 at ~160px left, with a Lora italic serif pull statement right. Use the sidebar rule to label the data source.
- **Quote:** Centre the Lora italic display text on the cream field with no container — let the type float. Place the attribution in JetBrains Mono at the bottom-left annotation position.
- **Comparison:** Use a thin vertical rule to split the slide into two columns. Both sides use Jost body; differentiated by weight (200 vs. 500) not by colour.
- **Process/Steps:** Number each step in JetBrains Mono (left gutter); use the sidebar rule as the process spine.

## Dark theme notes
The source template is a strict light (cream + black ink) system with no dark mode. Adapting to the dark theme required:

- **Background replaced:** `#fafadf` cream → `var(--bg)` near-black (`oklch(12% 0.008 258)`).
- **Surface for inset areas:** `var(--surface)` (`oklch(17% 0.008 258)`) used for card and sidebar backgrounds.
- **Black ink text → light primary:** `#1a1a16` → `var(--text-primary)` (`oklch(93% 0.007 68)`) for all primary text.
- **Graphite secondary text:** `#5e5e54` → `var(--text-muted)` (`oklch(55% 0.009 258)`).
- **Accent introduced:** The source collapses accent to black, which is unusable on dark. The dark adaptation maps `--accent` (`oklch(62% 0.14 158)` jade) to the Lora serif pull quote text and sidebar mono labels — a minimal accent presence that doesn't violate the austere identity.
- **Divider/border lines:** `#1a1a16` black rules → `var(--divider)` (`oklch(25% 0.008 258)`) to prevent harsh contrast against the dark background.
- **Left sidebar hairline:** Dimmed from black to `var(--divider)` to remain structural without dominating.
