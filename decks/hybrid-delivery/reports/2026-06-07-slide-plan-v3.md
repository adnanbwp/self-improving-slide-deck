# Slide Plan: Hybrid Delivery Deck
**Version:** v3 (build spec for v1.5.0)
**Date:** 2026-06-07
**Author:** Coda (via Larry, inline)
**Inputs:**
- Feedback ledger: `decks/hybrid-delivery/reports/2026-06-07-feedback-v1.4.0.md`
- Research brief v3: `decks/hybrid-delivery/research/2026-06-07-research-brief-v3.md`
- Prior slide plan: `decks/hybrid-delivery/reports/2026-05-30-slide-plan-v2.md`
- Base build: `decks/hybrid-delivery/versions/v1.4.0/canonical.html`
- Slide vocabulary: `shared/slide-vocabulary.md`

---

## Global directives (apply to every slide)

- **G-1 IM-only:** every "DM" / "IM/DM" → "IM" (Iteration Manager). Update `pov.md` audience.
- **G-2 No SVG diagrams:** rebuild Slides 17, 18, 23, 25 as native HTML/CSS (was-numbers 17/18/22/27). Timeline SVG retired with Wave 1.
- **G-3 No Wave narrative:** remove the Wave 1/Wave 2 framing entirely. No backward/recession reference anywhere, including the CTA.

---

## v1.5.0 slide order (32 slides: 26 main + Team + 5 appendix)

| new # | was # | status | type | content / change |
|---|---|---|---|---|
| 1 | 1 | CARRY | Title | No change. |
| 2 | 2 | CARRY | Statement | "The jobs question is settled. The structure question isn't." No change. |
| 3 | — | **NEW** | List/Ladder | **Agent Capability Maturity.** 5 rungs, human-role anchored, labelled synthesis. (Content below.) |
| 4 | 8 | MOVE | Image+Claim | Chat vs agent. "Chat ends when you stop typing. Agents don't." |
| 5 | 9 | MOVE | Image+Claim | The loop. "The loop runs until it hits a gate you designed." |
| 6 | 23 | MOVE | Stat | Squad gap. 441% PR-review increase (DORA 2025). Now the early problem-setter. No content change. |
| 7 | 24 | MOVE+EDIT | Comparison | Locate yourself. **Soften criteria to plain language** — no forward-refs to HITL/ceremonies/governance. |
| 8 | 3 | MOVE | Comparison | Adoption 83% vs Integration 55%. "Wide. Not deep." |
| 9 | 4 | MOVE | Question | "What actually happens when a delivery team runs with AI — not beside it?" |
| 10 | 5 | CARRY | Stats | Evidence +40% / 25% / 3×. |
| 11 | 6 | CARRY | Stats | Counter-evidence (Malone). |
| 12 | 7 | CARRY+FIX | Stats | <40% redesign (McKinsey). **Remove stray half-width horizontal line (design defect).** |
| 13 | 13 | EDIT | Comparison | Generate vs govern. **Strip "Wave 2" eyebrow** → new eyebrow (e.g. "What's happening now"). Content kept. |
| 14 | 14 | EDIT | Stats | Governance gap. **Make the population explicit:** "84% of agile teams use AI tools / 49% have governance guardrails" (Digital.ai n=350). |
| 15 | 15 | CARRY | Comparison | The Boundary (generate / cannot decide). |
| 16 | 16 | EDIT | Statement | Centaur. **Eyebrow → "Centaur Teams".** **Fix headline overflow** (3-line wrap hides source — resize/relayout so source sits in-bounds). IM-only. |
| 17 | 17 | REBUILD | List | HITL pattern selector. **SVG → HTML/CSS.** IM-only. Content kept (3 patterns). |
| 18 | 18 | REBUILD+EDIT | Comparison | The Fork. **SVG → HTML/CSS.** IM-only. **Remove "PM takes prioritization"** from fragmentation path. |
| 19 | 10 | MOVE | List | The Collision (5 failure modes). Relocated into Arc 4 (between Fork and Capabilities). Content kept. |
| 20 | 19 | CARRY | List | Three capabilities. |
| 21 | 20 | **REWRITE** | List | Ceremony redesign → **VERDICT-pillar → IM-cadence mapping.** (Content below.) |
| 22 | 21 | CARRY | List | Governance failure modes (Replit/Meta). |
| 23 | 22 | REBUILD | List/Ladder | **AI Governance Maturity** ladder (Unseen→Observed→Controlled→Autonomous). **SVG → HTML/CSS.** IM-only. Title made distinct from Slide 3. |
| 24 | 26 | CARRY | List | Action: this week (squad audit questions). |
| 25 | 27 | REBUILD | Process | 12-month path. **SVG → HTML/CSS.** IM-only. |
| 26 | 28 | EDIT | CTA | **Remove the "roles that survived 2022" line; replace with a forward-looking close.** Keep "Own the decisions agents can't make" + squad-audit CTA. |
| 27 | 29 | CARRY | Team | The Team. |
| 28 | 30 | CARRY | Divider | Appendix. |
| 29 | 31 | CARRY | Stats | App A — Malone in full. |
| 30 | 32 | CARRY | Stats | App B — Wave 1 sources (kept as live-Q&A backup despite G-3). |
| 31 | 33 | CARRY | Stats | App C — governance incidents. |
| 32 | 34+25 | MERGE | List | App D — full credential landscape. **Fold the curated 3 (was Slide 25) in as the "start here" rows** mapped to deck capabilities. |

---

## New content — Slide 3: Agent Capability Maturity

**Eyebrow:** "Age of Agents" · **Title:** "Agent Capability Maturity"
**One-line takeaway (load-bearing):** *As agents mature, the human's job shifts from doing the work → steering it → governing it. Gatekeeping becomes auditing.*
**Source line (small):** *Synthesis; autonomy-level framing after Feng, McDonald & Zhang (Univ. of Washington, 2025); cf. SAE J3016, Cloud Security Alliance 2026.*

| Rung | Human's role | One line |
|---|---|---|
| 1 Assisted | Operator | Human does the work; AI suggests and speeds discrete steps (autocomplete, draft, summarize). |
| 2 Augmented | Reviewer | AI drafts and recommends actions; the human executes and edits. |
| 3 Collaborative | Supervisor | AI plans and executes a task alongside the human, who steers and can grab the wheel. |
| 4 Orchestrated | Architect | Multiple agents hand off with shared memory; the human sets the gates and escalation. |
| 5 Autonomous | Governor | Agents run end-to-end; the human monitors, audits, holds the kill-switch. |

**Speaker note must state:** this is a synthesis of industry maturity models (Microsoft, Salesforce, Adaline, Bessemer); the rung *labels* are vivid shorthand, the *substance* is the human-role escalation, which is independently grounded (UW, CSA, SAE). This ladder pre-arms Slide 17 (HITL patterns) and Slide 15 (the boundary). Keep distinct from Slide 23 (AI **Governance** Maturity — different axis: how well the org governs, not what the agent can do).

---

## Rewritten content — Slide 21: Ceremony redesign via VERDICT

**Eyebrow:** "Practice Changes" · **Title:** "Governance isn't a new ceremony. It's the old ones, upgraded."
**Frame:** the VERDICT 7-pillar governance model, mapped onto the IM's existing cadences. Attribute as a practitioner model (Srivastav & Saxena, 2026); the cadence mapping is the deck's own synthesis.

| VERDICT pillar | IM cadence | What the IM does |
|---|---|---|
| V — Validation | Definition of Done / Sprint Planning | Bake "which agent actions need a human gate before execution" into the DoD. |
| E — Evidence | Daily Scrum | Review agent action logs as part of the deviation check. |
| R — Runtime control | Backlog / WIP / stop-the-line | Define the kill-switch protocol and escalation thresholds. |
| D — Decisions | Retrospective | Make agent decision-rationale a retro input; debug reasoning failures. |
| I — Identity | Working agreements / RACI | Every agent gets a named human owner. |
| C — Cost & Compliance | Sprint review | Track agent spend + compliance alongside velocity. |
| T — Transparency | Stakeholder reporting | Make agent activity legible to stakeholders — a dashboard line, not a black box. |

(7 pillars is a lot for one slide — Coda may foreground 4–5 highest-impact pillars as primary blocks and group the rest, rather than a 7-row list. Keep it scannable.)

**Speaker note must flag:** VERDICT is a single-source practitioner heuristic; present the pillars as an actionable scaffold, not validated research. Borrow credibility from the documented incidents on Slide 22.

---

## Narrative-integrity notes for Rex (re-audit targets)

1. **Wave 1 scaffold removed** — confirm the structural argument (13→14→15) still stands without the historical precedent that previously made it credible.
2. **Locate-yourself moved early (Slide 7)** — confirm the softened criteria no longer forward-reference unexplained concepts.
3. **Collision moved to Slide 19** (after Fork, before Capabilities) — confirm a "problem" slide reads correctly there amid "solution" slides; alternative home is before Capabilities/after Boundary if it jars.
4. **Fork (Slide 18)** — confirm the fragmentation path still balances after removing the PM/prioritization item.
5. **CTA (Slide 26)** — confirm the forward-looking close lands the PoV without the 2022 callback.

---

## Production order for Coda (Pass 2)

1. Copy `versions/v1.4.0/` → `versions/v1.5.0/`.
2. Apply G-1 (IM-only) globally first.
3. Delete Wave 1 slides; renumber per table.
4. Build new Slide 3; rewrite Slide 21; rebuild Slides 17/18/23/25 in HTML/CSS.
5. Apply edits (eyebrows, clarity, design-defect fixes, CTA).
6. Merge credentials into App D.
7. Run humanizer on all modified text + speaker notes.
8. Hand changed slides to Iris for any image re-brief (Slides 4/5 images carry forward unchanged).
