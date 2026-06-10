# Slide type: team

A closing credits slide crediting the human presenter and the AI specialist team. Use as the final slide in any deck.

## Visual spec — aha agile decks (brand default from 2026-06-10)

Use the `t-team-avatars` layout from `shared/templates/aha-agile/layouts.css` — no per-deck CSS needed:

- **Field:** `f-paper` on the `.slide-inner`
- **Header:** `.tag` = `Credits`; `h2.head.display` = `The team behind this deck`
- **Layout:** `.pad` > `.rows` > `.row` > `.person` (`.av` + `.nm` + `.ro`), row split per the table below
- **Avatar:** 92px circle (`.av`), ink ring, initials fallback behind the `<img>`
- **Adnan's card:** add `.presenter` to his `.av` for the orange ring
- **Reference implementations:** `decks/hybrid-delivery/versions/v2.0.0/canonical.html` slide 27 (9 members, 3-3-3) and `decks/ai-and-kids/versions/v2.0.0/canonical.html` slide 20 (12 members, 4-4-4)

## Visual spec — legacy Signal decks (pre-v2 maintenance only)

- **Background:** cream (no `.dark` class on `<section>`)
- **Header:** `.kicker` + `<hr class="rule">` — text is always `The team behind this deck`
- **Layout:** staggered rows using `.team` > `.row` > `.team-cell`
- **Avatar:** 54px circle with initials fallback; real portrait drops in automatically once `shared/assets/avatars/[slug].png` exists
- **Adnan's card:** always add `.presenter` to his `.team-av` for the gold ring
- **Card content:** `.team-name` (Source Serif 4) + `.team-role` (IBM Plex Mono gold) — no bio line

## Layout rule

**Odd member count → natural stagger.** Use unequal rows so the shorter middle row(s) center naturally between the longer ones. No manual offset needed — `justify-content: center` does the work.

**Even member count → symmetric equal rows.** No stagger. All rows the same length, all centered. A manual offset on equal rows looks misaligned, not staggered.

## Row split by team size

| Members | Row pattern | Layout type |
|---------|-------------|-------------|
| 12      | 4 – 4 – 4   | symmetric   |
| 11      | 4 – 3 – 4   | stagger     |
| 10      | 4 – 3 – 3   | stagger     |
| 9       | 3 – 3 – 3   | symmetric   |
| 8       | 4 – 4       | symmetric   |
| 7       | 4 – 3       | stagger     |
| 6       | 3 – 3       | symmetric   |
| 5       | 3 – 2       | stagger     |
| 4       | 2 – 2       | symmetric   |
| 3       | 2 – 1       | stagger     |

## Canonical roster

All member data (name, initials, role, color, avatar path) lives in `shared/team.yaml`. Read it to populate a team slide. Include only the members relevant to the deck.

## Avatar image fallback

```html
<div class="team-av" style="background:[color]">
  <img src="../../../../shared/assets/avatars/[slug].png" alt="[Name]" onerror="this.style.display='none'">
  [INITIALS]
</div>
```

When the image file exists it covers the initials. When it is missing, `onerror` hides it and the initials show through. The path depth (`../../../../`) assumes `decks/[deck]/versions/[version]/canonical.html` — adjust for different nesting.

## CSS classes (already in Signal canonical style block)

```
.team            flex column, 0.8rem gap
.team .row       flex row, centered, 1.2rem gap
.team-cell       flex column, centered, 72px wide
.team-av         54px circle, initials fallback
.team-av.presenter  gold ring around Adnan
.team-name       Source Serif 4, 600wt
.team-role       IBM Plex Mono, gold
```

These classes must be added to the `<style>` block of any `canonical.html` that uses this slide type. Copy from `decks/ai-and-kids/versions/v1.3.0/canonical.html` (the `Team slide` CSS section).

## Slide number

Update `.page-num` and the `deck-label` footer to match the deck's actual last slide number.
