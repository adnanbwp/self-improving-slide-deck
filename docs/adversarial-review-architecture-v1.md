# Adversarial Review: Proposed Architecture vs Mission & Objectives
*Reviewer: Vera (Adversarial Critic)*
*Subject: Architecture proposed in brainstorming session 2026-05-25*
*Status: Open — gaps to be resolved before design proceeds*

---

## Context

This review tests the architecture proposed during the initial brainstorming session against the mission and objectives document (`docs/mission-and-objectives.md`). Six attacks were identified. Three are critical or high severity and must be resolved before any deck work or design begins.

---

## ATTACK 1 — The team doesn't exist yet, and the mission depends on it

**Severity: Critical**

The mission requires Rex (logic audit), Vera (adversarial), and Aria (audience persona) to function. None of them have been hired. The architecture names them as if hiring is a minor detail. Until their contracts are written, reviewed, and activated, the engine has no adversarial layer, no logic audit, and no audience scoring. The mission's four-dimensional quality score collapses to one dimension (research) until this is resolved.

**Architectural gap:** No SOP exists for hiring these specialists. No research brief on what world-class looks like for each role. No timeline.

**Required resolution:** Hiring Rex, Vera, and Aria must be step one of implementation — before any deck work begins. Nolan must brief Pax for each role, Pax researches what world-class looks like, Nolan drafts the contracts, Adnan approves.

---

## ATTACK 2 — The self-improvement cycle has no memory of why decisions were made

**Severity: High**

When Pax finds new research or Vera finds a new counter-argument, the cycle produces a PR. But nothing in the architecture records *why* the previous version was the way it was. Was that argument already considered and rejected? Was that source assessed and found unreliable? Without decision memory, the engine re-litigates the same ground every cycle.

**Architectural gap:** `decks/<topic>/research/` holds synthesis briefs but there is no decision log — a record of what was considered, what was decided, and why.

**Required resolution:** Add `decisions.md` to every deck's folder structure. This file logs: what was considered, what was decided, why. Vera reads it before running her adversarial pass. Pax reads it before researching. This is the engine's long-term memory per topic.

**Resolved 2026-05-25:** `decisions.md` added to the per-deck folder spec (`docs/deck-folder-spec.md`). Template at `myPKA/Team Knowledge/Templates/decisions-template.md`. Each specialist logs their own decisions; entries are included in the cycle PR for Adnan's approval. Vera and Pax read `decisions.md` before starting any pass.

---

## ATTACK 3 — aa2brain integration has no defined schema contract

**Severity: High**

The mission says research synthesis gets written back to aa2brain as `raw/articles/` and derived notes. But aa2brain has a strict SCHEMA.md — domain tags, pillar tags, epistemic tags, confidence levels, frontmatter conventions. The architecture says nothing about how engine output conforms to that schema. The "quality gate" is mentioned but undefined: who runs it, what does it check?

**Architectural gap:** If Silas writes a synthesis brief to aa2brain without conforming to SCHEMA.md, it breaks the vault's integrity. The gate is a name without a procedure.

**Required resolution:** The quality gate into aa2brain must be a named SOP owned by Silas that validates engine output against SCHEMA.md before any write. Until that SOP exists, no automatic writes to aa2brain.

**Resolved 2026-05-25:** SOP-003 written at `myPKA/Team Knowledge/SOPs/SOP-003-aa2brain-quality-gate.md`. Silas owns the gate. Seven validation steps: domain relevance, type/directory, frontmatter, filename, wikilinks, source traceability, write + log. Off-domain engine research stays in `decks/<topic>/research/` and never reaches aa2brain.

---

## ATTACK 4 — Token tracking is architectural debt from day one

**Severity: Medium**

The mission requires token and cost tracking at three levels (session, deck, cycle). The architecture says each specialist logs tokens to `logs/costs.jsonl`. But Claude Code does not expose per-call token counts in a way agents can self-report reliably. Specialists cannot know their own consumption — the harness does.

**Architectural gap:** Self-reporting by agents is unreliable. The mechanism for capturing token usage is undefined.

**Required resolution:** Mack must design the token tracking mechanism as part of the engine build — not deferred. Options: Claude Code hooks that capture usage, session-close estimates based on model and approximate context size, or manual tracking as a starting point. The architecture must pick one before implementation.

**Deferred 2026-05-25 — Phase 2:** Deliberately deferred by Adnan. The engine can be set up and run without token tracking; this creates a known governance gap (no ROI visibility, no cost-per-cycle data) but does not block any other capability. Mack picks this up when the engine is operational and the governance layer is prioritised.

---

## ATTACK 5 — The engine is not applying its own methodology to itself

**Severity: Medium**

The mission explicitly states: *"every decision the team makes — including tool choices, framework selections, and process design — must pass the same research, argument, persuasion, and adversarial tests."* The architecture proposes the HTML framework as TBD. The specialist roster was designed without a Pax research brief. Nolan hasn't validated the team structure against world-class standards.

**Architectural gap:** The architecture was designed by one agent reasoning from first principles, without adversarial review, evidence scoring, or argument audit. The engine is not eating its own cooking.

**Required resolution:** Before implementation begins, the team must run a scored review of: (a) the HTML framework choice, (b) the specialist roster, (c) the folder structure — using the four-dimensional scoring rubric. This review *is* the engine's first self-application.

**Resolved 2026-05-25:** Scored review completed. Pax researched HTML framework options (Reveal.js selected — see `docs/engine-decisions.md`). Rex audited roster (4/10) and folder structure (5/10). Vera attacked both (7/10 and 6.5/10). Findings addressed: Deck Author specialist hired (closes the production gap); Aria scoped to scoring only (no self-marking); folder spec rewritten with shared assets, audience variant convention, scorecard naming, reports/ rename, deprecation status; disagreement protocol and PR legibility defined. Engine decisions documented in `docs/engine-decisions.md`.

---

## ATTACK 6 — No per-deck engagement model

**Severity: Low-Medium**

The mission says Adnan is a team member, not just an approver. But the design has no mechanism to distinguish decks where he wants to be hands-on from decks he delegates. If the engine runs autonomously on a VPS, Adnan may not see a deck until a PR arrives — by which point many cycles may have run without his directional input.

**Architectural gap:** No engagement model per deck. No way to declare "check with me before each cycle" vs "run autonomously."

**Required resolution:** Each deck's `pov.md` should carry an `engagement_level` field: `autonomous`, `collaborative`, or `co-author`. The engine's behaviour in each cycle adjusts accordingly.

**Resolved 2026-05-25:** `engagement_level` (`autonomous` | `collaborative` | `co-author`) and `status` (`active` | `archived` | `overturned`) fields defined in `pov.md` — see `docs/deck-folder-spec.md`. The two fields are independent: engagement level controls how the cycle runs; status controls whether the deck is live at all. Behaviour per level documented in the folder spec.

---

## Summary Scorecard

| # | Attack | Severity | Must resolve before |
|---|---|---|---|
| 1 | Team doesn't exist yet | **Critical** | Any deck work |
| 2 | No decision memory per deck | **High** | First improvement cycle |
| 3 | aa2brain schema contract undefined | **High** | Any write to aa2brain |
| 4 | Token tracking mechanism undefined | Medium | Engine build |
| 5 | Engine not applying own methodology | Medium | Design finalised |
| 6 | No per-deck engagement model | Low-Medium | VPS deployment |

---

## Next Steps

Address attacks in severity order before proceeding to design:
1. Resolve Attack 1 — hire Rex, Vera, Aria via Nolan
2. Resolve Attack 2 — add `decisions.md` to deck folder spec
3. Resolve Attack 3 — Silas drafts aa2brain quality gate SOP
4. Resolve Attack 4 — Mack designs token tracking mechanism
5. Resolve Attack 5 — run scored review of architecture decisions
6. Resolve Attack 6 — add `engagement_level` to `pov.md` spec

*This document is version-controlled. It should be updated as each attack is resolved.*
