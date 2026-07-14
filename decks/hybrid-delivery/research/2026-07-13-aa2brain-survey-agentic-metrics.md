---
date: 2026-07-13
author: Pax
mission: >
  In-depth survey of the aa2brain Obsidian vault for material relevant to updating
  the "hybrid-delivery" slide deck (The Iteration Manager in the Age of Agents,
  v2.1.0) — focused on the deck's new gap: delivery measurement and ways of working
  in agentic squads (velocity/story points, WIP, sustainable pace, agile cadences,
  the "strong middle" shape, squad success measurement).
vault_snapshot_date: 2026-07-09 (latest vault commit; verified via `git log` on
  /mnt/c/Users/adnan/Google Drive/aa2brain, checked 2026-07-13)
---

# aa2brain Survey — Agentic Delivery Metrics & Ways of Working

## Methodology

1. Read `SCHEMA.md` for vault taxonomy/navigation, then `pov.md` and the v2.1.0
   narrative spine (`decks/hybrid-delivery/reports/2026-07-02-narrative-spine-v2.1.0.md`)
   in this repo to calibrate what the deck already argues (PR-review bottleneck,
   generate-vs-decide boundary, VERDICT, centaur/HITL patterns) so I don't re-surface
   what's already load-bearing.
2. Used `git log --since="2026-07-02" --name-only` (not `find -newermt`, which returned
   near-every file in the vault — likely a sync/clone touched all mtimes) to get an
   accurate "what's new" list. The vault's most recent commit is 2026-07-09.
3. Ran targeted `rg` searches across `concepts/`, `entities/`, `comparisons/`,
   `queries/`, and `30 Permanent Notes/` for each theme's keywords (story point,
   velocity, WIP, sustainable pace, cycle time, flow metric, standup, retro, sprint
   planning, Definition of Ready/Done, capacity planning, predictability, throughput,
   taste, judgment).
4. Read every note that surfaced as a plausible hit — 30+ notes in full — prioritizing
   depth over breadth per Larry's brief.
5. Distinguished note types throughout: **Adnan's own synthesis/fleeting notes**
   (marked "Adnan-authored") vs **literature notes citing one external source**
   vs **filed queries synthesizing multiple sources**.

## Limits

- I did not open every file in `raw/`, `Readwise/`, or `Literature Notes/` individually
  — I worked from the concept/comparison/query layer (the vault's own synthesis layer)
  and only dropped into `raw/` when a concept's sourcing needed checking. If Adnan
  wants the raw article text itself for a specific claim, flag it and I'll pull it.
- `find -newermt` gave a false signal (whole-vault mtime touch, likely from the
  Google Drive sync or a bulk restore commit on 2026-07-05 that reconciled 88
  "local-only" notes). I used `git log --since` instead, which is accurate to the
  commit history but will miss any uncommitted local edits.
- Themes 1–4 (velocity/story points, WIP, sustainable pace, cadences) have **no
  notes that name Scrum/Kanban delivery metrics directly** except one Adnan fleeting
  note and one pre-existing concept page — see Gaps below. Most of the load-bearing
  material for these themes has to be **inferred/adapted** from adjacent concepts
  (botsitting tax, PR-review bottleneck, workflow collision, human sandwich) rather
  than lifted verbatim, and I've flagged that inference clearly per note.

---

## Theme 1 — Velocity & Story Points: Value and Alternatives

**Coverage: thin and indirect.** No note in the vault does a head-on "story points
are dead, here's what replaces them" argument. The closest material is either
Adnan's own unpublished fleeting insight, or evaluation/cost concepts that function
as candidate alternative metrics.

- **`00 Inbox/Product Backlog Item is the unit of valuable work and not a task.md`**
  (also duplicated in `100 Inbox/`) — Adnan-authored fleeting note, created
  2026-04-30 (predates the July window but never promoted to a concept page — worth
  flagging as a live gap in his own PKM).
  > "Reading the book 'Flow Metrics For Scrum', I had a realization that the tasks
  > that the team creates to work on, and moves from step to step on the board are
  > not the unit of value. It is in fact the Product Backlog Item (PBI) which is the
  > unit of value. Therefore, metrics measuring the flow should measure the progress
  > of the PBI, and not the task."
  External source cited inline: the book *Flow Metrics For Scrum* (no author/URL
  captured). **Relevance: High** — directly answers "what should we measure instead
  of task-level velocity," and it's Adnan's own voice, which the deck can quote
  verbatim as the presenter's-scar beat material.

- **`concepts/eval-hard-product-smell.md`** (2026-07-02, lit. note on Hamel Husain's
  blog) — argues eval difficulty is a product-design failure, not a measurement
  failure; ships concrete "verifiable artifact" design patterns (surface intermediate
  work, show the query, flag what couldn't be verified).
  > "When teams say 'our product is hard to eval,' it signals that the product
  > wasn't designed for verifiability."
  **Relevance: Medium-High** — reframes "eval pass rate" as a metric that only works
  if you designed for verifiability in the first place; useful caveat for the deck if
  it proposes eval-pass-rate as a velocity replacement.

- **`concepts/vibe-coding-agent-evaluation-dimensions.md`** (2026-06-28, course
  notes) — seven measurable dimensions for agent output quality: intent satisfaction,
  functional correctness, visual/behavioural correctness, **cost & efficiency
  (tokens, latency, iteration count)**, code quality, trajectory quality, self-repair.
  > "Cost & efficiency (tokens, latency, *iteration count* — 1 turn vs 8 corrections
  > is a different product)."
  Cited sources: SWE-bench, Vibe Code Bench, Kaggle SAE benchmarks (all named,
  none independently verified by me). **Relevance: High** — this is the most
  concrete "outcome metric" candidate set in the vault; iteration count is a genuine
  flow-metric analogue for agent work.

- **`comparisons/tests-vs-evaluation-for-ai-systems.md`** (2026-06-28) — the
  tests-vs-evals distinction operationalized: "Tests catch deterministic
  regressions; evaluation catches behavioural drift." **Relevance: Medium** —
  foundational vocabulary if the deck wants to argue eval-pass-rate is a legitimate
  velocity substitute, but it's about code quality, not delivery throughput per se.

- **`concepts/agentic-evaluations-at-scale.md`** (2026-07-08, YouTube notes on
  Kaggle) — names the eval-scarcity problem (30K researchers building evals for
  30M+ workers) and four platform responses (hackathons, standardized agent exams,
  Game Arena, benchmarks). **Relevance: Low-Medium** — infrastructure story, not a
  squad-level metric; useful only as "the industry is still building the
  measurement tooling" evidence.

- **`concepts/llm-cost-tracking-tools-2026.md`** (2026-07-02, lit. note on
  Braintrust) — three layers of cost tracking (token counts → span-level tracing →
  tag-based grouping by feature/user/workflow); explicit "cost-quality feedback
  loop" workflow. **Relevance: Medium** — closest thing in the vault to
  "cost-per-outcome" as a delivery metric, but framed for engineering-org cost
  governance, not sprint reporting.

- **`concepts/verification-loop-closed-agent-coding.md`** (2026-07-08, lit. note on
  IronBee experiment) — quantifies that a cheap model + verification loop matches a
  frontier model's quality at ~1/7th the cost ($2.40 vs $15/run).
  > "The wall wasn't coding ability — it was absence of ground truth."
  **Relevance: Medium** — a concrete cost-per-outcome data point (single-source,
  n=1 experiment, explicitly caveated by the author as not yet ablated).

- **Broken wikilink found:** two notes (`llm-cost-tracking-tools-2026.md`,
  `eval-hard-product-smell.md`'s neighbourhood) reference `[[token-budget-as-sprint-capacity]]`
  as a "Related" concept — **this page does not exist in the vault**. It's a
  concept Adnan has named in his own head (or in conversation) but never written.
  Flagging as both a gap and an opportunity: the exact "story points →
  token budget" reframe the deck needs may already be half-formed in his notes
  elsewhere (check `raw/` or daily notes) but isn't captured as a concept page yet.

**Theme 1 confidence:** Low-Medium overall coverage; what exists is credible
(mostly `confidence: high` frontmatter) but nothing directly answers "what replaces
story points."

---

## Theme 2 — WIP and Parallel Agent Workstreams

**Coverage: strong, concentrated in three new notes plus one pre-existing anchor.**

- **`concepts/four-loop-architecture-taxonomy.md`** (2026-07-08, lit. note on
  Aparna Dhinakaran/@seldo, sourced from AI Engineer World's Fair discourse) — maps
  five loop types (Execution, Task/Ralph, Product/Software-Factory, System/
  Autoresearch, Oversight) and states autonomy is "a dial that exists separately on
  every loop."
  > "Addy Osmani: 'Inner loop is capability. Outer loop is agency.'" ... "Even
  > inside Anthropic, the team running Tag reports being bottlenecked on reviews —
  > the checkpoint humans kept for themselves is now the constraint."
  **Relevance: High** — gives the deck vocabulary for "how many loops can a human
  actually oversee at once," i.e. the real WIP-limit question for a hybrid squad.
  Names a live debate (Zach Lloyd/Roland Gavrilescu "ratchet autonomy" vs Geoffrey
  Litt/Paul Bakaus "there is no auto") worth flagging as contested.

- **`comparisons/conductor-vs-orchestrator.md`** (2026-06-28, course notes,
  Addy Osmani framing) — Conductor (real-time, one agent, fine-grained) vs
  Orchestrator (async, many agents in parallel, goals not instructions); failure
  modes named for each (throughput bottleneck vs losing the thread on the
  judgment-heavy 20%). **Relevance: High** — directly maps to "how many parallel
  workstreams can one IM/engineer run before quality degrades" — the WIP-limit
  question restated as a mode choice, not a number.

- **`raw/articles/workflow-collision.md`** + its concept page
  **`concepts/workflow-collision.md`** (pre-existing, created 2026-05-19, predates
  the July window but core to this theme) — names the structural incompatibility
  between Kanban WIP-limited pull-based team flow and agent state-machine
  lifecycles, and proposes composition (agent lifecycle nested inside the team's
  "In Progress" column) as the fix.
  > "Collapse agent states into six Kanban columns and you lose guardrails. Expand
  > your board to match the agent lifecycle and you drown your human team." ...
  > "One optimizes for learning velocity. The other optimizes for execution
  > correctness."
  External sources cited: Webframp (webframp.com), Paul Stack's "six parallel
  workstreams across eight days" case study (stack72.dev). **Relevance: High** —
  this is the single best answer in the vault to "how does WIP change with agents,"
  and it's the most citable single artifact for a slide on redesigning the board.

- **`concepts/seven-components-long-running-agents.md`** (2026-07-03, YouTube
  lit. note) — component 4, "Outer Loop," and component 5, "Orchestration," are
  directly about running many agents/long tasks without losing track; explicit
  warning that model-choice-per-role (planner vs executor vs evaluator) is itself
  an architecture decision. **Relevance: Medium-High** — operational detail under
  the WIP question (how many agents can run unattended, what catches drift).

- **`concepts/claude-tag-proactive-multiplayer-agents.md`** (2026-07-03, YouTube
  lit. note on Anthropic) — Claude Tag as a persistent, proactive teammate that
  self-schedules follow-ups over days/weeks/months and runs multiple parallel
  workstreams inside one Slack channel; ~65% of Anthropic's product-org PRs now
  written by Tag. **Relevance: Medium-High** — concrete "many parallel workstreams"
  example, but it's a vendor case study (single company, self-reported), not
  independently verified — treat as illustrative, not proof.

**Theme 2 confidence:** High coverage, good triangulation (three independent
sources — Anthropic, Webframp/Stack72, Osmani/AI Engineer — converge on "parallel
agent work needs a different flow-control model than human WIP limits").

---

## Theme 3 — Sustainable Pace: Human Attention as the Scarce Resource

**Coverage: strong — this is the best-covered theme in the whole survey.**

- **`concepts/botsitting-tax.md`** (2026-07-04, digest of Glean Work AI Index +
  HN discussion) — **the single most load-bearing new note for this theme.**
  Quantifies the supervision tax: AI saves ~11 hrs/week, ~6.4 hrs go straight back
  into supervision (~58% erosion of the raw saving); only 13% say AI significantly
  improved company performance despite 87% daily use.
  > "Botsitting is the hidden labour of making AI usable: feeding it context,
  > checking its outputs, debugging errors, cleaning up its work, and switching
  > between tools." ... "Leading organisations don't spend *more* time using AI —
  > they spend more time on the work *around* it: setting context, defining quality
  > bars, building judgment, and deciding what should **never** be automated."
  Sources: Glean Work AI Index (6,000 workers, US/UK/AU — named, primary), HN
  thread 48490057 (281 pts). **Relevance: High.** This is the direct evidentiary
  base for "sustainable pace = protecting the supervision budget," not raw hours.

- **`concepts/pr-review-as-primary-engineering-constraint.md`** (2026-07-04,
  digest of Codacy + HN AskHN thread) — quantifies the engineering-specific version:
  PR volume +29% YoY, agentic PRs queue 5.3× longer, 31% of PRs merge with zero
  review, trust in AI accuracy down to 29% (Stack Overflow 2025 survey — named,
  independently sourced from the PR-volume data).
  > "The self-driving-car complacency failure, applied to code." ... "If reviewing
  > a swarm of agent PRs is your full-time job and they're 'good enough' 95% of the
  > time, you stop paying attention and bad changes slip through."
  **Relevance: High** — this note likely already underpins the deck's existing
  "441% PR review time" stat (per the v2.1.0 narrative spine); worth checking
  whether the deck's number traces to LinearB/CircleCI/Faros as cited here or to a
  different source — recommend verifying before reusing.

- **`concepts/continuous-code-review-three-tiers.md`** (2026-06-28) — three-tier
  review architecture (managed → hybrid → custom) as the structural answer to
  review-fatigue; explicit "the right starting point for most teams" call on
  tier 2. **Relevance: Medium-High** — gives the deck an actionable mechanism, not
  just a diagnosis.

- **`concepts/coding-not-bottleneck-ai-exposes-constraints.md`** (2026-06-05,
  predates window but central) — four-practitioner panel (Shalloway, Zuill, Müller,
  Bernstein) argues coding was never the bottleneck; cites Anthropic's internal May
  2026 data (>80% AI-authored code, 8× more code shipped, review now the binding
  constraint — an "Amdahl's Law" for hybrid teams).
  > "If you're making developers 10x faster at writing bad code, you've just made
  > the problem worse." (Shalloway)
  **Relevance: High** — the deepest-rooted articulation of "human attention is the
  scarce resource," and it triangulates independently against botsitting-tax and
  pr-review-as-constraint (three separate source chains — Glean, Codacy/LinearB/
  Faros, and this panel/Anthropic — all converge on the same claim).

- **`concepts/uncomfortable-truths-ai-coding-agents.md`** (2026-07-03, HN
  discussion, `contested: true`) — names skill-atrophy/complacency as one of four
  contested structural risks, with the same self-driving-car analogy independently
  arrived at (palmotea/jonah on HN, not the same people as the Anthropic panel).
  > "AI-assisted coding is at Level 2–3 autonomy while being treated like Level 5."
  **Relevance: Medium-High** — good counter-evidence/tension material; explicitly
  marked contested in frontmatter, so cite it as "debated," not settled.

**Theme 3 confidence:** High. Three to four independent source chains (Glean
survey, Codacy/LinearB/Faros PR data, a four-practitioner panel + Anthropic
internal data, and an HN discussion) converge on the same underlying claim: **human
review/supervision capacity, not agent output, is the sustainable-pace ceiling.**

---

## Theme 4 — Agile Cadences: Survive, Transform, or Replace?

**Coverage: moderate, mostly indirect — no note directly asks "do standups/retros
survive," but several supply the "bolt-on vs. redesign" framing the deck needs.**

- **`concepts/human-ai-team-tooling-category.md`** (2026-07-04, digest of Paca HN
  launch) — argues AI-native PM tooling is becoming its own category rather than a
  feature bolted onto Jira/Linear; direct "feature vs architecture" framing.
  > "Adding 'AI assist' to Jira is a feature. Rebuilding the board so an agent has
  > a first-class identity, a queue, an accountability trail, and a review gate is
  > an **architecture** — and architectures spawn categories."
  **Relevance: High** for the "AI sticker on old practices" angle — this is close
  to verbatim the bolt-on-vs-redesign distinction Larry asked about, just phrased
  for tooling rather than ceremonies.

- **`entities/paca.md`** (2026-07-04, entity page, single HN-launch source) — Paca:
  open-source Jira alternative treating agents as first-class Scrum teammates
  participating directly in sprint planning, task assignment, and spec-writing.
  **Relevance: Medium-High** as a concrete existence proof, but **confidence:
  medium, single source (HN launch post)** — do not cite adoption/success claims,
  only "such a tool exists and got traction" (162 HN points, 57 comments, ~1.5k
  GitHub stars).

- **`concepts/four-new-agentic-org-roles.md`** (2026-07-04, digest of MIT Tech
  Review + AWS video) — four new human roles around every agentic deployment
  (Agent Supervisor, Eval Owner, Exception Handler, HITL Reviewer); explicit
  "rebuild, not patch" framing citing McKinsey's ~75%-of-roles-need-redesign
  estimate. **Relevance: High** for reframing what an Iteration Manager's ceremony
  responsibilities decompose into — standups/retros may survive as the *venue*
  where these four roles report, even if their content changes.

- **`concepts/workflow-collision.md`** (2026-05-19, see Theme 2) — same note, but
  its Planning point applies here directly: "Team: just-in-time, collaborative.
  Agent: upfront, verified. Both are right in their context." **Relevance: High**
  — this is the clearest existing statement that sprint planning doesn't disappear
  but forks into two different planning acts (team-level and per-agent-task-level).

- **`concepts/definition-of-ready-can-be-harmful-for-new-scrum-teams.md`**
  (2026-05-19, lit. note on Maarten Dalmijn) — pre-agent-era argument that DoR used
  dogmatically blocks value delivery for immature teams. **Relevance: Low-Medium**
  — background/pre-agentic context only; worth citing as the *classical* counter-
  argument the deck can update ("DoR gets *more* important, not less, once an
  agent's task needs a machine-readable spec" — see Theme 5's spec-driven-development
  note), but this note itself doesn't mention agents.

- **`queries/hybrid-human-ai-teams-june-2026-digest-2026-06-15.md`** (2026-07-04,
  filed synthesis) — Adnan's own through-line synthesis across five sources:
  > "The teams pulling ahead aren't using AI *more* — they're investing in the work
  > *around* it and designing explicit roles and tooling for the seam between human
  > and agent."
  **Relevance: High** — this is Adnan's own synthesis (not a lit. note), directly
  usable as deck narration; it explicitly names the [[human-sandwich]] as "where
  2026's real hybrid-team design happens."

**Theme 4 confidence:** Medium. No note names standups/retros/reviews by name and
asks whether they survive; the vault's coverage is one level up (org roles and
tooling categories), so the deck will need to make the "so what does this mean
for the daily standup specifically" leap itself — flagged as a **gap** below.

---

## Theme 5 — The "Strong Middle" Shape

**Coverage: this is the deepest and best-triangulated theme in the whole vault.**
Multiple independent frameworks converge on the same shape (humans at the
start/end, agents in the middle) using different vocabulary.

- **`concepts/ai-driven-sdlc-phase-transformation.md`** (2026-06-28, course notes)
  — **the single best slide-ready artifact for this theme.** A phase-by-phase table
  of "what AI changes / what stays human" across the full SDLC.
  > "AI doesn't speed up the old SDLC uniformly — it **compresses it unevenly**.
  > Implementation that took weeks now takes hours, while requirements,
  > architecture, and verification remain stubbornly human-paced." ... "What stays
  > constant is human judgment, taste, and the skill to verify AI output."
  **Relevance: Very High** — this table *is* the strong-middle argument, phase by
  phase, ready to adapt into a slide.

- **`concepts/human-sandwich.md`** (2026-05-26, pre-existing, YouTube lit. note
  crediting Kieran/Every) — three-layer model: Human (Frame) → AI (Collapse) →
  Human (Judge and extend). Names the anti-pattern explicitly.
  > "The human sandwich explicitly locates human value at both ends of the
  > collaboration loop — not just at the start (tasking) but at the end
  > (judgment)." ... "The broken sandwich: human tasking without human judgment...
  > This produces high-volume, mediocre work — execution without taste."
  **Relevance: Very High** — this is the conceptual twin of "strong middle," same
  shape, independent source (Every/Kieran vs. the SDLC-phase course), which is
  good triangulation for the claim.

- **`comparisons/conductor-vs-orchestrator.md`** (2026-06-28, see Theme 2) — the
  failure modes named for each mode are exactly the edges of the strong middle:
  Conductor fails by becoming a throughput bottleneck (too much human in the
  middle); Orchestrator fails by "losing the thread on the judgment-heavy 20%"
  (too little human at the edges). **Relevance: High.**

- **`concepts/the-80-percent-problem.md`** (2026-06-28, course notes crediting
  Addy Osmani) — the sharpest single quantified claim: agents nail ~80% of the
  code, the remaining 20% (edge cases, ambiguous requirements, architecture) needs
  deep human judgment, and it's *invisible* because the code "looks right."
  > "A METR study could find experienced developers taking **19% longer** on
  > certain tasks with AI assistance: the time moved into verifying, debugging,
  > and correcting output."
  Cited source: METR study (named, not independently re-verified by me — flag as
  single-study, worth checking the original METR paper before quoting the 19%
  figure in a slide). **Relevance: Very High.**

- **`concepts/factory-model-of-software-production.md`** (2026-06-28, course
  notes) — "the developer's primary output is not code — it's the system that
  produces code"; frames the human as factory-manager/architect, not line-worker.
  **Relevance: High** — supports the "humans dominate start (design the system)
  and end (quality arbitration)" half of the strong-middle claim.

- **`concepts/spec-driven-development.md`** (2026-06-28, course notes) — "code is
  disposable," the spec is the reviewed/versioned source of truth; ties directly
  to Definition-of-Ready territory (a spec *is* a machine-readable DoR).
  > "Give the brain a *vibe* instead of a *blueprint* and it guesses — and guessing
  > is how 'Rogue Agent' incidents happen."
  Notable craft claim, single-source (Ouyang et al. 2026, cited as "SkCC" — I could
  not independently verify this citation; flag as **unverified, treat with
  caution** if the deck wants to quote the "40% performance drop" figure directly.
  **Relevance: High** for the "what/why belongs to humans" half of the theme.

- **`concepts/verdict-framework.md`** (2026-05-24, already referenced in the
  deck's Beat 4 per the narrative spine) — 7-pillar governance model; not new,
  but worth noting the vault's VERDICT page has not been updated since May 24 —
  if the deck cites VERDICT specifics, this is still the source of record and
  hasn't drifted.

- **`concepts/vibe-coding-agent-evaluation-dimensions.md`** and
  **`comparisons/tests-vs-evaluation-for-ai-systems.md`** (see Theme 1) — both
  reinforce "evaluation/acceptance is a human-owned judgment act," relevant to the
  "end" half of strong-middle.

**Theme 5 confidence:** High, well-triangulated. Four independent framings
(SDLC-phase table, human-sandwich, conductor/orchestrator, 80% problem) all locate
human value at the same two edges using different metaphors and different source
chains (a course, a YouTube essay, Osmani's own framing, and a METR-cited claim).
This is very likely the single strongest section of the whole survey to build new
slides from.

---

## Theme 6 — Squad Success: What Should an Iteration Manager Measure?

**Coverage: no note in the vault names "Iteration Manager" or proposes a
measurement dashboard directly** (checked via `rg -li "iteration manager|scrum
master|delivery lead|squad health|team health"` — no concept/entity/comparison/
query hits). Coverage here is assembled from adjacent material.

- **`concepts/four-new-agentic-org-roles.md`** (see Theme 4) — the four roles
  (Agent Supervisor, Eval Owner, Exception Handler, HITL Reviewer) are the closest
  thing to "what should be tracked" — each role implies a metric (supervision
  scope compliance, eval pass/fail rate, exception-closure time, approval
  latency). **Relevance: High**, but the mapping from roles → metrics is my
  inference, not stated in the source.

- **`queries/hybrid-human-ai-teams-june-2026-digest-2026-06-15.md`** (see Theme
  4) — Adnan's own through-line: "AI moved the bottleneck downstream from
  production to verification and supervision" — directly usable as the
  measurement thesis (measure the seam, not the output). **Relevance: High.**

- **`comparisons/conductor-vs-orchestrator.md`** — orchestrator-mode required
  skills ("specification, decomposition, evaluation, system design") read directly
  as a competency rubric for an Iteration Manager operating a hybrid squad.
  **Relevance: Medium-High.**

- **`concepts/ai-agents-stack-2026-six-layers.md`** (2026-07-02, lit. note on
  O'Reilly/Paolo Perrone) — names Eval & Observability and Guardrails as
  first-class stack layers with "the largest demo-to-production gap." **Relevance:
  Medium** — infrastructure-level, but useful if the deck wants to argue an IM's
  job includes owning/demanding these layers exist before trusting squad output.

- **`concepts/pr-review-as-primary-engineering-constraint.md`** and
  **`concepts/botsitting-tax.md`** (see Theme 3) — both supply concrete numbers
  (queue-time multipliers, % merged unreviewed, hours/week lost to supervision)
  that an IM could plausibly report as squad-health metrics instead of velocity.
  **Relevance: High**, though these are org-wide/industry benchmarks, not squad-
  level KPIs — the deck would need to adapt them into a per-squad measurement,
  which is itself the content gap.

**Theme 6 confidence:** Low-Medium. This is the theme most in need of
`storm-research` — the vault has good raw material on *what changed* but nothing
that directly answers "what does an Iteration Manager put in a weekly status
report for a hybrid squad."

---

## Recently created/modified (since 2026-07-02)

Full new-file list confirmed via `git log --since="2026-07-02" --diff-filter=A`
(87 new concept/entity/comparison/query files across 9 commits, 2026-07-02 through
2026-07-09). One-line descriptions for files not already covered above:

- `concepts/agents-as-new-saas-playbook.md` — the "agent-as-labor" SaaS business
  model (agents sold as headcount replacement, not software seats).
- `concepts/june-2026-ai-landmark-month.md` — a rollup framing June 2026 as an
  inflection point in AI adoption discourse.
- `concepts/self-improving-knowledge-loop.md` — agentic documentation that updates
  itself as code changes (meta-relevant to this very vault's own ingest pipeline).
- `concepts/claude-code-loop-primitives.md` — official Anthropic taxonomy of loop
  primitives in Claude Code (turn, goal, cron).
- `concepts/claude-opus-workflow-catalog.md` — catalog of 60 trigger-agent-
  verification workflow patterns.
- `concepts/context-engineering-three-layer-stack.md` — context engineering as
  the successor discipline to prompt engineering.
- `concepts/microsoft-frontier-tuning.md` — Microsoft's domain fine-tuning
  strategy.
- `concepts/ai-adopting-firms-hiring-more.md` — counter-narrative data point: AI
  adopters are net hiring, not shedding headcount.
- `concepts/subsidy-era-to-scarcity-era-ai-compute-shift.md` — macro shift from
  subsidized to scarcity-priced AI compute.
- `concepts/session-transcript-memory-overrated.md` — argues raw session
  transcripts are a weak memory substrate for agents.
- `concepts/agent-folder-structure-optimization.md` — best practices for
  structuring repos for agent navigation.
- `concepts/claude-code-skill-taxonomy.md` — nine categories of Claude Code
  skills.
- `concepts/claude-sonnet-5-tokenizer-inflation.md` — a tokenizer-cost gotcha
  specific to Sonnet 5.
- `concepts/confused-deputy-problem.md` — classic security problem reframed for
  agentic tool-calling.
- `concepts/ai-mystery-shopper-business-funnel.md` — using AI agents to audit a
  business's own customer funnel.
- `concepts/ai-tooling-software-engineers-2026.md` — Pragmatic Engineer's 2026
  AI-tooling survey results.
- `concepts/agent-tool-design-best-practices.md`, `agent-sessions-events-and-state.md`,
  `agent-memory-extraction-and-consolidation.md` — MCP/agent-infrastructure design
  patterns (memory, sessions, tool design).
- `concepts/agentic-security-red-blue-green-teaming.md`,
  `mcp-security-threat-landscape.md`, `seven-pillar-agent-security-architecture.md`,
  `zero-trust-agent-development.md`, `confused-deputy-problem.md` — a cluster of
  agent-security notes (course-derived, 2026-06-28) — not directly relevant to
  delivery metrics but relevant if the deck ever touches governance/risk reporting.
- `concepts/context-rot-and-history-compaction.md`, `mcp-architecture-hosts-clients-servers.md`,
  `harness-engineering-agent-equals-model-plus-harness.md`,
  `where-agent-instructions-live.md`, `codex-sites-disposable-web-apps.md` —
  agent-infrastructure/harness concepts, tangential to this deck's brief.
- Entities added: `addy-osmani`, `andrej-karpathy`, `antonio-gulli`,
  `boris-cherney`, `lee-boonstra`, `peter-steinberger`, `sokratis-kartakis`,
  `thariq`, `allie-k-miller`, `paca`, `glean-work-ai-index`, `google-antigravity`,
  `google-agents-cli`, `agent2agent-protocol`, `model-context-protocol`,
  `mai-thinking-1`, `openai`, `agent-engine-memory-bank`,
  `openai-agents-sdk-v0-18-0`, `copilotkit-channels-rename` — mostly named
  practitioners/entities backing the concept notes above; `paca` and
  `glean-work-ai-index` are the two most relevant to this deck (see Themes 3–4).
- Filed queries: `agent-security-and-evaluation-synthesis-2026-06-28`,
  `agent-tools-and-mcp-synthesis-2026-06-28`,
  `context-engineering-sessions-memory-synthesis-2026-06-28`,
  `cross-series-article-angles-2026-06-28`,
  `new-sdlc-vibe-coding-synthesis-2026-06-28`,
  `spec-driven-production-development-synthesis-2026-06-28` — five course-digest
  syntheses from a 2026-06-28 course-ingest batch (source: a bundled course, not
  individually re-verified against original video/text); plus
  `hybrid-human-ai-teams-june-2026-digest-2026-06-15` (Theme 3/4/6, covered above).

---

## Gaps (send to storm-research)

1. **Theme 1 — Velocity/story-point alternatives, direct.** Nothing in the vault
   argues head-on "story points break down at agent speed, here's the replacement
   metric framework." Adjacent material exists (eval-pass-rate dimensions, cost
   tracking, one Adnan fleeting note on PBI-vs-task) but no synthesized "flow
   metrics for agentic squads" piece. The referenced-but-never-written
   `token-budget-as-sprint-capacity` concept is the clearest signal Adnan already
   has the shape of this in mind — worth having storm-research chase down whether
   a source article prompted that (unwritten) title.

2. **Theme 4 — Agile ceremonies by name.** No note asks "do standups/retros/sprint
   reviews survive" directly. The vault has the one-level-up material (org roles,
   tooling categories, planning-collision) but the deck needs the ceremony-level
   translation itself — a genuine research gap, not just a synthesis gap.

3. **Theme 6 — IM/Scrum-Master-equivalent measurement dashboard.** No note
   proposes what a hybrid-squad status report should contain. This is the
   thinnest theme in the survey and the one most likely to need fresh external
   research (search terms to try: "AI-augmented team KPIs," "agentic delivery
   metrics dashboard," "Scrum Master role AI agents 2026").

4. **Sustainable pace, quantified for *non-engineering* roles.** Theme 3 is
   well-covered for engineers (PR review) and knowledge workers generally
   (botsitting), but nothing speaks specifically to Iteration-Manager-style
   coordination/planning fatigue as distinct from IC review fatigue.

5. Two of the strongest source citations in Theme 5 are **single-source and
   unverified by me**: the "40% performance drop from generic Markdown formatting"
   (attributed to "Ouyang et al. 2026, SkCC") and the METR "19% longer" study.
   Both are quoted in vault notes with `confidence: high` frontmatter, but I could
   not independently confirm either citation exists as stated — recommend a Pax
   or storm-research verification pass before either number appears on a slide.
