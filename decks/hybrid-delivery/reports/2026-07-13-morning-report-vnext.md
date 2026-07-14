# Morning Report — hybrid-delivery vNext overnight research run

---
date: 2026-07-13 (overnight)
orchestrated_by: Larry
for: Adnan
goal: In-depth aa2brain review + last30days + storm-research on the delivery-measurement gap; narrative analysis for an improved deck
status: GOAL MET — research complete, narrative analysed, pre-build gates passed with conditions
---

## TL;DR

Your instinct is validated by the evidence, and it does more than fill a content gap — **the delivery-measurement act is the missing answer to the deck's one unresolved Critical (A2: "why does the IM, not the tech lead, win the governance contest?").** But both gates agree the current framing *asserts* that win instead of *earning* it. The fix is known and concrete (below). Recommended: v3.0.0, one arc, measurement woven through crisis and climb — pending your approval before Coda builds.

## What ran tonight

| Step | Who | Output |
|---|---|---|
| aa2brain vault survey (30+ notes read) | Pax (Sonnet) | `research/2026-07-13-aa2brain-survey-agentic-metrics.md` |
| last30days social corpus (68 items, 5 sources) | Larry via skill | `~/Documents/Last30Days/agile-metrics-velocity-story-points-ceremonies-ai-coding-agents-raw-v3.md` |
| STORM lenses: Researcher + Economist | Pax (Sonnet) | `research/2026-07-13-storm-lens-researcher-economist.md` |
| STORM lenses: Skeptic + Historian | Pax (Sonnet) | `research/2026-07-13-storm-lens-skeptic-historian.md` |
| STORM synthesis + contradiction map | Larry | `research/2026-07-13-storm-note-measuring-squad-success.md` + vault copy `aa2brain/concepts/measuring-squad-success-agentic-delivery.md` |
| Consolidated deck-facing brief | Larry | `research/2026-07-13-research-brief-v4.md` |
| Narrative SHAPE (via /tactics) | Aria (Opus) | `reports/2026-07-13-narrative-spine-vnext-proposal.md` |
| Argument audit (pre-build gate) | Rex (Opus) | `reports/2026-07-13-rex-audit-vnext-proposal.md` |
| Adversarial pre-mortem (pre-build gate) | Vera (Opus) | `reports/2026-07-13-vera-premortem-vnext-proposal.md` |

## The five research headlines

1. **Velocity per developer and velocity per squad have decoupled.** Faros (22k devs): individual output +21-98% by metric, while bugs/dev +54% and incidents/PR +242.7%; org-level gains cluster ~10% across six research efforts. This decoupling — not "agents are fast" — is the honest hook.
2. **Velocity was already broken; agents made the pretence unaffordable.** Ron Jeffries: "I may have invented story points, and if I did, I'm sorry now." #NoEstimates predates agents by a decade; Goodhart gaming now costs nothing. Even Scrum.org has published the pivot ("From Velocity to Agent Efficiency").
3. **WIP survives; the constraint moved to human review/judgment capacity.** Reinertsen/ToC mechanism, new bottleneck. The concession is the power move: flow discipline is IM home turf.
4. **Sustainable pace now means an attention budget.** Glean (6,000 workers): ~6.4 of 11 saved hrs/week eaten by "botsitting." **No published framework budgets this — original-framework territory for you.** Same for `token-budget-as-sprint-capacity` (your vault references it twice; the page doesn't exist).
5. **Ceremonies survive by shrinking into judgment rituals — neither dying nor wearing an AI sticker.** Precedents: trunk-based dev decoupled deploy from release; GitLab's standups went async and shrank. Aria's reframe for slide 19: *"The ceremony survives as a judgment ritual. The metric inside it does not."*

## Narrative decision (Aria) and gate verdicts (Rex, Vera)

- **Aria:** v3.0.0 (MAJOR — objective extends, premise re-roots, original IP enters; prior scorecards don't carry). Keep Man in a Hole, ONE arc. Measurement woven through Beat 3 (crisis) and Beat 4 (climb) — a standalone measurement act would rebuild the framework plateau v2.1.0 demolished. Net slide count unchanged (+4 new, −3 to appendix, −1 compression). Hook sharpened to the measurement paradox.
- **Rex: GO-WITH-CONDITIONS.** Blocker B1: do not build as "A2 resolved" — the entailment ("own the outcome → govern the boundary") relocates the unproven step; state the warrant on-slide and pull the flow-discipline strut forward. Conditions: fix VERDICT pillar-C self-contradiction ("track spend next to velocity" vs "velocity is out"); three-strut warrant for the proposed frameworks (grounded need + proven mechanism + explicit synthesis); don't overload one slide with both frameworks; keep the task-type conditional welded to the compressed evidence slide; Pax verification gate on 441%/242.7% and Scrum.org before figures land.
- **Vera: 1 Critical / 6 Significant.** C1 (same finding as Rex's B1, from the attack side): the metrics defining "delivery outcome" are engineering telemetry the tech lead owns — establish on-slide why outcome measurement is an IM *decision*, not telemetry. S1: hook's "never shipped less predictably" is ungrounded — use the decoupling instead. S2: put the individual-vs-squad reconciliation on the slide face (METR 19% slower next to Faros +98% is a self-refuting slide otherwise). S6: de-risk the CTA (baseline = homework, pilot = invitation); no invented attention-budget number on-slide. Predicted score: 8.0-8.5 if the A2 kill is earned on-slide; 6.0-6.5 if built as proposed.

**Larry's synthesis of the C1/B1 fix** (the one thing to decide before build): the IM's claim isn't the telemetry (tech lead's dashboards) — it's the *decisions the telemetry forces*: what counts as done (judged, durable, shipped), how much review capacity the squad plans for, which work is WIP-capped, what gets reported to stakeholders as squad health. Tech leads own the sensors; IMs own the operating decisions and the reporting contract. That distinction, on one slide, is what earns A2.

## Verification flags (before any figure goes on a slide)

441% attribution (Faros telemetry vs DORA PDF — reconcile), Scrum.org article body (JS-gated), METR = 2025 RCT only (follow-up is selection-biased), Gates "aircraft weight" quote (unattributable), vault's "40% formatting penalty" citation (unverified). Full list in brief v4.

## For you to do (10 minutes)

1. **Approve / adjust the direction** — v3.0.0, weave-not-bolt, and the C1/B1 fix above. Then I brief Iris (design proposal per WS-006) and Coda (build), with Pax's verification gate on the flagged figures first.
2. **Optional — mirror the storm note to the VPS wiki** (auto-mode blocked remote writes overnight; note is already in your Drive vault + this repo):
   `cat decks/hybrid-delivery/research/2026-07-13-storm-note-measuring-squad-success.md | ssh root@178.105.51.174 "docker exec -i -u 1000 hermes-gateway sh -c 'cat > /opt/wiki/concepts/measuring-squad-success-agentic-delivery.md'"`
3. **Your unwritten concept** `token-budget-as-sprint-capacity` is the seed of your second framework — worth 20 minutes of your own words before we cite it as yours.
