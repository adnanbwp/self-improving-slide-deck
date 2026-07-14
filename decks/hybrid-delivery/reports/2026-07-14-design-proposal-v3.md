# Design Proposal v3 — hybrid-delivery v3.0.0

- **Date:** 2026-07-14
- **Author:** Iris (Image & Design Specialist)
- **For:** Coda Pass 2 (build), via Larry
- **Slide plan:** `decks/hybrid-delivery/reports/2026-07-14-slide-plan-v4.md` (Adnan-approved)
- **Template system:** `shared/templates/aha-agile/` — light theme, **locked** (shared/work deck; off-brand not requested)
- **Baseline build:** `decks/hybrid-delivery/versions/v2.1.1/canonical.html`
- **Budget source of truth:** `shared/templates/aha-agile/README.md` + `layouts.css` (measured, not remembered)

This deck stays on aha-agile. Step 3 is therefore layout mapping, not template selection. Every `t-*` choice below is checked against the layout's documented budget and the actual CSS geometry in `layouts.css`. Where a slide is tight or over budget, the Coda tip says what to tighten or split — never shrink fonts, never restyle `engine.css`, never unlock a layout.

---

## Section 1 — Field allocation & deck-arc rhythm

The brand rule: `f-orange` shouts, `f-paper` reads, `f-ink` breaks. If everything shouts, nothing does — so orange is rationed to the three highest-stakes whole-slide beats, ink is used exactly twice as structural punctuation, and every workhorse reads on paper. Compare slides split their field across the seam (one half shouts in orange, one reads in paper) — that split is the point of the type, so it does not count against the orange ration.

**Whole-slide `f-orange` (shout) — 3 slides:** 01 Title, 07 Pivot question, 23 CTA. These are the deck's spine anchors: the frame, the hinge, the ask. Nothing else on the main line shouts full-bleed.

**Whole-slide `f-ink` (break) — 2 slides:** 06 First-person trust beat (a deliberate tonal breath — the argument stops, a person speaks, then the pivot question fires), 25 Appendix divider (structural). Two ink breaks across 41 slides is correct restraint; a third would dilute the reset that slide 06 buys before the pivot.

**Split-field compares (orange half + paper half) — 7 slides:** 03, 08, 10, 11, 12, 13, 15. The orange half always carries the "punch" side of the seam (the IM's ownership / the cost), the paper half the "reads" side (adoption / signals / what agents generate). Slide 12's split is the crux — orange goes on the RIGHT (the decisions the IM owns), paper on the LEFT (the signals engineering reads).

**Everything else `f-paper` (read):** all evidence, cards, stat-grids, list, figure, team, and the entire appendix (26–41). The appendix is reference material; a uniform paper field keeps it calm and navigable.

Rhythm read end-to-end: orange frame (01) → paper evidence build (02–05) → ink breath (06) → orange pivot (07) → paper/orange argument core (08–22) → orange ask (23) → paper credits (24) → ink divider (25) → paper reference (26–41). Orange lands only where the audience must feel a beat change; the argument itself reads on paper so the shouts keep their force.

---

## Section 2 — Per-slide layout table

Legend for **Budget**: FITS = within documented budget · TIGHT = at the ceiling, screenshot-verify · FLAG = over budget, Coda tip is mandatory. Compare fields shown as `orange|paper`.

### Main line (01–24)

| # | Purpose (short) | Type | Layout class | Field | Budget | Coda tip |
|---|---|---|---|---|---|---|
| 01 | Frame the deck | Title | `t-title` | orange | FITS | Version badge → **v3.0.0**. h1 ≤3 lines — current headline is 2, fine. |
| 02 | Hook: the decoupling | Evidence | `t-evidence` | paper | **FITS-WITH-FALLBACK** | See Flag A. Decoupling claim rides the 2-sentence head; `.ctx` = exactly 2 lines (441-is-PR-review-time+caveat / reconciliation line); one `.src` line only. |
| 03 | Locate yourself | Comparison | `t-compare` | orange\|paper | FITS | mini-list ≤6/half, no head — well under. |
| 04 | The loop (agent=acts folded) | Figure | `t-figure` | paper | FITS | See Flag B. Head = chatbot→acts framing (first line, binding). Existing asset `assets/images/slide-09-agentic-loop.png`. |
| 05 | The strong middle | Cards | `t-cards` cols-3 | paper | FITS | See §3. 3 cards Frame/Collapse/Judge; METR 19% stays in notes+appx 29, not on a card. |
| 06 | First-person trust beat | Statement | `t-statement` | ink | FITS | ≤14 words claim; `.support` is ONE short line only (pitfall). If the story needs a paragraph it is not a statement — it doesn't; keep it terse. |
| 07 | Pivot question | Question | `t-question` | orange | FITS | ≤12 words. Current is ~13 — trim to fit one centered line at 92px. |
| 08 | Velocity decoupled | Comparison | `t-compare` has-head has-annot | orange\|paper | **FITS-WITH-FALLBACK** | See Flag A + §3. mini-list ≤4/half (has-head) — 2 each, fine. annot-line tightened to ≤2 lines; both reconciliations stay on face. |
| 09 | Advantage real & conditional | Stat grid | `t-stat-grid` cols-3 | paper | TIGHT | 4 items > clean 3. Render as 3 cards (+40%, 90%, one `.hot` pointer) and move the "real **and** conditional" statement to `.lead`, not a 4th card. |
| 10 | Generating vs governing | Comparison | `t-compare` has-annot | orange\|paper | FITS | 84/49 number lives at appx 31; keep this qualitative. mini-list ≤6/half. |
| 11 | The boundary | Comparison | `t-compare` has-annot | orange\|paper | FITS | Right half (cannot-decide) ~5 items ≤6 no-head — fits. |
| 12 | Sensors aren't decisions | Comparison | `t-compare` has-head has-annot | paper\|orange | **FLAG** | See §3. RIGHT half has 5 decisions > ≤4 (has-head). Merge to 4 (fold "stakeholder reporting contract" into the annot-line ownership warrant, or pair "review capacity"+"WIP caps"). |
| 13 | Centaur teams | Comparison | `t-compare` has-head has-annot | orange\|paper | FITS | mini-list ≤4/half — 4 each, at ceiling; keep each item one line. |
| 14 | HITL patterns | Cards | `t-cards` cols-3 | paper | FITS | 3 cards, `.d` one short line each. |
| 15 | The fork | Comparison | `t-compare` has-annot | orange\|paper | FITS | Each path is a mini-list ≤6 no-head. Prioritisation deliberately absent — do not add it. |
| 16 | Three capabilities | Cards | `t-cards` cols-3 | paper | FITS | 3 cards, clean. |
| 17 | The attention budget | Cards | `t-cards` cols-3 | paper | TIGHT | See §3. 3 struts → 3 cards. NEED card is dense (11h / 6.4 / 69%); show 58% as a derived `.note`. NO invented attention-budget number anywhere (Vera S6). |
| 18 | The token budget | Cards | `t-cards` cols-3 | paper | **FLAG** | See §3. 3 parts + 3 struts = 6 concepts > 3 cards. Cards = the 3 PARTS; fold the 3 struts into `.lead` + notes. Do NOT cite Scrum.org (src guard). No invented squad number. |
| 19 | Ceremony survives, metric doesn't | Cards | `t-cards` cols-2 dense | paper | TIGHT | 7 VERDICT pillars = the dense ceiling (≤7). This is the Appendix-D 7-card pattern. Each card: `.k`=pillar, `.t`=ritual (e.g. "DoD"), minimal `.d` — one line each or it busts. Velocity appears nowhere as a live metric. Pillar-C copy FIX is mandatory. |
| 20 | Failure modes | Cards | `t-cards` cols-3 | paper | FITS | 3 cards (Replit / Meta / context-leak). |
| 21 | Squad audit + measurement question | List | `t-list` | paper | FITS | ≤6 items — 5 audit Qs + 1 reframed = 6, at ceiling. If any item needs a `.sub`, cap the list at ≤4 with subs (pick which get subs) rather than adding a 7th. |
| 22 | The 12-month path | Cards | `t-cards` cols-3 | paper | FITS | 3 cards (quarter / year / success). |
| 23 | CTA | CTA | `t-cta` | orange | FITS | imperative ≤8 words. `.support` carries homework + invitation (2 moves) — keep to 2 mono lines; the pilot line is opt-in, not an assignment. |
| 24 | The team | Team | `t-team-avatars` | paper | FITS | The ONE slide where specialist names are legitimate. Row split per `shared/slide-types/team.md`. Inline avatars base64 for the portable build. |

### Appendix (25–41)

| # | Purpose (short) | Type | Layout class | Field | Budget | Coda tip |
|---|---|---|---|---|---|---|
| 25 | Divider | Divider | `t-divider` | ink | FITS | title ≤4 words. |
| 26 | Decoupling deep-dive | Stat grid | `t-stat-grid` cols-2/3 | paper | TIGHT | FORGE '26 + Faros reconciliation is number-dense. Use `.num.long` for >4-char figures (+59.1%, +242.7%); carry FORGE's 3-teams/13-month caveat as a `.note`, not a headline. |
| 27 | Jeffries / #NoEstimates lineage | Quote | `t-quote` | paper | FITS | Quote ≤30 words; `.by` = Ron Jeffries. If the pre-concession needs prose beyond the quote, use `t-content` instead — do not overstuff `.q`. |
| 28 | Malone in full | Stat grid | `t-stat-grid` cols-2/3 | paper | FITS | 106 / 90% / 10% as cards. **Must stay intact** — it is what slide 09 points to. |
| 29 | Strong-middle / METR detail | Content | `t-content` `.cols` | paper | FITS | Body ≤5 blocks; put METR's generalizability caveats in the `.aside` column. The 2026 follow-up is selection-biased per METR — say so. |
| 30 | Wide, not deep (83/55) | Comparison | `t-compare` | orange\|paper | FITS | Two numbers, one seam. |
| 31 | Governance gap (84/49) | Comparison | `t-compare` | orange\|paper | FITS | The on-slide number moved off main line 10 — lives here. |
| 32 | Bolt-on (<40%) | Evidence | `t-evidence` | paper | FITS | Single hero number, `.ctx` ≤2 lines. |
| 33 | Autonomy ladder (5 rungs) | List | `t-list` `.labels` | paper | FITS | 5 rungs ≤6; `.labels` widens `.n` for the rung names. |
| 34 | Chat vs agent | Figure | `t-figure` | paper | FITS | The 4C anatomy (Context/Connections/Capabilities/Cadence) — if no diagram asset exists, run as `t-cards` cols-2 dense instead of an empty `.fig`. |
| 35 | The five collisions | List | `t-list` | paper | FITS | 5 items ≤6. |
| 36 | Governance maturity ladder | Cards | `t-cards` cols-2 dense | paper | FITS | 4 rungs (Unseen→Observed→Controlled→Autonomous), mark Controlled `.hot` (the target). |
| 37 | Governance incidents — sources | Cards | `t-cards` cols-1 dense | paper | FITS | 3 rows (Replit / Meta / Gartner). cols-1 renders label-left rows — keep `.d` to 2 lines. |
| 38 | Wave 1 dissolution | Stat grid | `t-stat-grid` cols-2 | paper | FITS | Dormant Q&A backup — 49%→<5%. |
| 39 | Attention budget — full detail | Content | `t-content` `.cols` | paper | FITS | The WIP/ToC mechanism + Glean botsitting math in full; the 58% derivation is fine to show here (unlike main-line 17). |
| 40 | Token budget — full detail | Cards | `t-cards` cols-2 dense | paper | FITS | Rate card / breach / review contract / growth path = 4 cells. src guard: no Scrum.org. |
| 41 | Sources + credentials | Sources + Cards | `t-sources` **+** `t-cards` | paper | **FLAG** | See §6. ~12 citations already hit the `t-sources` ≤12 ceiling; credentials bust it. **Split into 41a (sources, `t-sources`) and 41b (credentials, `t-cards`).** Appendix absorbs the extra slide freely. |

---

## Section 3 — The new slides: type choices, slot allocation, one Coda tip each

### 04 · The loop (agent=acts folded) — `t-figure`, f-paper
- **Type rationale:** the argument is a diagram (the agentic loop). `t-figure` frames a diagram on a bone panel with a claim head above it — exactly the shape this slide needs, and the asset already exists.
- **Slots:** `.head` (38px, first element) = the chatbot→acts framing claim (binding guardrail — see Flag B). `.fig` > `<img src="assets/images/slide-09-agentic-loop.png">` fills the rest. Optional single in-flow `.lead` mono line between head and fig for the "loops until a gate you designed → that gate is the IM's" beat.
- **Coda tip:** the chatbot→acts line is the `.head` and must be the FIRST thing on the face. If you add the `.lead` beat line, add it inside `.pad`'s flex flow (NOT absolutely positioned) so `.fig` (flex:1) absorbs the height — keep head ≤2 lines at 38px so the figure doesn't get crushed.

### 05 · The strong middle — `t-cards` cols-3, f-paper
- **Type rationale:** the claim is a three-part division of labour (Frame / Collapse / Judge). Three cards render the shape directly; the cards ARE the visual (see §5 on why no separate figure).
- **Slots:** 3 cards. Card 1 `.k`=FRAME `.t`=Humans `.d`=the what/why (planning, intent). Card 2 `.k`=COLLAPSE `.t`=Agents `.d`=construction, compressed. Card 3 `.k`=JUDGE `.t`=Humans `.d`=what's good enough to ship. `.src` = METR line. Optionally `.hot` on card 3 (judgment is where the binding constraint moved).
- **Coda tip:** keep METR's 19%-slower finding OFF the cards — it goes in speaker notes and appendix 29. On-slide, the cards carry only the division-of-labour claim, or the "is 19% a constant?" objection lands on the wrong slide.

### 08 · Velocity decoupled — `t-compare` has-head has-annot, orange\|paper
- **Type rationale:** the slide IS a two-column decoupling (output up / value flat) with a cross-cutting reconciliation — the seam-head states the claim, the two halves carry the split, the annot-line carries the reconciliation. That is precisely `has-head` + `has-annot`.
- **Slots:** seam-head = "Output and value came apart. Velocity now measures the wrong one." LEFT half f-orange, `.lab`="Individual output — up", `.mini-list` = PRs/dev +98% (2025), tasks/dev +21%(2025)/+33.7%(2026). RIGHT half f-paper, `.lab`="Squad delivery — flat or worse", `.mini-list` = incidents/PR +242.7%, bugs/dev +54%. `.annot-line` = both reconciliations (see Flag A for the fit).
- **Coda tip:** render the stats as `.mini-list` rows, NOT the 110px `.val` display — two big `.val` numbers per side would blow the has-head+has-annot vertical envelope (halves are squeezed to ~340px between the 210px top pad and 170px bottom pad). Cite the Faros year on the figures (D-3).

### 12 · Sensors aren't decisions — `t-compare` has-head has-annot, paper\|orange
- **Type rationale:** this slide carries the whole spine's weight and its argument is a clean cut — signals engineering reads (LEFT) vs decisions the IM owns (RIGHT). The compare seam IS the argument; the annot-line states the warrant. Do not soften the warrant into notes.
- **Slots:** seam-head = "Agents didn't retire your job. They moved it from the metric to the decision the metric forces." LEFT f-paper `.lab`="Engineering reads the signals" `.mini-list`= incidents/PR, code churn, durability, review latency (4 items). RIGHT f-orange `.lab`="You own the decisions the signals force" `.mini-list`= what counts as done · planned review capacity · WIP caps · what the sprint commits to · stakeholder reporting contract (**5 items — over budget**). `.annot-line` = the ownership warrant.
- **Coda tip (mandatory — this is the FLAG):** `has-head` caps mini-list at **≤4 per half**; the RIGHT half has 5. Fold one out — cleanest is to move "stakeholder reporting contract" into the `.annot-line` (the warrant already speaks to who owns the outcome), leaving exactly 4 decisions on the right. Do NOT shrink the list font.

### 17 · The attention budget — `t-cards` cols-3, f-paper (primary framework)
- **Type rationale:** three struts (need / mechanism / synthesis) map one-to-one to three cards and parallel slide 18's rhythm, reinforcing the companion-frameworks pairing typographically.
- **Slots:** Card 1 `.k`=THE NEED IS REAL `.d`=~11 hrs/wk saved, ~6.4 back to supervising, 69% ship unverified; `.note`=~58% of the saving erodes (derived). Card 2 `.k`=THE MECHANISM IS PROVEN `.d`=cap WIP to the binding constraint (Reinertsen/ToC, 15+ yrs); only the constraint moved. Card 3 `.k`=THE PROPOSAL `.d`=name human-review capacity as the squad's budgeted WIP limit — Adnan's proposal, open territory. `.hot` on card 3 (it is the synthesis being claimed).
- **Coda tip:** the NEED card is the dense one — show the two raw Glean numbers (11 and 6.4) and let 58% be a visible derived `.note`, never a headline stat. **No invented attention-budget figure anywhere on the slide** (design note / Vera S6); if asked "is it 3 hrs a day?", that answer is a pilot output, not a slide number.

### 18 · The token budget — `t-cards` cols-3, f-paper (subordinate framework)
- **Type rationale:** subordinate to 17, so it must not out-weigh it — three cards, same cols-3 rhythm, visually junior by staying calm (no `.hot`). The content ships as the three PARTS (the concrete instrument), with the three struts compressed into support.
- **Slots:** Card 1 `.k`=RATE CARD `.d`=$/sprint per role, squad-tuned; budget=Σ(headcount×rate). Card 2 `.k`=BREACH = A DECISION `.d`=top-up / descope / downgrade — logged, never an auto-halt. Card 3 `.k`=REPORTS AT SPRINT REVIEW `.d`=burn vs budget next to judged outcomes, never raw output. `.lead` = the three struts in one line (grounded need · 15-yr mechanism · my synthesis). `.src` = need+mechanism line.
- **Coda tip (this is the FLAG):** do NOT try to put both the 3 parts AND the 3 struts on cards — 6 concepts in 3 cells overflows. Parts on the cards, struts in the `.lead`. The $150–250/mo range may appear only as a labeled `.note` with its source. **Do not cite Scrum.org as token-budget precedent** (src guard — verification gate confirmed no such recommendation). No invented squad budget number.

---

## Section 4 — The two escalation flags: verdicts

### Flag A — slides 02 & 08 must carry multiple reconciliation lines on the slide face

**Measured geometry.** `t-evidence` (`.ctx max-width:760px; font-size:22px`) documents `ctx ≤2 lines`. The v2.1.1 screenshot ran 4 ctx lines + 4 wrapped src lines — but that was v2.1.1's copy (four stacked source citations + a four-line context). **Plan v4 is leaner, not heavier:** one `.src` line and a disciplined 2-line ctx. `t-compare` with `has-head`+`has-annot` squeezes each half to ~340px (720 − 210 top pad − 170 bottom pad) and gives the `.annot-line` a ~2-line envelope at bottom:100px before it collides with the 170px half padding.

**Slide 02 — VERDICT: FITS-WITH-FALLBACK.** The decoupling claim rides the 2-sentence `.head` (that is exactly what plan v4 specifies — it is the reframed headline). That frees `.ctx` to carry exactly two lines: line 1 merges the 441 anchor + caveat ("441% is PR review time — one triangulating signal, not the whole story"), line 2 is the mandatory reconciliation ("Velocity didn't break today — agents just made gaming it free"). Two lines = within the ≤2 budget. **Named fallback (plan's own):** if a build screenshot shows those two lines wrapping to three, promote the reconciliation line to the headline's second sentence and drop it from ctx — nothing goes to notes. No font shrink. **Not escalated to Adnan** — it fits with the composition move above.

**Slide 08 — VERDICT: FITS-WITH-FALLBACK.** Halves carry 2 mini-list items each (has-head cap is ≤4) — comfortable. The load-bearing risk is the `.annot-line`, which must hold BOTH reconciliations (~45 words as written = ~3 lines, which collides with the 170px bottom pad). **Primary fallback:** tighten the annot copy to ≤2 lines — e.g. "Different levels, same story: METR's 2025 RCT put experienced devs 19% slower on familiar code; velocity was already soft (Jeffries, 2012) — agents just made gaming it free." (~35 words, ~2 lines at 16.5px full width). **Secondary fallback (plan's own):** if 2 lines still won't hold, split — the METR level-reconciliation stays in `.annot-line`; the "gaming free / Jeffries" line moves up as a deck-scoped sub-line under the seam-head (scope it `.t-compare.has-head .subhead{position:absolute;top:~150px;...}`, confirm it clears the halves — this is a deck-`<style>` override, permitted, not a `layouts.css` edit). Both reconciliations stay on the face either way. **Not escalated to Adnan.**

**Escalation trigger, stated plainly:** the moment a build screenshot shows either slide's mandatory lines overflowing *after* the named fallbacks are applied, that goes back to Larry → Adnan as a copy-density decision — it is NOT solved by shrinking a font or unlocking the layout. Both flags currently resolve without that.

### Flag B — Aria's binding guardrail: chatbot→acts line must be FIRST on the folded loop slide (04)

**VERDICT: CONFIRMED — the native `t-figure` layout carries it, no variant needed.** `.t-figure .pad` is `display:flex; flex-direction:column; padding-top:110px`, and `.head` is its first child — so the head is structurally the first thing on the face, above the `.fig`. Put the chatbot→acts framing in `.head` (the fold's lead) and it satisfies the guardrail natively. `.fig` is `flex:1`, so it absorbs whatever vertical space the head (and an optional one-line in-flow `.lead`) leaves — head 2 lines (~80px) + optional lead (~30px) + gaps (~40px) = ~150px below the 110px top pad, leaving ~460px for the diagram before the bottom chrome. No crowding. **Coda tip:** keep the head to ≤2 lines at 38px, and if you add the loop/gate beat as a `.lead`, keep it in the flex flow (not absolute) so the figure resizes cleanly. Do NOT split the framing across head and a floating caption — the guardrail wants it first and whole, and the head slot delivers exactly that.

---

## Section 5 — Image brief needs

**Proposed new images: ZERO.**

Argument-first is the rule: an image earns its place only when it makes a specific claim more credible or more legible than the layout already does. On this deck every new slide's argument is carried by a *structural* layout — the compare seam (08, 12) IS the decoupling/sensors-vs-decisions visual; the three cards (05, 17, 18) ARE the three-part shape. Generating art to sit alongside them would be decoration, and this is a duotone editorial system whose argument slides are typographic by design. So:

- **Slide 05 (strong-middle / human-sandwich shape):** the Frame→Collapse→Judge cards already render the shape. A separate figure would compete with them. **Not briefed.** *One conditional for Adnan:* if he wants the hourglass/"pinched middle" shape emphasized as a diagram, that is a type-swap (cards → `t-figure`) — a Larry/Adnan call, not mine — and only THEN would it warrant exactly one image brief. I am not pre-briefing it because the approved plan chose cards.
- **Two-budgets pairing (17 + 18):** the companion relationship is narrative (17 then 18) and each slide's claim is its three struts, carried in cards. A pairing diagram is not load-bearing for either claim. **Not briefed** (decoration).
- **Slide 04 (loop):** the only figure the main line needs, and its asset already exists at `assets/images/slide-09-agentic-loop.png`. The fold changes the head text, not the diagram. **No re-brief needed.**
- **Appendix 34 (chat vs agent):** flagged in the table as needing either an existing 4C diagram asset or a fallback to `t-cards` — this is an asset-availability check for Coda, not a new generative brief.

Net: no `image-brief-vN.md` is required for this build. If Adnan elects the slide-05 hourglass swap, route back to me for a single-entry brief.

---

## Section 6 — Slide-count & budget sanity check

**Counts (vs plan v4):**
- **Main line: 24 slides** = 21 body + Title (01) + CTA (23) + Credits (24). At Larry's ≤21-body ceiling, not over. ✓ (The +1/−1 delta from Aria's math — Open Item 1 — is a narrative/compression question for Aria/Larry, not a layout question; the layouts hold at 24.)
- **Appendix: 17 slides (25–41)** — matches plan, before the 41-split below. ✓

**Slides at or over their type budget (Coda tips are mandatory on these):**
1. **12 — FLAG:** RIGHT half 5 mini-list items > ≤4 (has-head). Fold to 4 (§3).
2. **18 — FLAG:** 6 concepts (3 parts + 3 struts) > 3 cards. Parts on cards, struts in `.lead` (§3).
3. **41 — FLAG:** ~12 citations hit the `t-sources` ≤12 ceiling; adding the credential landscape busts it. **Split into 41a (sources) + 41b (credentials).** Plan already anticipated this; the appendix absorbs the extra slide, taking the appendix to 18.
4. **09 — TIGHT:** 4 stat items > clean 3. Move "real **and** conditional" to `.lead`; keep 3 cards (§3).
5. **19 — TIGHT:** 7 VERDICT pillars = the `cols-2 dense` ceiling (≤7) — the exact Appendix-D 7-card pattern from v2.1.1. Each card must be one line (`.k`=pillar, `.t`=ritual, minimal `.d`); if any pillar→ritual pairing wants two lines, it busts and one pillar must fold or the slide splits.
6. **21 — TIGHT:** 6 list items = the ≤6 ceiling; if any needs a `.sub`, the cap drops to ≤4-with-subs — pick which get subs rather than adding a 7th item.
7. **26 — TIGHT:** number-dense; use `.num.long` for >4-char figures and carry FORGE's caveat as a `.note`.

Everything else fits its type's documented budget as planned.

---

## Handoff summary (for Larry)

- **New-slide type choices (one line each):**
  - 04 loop-fold → `t-figure` f-paper (existing asset; head carries chatbot→acts, first line).
  - 05 strong-middle → `t-cards` cols-3 f-paper (Frame/Collapse/Judge; METR off-card).
  - 08 velocity-decoupled → `t-compare` has-head+has-annot orange|paper (mini-lists, not `.val`).
  - 12 sensors-vs-decisions → `t-compare` has-head+has-annot paper|orange (**RIGHT half over budget — fold to 4**).
  - 17 attention budget → `t-cards` cols-3 f-paper (3 struts; no invented number; 58% as derived note).
  - 18 token budget → `t-cards` cols-3 f-paper (**parts on cards, struts in lead**; no Scrum.org; no invented number).
- **Flag A (02 & 08 face-density):** both **FITS-WITH-FALLBACK** — named fallbacks keep every mandatory reconciliation on the slide face; nothing drops to notes, no font shrink. Not escalated to Adnan (trigger to escalate = a build screenshot overflowing *after* the fallbacks).
- **Flag B (loop first-line guardrail):** **CONFIRMED** — native `t-figure` carries the chatbot→acts line first (head is the first flex child; fig absorbs the rest). No new layout variant.
- **New images proposed: 0.** Every new slide's argument is carried by its layout; generative art would be decoration. One conditional (slide-05 hourglass) available only if Adnan elects a cards→figure swap.
- **Slide-count:** main 24 (21 body, at ceiling); appendix 17 → **18 after the mandatory 41 split**. Budget FLAGs on 12, 18, 41; TIGHT on 09, 19, 21, 26.
- **File:** `/home/aali/projects/self-improving-slide-deck/decks/hybrid-delivery/reports/2026-07-14-design-proposal-v3.md`
