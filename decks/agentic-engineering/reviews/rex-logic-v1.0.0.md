# Rex — Logic Audit · Agentic Engineering base deck `v1.0.0`

- **Target:** `decks/agentic-engineering/versions/v1.0.0/canonical.html` (21 slides)
- **Reference:** design spec `docs/superpowers/specs/2026-07-03-agentic-engineering-base-deck-design.md`; research brief `decks/agentic-engineering/research/2026-07-03-research-brief-v1.md`
- **Auditor:** Rex (Logic Auditor). Scope: argument structure only — no fact-check, no persuasion score, no content rewrite.
- **Date:** 2026-07-03

---

## 1. Reconstructed argument map

**Conclusion (slide 20):** "The build dial earns you a great output; being able to see it, stop it, and own it is what earns you a deployment. Climb both axes."

Premise chain:

1. (2) The build dial (vibe → structured → agentic) is real: it moves verification out of your head into artifacts → earns a better **output**.
2. (3, the turn) The dial answers only *"is the output verified before ship?"* It never measures *"while it runs, can we see / stop / own it?"* → passing every test ≠ safe to deploy.
3. (4) Therefore two axes, not one: **build** (how it's built) × **governance** (how it's governed). One corner — agentic × Unseen — is a silent time-bomb. Knight Capital = structural analogy for speed × no runtime control.
4. (5) Set the dial **per task** (build-axis stakes guard); read each day through IC / Team / Org.
5. (6–12) Each of 5 build-axis days maps to VERDICT pillars + a phase (EXPOSE/BIND/ENFORCE), filling one map cell.
6. (10) Google SAIF 2.0 independently reproduces a subset of VERDICT → convergence, not one wiki's opinion.
7. (13) Runtime, not pre-deployment review, is the only place left to govern a running agent.
8. (14) VERDICT = 7 questions you must answer while it runs; multi-source convergence; frontier gap = multi-agent risk.
9. (15) Governance is a ladder L1–L4; most orgs at L1; L3 = production-ready.
10. (16) The climb is sequential: EXPOSE → BIND → ENFORCE → SELF-GOVERN.
11. (17) Payoff: map filled; production-ready = agentic × L3 (task-dependent botnote).
12. (18) CTA: EXPOSE first — valid at every altitude. (19) Worked example: refund agent, agentic × L3. (20) Close. (21) Sources & confidence.

The named load-bearing spine — *build-verify ⊥ runtime-govern; production-ready = agentic × L3; trap = agentic × Unseen* — is present, cited, and structurally carried by the two recurring motifs (readiness map + 3-lens matrix). The four Pax red-flags (slide-10 relabel, task-dependency guard, multi-agent frontier caveat, Knight-as-analogy) are all visibly addressed on-slide. This is a strong argument. The findings below are what stands between it and *airtight*.

---

## 2. Toulmin decomposition — load-bearing claims

**Claim A — "Build earns an output; deployment needs a second, orthogonal governance axis."**
Data: verification→artifacts (2); every framework separates "verified" from "controllable at runtime" (brief T1/T5). Warrant: the two dimensions are *independent* — you can be high on one and zero on the other. Backing: the filled map (17) realizes all nine cells. Qualifier: build axis is task-dependent. **Weakness:** the deck's own overlays (6–12) and slide 7 argue the axes are *coupled* (build work seeds / *is* governance) — this undercuts the orthogonality warrant it relies on. → Finding **S1**.

**Claim B — "Production-ready = agentic build × L3 governance."**
Data: L3 = you can stop it (15); refund example (19). Warrant: deployed work must be stoppable/observable. Qualifier applied: build axis flexes (structured × L3 for lower stakes). **Weakness:** the *L3 floor itself* is held universal and never warranted, while the map's own "governed toy (overkill)" cell says L3 is sometimes too much. → Finding **S2**.

**Claim C — "The only place left to govern an agent is while it runs."** (13)
Data: agents outrun review, ignore the org chart, don't ask permission. Warrant: controls that only act *before* ship can't touch a running agent. **Weakness:** conflates "configured pre-ship" (harness, least-privilege, spend caps — all set on slide 7) with "reviewed once." Several VERDICT pillars are set pre-runtime. → Finding **S3**.

**Claim D — "VERDICT is a single-source *name* for a multi-source *consensus*."**
Data: SAIF crosswalk (10), 4-body footnote (14), confidence flag (21). Warrant: independent bodies converging corroborates the substance. Backing: brief T1. **Handled well** — this is the deck's strongest honesty move. Residual nit only (**N1**).

**Claim E — "Each build day seeds specific VERDICT pillars, filling one cell."** (6–12)
Warrant: build-axis activities produce governance surfaces. **Weaknesses:** asserted as fact, not flagged as synthesis the way slide 10 is (**S5**); Day 4 "governs all 7" overclaims (**S4**); Day 5 "T" unsupported + phase-label mismatch (**N2**); Day 1 pillar-set inconsistent with its own artifact (**N3**). This claim is also the coupling half of **S1**.

---

## 3. Gap register (ranked)

### BLOCKER (Fatal) — none

No claim's failure collapses the conclusion. The two-axis thesis is independently corroborated and structurally sound. Reported honestly: there is no Fatal gap.

### SHOULD-FIX (Significant)

**S1 — Orthogonality vs. coupling: the deck argues both. [slides 3, 7, 12, 13, 20 vs 6–12] — TOP FINDING**
The hook and close assert the axes are **independent**: the build dial earns "only an output" (20), "you passed every test, nobody's watching" (3), "you climbed the dial completely — and still only have an output" (12 notes), "pre-deployment governs a plan; the only place left is while it runs" (13). But the overlays assert the axes are **coupled**: Day 1 "Governs V·E·R," Day 4 "Governs all 7," and slide 7's title flatly says *"The harness is a file you can read, and it is already governance."* If doing the 5 build days seeds V·E·R → V·I·C → E·D·C → all-7 → I·V·T, the reader has *governed every pillar just by climbing the build axis* — which contradicts "climbed the dial, still only an output." A sharp reader hits slide 7 ("already governance"), then slide 20 ("earns you *only* an output") and sees the collision.
*Minimal fix:* one explicit line (best on 5 or 7) distinguishing **substrate from maturity** — the build days give you the *fields/surfaces* where governance lives (a config with an `approval_gate:` line), but your position on the L1→L3 *ladder* (actually seeing/stopping/owning) is the separate axis Act 2 measures. Populating the config ≠ climbing the ladder. With that line, overlays and hook are consistent; without it, orthogonality (a named load-bearing claim) is self-undercut.

**S2 — The L3 production-ready floor is asserted, not warranted, and flexes only on one axis. [5, 15, 17, 19]**
The deck rigorously guards the *build* axis as task-dependent ("more agentic is not more better," weekend prototype stays vibe). It does **not** apply the same logic to the governance axis: L3 is held as the universal production-ready floor for all deployed work (17: "lower-stakes = structured × **L3**"; 15: "L3… This is production-ready"). Yet slide 17's own cell calls vibe × L3 a "governed toy (**overkill**)" — conceding L3 can be excessive for low stakes. So governance-to-stakes matching is admitted for toys but silently forbidden for low-stakes *deployed* work: why must a read-only, no-side-effect deployed agent be L3 (kill-switch + approval) rather than L2? The builder audience will ask exactly this.
*Minimal fix:* one guard line stating the warrant — e.g., "≥L3 is the floor for any agent that can change state or move money; genuinely read-only/no-side-effect deployed work can be production-ready at L2" — or explicitly justify why deployment ⇒ L3 regardless of stakes. Right now the strong claim rides on an unstated premise.

**S3 — "Runtime" is overloaded; the "only while it runs" dichotomy overshoots. [13, 14]**
Slide 13: "Pre-deployment review governs a plan… the only place left to govern it is while it runs." But Identity (named owner), Validation (least-privilege permission ceiling), and Cost (spend caps) are all **set before the agent runs** — slide 7 shows them as static harness fields. They are runtime-*enforced*, not runtime-*decided*. Calling all seven "questions you must answer *while it runs*" (14) mislabels the pre-set pillars. The accurate distinction the deck wants is **runtime-enforced-continuously vs. reviewed-once-before-ship**, not "governance happens only at runtime" — otherwise slide 13 contradicts Day 1's pre-deployment harness.
*Minimal fix:* sharpen slide 13 to "reviewed once at the door vs. *enforced continuously while it runs*"; on 14, drop or qualify "while it runs" for I/V/C (they are set up front, enforced throughout).

**S4 — Day 4 overlay "Governs all 7" overclaims relative to what the slide shows. [11]**
The slide substantiates exactly two pillars: evals = Validation, intent-drift = Runtime control. "Governs **all 7**" is asserted, not shown, and it quietly breaks the day→pillar structure the deck spent slides 6–9 building (if one day governs all seven, why did the others get subsets?).
*Minimal fix:* scope the overlay to the pillars the slide actually demonstrates (V + R, plus T for drift-transparency if desired), or relabel to "touches all 7 because security is cross-cutting" and say so — don't imply Day 4 alone achieves full governance.

**S5 — The day→pillar overlays are presented as fact; slide 10 is scrupulously flagged as "our mapping." Asymmetric honesty. [6, 8, 9, 11, 12]**
Slide 10 correctly labels its SAIF↔VERDICT crosswalk "our mapping, not 'Google's seven pillars.'" The day→VERDICT overlays (V·E·R, V·I·C, E·D·C, all-7, I·V·T) are the *same kind of authored synthesis* but are stated as bare fact ("Governs V·E·R"). The deck's own honesty rule should apply evenly.
*Minimal fix:* one framing beat (on 5 or 6) that the day→pillar overlays are the deck's synthesis/reading, not a published taxonomy — the same epistemic flag slide 10 already carries.

### NIT (Minor)

**N1 — Slide 10 title personifies the later synthesis. [10]**
"Google independently arrived at a subset of **VERDICT**" — Google arrived at three *controls*; the deck maps them onto VERDICT, which postdates SAIF (2026-05-24 vs 2025). The honest annotation already says "our mapping," but the title re-imports the overclaim, and "convergence" slightly oversells *mutual* independence (VERDICT could have drawn on SAIF). Fix: "Google independently arrived at three controls that match a subset of VERDICT." Corroboration direction (SAIF → VERDICT substance) is valid regardless.

**N2 — Day 5 overlay: T unsupported + phase mismatch. [12]**
Slide derives only I and V (zero-trust = I+V); T (Transparency) in "I·V·T" has no on-slide support. Phase label "BIND→ENFORCE" also disagrees with spec §6 ("ENFORCE→SELF-GOVERN"). Fix: drop T or add its one-line basis; reconcile the phase label with §6.

**N3 — Day 1 overlay omits Identity, which its own artifact foregrounds. [6 vs 7]**
Overlay says "V·E·R"; slide 7's artifact labels `owner: … (Identity)` as the very first field. The pillar set and the exemplar disagree (I·V·E·R shown, V·E·R claimed). Fix: align the set (I·V·E·R), or note owner is introduced Day 1, formalized as I later.

**N4 — Slide 15 "most orgs are L1" outruns its cited data. [15]**
The visibility claim ("you don't know it runs" = L1) is carried by "~43% cannot produce an AI inventory" (a minority) and "63% no governance policy" (about *policy*, not *visibility*). Neither cleanly supports the quantifier "**most**… live at L1." Rex does not check the numbers' accuracy — only that, as cited, they don't reach "most" on the visibility construct. Fix: soften to "a large share / nearly half" or cite a visibility-specific majority stat.

**N5 — "Most agent failures are config failures, not model failures." [6]**
A quantified empirical premise ("most… not…") with no backing, in a deck otherwise scrupulous about citing (IBM, SEC, SAIF). It's load-bearing for "the config is the product / fund the platform." Fix: cite it or soften the quantifier ("many"/"a large share").

**N6 — "the exact structural analogy." [4]**
Knight Capital is correctly and repeatedly labeled a *pre-AI automated-trading failure* used as **analogy, not an AI incident** (4 botnote, 21 src, notes) — this is handled well. Only "**exact**" overstates: Knight was a deterministic dormant-code/partial-deployment error, not autonomous decision-making; the analogy is apt for the R pillar (speed × no kill-switch), not "exact." Fix: drop "exact."

---

## 4. Argument score: **8 / 10** — PASS

**Rationale.** The core inference is sound and independently corroborated: build-verification and runtime-governance are genuinely distinct dimensions, orthogonality is *demonstrated* (not just asserted) by the fully-populated readiness map on slide 17, and the conclusion "governance is what earns the deployment" follows cleanly from the turn on slide 3. Every previously-identified logic risk is visibly defused on-slide — VERDICT's single-source status is flagged and reframed as multi-body consensus, slide 10 is honestly labeled "our mapping," the build axis is guarded as task-dependent, Knight Capital is scoped as a pre-AI analogy, and the multi-agent frontier gap is named twice. That honesty is what earns the 8. What holds it below 9 is one genuine coherence defect on a named load-bearing claim (S1: the hook says the axes are independent while the overlays and slide 7 say build work *is already* governance), one unwarranted universal (S2: the L3 floor flexes on neither stakes nor its own "overkill" admission), and a recurring imprecision in how "runtime" is used (S3). None is Fatal — each is a one-line addition or relabel, and the thesis survives all of them — so the deck clears the gate. **PASS**, with S1–S4 logged as required before the argument can be called airtight; fold them into v1.0.1.
