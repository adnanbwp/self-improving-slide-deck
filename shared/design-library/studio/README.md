# Studio

**Aesthetic register:** Design-agency / Brutalist typographic
**Source:** `shared/design-library/_source/templates/studio/`

## Visual character
Studio is a two-mode template — near-black (`#1c1c1c`) dark slides and acid yellow (`#f5d200`) light slides — where the yellow is the entire environment, not an accent. Barlow 900 (weight 900, uppercase, tight tracking) carries every headline and display element; at large scale it becomes a graphic object rather than readable text. Barlow 400/500 handles body; IBM Plex Mono handles chrome metadata, counters, and footer columns. The signature structural element is a three-column metadata bar across the base of the cover slide, and the em-dash bullet list on dark slides (yellow em-dash in accent, body text receding). The overall mood is a Boring Studios / design-agency credentials deck: bold, systematic, zero decoration — the headline IS the layout.

## Strengths
- Barlow 900 at maximum scale (12vw display) has a graphic mass that makes any slide command attention — the type itself is the visual object.
- The two-mode light/dark system (dark slides for content, yellow slides for chapter breaks) creates strong visual rhythm across a full deck without needing imagery.
- IBM Plex Mono metadata bars give the template a credentials-deck authority — every slide feels like it comes from a systematic production process.
- The em-dash bullet list (yellow dash, body text) is a self-contained visual system that scales from 2 to 10 items without needing icons or colour variation.

## Weaknesses
- The acid yellow light slide background is highly opinionated — it reads as design-agency specific and may not suit educational, institutional, or public-sector contexts.
- Barlow 900 uppercase requires generous type scale to work — at sub-32px the condensed grotesque at max weight becomes illegible on projection.
- The strictly two-colour dark/light logic offers no mid-register — there is no neutral grey variant that tones down the acid yellow for more conservative audiences.
- Services/Offerings cards lack native icon support; the template uses numbered text blocks rather than icon + label pairs.

## Best-fit slide types
Services/Offerings, Comparison, List, About Me, Gallery

## Known adaptations
- **Services/Offerings:** 2×2 grid on dark background. Each card has a symbol/glyph in Barlow 900 at ~48px, followed by the service name in Barlow 700 uppercase, followed by a one-sentence body in Barlow 400. Cards separated by `var(--divider)` borders.
- **Comparison:** Two columns on a split slide — left column dark, right column yellow (or both dark with a divider). Barlow 900 category names; Barlow 400 comparison body.
- **List:** Dark slide, full-width. Barlow 900 list title at h2 scale; em-dash bullet list below. Up to 6 items fits comfortably.
- **About Me:** Yellow slide. Barlow 900 name at large scale; IBM Plex Mono role/metadata below. Photo placeholder (dark grey box) as right element.
- **Gallery:** 3-up or 4-up image grid on dark. IBM Plex Mono captions below each image.

## Dark theme notes
The Studio source template natively uses near-black (`#1c1c1c`) for dark slides, which is very close to the design system `--bg`. Adapting to the dark design system required minimal changes for dark slides; the yellow light-slide variant required more:

- **Dark slide background:** `#1c1c1c` near-black → `var(--bg)` (`oklch(12% 0.008 258)`). The warm near-black of the source becomes a cooler near-black in the design system — subtle temperature shift.
- **Dark secondary surface:** `#242422` → `var(--surface)` (`oklch(17% 0.008 258)`).
- **Acid yellow primary text on dark:** `#f5d200` → `var(--text-primary)` (`oklch(93% 0.007 68)`). The warm yellow foreground is replaced with near-white — the high-energy yellow personality is lost on dark slides.
- **Muted text on dark:** `rgba(245, 210, 0, 0.58)` → `var(--text-muted)` (`oklch(55% 0.009 258)`).
- **Accent (yellow em-dash bullets):** `#f5d200` → `var(--accent)` (`oklch(62% 0.14 158)`). Em-dash bullets use jade instead of yellow.
- **Light (yellow) slide background:** `#f5d200` acid yellow → `var(--surface)` (`oklch(17% 0.008 258)`) — this collapses the light variant to dark surface, eliminating the two-mode system. If the yellow chapter-break identity needs to be preserved, use the source `#f5d200` value directly on chapter slides rather than the design system token.
- **Divider borders on dark:** `#2e2e2c` → `var(--divider)` (`oklch(25% 0.008 258)`).
