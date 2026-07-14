# Design — Token Budget as Sprint Capacity

---
date: 2026-07-14
author: Adnan Ali (framework) with Larry (facilitation)
status: draft for Adnan's review
consumers: aa2brain concept page; hybrid-delivery v3.0.0 (proposal slide, paired with the Attention Budget); Adnan's org pilot
---

## What it is

A governance and cost-control instrument for hybrid (human + agent) squads: the squad's agentic capacity is planned, spent, and reviewed as an explicit **dollar budget per sprint**, built bottom-up from a per-role rate card. It operationalises VERDICT's C-pillar (Cost & Compliance) and replaces velocity as the number spend is read against — spend sits next to **judged outcomes**.

The name keeps "token budget" because tokens are what agents consume; **dollars are the ledger** because they survive tokenizer and model changes (see vault: `claude-sonnet-5-tokenizer-inflation`) and natively speak to stakeholders.

## The three parts

### 1. Rate card (the budget's structure)

Every squad member gets a fit-for-purpose agentic allocation — not just developers. In an AI-SDLC, agents amplify BAs, UX designers, QA engineers, Iteration/Delivery Managers, and other leads, each with a different model/effort profile (vault: `model-vs-effort-claude-code` is the operational foundation).

- Each **role** maps to a **tier** (frontier / mid / fast models, effort level) fit for that role's work.
- Each role-tier maps to a **$/sprint rate** (industry precedent: the $X/dev pattern reported at large tech firms, generalised to $X/squad-member).
- **Squad token budget per sprint = Σ (headcount × role rate).**

The rate card is the squad's to tune; the budget is the sum, owned by the Iteration Manager.

### 2. Breach semantics (the teeth)

Hitting the budget mid-sprint is a **decision trigger**, not a hard stop and not a mere signal:

- The budget owner (IM) makes a named, logged decision: **top-up** (with stated reason), **descope**, or **downgrade tier** for the remaining work.
- Nothing halts automatically; critical work never stalls on an accounting rule.
- Every breach decision is visible at sprint review.

This mirrors WIP-limit breach semantics from Lean flow practice (Reinertsen): the limit exists to force a conversation at the moment of constraint, not to brake the system.

### 3. Review contract (where it reports)

- Burn vs budget is reported at **sprint review, next to judged outcomes** (shipped, verified PBIs) — never next to raw output.
- Trend over sprints belongs to the IM's squad-health reporting (sensors may be engineering dashboards; the **decisions and the reporting contract are the IM's**).
- Explicit Goodhart guard: the budget is a **constraint, not a score**. Under-spend is not a virtue; over-spend is not a sin; unexplained variance is what triggers questions.

## Growth path (not in v1)

Named as the maturity direction, deliberately not proposed for day one:

1. **Cost-per-judged-outcome trending** across sprints (unit economics per PBI).
2. **Routing rules** — work classes pre-mapped to tiers at refinement time.
3. **Eval-gated top-ups** — breach top-ups conditioned on eval pass-rates, closing the loop with quality.

## Warrant (the three struts — per Rex condition S2)

1. **Grounded need:** enterprise AI spend rose ~$1.2M (2024) → ~$7M (2026) despite ~280x per-token price falls; Gartner predicts >40% of agentic projects canceled by end-2027 on cost/value/risk; typical per-dev agent spend $150–250/month, heavy shops $500–2,000 (sources in `decks/hybrid-delivery/research/2026-07-13-storm-lens-researcher-economist.md` §E1).
2. **Proven mechanism:** budget-with-breach-decision semantics are Reinertsen/ToC flow control; per-head dollar allocation is established industry practice ($X/dev). Nothing mechanically novel — deliberately.
3. **Explicit synthesis (the original part, claimed as a proposal):** (a) whole-squad, role-rated scope — agentic capacity as a property of the squad, not the developers; (b) the pairing of spend with *judged outcomes* rather than velocity/output; (c) the companion **Attention Budget** on the human side. Verification note: Scrum.org's "Agent Efficiency" article does **not** contain a token-budget recommendation (verified 2026-07-14, `research/2026-07-14-verification-gate-v3.md`) — do not cite it as precedent; this synthesis is Adnan's.

## Relationship to the Attention Budget

Two sides of one capacity model for a hybrid squad:

| | Attention Budget | Token Budget |
|---|---|---|
| Caps | Human review/judgment capacity | Agent spend capacity |
| Scarce resource | Attention (hrs/sprint) | Dollars (tokens) |
| Breach means | Stop pulling agent work | Top-up / descope / downgrade |
| Reports at | Sprint review, next to review-queue health | Sprint review, next to judged outcomes |

Deck treatment: separate slides (Rex S3 — don't overload one slide); token budget subordinate to attention budget in narrative order (attention is the binding constraint per the research; tokens are the purchasable one).

## How it lands (consumers)

1. **Vault concept page** `aa2brain/concepts/token-budget-as-sprint-capacity.md` — Adnan's voice, `adnan-perspective` + `pillar-3` tags; closes the broken wikilink flagged by four notes.
2. **Deck (v3.0.0):** one proposal slide, explicitly framed as Adnan's proposal ("here is my answer, pilot it with me"), CTA = baseline as homework, pilot as invitation (Vera S6). No invented budget numbers on-slide; the $/dev industry figures may appear as context with their sources, labeled as ranges.
3. **Org pilot (later):** one squad, one sprint baseline (measure current burn, build the rate card), two sprints with breach semantics live. Out of scope for this design.

## Failure modes designed against

- **Reporting theatre** (signal-only) — rejected at design time; breach must trigger a logged decision.
- **Goodhart inversion** (budget becomes a performance score) — explicit constraint-not-score rule in the review contract.
- **Tier sandbagging** (roles hoard frontier-tier access) — rate card is squad-tuned and revisited at retro, not fixed by fiat.
- **Unit drift** (tokenizer/model changes silently rewriting the budget) — dollars as ledger.

## Success criteria

- The concept page exists in Adnan's voice and the wikilink graph resolves.
- The deck slide survives Rex's three-strut warrant test and Vera's "who else uses this?" attack with the recovery line: *"Nobody yet — the mechanism is 15 years old, the synthesis is mine, and I'm running the pilot."*
- An IM outside this project could run the pilot from the concept page alone.
