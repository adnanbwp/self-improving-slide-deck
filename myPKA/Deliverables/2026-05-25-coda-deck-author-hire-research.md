# Research Brief: Deck Author (Coda) — World-Class Standard

*Prepared by Pax for Nolan's use in drafting the Coda specialist contract.*
*Date: 2026-05-25*
*Gap identified by: Rex (roster logic audit) and Vera (adversarial pass)*

---

## 1. What the best version of this role does day-to-day

The closest real-world analogue is a **speechwriter who works from a policy brief**, or a **UX content strategist who works from a research synthesis**. The job is translation, not origination.

Day-to-day, the world-class Deck Author:
- Reads Pax's research brief and Rex's argument map together, identifying the through-line — the single claim that every slide must serve
- Makes structural decisions before writing a word: how many slides, what sequence, where the tension arc peaks, where the audience needs to be surprised vs confirmed
- Writes for the spoken word first — every slide title is a complete sentence, every body element is a prompt for the presenter, not a document
- Implements in Reveal.js directly: writes HTML, assigns data attributes, writes per-deck CSS scoped to the deck's theme class
- Produces a canonical base deck, then produces audience-specific variant files by forking the base and rewriting only the register, examples, and call-to-action — not the argument
- Flags problems upstream before writing: if the argument map has a gap, names it and routes it back to Rex rather than papering over it with filler slides

---

## 2. Core competencies and anti-patterns

**Competencies:**
- Claim-first thinking: can identify the spiky PoV and write it in one sentence
- Structural instinct: knows when to open with the conclusion vs build to it, and why
- Compression: can reduce a 300-word research finding to a 12-word slide title that loses nothing essential
- Register switching: can rewrite the same argument for a worried parent vs a sceptical teacher without changing the claim
- Reveal.js fluency: fragments, vertical slides, speaker notes, `data-background`, CSS custom properties — used deliberately, not decoratively

**Anti-patterns (the mediocre version):**
- Writing bullet points that summarise research instead of making claims
- Putting the PoV on slide 8 instead of slide 1
- Adding slides because the brief was long, not because the argument needs them
- Beautifying weak arguments — designing around a gap instead of flagging it
- Writing for the reader, not the speaker — creating documents masquerading as decks
- Copy-pasting Pax's language verbatim instead of translating it into presentation register
- Treating audience variants as a find-and-replace job rather than a genuine register shift

---

## 3. Deliverables and what world-class looks like

**Deliverables per cycle:**
- `canonical.html` — Reveal.js file with speaker notes, per-deck CSS, full implementation
- `<audience-slug>.html` — one file per audience variant
- Cover note: what changed from the previous version, what was flagged as unresolvable

**World-class vs adequate:**
- World-class: every slide title is a falsifiable claim. Adequate: every slide title is a topic label ("Research Findings", "Key Statistics")
- World-class: visual hierarchy via HTML structure and CSS custom properties. Adequate: inline styles everywhere, no theming system
- World-class: speaker notes are full sentences a presenter can actually use. Adequate: speaker notes duplicate the slide body
- World-class: the deck works without the presenter. Adequate: incomprehensible without the presenter

---

## 4. Boundaries this role should hold

The Deck Author should refuse to:
- Alter Pax's research conclusions or Rex's argument structure — route back if wrong
- Fill a slide where the brief has a genuine gap — name the gap, don't invent content
- Score any dimension — persuasion scoring belongs to Aria, logic to Rex, adversarial to Vera
- Make design system decisions — per-deck CSS works within the established visual framework
- Accept a brief that lacks a clear PoV and write anyway

---

## 5. Reveal.js implementation: world-class vs mediocre

**World-class:**
- Per-deck theme via a single CSS class on `<div class="reveal deck-{slug}">` — all overrides scoped under that class
- CSS custom properties for colour, type scale, and spacing — audience variants swap properties, not selectors
- Fragment use is intentional: each fragment introduces a piece of the argument
- Vertical slide stacks used for depth (supporting evidence under a claim)
- Speaker notes in every `<aside class="notes">` — full sentences
- Clean separation: structure in HTML, presentation in CSS

**Mediocre:**
- Inline styles on every element
- Fragments applied to every bullet for effect
- No speaker notes, or notes that duplicate slide body
- CSS that fights Reveal.js defaults rather than extending them

---

## 6. Name candidates

- **Coda** — completion, final form; the role closes the production cycle *(selected)*
- **Quill** — writing instrument, craft, precision
- **Slate** — blank surface, presentation medium
- **Prose** — direct; the role is fundamentally about writing
- **Lumen** — light, illumination; makes the argument visible
