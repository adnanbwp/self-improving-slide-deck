---
id: measuring-squad-success-agentic-delivery
tags: [agility, delivery, hybrid-teams, pillar-3, contested, angle-candidate]
aliases: ["velocity after agents", "agentic squad metrics", "attention budget", "agile cadences agentic era"]
created: 2026-07-13
modified: 2026-07-13
contested: true
confidence: medium-high
source-method: STORM five-lens research (Practitioner via last30days social corpus; Researcher/Economist and Skeptic/Historian via Pax web-grounded passes, 2026-07-13)
---

# Measuring Squad Success & Redesigning Agile Cadences in Agentic Delivery

**Frame:** When agents complete the middle of the work (construction), what should a delivery team measure as squad success — and what happens to velocity/story points, WIP, sustainable pace, and the agile ceremonies? Researched for Iteration/Delivery Managers who must keep owning delivery outcomes, not only the human-AI governance boundary.

## The one-line synthesis

Velocity per developer and velocity per squad have **decoupled**: individual output is up sharply while team-level delivery is flat or degrading — so the honest unit of measurement moves from construction output (points, velocity) to the flow of judged, durable outcomes through the human judgment constraint (review/verification), and the cadences survive by **shrinking and decoupling** into judgment rituals, not by dying or by wearing an AI sticker.

## Key findings per lens

### Practitioner (social corpus, last 30 days)
- The bottleneck inversion is a live practitioner question in exactly these words: "AI is producing our increment faster than we can refine the backlog. Is Scrum still the right frame" (r/scrum, 33 comments, 2026-06-23).
- Review fatigue is the felt sustainable-pace problem: "The AI burns the toast, I scrape it"; r/ExperiencedDevs asks "Has AI made developers less collaborative in your team?" (282 pts).
- Teams are improvising the successor system: deterministic checks before human review, humans reserved for "intent and design", risk-scores routing which PRs get a human, async standup digests, AI-native boards where agents are first-class teammates (Paca, 174 HN pts).

### Researcher
- **METR RCT (2025):** experienced OSS devs 19% *slower* with AI on familiar code while believing they were 20% faster — individual speedup is context-dependent, and perception is unreliable. (High confidence; follow-up cohort data is methodologically fragile.)
- **Faros AI telemetry (22k devs, 1,255 teams):** tasks/dev +21-34%, PRs/dev up to +98%, while bugs/dev +54% and incidents per PR +242.7%; median PR review time +441% YoY. Individual gains are not reaching org throughput ("AI Productivity Paradox").
- **DORA 2025:** AI is an *amplifier* of existing strengths/dysfunctions; DORA's response is a **capabilities model** (7 conditions), explicitly not a new velocity number.
- **GitClear (623M changes):** refactoring collapsed 21%→3.8% of changed lines, duplication +81%, churn +15% — code durability is falling as AI writes more of the code. Durability (30/60/90-day survival) is a candidate honest metric.
- **Scrum.org's own pivot:** "From Velocity to Agent Efficiency" — retire velocity as vanity metric, don't story-point agent work, budget agents in tokens/compute, measure outcomes via Evidence-Based Management.

### Skeptic
- Velocity was broken **before** agents: Ron Jeffries ("I may have invented story points, and if I did, I'm sorry now"), #NoEstimates (2012), Goodhart's law. AI *exposes and raises the cost of* the pretence; it does not create the flaw.
- The strongest counter to "agents changed everything": the constraint was **never construction** — it is human comprehension (Khononov applying Theory of Constraints; Stack Overflow blog "The new bottleneck").
- "WIP capped by human review capacity" is Reinertsen/ToC flow control (2009/1980s) pointed at a new constraint — the mechanism is old, only the constraint moved. This is *good news for delivery managers: they are already fluent in the discipline that governs the new bottleneck.*
- Manifesto-author dissent is against killing *agility*, not preserving ceremonies: Holub ("AI Makes Agile Irrelevant! 🙄" — discipline matters more), Beck (agents as "genies"; tests as immutable truths), Fowler ("Agents can generate code faster than humans can manually inspect it" — move humans from in-the-loop to on-the-loop).

### Economist
- Token spend is becoming a real budget line: enterprise AI spend ~$1.2M (2024) → ~$7M (2026) despite ~280x per-token price falls; $150-250/dev/month typical, heavy shops $500-2,000. Gartner: >40% of agentic projects canceled by end-2027 (costs/value/risk).
- The "agile is dead" narrative has named commercial sponsors (Capgemini EVP, McKinsey video, AWS "Intent Design") — vendors selling the successor. Forrester's 95%-still-relevant counter-survey has its own incentives. Triangulate, don't adopt either.
- What becomes scarce when construction is ~free: judgment, specification quality, review attention (convergent essay genre + Kent Beck's "augmented coding": vision, strategy, task breakdown, feedback loops).
- **Supervision tax quantified:** Glean Work AI Index (6,000 workers): AI saves ~11 hrs/wk, ~6.4 hrs go back into "botsitting" (~58% erosion); 69% admit shipping unverified AI work.

### Historian
- Precedent: LOC died as a metric when construction cost per unit of function decollapsed (1980s) → function points → flow metrics. Output-volume metrics die when construction gets cheap; flow/outcome metrics succeed them. Velocity is next in that lineage.
- Story points were born (XP, Chrysler C3) as a *defensive euphemism* to stop stakeholders over-indexing on hours; they degenerated into performance management (SAFe itself warns against velocity as a performance signal).
- Sustainable pace was XP's "40-hour week" → Manifesto Principle 8; it protected the scarce resource of the era (programmer energy). The agentic-era equivalent scarce resource is **attention/judgment capacity** — but no Manifesto author has made that bridge explicitly (inference, not their words).
- Cadence precedent: trunk-based dev + feature flags already decoupled deploy from release; GitLab's async handbook shows standups survived remote work by shrinking and going async. **Ceremonies survive by shrinking and decoupling, not disappearing** — the sprint stopped being a release gate but kept being a planning/forecasting rhythm.

## Contradiction map (the tension that makes this non-obvious)

1. **"Velocity is now meaningless" vs "velocity was always broken".** Scrum.org/McQueen say agents killed it; Jeffries/#NoEstimates/Goodhart say it was already dead. Resolution: agents made the pretence *unaffordably expensive* — an agent can inflate points infinitely at near-zero cost, so Goodhart gaming goes vertical.
2. **Individual speedup vs team slowdown.** BCG/P&G RCTs and vendor telemetry show real individual gains; METR shows slowdowns and org-level gains cluster ~10%. Resolution: the gains are real *and conditional* — on task type (generative vs decision) and on **level** (individual vs squad). Squad-level measurement is where the truth lives.
3. **"Replace the ceremonies" vs "keep the ceremonies".** AWS/Capgemini (sellers of the successor) vs Holub/Fowler/GitLab precedent. Resolution: the *coordination function* survives; the *content and metrics* inside each ceremony must be rebuilt around agent evidence (logs, eval results, attention budget) — neither an AI sticker on old practices nor a bonfire of them.
4. **"WIP limits are the answer" vs "that's just ToC".** Both true: mechanism decades old, constraint new (human review). The novelty claim should be modest; the fluency claim (flow discipline is delivery managers' home turf) is the leverage.
5. **Governance framing vs delivery framing of the same role.** Owning the human-AI boundary (governance) risks ceding delivery accountability; but the measurement evidence (incidents/PR, durability, review queues) says delivery outcomes are exactly what needs an owner. The two are one job: govern the boundary *because* you own the delivery outcome.

## Genuinely open territory (no published framework found)

- **A named "attention budget" / human-supervision WIP framework does not exist in the literature** (July 2026). Glean quantifies the cost; Scrum.org gestures at token budgets for agent capacity; nobody has formalized *human review capacity as the planned, budgeted constraint of a hybrid squad*. Original-framework territory.
- **Token-budget-as-sprint-capacity**: same status — referenced as an idea, never written up as a framework.
- Story-point validity under AI implementation: being studied (FORGE '26, arXiv 2602.13766) but no published numbers extracted yet.

## Sources

- **METR RCT (2025-07-10):** https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ — **URL:** primary, RCT
- **METR follow-up / bias note:** https://metr.org/blog/2026-02-24-uplift-update/ — **URL:** primary
- **DORA 2025 report:** https://dora.dev/dora-report-2025/ — **URL:** primary landing (PDF gated); AI Capabilities Model: https://dora.dev/ai/capabilities-model/report/
- **Faros AI (441%, 242.7%, decoupling):** https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025 — **URL:** vendor telemetry
- **GitClear Maintainability Gap:** https://www.gitclear.com/the_ai_code_quality_maintainability_gap — **URL:** primary
- **Scrum.org, Velocity → Agent Efficiency:** https://www.scrum.org/resources/blog/velocity-agent-efficiency-evidence-based-management-ai-era — **URL:** primary (body JS-gated; verify before verbatim quote)
- **Ron Jeffries, Story Points Revisited:** https://ronjeffries.com/articles/019-01ff/story-points/Index.html — **URL:** primary
- **Vladik Khononov, AI Doesn't Fix Your Real Bottleneck:** https://vladikk.com/2026/02/23/ai-toc-bc/ — **URL:** primary
- **Martin Fowler, Humans and Agents:** https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html — **URL:** primary
- **Allen Holub, AI Makes Agile Irrelevant! 🙄:** https://blog.holub.com/p/ai-makes-agile-irrelevant — **URL:** primary
- **Kent Beck / Pragmatic Engineer:** https://newsletter.pragmaticengineer.com/p/tdd-ai-agents-and-coding-with-kent — **URL:** primary interview
- **Glean Work AI Index (botsitting):** https://www.cio.com/article/4183804/the-hidden-cost-of-enterprise-ai-6-4-hours-a-week-babysitting-bots.html — **URL:** secondary of primary survey
- **Gartner 40% cancellations:** https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 — **URL:** primary press release (bot-gated; triangulated)
- **InfoQ Manifesto-obsolete debate:** https://www.infoq.com/news/2026/02/ai-agile-manifesto-debate/ — **URL:** independent reporting
- **GitLab async ceremonies:** https://about.gitlab.com/blog/2021/03/02/agile-for-remote-work/ — **URL:** primary
- **Steven Thomas, sprints as release-organising:** https://itsadeliverything.com/are-sprints-just-a-way-to-organise-releases — **URL:** primary practitioner
- **Huy Tieu, We Built Agile to Manage Slow Building:** https://huytieu.com/blog/ways-of-working-ai-era/ — **URL:** primary practitioner
- **r/scrum bottleneck-inversion thread:** https://www.reddit.com/r/scrum/comments/1udqffq/ai_is_producing_our_increment_faster_than_we_can/ — **URL:** practitioner corpus
- **r/ExperiencedDevs collaboration thread:** https://www.reddit.com/r/ExperiencedDevs/comments/1uecvi7/has_ai_made_developers_less_collaborative_in_your/ — **URL:** practitioner corpus
- **FORGE '26 SPACE/GenAI longitudinal study:** https://arxiv.org/pdf/2602.13766 — **URL:** peer-reviewed (numbers not yet extracted)
- Full lens files with per-claim confidence: `decks/hybrid-delivery/research/2026-07-13-storm-lens-researcher-economist.md`, `2026-07-13-storm-lens-skeptic-historian.md`, `2026-07-13-aa2brain-survey-agentic-metrics.md` (self-improving-slide-deck repo); raw social corpus: `~/Documents/Last30Days/agile-metrics-velocity-story-points-ceremonies-ai-coding-agents-raw-v3.md`

## Related
- [[pr-review-as-primary-engineering-constraint]] · [[botsitting-tax]] · [[coding-not-bottleneck-ai-exposes-constraints]] · [[the-80-percent-problem]] · [[human-sandwich]] · [[workflow-collision]] · [[four-loop-architecture-taxonomy]] · [[conductor-vs-orchestrator]] · [[spec-driven-development]] · [[verdict-framework]] · [[four-new-agentic-org-roles]] · [[token-budget-as-sprint-capacity]] (unwritten — flagged twice in vault)
