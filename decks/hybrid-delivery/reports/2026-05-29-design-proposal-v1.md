# Design Proposal — The Iteration Manager in the Age of Agents
**Version:** v1
**Date:** 2026-05-29
**Deck slug:** hybrid-delivery
**Slide plan source:** `decks/hybrid-delivery/reports/2026-05-29-slide-plan-v1.md`
**PoV source:** `decks/hybrid-delivery/pov.md`
**Design library:** `shared/design-library/INDEX.md`

**Library status:** 8 annotated entries available. Minimum floor (3) met. Full proposal — 3 of 3 options.

---

## Section 1: Template Options

### Slide-type coverage summary

The deck requires 10 distinct slide types across 20 slides:

| Type | Count | Slides |
|---|---|---|
| Title | 1 | 1 |
| Statement | 2 | 2, 10 |
| Comparison | 4 | 3, 11, 13, 14 |
| Question / Hook | 1 | 4 |
| Evidence | 3 | 5, 6, 12 |
| Stat | 2 | 7, 17 |
| List | 4 | 8, 15, 16, 18 |
| Timeline | 1 | 9 |
| Process / Steps | 1 | 19 |
| CTA | 1 | 20 |

---

### Option 1: Monochrome (Ivory Ledger) — Ranked #1

**Aesthetic register:** Archival / Research-grade editorial

**Deck-level rationale:**
Monochrome is the strongest fit for this deck on every axis. The PoV demands credibility without corporate gloss — the deck must feel like it was written by someone who has done the work, not sold it. Monochrome's archival/research-grade register lands exactly there. Ultra-light Jost at weight 200 reads as rigorous rather than designed; the em-dash bullet marker and JetBrains Mono chrome reinforce the "this is a research document" signal that earns analytical IMs and DMs rather than performing at them.

The native slide type coverage is the highest in the library. The template has explicit patterns for Statement (slide--statement), List (slide--list with em-dash bullets), Comparison (slide--compare with center-rule two-column), Evidence (slide--stats with rule-top stat cells and mono source notes), Timeline (slide--timeline with horizontal track and dots), and Process/Steps (slide--diagram with numbered flow-steps). Title (slide--cover) and CTA (slide--end) are also native. Only Question/Hook has no exact native pattern — the closest is the Statement pattern adapted to a single interrogative at display scale, which is a minor CSS adjustment.

The dark theme adaptation has been documented in the annotated README. The surface logic flips from cream to near-black (`oklch(12% 0.008 258)`), primary text maps to `oklch(93% 0.007 68)`, and a minimal jade accent (`oklch(62% 0.14 158)`) is introduced for Lora italic pull-quote text and sidebar labels — the only chromatic presence in what is otherwise a monochrome dark system. The theme feels consistent with the PoV's "credible, provocative, measured" register.

**Strengths for this deck:**
- Native Comparison pattern (slide--compare) is exactly the two-column center-rule structure the slide plan specifies for slides 3, 11, 13, 14 — the most frequently used type (4 of 20 slides).
- Native List pattern (slide--list) with em-dash bullets matches the slide plan's instruction that list items should appear as "standalone blocks," not traditional bullets.
- Native Timeline pattern on a warm-cream sub-surface creates a tonal shift that gives slide 9 a distinct textural beat within the dark deck — appropriate since Wave 1 is a narrative pivot.
- The stat-cell component (5.5vw Jost-200 numeral with rule-top and mono source note) handles both Evidence and Stat slides without structural adaptation.
- Lora italic serif in the dark adaptation provides the one moment of typographic warmth — appropriate for the Statement slides (2, 10) where the deck asks the audience to recognize something they already know.

**Weaknesses and risks:**
- No native Question/Hook slide type. The slide plan calls for a large rhetorical question with nothing else on slide 4 — this is achievable with minor CSS adaptation (display-scale Jost-200, suppressed chrome), but Coda must author it intentionally.
- No native CTA slide type. The slide--end pattern exists but is a generic close; Coda must adapt it for the single-imperative display structure required by slide 20.
- Ultra-light Jost weight 200 can degrade on low-quality projection hardware where sub-pixel rendering is unavailable. For conference room projection, this is a real risk; for screen-sharing and browser viewing, it is not.
- The dark theme substitutes the jade accent for the canonical no-accent identity — slides using Lora italic will have a chromatic presence that the canonical system deliberately avoids. This is a conscious design decision, not a defect, but Adnan should be aware the jade accent is a design-system addition, not a Monochrome original.

**Canonical vs. adaptation paragraph:**
The canonical Monochrome (Ivory Ledger) system is cream-paper black-ink with zero chromatic accent — the accent token resolves to darker ink. The design system's dark theme substitutes the background with near-black (`oklch(12% 0.008 258)`), maps the cream-paper surface to a slightly lifted near-black (`oklch(17% 0.008 258)`) for inset elements, replaces black ink text with a warm near-white (`oklch(93% 0.007 68)`), and introduces jade (`oklch(62% 0.14 158)`) as an accent for Lora serif pull-quote text and sidebar mono labels. The canonical Jost / Lora / JetBrains Mono font stack is preserved without substitution — this is a genuine strength. What is lost: the defining "black ink on cream paper" material identity. What is preserved: the ultra-light Jost weight, the Lora italic serif as a register-signal, the em-dash bullet markers, and the 1px hairline rule structure. The substitution is a register-equivalent dark translation, not a different design system — but the canonical warm-cream reading experience is gone.

---

### Option 2: Cobalt Grid — Ranked #2

**Aesthetic register:** Structured / Data-authority (Japanese trend-report)

**Deck-level rationale:**
Cobalt Grid is the highest-impact, most distinctive option. The permanent graph-paper grid and pixel-glitch decorations project a "this deck has a point of view" energy that matches the PoV's provocation level. The vbig-numeral token (up to 240px display stats) is the most capable large-number treatment in the library — directly suited to the $110K token cost figure on slide 17 and the 84%/49% governance gap on slide 12. The Newsreader / Hanken Grotesk / DM Mono three-face system communicates authority without conventional corporate dressing.

The native type coverage is strong for this deck's dominant visual focal points: Cover/Title (s-cover), Statement/Manifesto (s-manifesto), List/Index (s-index, 2×3 grid with numbered rows), Stat/Data (s-data with vbig-numeral and pixel-stack chart), and Closing/CTA (s-colophon). However, the template has no native Comparison, Timeline, Evidence (as a stat+qualifier pattern), or Process/Steps slide. These four types together account for 9 of 20 slides — more than the native-coverage types. All four require structural adaptation.

**Strengths for this deck:**
- The vbig-numeral display stat (clamp 110–240px) is the best large-number treatment in the library. Slides 7, 12, and 17 — the three highest-urgency data moments — benefit significantly from this scale.
- The manifesto pattern (s-manifesto) handles Statement slides 2 and 10 natively, including the italic-with-roman-flip treatment that creates a "human voice" register within the cobalt identity.
- The graph-paper grid creates a consistent visual plane that prevents the dark slides from feeling flat or atmospheric — the deck's analytical audience will read it as structured precision rather than mood.
- The pixel-stack bar chart directly echoes the pixel-glitch decoration, giving the data visualization slides a unified visual language.
- The s-colophon pattern (right-aligned display + pixel-glitch left + multi-column footer) is an excellent native CTA structure for slide 20.

**Weaknesses and risks:**
- The dark theme adaptation replaces the signature electric cobalt ink (`#1F2BE0`) with the design system's jade accent (`oklch(62% 0.14 158)`). This is a register-significant substitution: cobalt is cool, high-saturation, Japanese-magazine; jade is warm, botanical. The two-color risograph identity relies on the specific cobalt hue. Without it, the grid, the pixel-glitch columns, and the hairlines lose their defining character.
- No native Comparison pattern. The four Comparison slides (3, 11, 13, 14) are the deck's structural spine — the generate-vs-decide boundary on slide 13 is "the slide the entire argument has been building toward." Adapting a two-column Comparison from the index/table patterns requires meaningful structural work from Coda.
- No native Timeline pattern. Slide 9 requires a three-node horizontal timeline, which must be built from scratch within the cobalt grid identity.
- No native Process/Steps pattern. Slide 19 requires three numbered horizontal steps — constructable from the index row pattern but requiring structural adaptation.
- The permanent graph-paper grid reads well on dense data slides and declaration slides but can feel over-structured on Statement slides where the slide plan calls for "full-bleed type" — Coda may need to suppress non-essential chrome on slides 2 and 10.

**Canonical vs. adaptation paragraph:**
The canonical Cobalt Grid is strictly cream (`#F0EBDE`) and electric cobalt (`#1F2BE0`) — two colors, no exceptions. The design system's dark theme substitutes the cream canvas with near-black (`oklch(12% 0.008 258)`) and replaces cobalt entirely with the jade accent (`oklch(62% 0.14 158)`) for all text, borders, hairlines, and grid. What is lost: the defining cobalt ink color — the entire two-color risograph identity. The warm botanical jade does not carry the same high-saturation cool-tone authority that cobalt projects; the visual register shifts from "Japanese trend report" toward "design-system green," which lacks the cobalt's provocation level. The font stack — Newsreader / Hanken Grotesk / DM Mono — is not replaced; this is preserved. The graph-paper grid at 5% jade opacity instead of 10% cobalt opacity is visibly different in density. The permanent hairlines and pixel-glitch decorations survive the translation but change character significantly. For the hybrid-delivery deck, this substitution is the primary risk: the cobalt hue is what makes Cobalt Grid feel authoritative rather than decorative, and the dark jade adaptation mutes that authority.

---

### Option 3: Cartesian — Ranked #3

**Aesthetic register:** Classical analytical / Architectural editorial

**Deck-level rationale:**
Cartesian is the most accessible and least risky option. The Playfair Display serif headline system communicates authority through its didone letterforms; the warm sandstone palette reads as "considered, premium, unhurried." For a deck aimed at analytically oriented IMs/DMs who have survived a consolidation wave, this register is respectful and credible — it does not condescend, and it does not over-dramatize.

The native slide type coverage includes Title (slide-title with Playfair Display headline), Statement (slide-statement with quote-mark decoration and Playfair h2), Timeline (slide-timeline with horizontal taupe hairline and evenly distributed items), and Closing/CTA (slide-closing with centered Playfair display + geo-ring). The two-column split (slide-twocol) can serve as a base for Comparison slides. However, there is no native native Comparison pattern with labeled columns and a bottom annotation (as specified in the slide plan), no native Evidence pattern for the BCG/P&G stat display, no native Stat pattern for display-scale numbers, no native List pattern with standalone blocks, and no native Process/Steps pattern. Together these account for 10 of 20 slides.

**Strengths for this deck:**
- The Playfair Display / Inter pairing is the most familiar analytical editorial register in the library — IMs and DMs who read Harvard Business Review, McKinsey reports, or Gartner analyst papers will immediately trust this visual language.
- The decorative geometric circles (solid + dashed compass arcs) recede from content and create atmosphere without competing — appropriate for the deck's measured tone.
- The closing pattern (slide-closing) with centered Playfair h1 and decorative geo-ring is one of the cleanest CTA treatments in the library for slide 20.
- The Timeline pattern (slide-timeline with horizontal taupe hairline, Playfair date markers, Inter descriptions) handles slide 9 natively and suits the "Wave 1 historical precedent" narrative beat.

**Weaknesses and risks:**
- The Cartesian stat-figure token is only 2rem — the smallest stat numeral in the library. There is no hero-stat-numeral pattern. This is a significant problem for slides 7, 12, and 17, where the slide plan explicitly requires "one dominant number at display scale." Coda must build a larger stat treatment from scratch.
- Cartesian reads as warm and calm, which is appropriate for the respect-not-lecture tone — but the deck also needs to land as "provocative" and willing to say what no one else says plainly. The sandstone palette and gentle compass arcs may soften the argument's edge more than the PoV warrants.
- No native List pattern beyond the agenda-list row format (horizontal separator + numeral). The four List slides (8, 15, 16, 18) require standalone block items, not agenda rows — structural adaptation is needed.
- The dark theme adaptation replaces the warm sandstone canvas with near-black (`oklch(12% 0.008 258)`) and substitutes the warm taupe accent with jade (`oklch(62% 0.14 158)`). The most significant loss is the warmth: the "consulting-meets-architecture" register depends partly on the sandstone surface and warm taupe — both disappear in the dark adaptation. The Playfair Display serif survives in the dark adaptation with good legibility.
- No native Comparison, Evidence, Stat, or Process/Steps patterns. Five of ten required slide types are missing native patterns.

**Canonical vs. adaptation paragraph:**
The canonical Cartesian system uses warm sandstone (`#EDE8E0`) canvas, warm taupe accent (`#8A8178`), and muted sand dividers (`#B8B0A4`). The Playfair Display / Inter font stack is canonical and preserved. The design system's dark theme replaces the sandstone canvas with near-black, the taupe accent with jade, and the sand dividers with a near-black divider (`oklch(25% 0.008 258)`). The large geometric circle decorations survive at significantly reduced opacity (0.08) — nearly invisible on the dark surface. What is lost: the defining warmth and the "museum-catalog meets architectural editorial" material register, which both depend on the sandstone surface. The compass-arc atmosphere that gives Cartesian its "drafted, considered" signal is barely perceptible in the dark adaptation. The Playfair Display / Inter pairing is the strongest asset that survives intact.

---

## Section 2: Per-Slide Fit Table

**Rating key:**
- **Very strong** — native pattern in source template.html; no structural adaptation needed
- **Strong** — template handles this type with minor CSS adjustments only
- **Moderate** — structural adaptation required; Coda tip provided

| Slide | Purpose | Type | Monochrome | Cobalt Grid | Cartesian |
|---|---|---|---|---|---|
| 1 | Title | Title | Very strong | Very strong | Very strong |
| 2 | Statement — jobs question settled | Statement | Very strong | Very strong | Strong |
| 3 | Comparison — adoption vs. integration gap | Comparison | Very strong | Moderate | Moderate |
| 4 | Question / Hook — what happens with AI? | Question / Hook | Strong | Strong | Strong |
| 5 | Evidence — BCG/P&G performance data | Evidence | Very strong | Very strong | Moderate |
| 6 | Evidence — Malone counter-evidence | Evidence | Very strong | Very strong | Moderate |
| 7 | Stat — McKinsey <40% measurable gains | Stat | Very strong | Very strong | Moderate |
| 8 | List — five workflow-agent collision points | List | Very strong | Strong | Moderate |
| 9 | Timeline — Wave 1 (2020–2024) | Timeline | Very strong | Moderate | Very strong |
| 10 | Statement — roles that survived owned delivery | Statement | Very strong | Very strong | Strong |
| 11 | Comparison — what agents generate vs. govern | Comparison | Very strong | Moderate | Moderate |
| 12 | Evidence — Digital.ai 84%/49% governance gap | Evidence | Very strong | Very strong | Moderate |
| 13 | Comparison — generate vs. decide boundary | Comparison | Very strong | Moderate | Moderate |
| 14 | Comparison — evolution vs. fragmentation fork | Comparison | Very strong | Moderate | Moderate |
| 15 | List — three capabilities | List | Very strong | Strong | Moderate |
| 16 | List — ceremony redesigns | List | Very strong | Strong | Moderate |
| 17 | Stat — $110K token cost exposure | Stat | Very strong | Very strong | Moderate |
| 18 | List — governance maturity ladder | List | Very strong | Strong | Moderate |
| 19 | Process / Steps — three-step action path | Process / Steps | Very strong | Moderate | Moderate |
| 20 | CTA — "Own the decisions agents can't make" | CTA | Strong | Very strong | Very strong |

---

### Coda tips — Moderate cells and non-obvious enhancements

**Slide 3 (Comparison) — Cobalt Grid: Moderate**
Coda tip: The s-index pattern is a 2×3 grid of numbered rows — not a two-column labeled comparison. For this slide, suppress the num-tag column and replace it with two equal-flex columns separated by a 1.5px cobalt (or jade, in dark adaptation) vertical rule. Add Hanken Grotesk micro-text column headers above each column, and the bottom annotation label as a single Hanken micro-text row spanning both columns beneath. The topbar pattern can carry the slide's framing headline above the comparison body.

**Slide 3 (Comparison) — Cartesian: Moderate**
Coda tip: The slide-twocol pattern uses image-placeholder left + text right and is not a labeled comparison. Author a new two-column grid using the `--bg-secondary` fill for each panel card border, Inter uppercase labels as column headers, and a 1px `--line` vertical divider centered between the columns. The bottom annotation can use Inter `attribution` size with 2px tracking.

**Slide 5 (Evidence) — Cartesian: Moderate**
Coda tip: Cartesian's stat-figure token is only 2rem — unsuitable for displaying the BCG 12.2% and P&G 3x uplift figures at display scale. Author a custom `.hero-stat` class using Playfair Display at clamp(3.5rem, 6vw, 5.5rem) weight 400, with an Inter subtitle below for the qualifier. The slide plan specifies two distinct evidence items (BCG and P&G) — use the two-column split pattern with a stat cluster in each column, adding a 1px taupe `--line` top-border above each cluster. The qualifier sentence ("for complex, generative knowledge work") should appear in Inter `label` size in `--accent` taupe to signal its conditional status visually.

**Slide 6 (Evidence) — Cartesian: Moderate**
Coda tip: The Malone counter-evidence requires the dominant number (Malone finding) to read as authoritative before the reconciliation sentence. Use the same custom `.hero-stat` class from slide 5. The reconciliation sentence can use the Cartesian `quote-mark` Playfair treatment (5rem " mark at 50% taupe opacity) adapted as a visual emphasis device rather than a literal quote mark — or suppressed entirely in favor of the simpler two-line Playfair h2 + Inter body structure.

**Slide 7 (Stat) — Cartesian: Moderate**
Coda tip: Same issue as slides 5–6. The McKinsey "<40%" figure must dominate. Author the custom `.hero-stat` class (clamp 3.5–5.5rem Playfair Display). The qualifying context ("bolt AI onto legacy workflows") sits in Inter body below. The geo-decoration circle can be used as a background element to soften the otherwise sparse layout without competing with the stat.

**Slide 8 (List) — Cobalt Grid: Strong**
Coda tip: The s-index pattern has 6 numbered rows in a 2×3 grid — this deck needs 5 standalone collision-point blocks without the index-list format. Use the topbar pattern for the claim title ("Agents don't slot in. They collide — unless you compose them."), then author five equal-flex rows using the faint-cobalt row-divider pattern. Each item should be a single Hanken body-lede line (15–18px) without a Newsreader headline — the standalone block format. Suppress the num-tag column or convert it to a DM Mono ordinal (01–05) used purely as a left-gutter marker.

**Slide 8 (List) — Cartesian: Moderate**
Coda tip: The agenda-list pattern uses Playfair numerals as left-gutter anchors with Inter text right. For this slide's standalone-block format, use the agenda-list pattern but suppress the agenda-number element and use the full-width body text directly. Add 1px taupe bottom-border between items (agenda-row style). The claim title ("Agents don't slot in. They collide — unless you compose them.") should sit as Playfair h2 above the list, separated by a 6vh gap.

**Slide 9 (Timeline) — Cobalt Grid: Moderate**
Coda tip: The s-table ledger and s-index patterns are the closest available structures but neither is a horizontal timeline. Build the timeline using the standard cobalt-grid chrome frame (hairlines, page number), a topbar for the section label, and a three-column equal-flex grid with a 1.5px horizontal cobalt rule above each column (the top border serves as the timeline track). Each column carries: DM Mono year label, Hanken micro-text era name, Hanken body description. The absence of a native dot-and-line timeline in cobalt-grid means the structure must be authored from the row/frame primitives. Keep it architecturally simple — the graph-paper grid provides enough visual rhythm without explicit dot markers.

**Slide 11 (Comparison) — Cobalt Grid: Moderate**
Coda tip: See slide 3 Cobalt Grid tip — same pattern required. For this slide specifically, the right column ("Nobody's governing this") contains governance gap items that are the deck's urgency signal. Use the vstack-label component on the right column edge as an optional mono annotation ("NO GOVERNANCE") to reinforce the column's meaning without adding body text.

**Slide 12 (Evidence) — Cartesian: N/A — rated Moderate above**
Coda tip: The 84%/49% governance gap is the deck's most important number pair. Use two side-by-side `.hero-stat` blocks (same custom class from slide 5) with a 1px taupe vertical divider between them. Left block: "84%" with Inter label "AI TOOL ADOPTION" in `--accent` taupe. Right block: "49%" with Inter label "HAVE GOVERNANCE GUARDRAILS" in `--accent` taupe. The tension between the two numbers should be visually obvious from size and proximity alone.

**Slide 13 (Comparison) — Cobalt Grid: Moderate**
Coda tip: This is the deck's conceptual hinge. For Cobalt Grid, use the two-column pattern from slides 3 and 11 but apply the pixel-glitch column decoration at the boundary between the two panels (centered) rather than at the slide edge — this creates a visual "dividing line" that reinforces the generate/decide distinction. The bottom annotation label ("The boundary is not permanent. Your job is to own it right now.") is the most important sentence in the deck — render it in Hanken micro-strong (13–16px, uppercase, 0.18em tracking) spanning the full width below the two columns.

**Slide 13 (Comparison) — Cartesian: Moderate**
Coda tip: See slide 3 Cartesian tip for base pattern. This slide is the intellectual peak — the geo-decoration should be suppressed or reduced to 10% opacity on this slide to avoid visual competition with the conceptual content. The bottom annotation is load-bearing; use Playfair h3 (not Inter label) so it reads as a statement, not chrome.

**Slide 14 (Comparison) — Cobalt Grid: Moderate**
Coda tip: See slide 3 Cobalt Grid tip. For this slide, the two-column fork requires visual balance between "Evolution path" and "Fragmentation path." Avoid using any visual asymmetry that implies the deck has already decided the winner — both columns should appear structurally equal. Reserve the bottom annotation label ("This fork is real. Here's the argument for evolution.") in Hanken micro-strong.

**Slide 14 (Comparison) — Cartesian: Moderate**
Coda tip: See slide 13 Cartesian tip. Both columns must be equally weighted visually. Do not use the Playfair quote-mark decoration on this slide — the fork is a structural argument, not a quotation.

**Slide 15 (List) — Cartesian: Moderate**
Coda tip: The three capabilities require standalone block treatment, not agenda rows. Use three `card` instances (1px taupe-bordered, semi-transparent white fill) in a three-column grid. Each card: Playfair card-headline for the capability name, Inter body-sm for the description. The claim title ("Three capabilities. One survival argument.") sits as Playfair h2 above the grid.

**Slide 16 (List) — Cartesian: Moderate**
Coda tip: Same as slide 15 — three card blocks for the three ceremony redesigns. The claim title ("Ceremonies don't disappear. They absorb the new accountability.") as Playfair h2. Differentiate the three ceremonies by using Inter label text in `--accent` taupe as a small eyebrow above each Playfair card-headline.

**Slide 17 (Stat) — Cartesian: Moderate**
Coda tip: This is the urgency peak. The $110,000/month figure must dominate. Use custom `.hero-stat` at the largest scale available (clamp 4rem, 7vw, 6.5rem — larger than the standard custom class). The "20-person team" context sits as Inter subtitle below. The mitigation data (prompt caching 88% reduction, model tier routing 60–80% savings) can sit as two small stat clusters in Inter body-sm below a 1px taupe separator line.

**Slide 18 (List) — Cartesian: Moderate**
Coda tip: The four-level maturity ladder (Level 1–4) maps well to four agenda-row items. Use the agenda-list pattern with Playfair agenda-numeral for levels 1–4, Inter body for descriptions. The claim title ("Most teams are ungoverned. That's your opening.") as Playfair h2 above.

**Slide 19 (Process / Steps) — Cobalt Grid: Moderate**
Coda tip: Cobalt Grid has no native horizontal flow/steps pattern. Build the three-step structure using three equal-flex columns in a single row, each separated by a 1.5px vertical cobalt rule (or jade, in dark adaptation). Each column carries: DM Mono mono-tag for the time label ("THIS WEEK" / "THIS MONTH" / "THIS YEAR"), Newsreader row-headline for the step action, Hanken body for the specific tasks. A topbar above the grid carries the section framing headline and a mono lab-tag.

**Slide 19 (Process / Steps) — Cartesian: Moderate**
Coda tip: Author three `.card` instances in a flex row. Each card: Inter label (uppercase, `--accent` taupe) for the time horizon, Playfair h3 for the action header, Inter body-sm for the specific tasks. Use the `horizontal-accent` ink rule (20vw × 1px) above the three-card row as a strong structural separator from the slide headline above.

**Slide 20 (CTA) — Monochrome: Strong**
Coda tip: The slide--end pattern exists but is a generic close. Adapt it for the single-imperative format by placing the imperative ("Own the decisions agents can't make.") in Jost weight 200 at h1 scale (5vw), the supporting line in Jost weight 300 at lead scale (1.5vw) with muted graphite color, and any URL/next-step in JetBrains Mono label size. Suppress the chrome header; retain the chrome foot for the source metadata. The jade accent can be used on the supporting sentence to provide the one chromatic emphasis moment in the deck's close.

**Slide 2 / 10 (Statement) — Cartesian: Strong**
Coda tip: The slide-statement pattern includes a 5rem Playfair quote-mark glyph above the headline. For these slides, the claims are declarative statements ("The jobs question is settled. The structure question isn't." and "The roles that survived 2022 owned delivery. The roles that didn't, facilitated it."), not quotations. Suppress the quote-mark glyph and use Playfair h1 (clamp 2.5–4.5rem) for the full claim. This is the only adjustment needed — the centered layout and attribution line below are native.

---

## Recommendation

**Monochrome is the recommended template.**

The case rests on three factors:

1. **Coverage:** Monochrome is the only template that has native patterns for all ten slide types required in this deck. Cobalt Grid and Cartesian each require structural adaptation on 4–5 types, significantly increasing Coda's authoring burden.

2. **Register fit:** The archival/research-grade editorial register is the closest match to the PoV's tone — credible, measured, and willing to say what the audience already knows but hasn't named. The ultra-light Jost weight and em-dash bullets project rigorous analysis; the Lora italic serif provides the one moment of human-voice warmth the Statement slides require. Neither Cobalt Grid (provocative/magazine) nor Cartesian (warm/accessible) land on the specific "research-grade credibility" register the deck needs to hold analytically oriented IMs and DMs who are evaluating its claims, not just absorbing them.

3. **Audience trust:** An analytically oriented audience that survived a consolidation wave will be skeptical of deck aesthetics that feel performative. Monochrome is the least likely template in the library to trigger that response. It reads as written, not produced.

**If Adnan prefers higher visual impact** at the expense of authoring complexity, Cobalt Grid is the second choice — particularly because the vbig-numeral treatment on slides 7, 12, and 17 would be the most powerful stat display available. The tradeoff is explicit: four Comparison slides (3, 11, 13, 14) and the Timeline (9) require structural adaptation, and the cobalt-to-jade substitution weakens the template's defining authority.

**Cartesian is third** and recommended only if the audience profile is revised toward less analytically rigorous or more relationship-driven stakeholders — its warmth and accessibility are genuine strengths in a different context.
