# Research Brief v4 — hybrid-delivery vNext (the delivery-measurement act)

---
date: 2026-07-13
compiled_by: Larry (synthesis of Pax ×3, last30days corpus, STORM five-lens pass)
for: hybrid-delivery v3.0.0 proposal
status: complete — pending Rex/Vera pre-build gates
---

## Why this brief exists

Adnan's realignment (2026-07-13): v2.1.0 owns the *boundary/governance* story but is silent on *delivery measurement* — velocity/story points when agents outpace humans, WIP, sustainable pace, cadence redesign. IMs cannot own the boundary while losing sight of delivery responsibilities. His org has questions and no answers; this deck should propose the answers.

This brief consolidates tonight's research. Detail and per-claim confidence live in the four source files (§Sources at end); the STORM synthesis is also persisted to the aa2brain vault as `concepts/measuring-squad-success-agentic-delivery.md`.

## The findings, mapped to Adnan's six questions

### 1. What is velocity/story points worth now?
**The decoupling is the headline:** individual output up sharply (Faros: tasks/dev +21-34%, PRs/dev up to +98%) while squad-level delivery is flat or degrading (bugs/dev +54%, incidents/PR +242.7%, org-level gains cluster ~10% across six research efforts). Velocity per developer and velocity per squad are no longer the same number — so a construction-output metric measures the wrong level.
**The skeptic's correction (use it, don't fight it):** velocity was already broken — Ron Jeffries: "I may have invented story points, and if I did, I'm sorry now"; #NoEstimates (2012); Goodhart's law. Agents didn't break velocity; they made the pretence unaffordable (an agent inflates points at near-zero cost).
**Successor candidates (all cited):** outcome/EBM measures (Scrum.org's own "Velocity → Agent Efficiency" pivot), flow of *judged* outcomes (PBI-level flow — matches Adnan's own unpublished PBI-not-task note from Flow Metrics for Scrum), code durability 30/60/90-day survival (GitClear: refactoring 21%→3.8%, duplication +81%), DX Core 4 + AI extensions, DORA's capabilities-not-metrics stance.

### 2. How does WIP change?
WIP limits survive — but the constrained resource changes from developer capacity to **human review/judgment capacity**. Practitioner model: pull-based continuous flow where WIP is capped by review capacity (Huy Tieu; HN practitioners already improvising risk-score routing). Honest framing: this is Reinertsen/Theory-of-Constraints flow control pointed at a new constraint — the mechanism is 15+ years old, only the bottleneck moved. **That concession is the IM's power move: flow discipline is delivery-management home turf; the tech lead doesn't own it.**

### 3. What does sustainable pace mean?
The scarce resource shifted from programmer hours (XP's 40-hour week → Manifesto Principle 8) to **human attention/judgment capacity**. Quantified: Glean Work AI Index (6,000 workers) — AI saves ~11 hrs/wk, ~6.4 hrs eaten back by supervision ("botsitting", ~58% erosion); 69% admit shipping unverified AI work. Review fatigue is the new burnout vector ("The AI burns the toast, I scrape it"). **No published framework budgets this. Original-framework territory — see §Proposals.**

### 4. Do the cadences survive?
Historical pattern (three precedents: trunk-based dev/feature flags decoupling deploy from release; GitLab async standups; sprints already reduced to planning quanta): **ceremonies survive by shrinking and decoupling into judgment rituals — they neither die nor take an AI sticker.** What must be rebuilt is the *content and metrics inside them*: retro agendas add "what did agents fail at and why"; standups become async digests + deviation checks over agent logs; planning forks into team-level intent and per-agent-task spec (workflow-collision note). Resolves the tension with deck slide 19: "The ceremony survives as a judgment ritual. The metric inside it does not." (Aria's line.)

### 5. The "strong middle" shape
Best-triangulated theme in the vault — four independent framings converge: humans dominate the start (framing, what/why) and the end (judgment, what's good); agents own the middle (construction). Human-sandwich (Frame → Collapse → Judge), SDLC-phase compression table ("AI compresses the SDLC unevenly"), the 80% problem (Osmani; cites METR), conductor-vs-orchestrator failure modes. Kent Beck: skills shift to "vision, strategy, task breakdown, and feedback loops."

### 6. What does the IM measure and report as squad success?
Nothing published answers this directly (confirmed gap). Assembled answer from the evidence: measure the **seam, not the output** — flow of judged outcomes (PBI-level cycle time incl. verification), code durability, review-queue health (pickup time, % merged unreviewed), attention budget consumption, agent cost per outcome, eval pass rates. Each new agentic org role (Agent Supervisor, Eval Owner, Exception Handler, HITL Reviewer) implies a reportable metric.

## §Proposals — Adnan's leading-voice openings (original, framed as proposals)

1. **The Attention Budget** — human review/judgment capacity as the planned, explicit constraint of a hybrid squad: budgeted per sprint like capacity ever was, WIP-limited like Kanban ever was, reported like velocity ever was. Grounding struts: Glean's botsitting hours (the cost is measurable), Reinertsen WIP theory (the mechanism is proven), Faros review-queue data (the constraint is real). Nothing published combines them — Adnan can name it.
2. **Token budget as sprint capacity** — agent capacity planned in tokens/compute next to human capacity in attention (Scrum.org gestures at this; Adnan's vault references the concept twice but it was never written). Companion to VERDICT's C-pillar (cost next to velocity).

## Verification flags (before any figure goes on a slide)

- **441%**: originates in Faros AI telemetry coverage of DORA-adjacent data, not the DORA PDF itself — the deck currently attributes it to "DORA 2025". Download the primary DORA PDF and reconcile attribution. (Both Pax passes flagged this independently.)
- **Scrum.org "Agent Efficiency"**: body JS-gated; verified via search summaries. Manually open before quoting verbatim.
- **METR follow-up**: the famous 19% is the 2025 RCT (solid); the 2026 follow-up is selection-biased per METR itself — cite the RCT, not the follow-up, and don't present 19% as a stable constant.
- **"Ouyang et al. 2026 SkCC 40% formatting penalty"** and the vault's METR attribution: single-source, unverified — do not put on a slide.
- **Bill Gates "aircraft weight" quote**: attribution unverifiable — cite the idea, not the name.
- **Gartner 40%-canceled-by-2027**: triangulated via two syndications of the press release; primary bot-gated.
- Cost-per-task dollar figures vary 3-4x across sources — illustrative ranges only, labeled as such.

## Sources (detail + per-claim confidence)

- `research/2026-07-13-storm-note-measuring-squad-success.md` — STORM synthesis, contradiction map, full URL list (vault copy: `aa2brain/concepts/measuring-squad-success-agentic-delivery.md`)
- `research/2026-07-13-storm-lens-researcher-economist.md` — METR, DORA, Faros, GitClear, DX Core 4, Scrum.org, token economics, Gartner, judgment-bottleneck
- `research/2026-07-13-storm-lens-skeptic-historian.md` — Jeffries, #NoEstimates, Goodhart, Holub/Beck/Fowler, ToC/Reinertsen, LOC→function-points precedent, GitLab async, sustainable-pace history
- `research/2026-07-13-aa2brain-survey-agentic-metrics.md` — vault concept inventory (30+ notes read), theme coverage/confidence, unwritten `token-budget-as-sprint-capacity` flag
- `~/Documents/Last30Days/agile-metrics-velocity-story-points-ceremonies-ai-coding-agents-raw-v3.md` — social corpus (68 items: Reddit/HN/GitHub/X/YouTube) + web supplements
