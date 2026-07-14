---
deck: hybrid-delivery
version: v3.0.0-proposal
audited_artifact: reports/2026-07-13-narrative-spine-vnext-proposal.md
scored_by: Rex, Logic Auditor (via Larry)
date: 2026-07-13
audit_type: PRE-BUILD ARGUMENT GATE (spine, not deck) — full re-audit warranted (MAJOR)
baseline_argument_score: 7.0 (v2.1.0)
provisional_argument_score: 7.0 / 10 (conditional — see rationale)
gate_verdict: GO-WITH-CONDITIONS
gap_delta: 1 Blocker / 5 Significant / 4 Minor
---

# Rex Logic Audit — hybrid-delivery vNext Narrative Spine (v3.0.0 proposal)

**Scope.** This audits the *proposed argument*, before slides exist. Rex checks structure,
warrant, and entailment — not fact-accuracy (Pax), not persuasion (Aria), not the outside
attack (Vera). Where a finding overlaps Vera's A-series or Pax's verification queue, it is
flagged as overlap, per remit.

**One-line headline finding.** The spine's central new move — *"you own the delivery
outcome, therefore you govern the boundary"* — is a genuine upgrade over v2.1.0's land-grab,
but it does **not** resolve Critical A2 as the proposal claims; it relocates the unproven
step rather than discharging it, and the new evidence base sits *more* on the tech lead's
turf, not less.

---

## Reconstructed argument map (proposed spine)

Thesis (unchanged): the IM/DM should own the human-AI boundary, because that *is* delivery
ownership in the agentic era.

New load-bearing chain (the A2 re-root, Beat 3, slide C):

- **P1** — You (IM) own the delivery outcome. *[asserted as role identity, Beat 1]*
- **P2** — The delivery outcome now flows through the human-judgment boundary
  (generate → decide), because construction is ~free and the binding constraint is
  review/judgment. *[grounded: Faros incidents/PR, GitClear durability, Glean botsitting,
  "review is the new bottleneck"]*
- **W (unstated warrant)** — Whoever owns the outcome should govern the mechanism that
  determines it (accountability-follows-ownership). *[normative, unstated, ungrounded]*
- **C** — Therefore you govern the boundary.

Supporting threads: strong-middle shape (Beat 2, slide A); velocity-decoupling crisis
(Beat 3, slide B); proposed frameworks (Beat 4, slide D); ceremony-reframe (slide 19).

---

## Q1 — The A2 entailment: valid defeater, or the claim restated on friendlier ground?

**Verdict: RESTATED, not defeated. The entailment improves the argument but does not
discharge Critical A2. The proposal's "this is the A2 kill" (Beat 3) overclaims; its own
Flags section is more honest ("Rex's call to establish"). Adjudication: partially
establishes, does not close.**

Warrant chain and grounding status:
- *"Boundary decisions determine squad outcomes"* (P2) — **GROUNDED.** Faros incidents/PR
  +242.7%, bugs/dev +54%, GitClear durability collapse, Glean supervision tax, review-as-
  constraint all locate outcome-determination at the judgment boundary. This premise is solid.
- *"Measurement of squad outcomes is uncontested IM turf"* — **ASSERTED, and contradicted
  by the opponent model.** Slide C states "the tech lead does not contest" this. Nothing in
  the four research files establishes that. The whole point of A2 is that the motivated
  opponent (staff tech lead who owns the tooling, reads the RCTs) *does* contest exactly this.
- *"IM owns the delivery outcome"* (P1) — **ASSERTED as status-quo identity.** True as a role
  label; not established as a *contest won against the tech lead*, which is what A2 requires.
- *Bridging warrant W* (owner-of-outcome governs the mechanism) — **UNSTATED, normative,
  ungrounded.** Load-bearing and invisible: the audience cannot evaluate it.

Research grounds the *reframe* only, not the *contest*. Contradiction-map #5 says "the two
are one job: govern the boundary *because* you own the delivery outcome." That grounds the
framing that boundary-governance and delivery-ownership are the same job. It does **not**
ground the identity of the "you" — it does not show the IM, rather than the tech lead, is
the owner. The research supplies the syllogism's shape; it does not supply premise P1's
contested content.

Why it fails against the motivated opponent — and is arguably *more* exposed:
The new crisis evidence (slide B) is entirely engineering telemetry — PR review time +441%,
PRs/dev +98%, bugs/dev +54%, incidents/PR +242.7%, code durability. This is the tech lead's
home turf. The opponent runs the same syllogism in reverse: *"The measurement crisis is in
my domain — code review, CI, PR pipeline, incidents. By your own logic, I own the delivery
outcome, so I govern the boundary."* v2.1.0's A2 was "the hook foregrounds the tech lead's
metric (PR review time)"; vNext re-roots the *entire spine* on PR/incident/durability
metrics. The only IM-coded metric in the mix is velocity — the metric the deck is
simultaneously declaring dead. So the IM's claimed turf is the retired metric, and the
replacement metrics read as engineering signals.

**Repair spec (Blocker B1).** (a) Stop asserting A2 is resolved — treat it as the improved-
but-still-open deferred Critical. (b) Make warrant W explicit on-slide. (c) Supply at least
one *reason the IM, not the tech lead, owns the delivery outcome* — the strongest available
strut is the flow-discipline / WIP home-turf argument from slide D (ToC/Reinertsen is
decades-old delivery-manager craft; the constraint moved, the discipline is the IM's).
Pull that forward as backing for P1. Without it, the entailment is a non-sequitur dressed
as delivery language. Final A2 adjudication remains Vera's.

---

## Q2 — Proposed frameworks inside an evidence-led deck: authority gap?

**Verdict: REAL but MANAGEABLE risk, on conditions. Not fatal.**

In a deck where every slide carries a citation + confidence level, two uncited "here is my
framework" slides read as opinion unless re-warranted. A proposal-claim needs a different
Toulmin structure than an evidence-claim — three struts:
1. **The need is grounded** — Glean botsitting 6.4/11 hrs to supervision. **HIGH confidence.** ✓
2. **The mechanism is proven elsewhere** — Reinertsen/ToC WIP; "the mechanism is old, only
   the constraint moved." **MEDIUM** (secondary summaries; Reinertsen primary not fetched). ✓
3. **The synthesis is the original step** — naming human-review-capacity as the planned,
   budgeted WIP constraint. Correctly labelled "proposal, open territory." ✓

This is the research's own framing (contradiction-map #4: *novelty modest, fluency the
leverage*). Executed with the three struts on-slide, "original IP" flips from liability to
an **independent support for A2** — flow discipline is IM home turf that does not route
through the tech lead's tooling. Honesty alone ("these are proposals") is a hedge; honesty
+ struts is a warrant. Require the struts.

Two structural gaps:
- **Uneven grounding.** Attention-budget = Glean (need, High) + Reinertsen (mechanism, Med).
  Token-budget = Scrum.org token "gesture" only (Medium, **JS-gated page, unverified**) +
  the vault's `token-budget-as-sprint-capacity` link is **unwritten/broken**. Do not present
  the two as equally grounded; token-budget is the more tentative. (Significant S2.)
- **Slide overload.** Slide D carries WIP + sustainable pace + attention budget + token
  budget. The weaker proposal rides the stronger; if challenged they fall together.
  Subordinate or split. (Significant S3.)

---

## Q3 — Slide-19 reframe: internally consistent?

**Verdict: CONSISTENT with the deck's direction and RESOLVES a real pre-existing
contradiction — but introduces one localized contradiction that must be reconciled.**

The reframe ("ceremony survives as a judgment ritual; the metric inside does not") is a
sharper, correct version of the current "old ones, upgraded" line, and it fixes the genuine
tension between slide 19 and Adnan's "no AI sticker on old practices." Grounded: Historian
H4, GitLab async precedent (High), trunk-based/feature-flags (High). The metric it installs
(flow of judged durable outcomes + attention budget + agent cost; velocity/story points out)
matches slide C's new unit of success — coherent thread.

**New internal contradiction (Significant S1).** The retained VERDICT card, pillar C, reads
*"Track agent spend and compliance next to velocity."* The reframed headline says velocity
is **out**. If the VERDICT card bodies are retained verbatim (the proposal changes only the
headline/framing), slide 19 contradicts itself on its own face. Reconcile pillar C's copy —
swap "next to velocity" for the new honest metric.

No *other* retained slide re-asserts "nothing fundamental changes": slide 22 uses DoD-as-gate
(consistent); the bolt-on/"no AI sticker" point moves cleanly from slide 11 to the reframe.

---

## Q4 — 09+10 compression: does it put the Malone reconciliation at risk?

**Verdict: ACCEPTABLE on a hard constraint. Not fatal — the reconciliation has redundant
anchoring (slide 16 Vera-A1 repair, retained; Appendix A 30, mandated intact).**

The argument depends on the task-type conditional: BCG/P&G gains apply to the ~10%
generative/iterative work; Malone's 90% decision/classification is where AI degrades. Drop
the qualifier and the Malone challenge is unanswerable (scorecard G1, Vera-A1).

**Minimum content that MUST survive on the compressed main-line slide:**
1. ≥1 upside stat (BCG or P&G) with the qualifier **welded to it** ("for complex, generative
   work") — not a detachable caveat.
2. The Malone counter as the *source* of the conditional — name the task-type split
   (majority decision/classification = where human+AI underperforms). This is the load-bearing
   half most likely to be dropped in compression; without it the conditional is asserted, not
   evidenced.
3. The explicit "real **and** conditional on task type" statement.
4. Pointer to Appendix A (30).

**Risk:** compression drifts toward "the upside is real (conditional)" and silently drops
Malone's 90%/decision-task mechanism from the main line, leaving the conditional as an
assertion answerable only by a nav-jump. Preserve item 2 on the main line and keep 30 intact.

---

## Q5 — New-claims inventory (main line), with source confidence

| Claim (main line) | Slide | Source | Confidence | Load-bearing? |
|---|---|---|---|---|
| Velocity decoupled (indiv up / squad flat-degrading) | hook, B | Faros + synthesis | Med-High (single-vendor, triangulated) | YES (new hook) |
| PR review time +441% | hook/B | Faros/DORA | High direction / **Med exact** | YES |
| incidents/PR +242.7%; bugs/dev +54%; PRs/dev +98%; tasks/dev +21–34% | B | Faros telemetry | Med-High (single vendor) | YES (concreteness) |
| Strong-middle: Frame/Collapse/Judge | A | SDLC-phase + human-sandwich + 80%-problem | **HIGH** (best-triangulated) | YES |
| METR 19% slower | A/B | METR RCT | High RCT; **follow-up fragile** | supporting |
| Velocity is a vanity metric (agents inflate at ~0 cost) | B | Scrum.org "Velocity→Agent Efficiency" | **MEDIUM — JS-gated, unverified** | YES (pillar of crisis) |
| Velocity was already broken pre-agents | B | Jeffries "I'm sorry now" / #NoEstimates | **HIGH** (primary) | YES (Data-Sceptic move) |
| DORA AI Capabilities Model (capabilities, not a velocity number) | C | DORA 2025 | **HIGH** (primary) | YES |
| GitClear durability (refactor 21%→3.8%, churn +15%) | C | GitClear | High (single-vendor, directional) | supporting |
| 30/60/90-day survival as honest metric | C | deck synthesis on GitClear | Medium (proposed metric) | supporting |
| Glean botsitting 6.4/11 hrs | C/D | Glean Work AI Index | **HIGH** | YES |
| Reinertsen/ToC WIP mechanism | D | secondary summaries | Medium (primary not fetched) | YES (framework strut) |
| Scrum.org token-budget gesture | D | Scrum.org | Medium (JS-gated) | YES (framework strut) |
| Ceremonies shrink+decouple (trunk/flags/async) | 19 | GitLab + trunk-based | **HIGH** | supporting |

**Flags — Low/Medium confidence made LOAD-BEARING (verification is Pax's gate; structural
dependency is Rex's flag):**
- **Faros 441% + 242.7%** — single-vendor proprietary telemetry, traced to *secondary*
  aggregators, **not** the DORA primary PDF. Research explicitly: *"download the actual DORA
  PDF before putting exact percentages on a slide."* Now promoted to hook + crisis; exposure
  higher than v2.1.0 (441% already carried an on-slide caveat — keep it; add same for 242.7%).
- **Scrum.org velocity-as-vanity** — Medium, JS-gated page, *"verify before verbatim quote."*
  Pillar of the crisis; the "agents killed velocity" half rests largely on it (the "already
  broken" half is Jeffries, High — so partial High backing survives if Scrum.org is cut).
- **METR 19%** — present as a point-in-time RCT, **not** a durable constant; follow-up cohort
  is selection-biased/"methodologically fragile." An opponent can cite the follow-up to muddy.
- **Token-budget mechanism** — Scrum.org gesture only; weakest framework strut (see Q2/S2).

These are verification preconditions to hand to Pax. The one that is Rex's own logic gate is
the entailment premise (Q1), which no fact-check can rescue.

---

## Q6 — Gap-register delta vs v2.1.0 argument scorecard

**Advances (not fully closes):**
- **G-NEW-1 (IM-over-tech-lead explicit case)** — the entailment supplies a *reason* where
  v2.1.0 had a land-grab. Real progress; not closed (P1 still asserted — Q1/B1).
- **G-NEW-2 (learnable centaur competency)** — slide D's "flow discipline is IM home turf,
  decades old" grounds an *already-held* competency from a new angle. Partial adjacent progress.

**Left open / unchanged:**
- **Vera-A1 / Malone coherence** — survives via slide 16 + Appendix A 30, *conditional on Q4*.
- **A2 Critical** — NOT closed. Reframed, improved, still open. Proposal's claim to fix it is
  the headline overstatement.
- G3, G5, G-NEW-3 — untouched.

**Newly opened:**
- **N1** — entailment's unstated warrant + asserted contested premise (Q1). Load-bearing.
- **N2** — original-framework authority gap; token-budget under-grounded (Q2).
- **N3** — slide-19 internal contradiction (velocity in/out) (Q3).
- **N4** — single-vendor/unverified sources promoted to load-bearing (Q5).
- **N5** — slide D overload (Q2).
- **N6 (structural)** — the objective now answers *two* questions (own the boundary + rebuild
  measurement). Their unification rests **entirely** on the entailment. If the entailment is
  softened (B1), the measurement thread must be explicitly *subordinated* to the boundary
  thesis, or the deck reads as two arguments stapled together.
- Compounding: slide 13 (84/49) also leaves the main line, thinning on-slide governance
  evidence further (M-R1 territory) — not a logic break (12+14 carry it).

---

## Ranked issues

### BLOCKER (1)
- **B1 — The entailment does not defeat A2; do not build the spine as "A2 resolved."**
  The load-bearing move relocates the unproven step (from "governs boundary" to "owns
  delivery outcome") without discharging it, and the new evidence base is engineering
  telemetry the tech lead owns more naturally. Repair: (a) de-claim A2 resolution; (b) state
  warrant W on-slide; (c) back P1 with the flow-discipline/WIP home-turf strut pulled forward
  from slide D. Coda may build the unaffected slides (A, hook, 19 modulo S1) immediately;
  slide C is gated on B1.

### SIGNIFICANT (5)
- **S1 — Slide-19 self-contradiction.** VERDICT pillar C ("agent spend next to velocity") vs
  new "velocity out" headline. Reconcile the card copy.
- **S2 — Framework authority gap / uneven grounding.** Slide D must carry the three struts
  (grounded need + proven mechanism + explicit synthesis). Token-budget is under-grounded
  (JS-gated Scrum.org gesture; unwritten vault note) — do not present it as equal to
  attention-budget.
- **S3 — Slide D overload.** WIP + sustainable pace + two frameworks on one slide; the weaker
  proposal rides the stronger. Subordinate or split.
- **S4 — Compression minimum-content constraint.** Keep the task-type conditional welded to
  the upside stat and name Malone's decision-task split on the main line; keep Appendix A 30
  intact.
- **S5 — Load-bearing unverified sources.** Faros 441%/242.7% (verify vs DORA PDF) and
  Scrum.org velocity-vanity (verify JS-gated page) are now pillars. Verification precondition
  → Pax, before build.

### MINOR (4)
- **M1 — Two-thesis subordination.** Once B1 softens the entailment, make the measurement
  thread explicitly serve the boundary thesis, not co-equal to it.
- **M2 — METR framing.** Present 19% as a point-in-time RCT, not a durable constant.
- **M3 — Governance-evidence thinning.** Slide 13 also to appendix; note cumulative on-slide
  thinning (not a break; 12+14 carry it).
- **M4 — Proposed-metric labelling.** "30/60/90-day survival" is deck synthesis, not a
  published metric — label consistent with the frameworks-as-proposals honesty.

---

## Provisional argument score: 7.0 / 10 (conditional)

Pre-build, contingent on conditions. The spine advances reason-giving over v2.1.0 (land-grab
→ delivery-accountability warrant; G-NEW-1 and G-NEW-2 both move) and grounds the measurement
thread well (strong-middle High; Jeffries High; DORA/Glean High). But the load-bearing
entailment carries an unstated warrant and an asserted, contested premise, and the proposal
overclaims A2 resolution — so, mirroring how a score is capped by its strongest unaddressed
structural flaw, it holds at 7.0. **Upside to 7.5+ if B1's warrant is supplied and P1 is
backed; downside to ~6.5 if built as "A2 fixed," because the overclaim plus the framework
authority gap would be exposed on contact.**

## Gate verdict: **GO-WITH-CONDITIONS**

Coda may start on the well-grounded, unaffected slides now (strong-middle A, sharpened hook,
reframed 19 pending S1). The entailment slide C and framework slide D are gated on B1/S2/S3.
S4 governs the compression. S5 is a Pax verification gate before any Faros/Scrum.org figure
lands. Version bump to v3.0.0 (full re-audit) is logically warranted — the objective extends,
the core premise re-roots, and original IP enters; prior scorecards do not carry.
