# Broadside

**Aesthetic register:** Typographic Poster / High-provocation
**Source:** `shared/design-library/_source/templates/broadside/`

## Visual character
Broadside is a protest-poster editorial system where type is so large it stops being copy and becomes graphic element. Display type runs at 13vw weight-900 lowercase Barlow — approximately 187px at 1440px wide — treating individual words as shapes. The system operates in two registers only: near-black canvas with cream text and fire-orange accent, or full fire-orange background with dark-ink text ("ink on fire"). There is no cream or paper slide. Barlow is the only display face; IBM Plex Mono handles all chrome. The entire identity is constructed from weight, size, one color, and flat negative space. The cultural reference is broadside printing and SPACE10 reports — one statement, one rule, breathing room, nothing else.

## Strengths
- The single-typeface-plus-chrome system (Barlow + IBM Plex Mono) produces extremely fast composition: there are no font-choice decisions within a slide, only weight and size decisions.
- The two-register color model (dark / orange) provides a natural vocabulary for distinguishing declaration slides (orange) from content slides (dark) without any per-slide color decisions.
- The negative-space-as-composition philosophy makes statement and question slides render at a consistently high impact level with minimal markup.
- Barlow is already the design system's primary font family, so the Broadside source adapts to the dark theme with no font swap required.

## Weaknesses
- The system's highest-impact register (orange cover/chapter slides) cannot be preserved under the dark theme — the fire-orange full-background environment becomes an accent-colored border or kicker at best.
- Dense information layouts are difficult: the system explicitly caps bullet lists at three items, and has no native evidence or multi-stat table pattern. Data-adjacent content requires significant structural additions.

## Best-fit slide types
Statement, Question / Hook, Title, Stat, Section Divider

## Known adaptations
- **Stat:** Suppress all decorative poster elements. Use only the number at full scale and the stat label below — nothing else.
- **Evidence:** Add a contained evidence block below the dominant stat; scale back poster typography on the source/context text.
- **Chart / Graph:** Not recommended without significant structural rework — Broadside has no native data pattern.

## Dark theme notes
Broadside is already dark-native (near-black `#111111` is the default canvas). The dark theme adaptation required minimal color work:

- **Background:** Source `#111111` near-black is nearly identical to `var(--bg)`; replaced for token consistency.
- **Accent color replaced:** Source fire-orange (`#E85D26`) → `var(--accent)` jade green (`oklch(62% 0.14 158)`). This is the most significant identity change: the protest-poster "fire" register becomes a cooler jade provocation. The structural use of the accent (kickers, rules, question text) is preserved.
- **Primary text:** Source cream (`#F0ECE5`) → `var(--text-primary)`.
- **Muted text:** Source `#888880` → `var(--text-muted)`.
- **Borders:** Source `#282826` → `var(--divider)`.
- **Orange slide register dropped:** The fire-orange full-background slides have no equivalent in the dark theme. Cover/question slides use the dark canvas with the accent-colored headline to approximate the declaration register.
- **Fonts preserved:** Barlow is already the design system font, so no font swap was needed — this is the only Broadside-specific structural advantage in dark theme adaptation.
- **Lowercase display preserved:** The weight-900 lowercase Barlow display treatment is carried through unchanged, maintaining the poster identity within the dark-theme constraint.
- **Chrome suppressed on Question / Hook slides:** Following the source's pattern for declarative slides, no top/bottom chrome is shown — the question sits alone on the dark canvas.
