# Vellum

**Aesthetic register:** Gallery / Literary dark-chromatic
**Source:** `shared/design-library/_source/templates/vellum/`

## Visual character
Vellum is a single-palette all-dark template: deep periwinkle navy (`#2a3870`) forms the entire canvas, and warm chartreuse yellow (`#E8D85C`) carries every glyph. There is no light-mode variant — every slide is navy + yellow regardless of content type. Cormorant Garamond italic (weight 300–600) carries all display and headline text; DM Sans (weight 300–500) carries all body; Courier Prime carries all attribution labels and mono chrome. The signature structural element is a large decorative open-quote glyph in dusty teal (`#3a7878`) that frames pull-quote slides — dramatically oversized, purely decorative, printed behind the quote text. The overall mood is an art gallery catalogue or independent literary publication: chromatic, personal, and slightly unexpected.

## Strengths
- The periwinkle + chartreuse palette is immediately distinctive — no other template in the library shares this chromatic identity, making Vellum slides instantly recognisable.
- Italic Cormorant Garamond at display weight creates a literary gravity that elevates even simple statements; the oversized quote-mark glyph amplifies this on quote slides.
- The single-palette constraint (no light variant) simplifies the adaptation surface — there are no per-slide background decisions to make.
- DM Sans body text recedes cleanly behind the personality type, preventing typographic competition on mixed content slides.

## Weaknesses
- The navy + yellow palette is strongly opinionated and may conflict with certain institutional brand guidelines that prohibit bold chromatic fields.
- Cormorant Garamond italic at small sizes (~14px and below) on the navy field approaches the WCAG AA contrast threshold — body text must use DM Sans instead.
- The template has no light-mode or neutral variant; it cannot be toned down for audiences expecting conventional presentation aesthetics.

## Best-fit slide types
Quote, About/Vision, About Me, Team/People, Split

## Known adaptations
- **Quote:** Centre the Cormorant Garamond italic at display scale. Place the oversized open-quote mark in dusty teal behind the text. Attribution in Courier Prime at the bottom-left annotation position.
- **About/Vision:** Use the navy field as full-bleed. Headline in Cormorant italic; supporting text in DM Sans. No containers needed — the field is the container.
- **Split:** Left half navy, right half a slightly lighter navy (`#343f80`). Yellow type on both sides. A thin yellow rule at the split line.
- **Team/People:** Photo (or photo placeholder) right; name and role in Cormorant + DM Sans left. The chromatic field makes photo integration feel editorial rather than corporate.

## Dark theme notes
Vellum is natively dark (navy field) but its palette differs from the design system dark tokens. Adapting to the standard dark system required:

- **Background replaced:** `#2a3870` periwinkle navy → `var(--bg)` near-black (`oklch(12% 0.008 258)`). This is a significant register shift — the distinctive periwinkle identity is lost in favour of the design system near-black.
- **Surface:** `#343f80` lighter navy → `var(--surface)` (`oklch(17% 0.008 258)`) for card and split-panel backgrounds.
- **Primary text:** `#E8D85C` warm chartreuse yellow → `var(--text-primary)` (`oklch(93% 0.007 68)`). The yellow personality is replaced with near-white — the warm chromatic identity of the source is substantially changed.
- **Muted text:** `rgba(232, 216, 92, 0.62)` yellow at 62% → `var(--text-muted)` (`oklch(55% 0.009 258)`).
- **Accent (quote-mark glyph):** `#3a7878` dusty teal → `var(--accent)` (`oklch(62% 0.14 158)` jade). Teal and jade are colour-adjacent; the decorative quote mark reads similarly.
- **Borders:** `rgba(232, 216, 92, 0.20)` yellow at 20% → `var(--divider)` (`oklch(25% 0.008 258)`).
- **Identity concern:** The dark theme adaptation substantially changes Vellum's visual identity. If the goal is to preserve Vellum's periwinkle + yellow character, consider using the source palette directly rather than the standard design system tokens.
