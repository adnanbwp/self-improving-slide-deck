---
agent_id: larry
session_id: hybrid-delivery-v3-build-and-deploy
timestamp: 2026-07-14T15:36:00+10:00
type: close-session
linked_sops: ["SOP-10-research-steeped-content"]
linked_workstreams: ["WS-006-slide-plan-design-selection"]
linked_guidelines: []
---

# hybrid-delivery v3.0.0: approval → build → gates → merge → deploy

## Context

Continuation of the overnight research session ([[2026-07-13-23-15_larry_hybrid-delivery-vnext-overnight-research]]). Adnan reviewed the morning report, approved the v3.0.0 direction, and the session ran the full cycle: framework brainstorm, verification gate, slide plan, design proposal, build, scoring gates, fix pass, merge, and deployment to slides.ahaagile.com.au.

## What we did

- Larry committed the overnight research batch on main; captured two new working preferences from Adnan as memory (no pipeline meta-language in deck artifacts, enforce with evals; generous appendix for solo readers and Q&A).
- Larry + Adnan brainstormed **token-budget-as-sprint-capacity** to an approved design (governance spine, dollar ledger, role-rated rate card across the whole squad, breach-as-decision-trigger, constraint-not-score): `decks/hybrid-delivery/reports/2026-07-14-token-budget-framework-design.md`.
- Penn drafted the vault concept page `aa2brain/concepts/token-budget-as-sprint-capacity.md` (closes the broken wikilink four notes referenced).
- Pax ran the verification gate: **441% is Faros AI telemetry, not DORA** (live-deck correction required); Scrum.org does NOT recommend token budgets (strut removed — the synthesis is Adnan's); FORGE '26 numbers extracted (+59.1% completed / +≈150% planned story points, activity flat). Follow-up pass verified slide-18 figures (Anthropic $150-250/dev/month primary; Gartner >40% wording confirmed).
- Coda shipped **v2.1.1** (attribution hotfix, four edits) and **slide plan v4**; Aria adjudicated the 04→06 fold (confirmed, with the binding chatbot→acts first-line guardrail); Iris delivered the WS-006 design proposal (both layout flags resolved, zero new images).
- Coda built **v3.0.0** (42 slides: 24 main line, 18 appendix) on a branch in a worktree; eval checklist, attribution audit, guardrail and screenshots all clean.
- Scoring gates on the built deck: **Rex 7.5** (all conditions landed), **Vera 8.0 — standing Critical A2 downgraded to Significant residual** (slide 12 "sensors aren't decisions" earns the re-rooting), **Aria 8/8 after the CTA fix pass, persuasion 8.5**.
- Coda's fix pass (payoff line to the CTA face, six-question count, decoupling-direction note, FORGE planned-points with Goodhart framing); Aria re-verified against the built slide before the flip.
- Silas normalized the storm note's frontmatter to house shape; the lesson saved to memory.
- Larry merged to main (`6c81d97`), recorded **five Closed decisions** in the deck's decisions.md, and deployed via `scripts/push.py` — v3.0.0 live and 200-verified at slides.ahaagile.com.au.

## Decisions made

All five are recorded canonically in `decks/hybrid-delivery/decisions.md` (SSOT — this log links, does not duplicate): Faros attribution; weave-not-bolt; sensors-vs-decisions as the A2 answer (closure requires field evidence); frameworks-as-proposals with Scrum.org excluded as precedent; deck hygiene (no meta-language + generous appendix).

## Insights

- **A content realignment doubled as an argument repair:** Adnan's delivery-measurement gap turned out to be the answer to the deck's oldest Critical (A2). Independent Rex/Vera convergence on the same flaw (asserted vs earned) validated the gate design.
- **The verification gate caught a live-deck factual error** (441%→DORA) that three prior scorecard passes missed — figure provenance checks belong before build, every cycle.
- **Concede-then-claim beats claim:** slide 12 wins by conceding the dashboards and claiming only the decision layer; Vera's motivated opponent "lands on a pre-printed concession."
- Coda's fix pass surfaced honest layout ceilings (7-card and CTA line budgets) and correctly escalated content tradeoffs instead of shrinking fonts — the "report rather than improvise" instruction worked.

## Realignments

None today — the session executed the realignment captured in [[2026-07-13-23-15_larry_hybrid-delivery-vnext-overnight-research]].

## Open threads

1. **Slide 06 personal story** — presenter personalisation still pending (carried from v2.1.0's slide 07).
2. **The pilot** — one real instance of an IM holding the boundary calls in a live agentic squad closes A2 outright and is the route to 9+ next cycle. The CTA is designed to generate it.
3. **Attention-budget concept page** — does not exist in the vault yet (Penn deliberately left it unlinked); candidate for Adnan's voice like the token-budget page.
4. **VPS wiki re-mirror** — the storm note's normalized frontmatter needs Adnan's one-liner re-run to sync `/opt/wiki`.
5. **Iris watch-item for next cycle** — slides 16–19 run four consecutive Cards layouts (visual monotony, not a story fault).
6. **Gartner primary page** remains bot-gated — manual browser check someday if a Gartner figure ever needs upgrading from Medium-High.

## Next steps

- Adnan: edit the two vault framework pages into his own voice; personalise slide 06; take the deck to work and start the pilot.
- Team: next improvement cycle opens with pilot data (A2 closure) and the Iris visual-rhythm item.

## Cross-links

[[2026-07-13-23-15_larry_hybrid-delivery-vnext-overnight-research]] · `decks/hybrid-delivery/decisions.md` · `decks/hybrid-delivery/reports/2026-07-14-slide-plan-v4.md` · `decks/hybrid-delivery/research/2026-07-14-verification-gate-v3.md` · scorecards `v3.0.0-{argument,adversarial,narrative,persuasion-canonical}.md`
