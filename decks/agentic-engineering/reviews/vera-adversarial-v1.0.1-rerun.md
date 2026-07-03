# Adversarial Re-Run — "Both Axes" Agentic Engineering base deck, v1.0.0 (rebuilt)

**Reviewer:** Vera (Adversarial Critic)
**Target:** `decks/agentic-engineering/versions/v1.0.0/canonical.html` (21 slides, updated in place)
**Screenshots:** `screenshots/agentic-engineering/slide-01…21.png` (re-captured)
**Prior review:** `decks/agentic-engineering/reviews/vera-adversarial-v1.0.0.md` (6/10 FAIL, two blockers)
**References:** research brief `decks/agentic-engineering/research/2026-07-03-research-brief-v1.md`
**Date:** 2026-07-03
**New adversarial score:** 8 / 10 — **PASS** (both blockers cleared; no new blocker; no regression)

---

## How this re-run was done

I re-read the prior review, then checked each flagged item against the current HTML **and** the re-captured screenshot — no item taken on trust. For the one fix that swapped in a *new* statistic (97%), I went back to the research brief and verified the substitution against the primary source rather than accepting "IBM primaries only" at face value. That check is where a lazy re-run would have missed a second mis-cite; it did not, but it was the right place to look.

---

## BLOCKER verification

### B1 — Slide 10 provenance reversal → **RESOLVED**
- **Title now reads:** "Three of VERDICT's seven pillars already shipped in Google's SAIF." Direction is correct — SAIF is the prior artifact; the word "already" and "shipped in Google's SAIF" both place authorship with Google, earlier.
- **Body:** left half labelled "Google SAIF 2.0 · agent principles (6 domains + 3)"; right half "VERDICT · our synthesis (7 pillars)" with "maps to →" arrows running SAIF-principle → VERDICT-pillar. Correct direction, and honest that SAIF is 6+3, not 7.
- **Annotation:** "VERDICT is a 2026 mnemonic; three of its seven pillars were already public in Google's 2025 SAIF — a different author, a different purpose. Our mapping, not 'Google's seven pillars.'"
- **Speaker notes:** now say explicitly "…already public in Google's earlier guidance, **not the other way round**."
- **Residual-reversal sweep:** the old phrasings ("Google independently arrived at a subset of VERDICT" / "SAIF reproduces three of VERDICT's pillars") appear **nowhere** in the deck body or notes. Note: the *research brief's* own executive summary and Finding 1b still carry the loose "Google independently arrived at a subset of VERDICT" phrasing — but the deck is now **more correct than its own brief** on this point. No deck-side residue. Cleared.

### B2 — Slide 15/21 stat mis-attribution → **RESOLVED (and the swap verified clean)**
- The vendor-sourced **43% "cannot produce an AI inventory" is gone** from both slide 15 and slide 21.
- Slide 15 foot now carries three figures, all attributed to IBM: **63% no AI governance policy · 97% of breached-AI orgs lacked access controls · shadow-AI breaches ~$670K more.**
- **The new 97% was NOT in my prior verification scope** (my B2 named only 63% and +$670K as genuine IBM primaries), so I verified it independently. Research brief **Finding 3a** lists all three under IBM Cost of a Data Breach 2025, and the cited IBM newsroom URL is literally `…13-of-organizations-reported-breaches…97-of-which-reported-lacking-proper-ai-access-controls`. The 97% is a genuine IBM primary — the fix dropped one vendor stat and replaced it with a real primary, not a second mis-cite.
- **Scoping check:** the brief's 97% is "97% *of those* [the 13% that reported AI breaches]." The slide says "97% of **breached-AI orgs**" — a correct rendering of that scope, not an inflated "97% of all orgs." No overclaim.
- Slides 15 and 21 now agree (source 07 lists the same three, no 43%). Cleared.

**Both blockers cleared. The FAIL trigger is removed.**

---

## SHOULD-FIX (in-scope this round) verification

### S1 — Honesty label applied selectively → **RESOLVED**
- Slide 6 now carries a synthnote: "Our synthesis: the day→pillar overlays are the deck's own reading of where build work seeds governance, not a published taxonomy." It reads as a general statement about *the* overlays (not just slide 6's), which is exactly the "single global note" my required resolution accepted.
- Slide 21 confidence line extended: "The day→pillar overlays **and the SAIF crosswalk** are our synthesis, not a published taxonomy."
- The honesty rule is now even: the strong (SAIF) mapping and the six weaker (day→pillar) overlays are both flagged. A pedant could note slides 8/9/11/12 carry unflagged overlays in isolation, but the deck is sequential and the slide-6 + slide-21 flags govern globally — which my own bar explicitly permitted. Cleared.

### S4 — No cost/proportionality model for governance → **RESOLVED**
- Slide 5: "more governed is not more better either… a weekend prototype stays vibe-coded **and ungoverned**; state-changing or money-moving work earns the full climb. **Governance has a real cost**, so spend it where the blast radius is."
- Slide 17 botnote: "**≥L3 is the floor only for state-changing, money-moving, or irreversible agents; read-only or low-stakes deployed work can be production-ready at L2. Governance has a cost — match it to the stakes, both ways.**"
- Slide 17 grid now labels the sub-target cells ("ships lower-stakes work" at L3×Structured, "seen and tested" at L2×Structured), giving the reader an actual decision surface.
- This answers the "when NOT to climb the governance ladder" objection directly: a stakes rule (≥L3 only for irreversible/money-moving/state-changing; L2 fine for read-only) plus an explicit statement that governance costs. *Residual (Low):* cost is asserted, not itemised (no line on approval-gate latency, HITL bottleneck, registry-maintenance burden). Acceptable at this level — the core objection is answered. Cleared.

### Slide 13 "runtime" sharpening → **RESOLVED**
- Now: "A pre-deployment review checks the plan once, **at the door**. The agent is already running the plan — so the controls have to be **enforced continuously while it runs**, not reviewed once before it ships." Door-check vs continuous-enforcement contrast is explicit. Cleared.

### Slide 11 overlay relabel → **RESOLVED**
- Overlay is now "Governs **V · R**" (was "Governs all 7"). Renders correctly on screenshot.
- Side benefit worth recording: with slide 11 corrected to V·R, the union of all day-overlays (6: V·E·R, 8: V·I·C, 9: E·D·C, 11: V·R, 12: I·V·T) now spans **all seven pillars** — the seven read more as a minimal spanning set than a cherry-pick, which quietly softens the old S2 attack even though S2 was not this round's target.

---

## Regression + new-issue sweep

- **Visual/overflow:** slides 5, 6, 10, 11, 13, 15, 17, 21 all re-checked against screenshots. The added slide-6 synthnote, the longer slide-17 botnote, and the sharpened slide-13 support all render inside the frame with no overflow, clipping, or grid breakage. No visual regression.
- **No new blocker introduced.** The one fix that carried real risk (swapping 43%→97%) was verified to a primary source and is clean.

### NEW — N-new (Low) · Slide 17 headline now slightly over-claims against its own footnote
The S4 fix introduced a mild internal tension: the headline still says "**Production-ready is one cell**: agentic build × Controlled governance," while the new footnote correctly says "read-only or low-stakes deployed work **can be production-ready at L2**," and the grid labels a second cell "ships lower-stakes work." A motivated reader can point at the same slide and say "you told me production-ready is exactly one cell, then named two more." It reads as "production-ready *for the hard case* is one cell," and the footnote is the honest qualifier — so it survives, but the absolute "one cell" is now looser than the deck's own text. **Low.** Optional tightening (e.g. "the production-ready target for high-stakes work is one cell"); not a ship-blocker.

---

## Standing attacks NOT in this round's scope (carried forward, still survivable)

These were Significant in v1.0.0, were not targeted by this fix round, and still stand — they cap the ceiling but none is a blocker:

- **S2 (seven-fold cut vs substance)** — softened by the overlay-union now spanning all 7 and by the synthesis flags, but slide 10 still showcases the flagship external source (SAIF) covering only 3 of 7. Survivable.
- **S3 (VERDICT vs just adopting the four real standards)** — softened by slide 21's "single-source *name* for a multi-source *consensus*… our synthesis," which positions VERDICT as a memorable synthesis, but the value-add over the four standards is still never stated outright. Survivable.
- **S5 (EXPOSE-theatre)** — partially mitigated (slide 18 now carries "named owner" and "last-seen"), but "the one nobody can argue against" still overclaims and there's no review-cadence guard against a stale registry. Survivable.
- **S6 (concreteness under-delivers for the builder audience)** — unchanged: still exactly one concrete artifact (slide-7 AGENTS.md); no eval/MCP/policy snippet added. Survivable **only** if this is scoped as the frame deck, not builder-actionable on its own.
- **Nits N1–N8** — unchanged; notably N5 persists (slide 11 lead still says an eval is "**proof**" while the IC card two lines down correctly says "validation evidence"). All Low.

---

## Adversarial score: 8 / 10 — PASS

**Rationale.** Both blockers are genuinely cleared, not papered over: the slide-10 provenance now runs the correct direction in title, body, annotation and notes with no residual reversal, and the slide-15 stat swap was verified to a primary source (97% is a real IBM Finding-3a number, correctly scoped) rather than trading one mis-cite for another. The two in-scope Significants (S1 honesty-evenness, S4 governance proportionality) are fully resolved, and the two sharpening asks (slide 11 relabel, slide 13 runtime) landed. No regression; the only new issue is a Low headline/footnote tension on slide 17. The score rises from 6 to 8 — my prior review named an 8+ ceiling once the blockers and the honesty/proportionality cluster were addressed, and that is where this lands. It does not reach 9 because a coherent set of survivable Significants remains untouched (S3 VERDICT-vs-standards value-add never stated, S6 one-artifact concreteness for a stated builder audience, S5 EXPOSE-theatre overclaim, S2 seven-fold cut) — real attacks the deck now *survives* rather than *answers*. Ship-ready under adversarial fire: **PASS**.

**New Critical / Significant / Low counts (this deck as it stands):**
- **Critical (blockers): 0** — both prior blockers cleared.
- **Significant: 4 carried-forward, all survivable** (S2, S3, S5, S6) — none blocks ship; each is a next-version target.
- **Low: 9** (N1–N8 unchanged + one new slide-17 headline/footnote tension).

**Remaining must-fix to block ship: none.** The four carried-forward Significants and the Lows are recommended for the next version, not gates on this one.

**Score set at submission. Not negotiable post-handoff — the deck team responds, Vera re-runs on the next version.**
