# Decisions Log — Delivery Leadership in Human+AI Hybrid Teams

Persistent memory for this deck across all improvement cycles. **Vera reads this before every adversarial pass. Pax reads this before every research sweep.** Specialists do not re-litigate a Closed decision without citing new evidence — if new evidence surfaces, flag it to Larry rather than silently opening the decision again.

Each entry is written by the specialist who owns the decision and is included in the PR for the cycle in which the decision was made.

---

## 441% is Faros AI telemetry, not DORA — 2026-07-14 | Pax

**What was decided:** The 441% PR-review-time figure (and incidents/PR +242.7%, the per-dev output figures) attributes to Faros AI's telemetry (22,000 devs, 4,000+ teams), never to "DORA 2025". Verified against primaries; v2.1.1 exists solely to correct this in the live deck. Faros vintages differ (2025 vs 2026 values) — cite the year, never merge into one range.

**Why:** The DORA 2025 primary PDF does not contain the figure; Faros's own text distinguishes its telemetry from DORA's survey. Full table: `research/2026-07-14-verification-gate-v3.md`.

**Status:** `Closed`

## Measurement act is woven, not a standalone act — 2026-07-14 | Aria

**What was decided:** The delivery-measurement material lives inside Beats 3–4 of the Man-in-a-Hole arc (crisis: velocity decoupled; climb: what you measure now). No standalone measurement act; the deck keeps one arc at the 21-body-slide ceiling. The 04→06 fold stands with a binding guardrail: the chatbot→acts line is the first line on the loop slide's face.

**Why:** A second act rebuilds the framework plateau the v2.1.0 recut demolished and regresses One-arc. Spine + addendum: `reports/2026-07-13-narrative-spine-vnext-proposal.md`.

**Status:** `Closed`

## Sensors-vs-decisions is the A2 answer; closure needs field evidence — 2026-07-14 | Vera

**What was decided:** Slide 12 concedes the telemetry dashboards to engineering and claims only the decision layer (what counts as done, planned review capacity, WIP caps, the stakeholder reporting contract). On that basis the standing Critical A2 is downgraded to a Significant residual (adversarial 8.0). The residual — exclusivity of the decision column — closes only with field evidence: a real IM holding those calls in a live agentic squad. The CTA's pilot is designed to generate it. Do not re-assert "the tech lead does not contest this" anywhere.

**Status:** `Closed` (residual tracked, not re-litigable without pilot data)

## The two frameworks are proposals; Scrum.org is not a token-budget precedent — 2026-07-14 | Rex

**What was decided:** The Attention Budget and Token-Budget-as-Sprint-Capacity present as Adnan's proposals carrying the three-strut warrant (grounded need / proven mechanism / explicit synthesis), token budget subordinate to attention budget on separate slides. Scrum.org's "Agent Efficiency" article contains no token/compute-budget recommendation (verified) and must not be cited as precedent. Framework spec: `reports/2026-07-14-token-budget-framework-design.md`.

**Status:** `Closed`

## Deck hygiene: no pipeline meta-language; appendix is the Q&A arsenal — 2026-07-14 | Larry (from Adnan)

**What was decided:** No research/plan meta-language in any deck artifact (gap codes, reviewer names outside credits, confidence audit-trail phrasing) — enforced by the greppable eval checklist in `reports/2026-07-14-slide-plan-v4.md`, run before any commit of deck HTML. The appendix is deliberately generous: full detail for solo readers and live Q&A, with each main-line note pointing to its appendix backup.

**Status:** `Closed`

## Template selection: Monochrome (Ivory Ledger) — 2026-05-29 | Larry

**What was considered:** Three candidates from the design library — Monochrome (Ivory Ledger), Cobalt Grid, Cartesian.

**What was decided:** Monochrome (Ivory Ledger).

**Why:** Highest native slide-type coverage (all 10 types native or Strong — no Moderate adaptations on critical slides). Archival/research-grade editorial register matches the PoV tone (credible, measured, not performative). Analytically oriented IM/DM audience trusts a register that reads as written rather than produced. Dark theme preserves the canonical Jost/Lora/JetBrains Mono font stack without substitution.

**Options not taken:** Cobalt Grid rejected — cobalt-to-jade substitution in dark theme significantly weakens defining identity; four Comparison slides (the deck's structural spine) require structural adaptation. Cartesian rejected — warmest register but 10 of 20 slides require structural adaptation; no native Stat display suitable for the deck's key evidence moments.

**Status:** `Closed`

<!-- Add new entries above this line, newest first -->
