---
agent_id: larry
session_id: impeccable-design-system-integration
timestamp: 2026-05-26T01:31:00Z
type: close-session
linked_sops: []
linked_workstreams: []
linked_guidelines: []
---

# Integrating impeccable into the slide deck design system

## Context

Adnan came in wanting to use the globally-installed impeccable skill to own the visual design of all future decks. The existing shared branding (Georgia serif, amber accent, cream background) was not working for him. The goal: run impeccable's teach flow once, lock a design system, wire it into Coda so every future deck inherits it automatically.

## What we did

- **Larry** ran the impeccable teach interview (two rounds of AskUserQuestion) to establish strategic context before writing any files.
- **Larry** wrote `PRODUCT.md` at the project root — register (brand), presenter profile (independent researcher/thinker), personality (credible, provocative, measured), four anti-references (startup pitch, corporate PPT, academic slides, Canva).
- **Larry** wrote `DESIGN.md` at the project root — committed dark theme, Barlow Condensed/Barlow font system via Google Fonts, jade accent (`oklch(62% 0.14 158)`), OKLCH-based neutrals, flat elevation, component specs for stat blocks and section labels.
- **Larry** updated `shared/branding/base.css` — Google Fonts `@import`, fonts swapped from Georgia/system-ui to Barlow Condensed/Barlow, italic removed from h1/h2, `--text-4xl: 6rem` added.
- **Larry** updated `shared/branding/theme-dark.css` — OKLCH color tokens replacing the old hex amber palette.
- **Larry** updated `shared/branding/theme-light.css` — OKLCH color tokens replacing the old cream/amber palette.
- **Larry** added a design system gate rule to `.claude/agents/coda.md` — Coda now reads PRODUCT.md and DESIGN.md before producing any HTML.
- **Larry** took screenshots of both light and dark themes on the existing AI & Kids deck (v1.0.0) to verify the new design rendered correctly.
- **Larry** saved a memory entry for Adnan's WSL2 URL preference (use IP, not localhost).

## Decisions made

- **Question:** Should impeccable own the design system for all decks?
  **Decision:** Yes. PRODUCT.md + DESIGN.md at the project root are now the single source of truth. Coda gates on them before producing any HTML.

- **Question:** What register?
  **Decision:** Brand by default, overridable per deck via `pov.md`. Slide decks are marketing artefacts — the design impression IS part of the argument.

- **Question:** Which theme is the presentation default?
  **Decision:** Dark. A darkened room is where these slides are presented. The DESIGN.md makes this explicit.

- **Question:** Which fonts?
  **Decision:** Barlow Condensed (display, SemiBold 600) + Barlow (body). Not on the impeccable reflex-reject list, has commanding condensed variant for stats, avoids all four anti-reference aesthetics.

- **Question:** Which accent?
  **Decision:** Jade (`oklch(62% 0.14 158)` dark / `oklch(40% 0.14 158)` light). One accent only, never a second per deck.

- **Question:** Dark or light for the AI & Kids v1.0.0 deck?
  **Decision:** Deferred. Adnan will run the improvement cycle and decide after seeing both themes in context. The deck stays on light theme for now.

## Insights

- The impeccable skill's loader script lives at `/home/aali/.claude/plugins/cache/impeccable/impeccable/3.1.1/skills/impeccable/scripts/load-context.mjs` — not at the project-local `.claude/skills/` path the skill docs assume. Always call it from the global install path.
- OKLCH-in-CSS is supported natively in Chromium (which Reveal.js uses via Puppeteer for screenshots). No polyfill needed for the slide deck context.
- The impeccable register for slide decks is nuanced: it can flip from `brand` to `product` per deck. PRODUCT.md captures the default and the override mechanism.

## Realignments

- Adnan clarified that the register is not fixed globally — it "can change from deck to deck." PRODUCT.md now documents `brand` as the default with `pov.md` as the per-deck override point. This is a meaningful scope correction from the initial assumption that one global register would govern all decks.
- On the visual reference question, Adnan rejected all four offered references (Economist, Tufte, Atlantic, Stripe) and stated: slides must NOT be verbose, NOT a document for pre-reading, but "an engaging masterpiece that pulls the audience in to focus on the words of the presenter." This shaped the entire DESIGN.md direction — no editorial-typographic aesthetic, type as the visual, silence as a design choice.

## Open threads

- [ ] Adnan to run the improvement cycle on the AI & Kids deck (quota reset needed) and compare light vs dark theme before deciding which becomes the permanent theme for that deck.
- [ ] Consider running `/impeccable document` once the improvement cycle produces a richer set of HTML components — the seeded DESIGN.md can be refined against real rendered output.
- [ ] The `--text-4xl: 6rem` token is defined but not yet used in any existing deck HTML. Coda should use it for single-stat impact slides in future deck versions.

## Next steps

- Adnan runs the AI & Kids improvement cycle (next session, after quota reset).
- Larry/Coda applies the new design system to the improvement cycle output.
- After reviewing both themes in context, Adnan decides on the theme for AI & Kids v1.1.0.

## Cross-links

- [[2026-05-26-larry-ws004-ai-and-kids-bootstrap]] — prior session that closed the v1.0.0 bootstrap cycle; the design system introduced this session will feed into v1.1.0.
