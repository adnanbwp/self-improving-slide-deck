---
deck: The Iteration Manager in the Age of Agents
target: reports/2026-07-13-narrative-spine-vnext-proposal.md (vNext / v3.0.0 spine, pre-build)
type: adversarial pre-mortem (red-team of a proposal, not a deck scorecard)
reviewer: Vera (Adversarial Critic), via Larry
date: 2026-07-13
prior_scorecard: scorecards/v2.1.0-adversarial.md (standing log A1–A9; v2.1.0 closed 7.5, capped by A2)
grounding:
  - research/2026-07-13-storm-note-measuring-squad-success.md
  - research/2026-07-13-storm-lens-researcher-economist.md
  - research/2026-07-13-storm-lens-skeptic-historian.md
  - research/2026-07-13-aa2brain-survey-agentic-metrics.md
attack_count: { critical: 1, significant: 6, low: 3 }
predicted_v3_score: "6.0–6.5 if built as proposed; 8.0–8.5 only if the Critical is resolved on-slide"
---

# Adversarial Pre-Mortem — hybrid-delivery vNext (v3.0.0 spine)

**Register:** This is a pre-build red-team. Attacks land on the *proposal* and, where noted, on the slide plan it must produce. "Required resolution" states what the slide plan or speaker notes must demonstrate — not how to build it (that is Rex/Pax/Aria).

---

## Steelman of the proposal (strongest form)

vNext folds a delivery-measurement thread through the existing Man-in-a-Hole arc without adding a second act. Its central strategic move is the **A2 kill**: re-root the governance claim in delivery ownership — *you own the delivery outcome → the delivery outcome now flows through the human-judgment constraint → therefore you govern the boundary*. It opens the crisis on an anomaly the IM can verify in their own sprint data (individual output up sharply, squad delivery flat/degrading), pre-concedes that velocity was already broken before agents (Jeffries/#NoEstimates) as a Data-Sceptic credibility play, and hands the audience two original frameworks (attention-budget WIP, token-budget-as-capacity) as the Guide's gift for un-mapped territory. It claims net-zero slide count (+4/−3/−1), preserves one-arc discipline by weaving rather than bolting, resolves the real slide-19 self-contradiction, and extends the CTA to "audit + one honest baseline." The version-bump reasoning (v3.0.0: new objective, new IP, argument-structure change) is sound and I do not attack it.

**What the proposal gets right and I do not contest:** the choice of target (A2 is correctly identified as the gate); the weave-not-bolt structural call; the slide-19 reframe genuinely dissolves a live contradiction; pre-conceding velocity-was-broken is the right instinct; and the WIP "home turf" wield (turning "it's not new" into "you're already fluent in the discipline that governs the new bottleneck") is a genuinely strong rhetorical move. My Critical is not that the re-rooting is the wrong idea — it is the right idea, executed as an assertion instead of an earned entailment, using metrics that live in the opponent's dashboards.

---

## Motivated opponents run

1. Staff tech lead (standing A2 opponent) — owns the agent tooling and the delivery dashboards.
2. Skeptical engineering director who has read METR.
3. Scrum purist / agile coach — knows velocity was never in the Scrum Guide and knows Kanban.
4. CFO / exec — wants a number, hears "measure judgment" as "ship less."
5. Presenter-risk view — Adnan proposes two unvalidated frameworks in a leading-voice room.
6. The fatalist — "the IM role is dissolving anyway" (the fork's fragmentation path, weaponized).

---

## Attack log (severity-ranked)

### CRITICAL

**C1 — The A2 re-rooting walks *into* the tech lead's turf; "the tech lead does not contest this" is asserted, not established, and is contradicted by the provenance of the deck's own evidence.**

The proposal's spine is the entailment on slide C: *you own the delivery outcome, therefore you govern the boundary* — and it rests on one load-bearing sentence: "This is a delivery-measurement job the tech lead does not contest." That sentence is unsupported. Worse, it is contradicted by the evidence the same slide cites. Every new metric the proposal introduces to define "delivery outcome" — PR review time +441%, incidents/PR +242.7%, bugs/dev +54%, GitClear code durability, DORA capabilities — is **engineering telemetry that lives in the tech lead's tooling** (Faros, GitClear, LinearB, DORA dashboards). The old boundary argument was at least about workflow *design* and decision gates (arguably a delivery/process concern). The re-rooting swaps that for metrics that are *deeper* in engineering turf than the boundary was.

The tech lead's lead attack writes itself: *"Delivery metrics are DORA metrics. Cycle time, change-fail rate, incidents per PR, review latency, code churn — those are my dashboards. You just re-rooted your entire claim in the numbers I already own."* The research supports the tech lead, not the deck: contradiction-map #5 establishes the *entailment logic* (govern the boundary because you own the outcome) but says nothing about non-contestation; and the provenance of the metrics points the other way. This is the same Critical (A2) that has capped every version since v1.5.0 — and the re-rooting risks **worsening** it, because it moves the argument onto ground the opponent owns more completely.

Because five other attacks route through this one (S2, S4, S5 especially), C1 is the gate on the whole vNext score.

**Required resolution (slide plan, not notes):** The deck must *establish*, on-slide, why the delivery-outcome measurement is a delivery-management decision the IM owns and not engineering telemetry the tech lead owns. The only defensible cut is to separate the two: engineering *reads* the health signals (incidents/PR, churn, durability), but the IM owns the **decisions those signals feed** — what the squad commits to, what counts as "done," what the sprint forecasts, which flow gets protected. If the deck cannot draw that line cleanly, the re-rooting must not be made the spine; the boundary-design framing (v2.1.0) at least did not concede the metric layer. Do not ship the sentence "the tech lead does not contest this" — either earn it or cut it.

---

### SIGNIFICANT

**S2 — The evidence architecture can be turned against itself at the crisis peak: slide B stacks METR "19% slower" beside Faros "+98% PRs" with the reconciliation off the slide face.**

The engineering director who has read METR leads with: *"You cite a study that says AI makes developers SLOWER to argue we need new metrics for AI speed. Which is it?"* Slide B (crisis opener) stacks Faros (output up: PRs/dev up to +98%, tasks/dev +21–34%) next to METR (19% slower) next to quality-degrading numbers. The research **does** reconcile these (contradiction-map #2: gains are real *and* conditional on task-type and on level — METR is experienced devs on familiar/unfamiliar OSS repos, Faros is aggregate telemetry; the point is *decoupling*, not raw speed). But that reconciliation is subtle and, as proposed, lives in the synthesis, not on the slide. This is the exact failure pattern of the v2.1.0 A5 finding: a multi-source stack where the disarming caveat sits in notes, now placed at the crisis peak instead of the hook. A prepared opponent calls it a self-refuting slide.

**Required resolution (slide plan):** Slide B must carry the reconciliation on its face — the load-bearing claim is the **decoupling** (individual output up, squad delivery flat), not "more code" versus "slower." METR and Faros must be framed as measuring different levels, on the slide, or the two numbers must not share a slide.

**S1 — The hook's middle claim, "your squad has never shipped less *predictably*," is an ungrounded superlative at maximum salience.**

Larry flagged this correctly. Check what the research actually supports: incidents/PR +242.7%, bugs/dev +54%, PR review time +441%, review-queue latency up, churn +15%, durability down, DORA "amplifier → instability." Those ground **quality degradation, review latency, and instability**. None of them measures delivery **predictability** — forecast accuracy, delivery-variance, the ability to commit to a sprint and hit it. "Predictability" is a specific delivery concept and the deck has no predictability metric behind it; the synthesis one-liner itself hedges to "flat *or* degrading," which the hook hardens into a superlative ("never shipped less predictably"). The v2.1.0 lesson was explicit: do not put an ungrounded claim at the hook, where it is the first thing a skeptic scrutinizes. The tech lead or director says: *"Show me the predictability number. You've shown me instability and latency — that's not the same thing."* And there is no such number in the four research files.

**Required resolution (slide plan):** Either ground "predictability" in a metric the research actually supports (it does not cleanly exist — the nearest is CircleCI main-branch success falling to 70.8%, which is reliability, not predictability), or change the word to what *is* grounded: the squad converts less of its rising output into delivered, durable value (the decoupling). "Predictably" is the puncture — replace it.

**S3 — The hook ("velocity just stopped meaning anything") is in visible tension with the deck's own pre-concession ("velocity was always broken").**

The Scrum purist exploits the deck against itself: *"You just told me — via Jeffries — that velocity was always broken and was never even in the Scrum Guide. So it did not *just* stop meaning anything. Agents did not break it. Your own slide B concedes this."* The hook asserts a **NOW rupture** ("just stopped"); the Data-Sceptic pre-concession asserts it was **ALWAYS broken**. The research resolves the tension (contradiction-map #1: agents did not create the flaw — they made the pretence *unaffordably expensive*, because an agent inflates points at near-zero cost, so Goodhart gaming goes vertical). That resolution is the strongest version of the point — but it is not on the hook. As proposed, the pre-concession undercuts the hook instead of reinforcing it.

**Required resolution (slide plan):** The hook and slide B must carry the reconciliation — agents did not break velocity, they made *gaming it free*. That single move converts the pre-concession from a contradiction into the hook's amplifier. Without it, the two most emphasized claims in the crisis argue against each other.

**S4 — The CFO turns the measurement act into "an excuse to ship less."**

*"'Judged flow' and 'attention budgets' sound unmeasurable and like a way to justify slowing down. Velocity at least gave me a number."* This is a strong attack on the whole recovery act. The proposal's concreteness defense (441%, +242.7%, 19%, Glean 6.4 hrs) is a defense of the **diagnosis** numbers — evidence the old way is broken — not of the **proposed metric**. "Flow of judged, durable outcomes through the human-judgment constraint" is abstract at the headline level, and "attention budget" is a capacity concept, not obviously a dashboard KPI. The genuinely reportable candidates (cycle-time of judged outcomes, review-queue depth, 30-day code survival) appear only in the CTA, not in the measurement slides. And the deck does not visibly arm the presenter with the rebuttal the research hands it: judged-flow ships *more* delivered value, because the vanity number was hiding a rework/incident tax (incidents/PR +242.7%, churn +15%, botsitting eroding 58% of the saving).

**Required resolution (slide plan for the concrete metrics; notes for the rebuttal):** The proposed metric must surface as concrete, reportable numbers on the measurement slides, not only in the CTA. Speaker notes must arm the presenter to pre-empt "excuse to ship less" by showing judged-flow *increases* delivered value against the hidden tax.

**S5 — The measurement act hands the fatalist new ammunition, and the deeper crisis makes the A2 re-rooting load-bearing for the whole deck.**

Beat 1 explicitly grounds the IM's identity in "velocity, flow, predictability, sustainable pace." The measurement act then retires or redefines *every one of those instruments* (velocity → vanity, story points → dead, sustainable pace → attention budget) and replaces them with metrics that read in engineering tooling (S under C1). The "role is dissolving anyway" fatalist — already voiced on the fork slide — now says: *"You just told me every instrument that defined my role is obsolete and the replacements live in the tech lead's dashboard. That is not a deeper hole I climb out of as an IM — that is the fragmentation case, made for me."* The proposal's intent is to deepen the hole so recovery lands harder; the risk is that a deeper hole is also more fuel for the exit. This attack is the flywheel between C1 and the crisis depth: **the deeper the measurement crisis, the more the A2 re-rooting has to actually hold** — and as written it is asserted, not won.

**Required resolution (slide plan):** For every old instrument the deck retires, it must hand the IM a new instrument they *demonstrably own* (a delivery-management decision, not an engineering read-out). If C1 is not resolved on-slide, S5 is not resolvable at all — the deck arms the fatalist.

**S6 — Leading-voice / presenter risk: the CTA transfers unvalidated-framework risk to the audience, and "attention budget" has no grounded budget number.**

The honesty framing ("these are proposals; no published framework exists") genuinely defuses the naive "who else uses this?" jab — credit where due. But two sharper failure modes remain. First, the **risk asymmetry**: proposing a framework from a stage is low-risk for Adnan; the CTA's "offer to pilot one proposed framework this sprint" asks the *audience* to bet their real squad on an unvalidated instrument. *"If it's unproven, why is my action item to pilot it?"* Second, the **novelty-vs-ToC trap** the purist sets: the deck wants "attention budget" to be both a leading-voice original (slide D: "no published framework exists") and reassuringly old ("just Reinertsen/ToC WIP, your home turf"). It cannot fully be both — *"Either it's new, and where's your validation? Or it's old ToC, and then it's Reinertsen's contribution, not yours, and it's the team's board, not your role."* Third, if asked "what *is* my attention budget — three hours a day? how do I set it?", the only number available (Margin-of-Safety "~3 productive hours") is single-Substack, flagged Low-Medium/illustrative — the presenter has no grounded budget figure.

**Required resolution (slide plan + notes):** De-risk the CTA — make "track one honest metric beside velocity for one sprint" the low-risk homework and the framework pilot an explicit invitation, not an assignment. Be precise about what is novel (naming human-review capacity as the *explicitly budgeted* sprint constraint) versus inherited (the WIP mechanism), and do not oversell the novelty. Do not put a specific attention-budget number on-slide; give the presenter a notes recovery line that owns the open-territory position rather than defending it.

---

### LOW

**L1 — Evidence-to-appendix pattern: supporting stats are pushed off the main line while the claims they support stay on it.**

No single main-line defense critically depends on the three appendix moves (05 autonomy ladder, 11 bolt-on <40%, 13 governance gap 84/49) — checked individually, each is restated qualitatively elsewhere (05 → 14/18; 11 → the slide-19 "no AI sticker" reframe; 13 → 12/14 plus the new measurement crisis). **But the aggregate is a pattern:** McKinsey <40%, Digital.ai 84/49, and (via the 09+10 compression) the Malone reconciliation all move to appendix while the claims they underwrite stay main-line. The main line gets more assertive and less self-evidencing; an opponent attacking sourcing finds it thinner on-stage. Answerable (stats available for questions), so Low — but the compression flag already tagged by the proposal (Malone must stay intact in Appendix A) is the right instinct; apply the same caution to 11 and 13.

**Required resolution:** Confirm no main-line *number* is asserted whose only proof is now appendix-only; where one is, keep a one-line on-slide anchor.

**L2 — Climb overload: Beat 4 now runs two mechanisms (governance + measurement) under one arc.**

One-arc is preserved on slide *count* (+4/−3/−1), but the *argument load* of the climb roughly doubles: centaur → HITL → fork → three capabilities → two new frameworks → reframed VERDICT → failure modes. The proposal's do-not-regress check #2 guards against a slide-count plateau; it does not guard against a two-engine climb where the audience loses which hole they are climbing out of. Low, because the weave is structurally sound — but watch the cognitive load, not just the slide tally.

**L3 — "Strong-middle" theme leans on METR (19%) and the "80% problem," both flagged single-source/unverified by Pax.**

Slide A (strong-middle) and slide B both lean on the METR 19% figure; Pax's own survey flags the METR citation and the "40% Markdown drop / Ouyang et al." as not independently re-verified, and METR's follow-up as "methodologically fragile, not a stable industry constant." Low, because the directional claim is well-triangulated — but do not present 19% as a fixed constant; frame it as one RCT's context-bound finding, or the director (who has read the METR follow-up) corrects the presenter live.

---

## Verdict — what must be resolved where

**Must be resolved in the slide plan (structural; cannot be patched in notes):**
- **C1** — the A2 re-rooting must be *established* on-slide (slide C), or the spine does not hold. This is the gate.
- **S1** — the hook word "predictably" must change to a grounded claim.
- **S2** — slide B must carry the METR/Faros level-reconciliation on its face.
- **S3** — the hook must carry "agents made gaming free," converting the pre-concession into an amplifier.
- **S5** — resolvable only *if* C1 is resolved; every retired instrument needs an IM-owned replacement on-slide.
- **S4 (part)** and **S6 (part)** — concrete reportable metrics on the measurement slides; de-risked CTA; no ungrounded attention-budget number on-slide.

**Can be handled in speaker notes (recovery lines):**
- **S4 (part)** — the "judged-flow ships more value, not less" rebuttal to the CFO.
- **S6 (part)** — the "who else uses this / open-territory" recovery line.
- **L2, L3** — framing discipline (don't overload the climb; don't present 19% as a constant).

**L1** is a pre-flight checklist item for Rex/Pax, not a slide-plan blocker.

---

## Predicted adversarial score for v3.0.0

v2.1.0 closed at **7.5**, explicitly capped below 8 by the single unresolved Critical (A2), with the file stating "no version can score above what its strongest unaddressed attack allows" and naming A2's closure as "the sole gate to a higher score."

**If built as proposed** — the re-rooting asserts the A2 kill rather than earning it, and moves the argument onto engineering-owned metric turf (C1 unresolved, arguably worsened), while adding new Significant surfaces at the hook (S1, S3) and the crisis peak (S2) and handing the fatalist ammunition (S5): **predicted 6.0–6.5.** This is the same mechanism that dropped v2.1.0's initial pass to 6.5 before fixes — a persistent Critical plus new Significants at maximum salience.

**If the slide plan resolves C1 on-slide** (establishes why delivery-outcome measurement is the IM's decision, not the tech lead's telemetry) **and fixes the hook** (S1/S3) **and reconciles slide B** (S2): the ceiling that A2 has held since v1.5.0 finally lifts — **predicted 8.0–8.5.** The proposal is aiming at exactly the right gate; the score is entirely a function of whether the A2 kill lands on-slide or stays an assertion.

**Single strongest attack, one sentence:** The vNext spine re-roots governance in "delivery ownership," but the metrics it uses to define delivery outcome — PR review time, incidents/PR, code durability, DORA — are engineering telemetry the tech lead already owns, so the re-rooting walks *into* the A2 opponent's dashboard while asserting, without evidence, that "the tech lead does not contest this."
