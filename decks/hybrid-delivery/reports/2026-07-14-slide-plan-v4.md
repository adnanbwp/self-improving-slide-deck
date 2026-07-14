# Slide Plan v4 — hybrid-delivery v3.0.0
**Version:** v4 (build spec for v3.0.0)
**Date:** 2026-07-14
**Author:** Coda (Deck Author)
**Gates on:** Adnan's approval → then design pass (Iris, WS-006). No HTML is written from this plan yet.

**Inputs (read in order):**
- Approved spine: `reports/2026-07-13-narrative-spine-vnext-proposal.md` (Man-in-a-Hole, measurement woven through Beats 3–4, +4/−3/−1, sharpened hook, reframed slide 19)
- Argument audit: `reports/2026-07-13-rex-audit-vnext-proposal.md` (B1; S1–S5; M1–M4)
- Pre-mortem: `reports/2026-07-13-vera-premortem-vnext-proposal.md` (C1; S1–S6)
- Verification gate: `research/2026-07-14-verification-gate-v3.md` (the ONLY source for figure attributions; FORGE '26 + Faros reconciliation now available)
- Research brief: `research/2026-07-13-research-brief-v4.md`
- Framework design: `reports/2026-07-14-token-budget-framework-design.md`
- Baseline deck: `versions/v2.1.0/canonical.html`

---

## Global directives (apply to every slide)

- **D-1 · Presenter-only notes.** Speaker notes carry only what a presenter uses in the room. **No** gap codes, **no** "Source confidence: X", **no** reviewer/specialist names (outside the credits slide), **no** "per Rex / per Vera", **no** audit-trail language. The build eval checklist at the end lists the greppable patterns a pre-merge check must reject.
- **D-2 · Claim-first headlines.** Every headline is a falsifiable claim, not a topic label.
- **D-3 · Attribution from the gate.** Every figure's `src` line uses the exact string from the verification gate's slide-ready table. Cite the year on the Faros split figures (2025 vs 2026). Never re-attribute the 441% to DORA (it is Faros telemetry).
- **D-4 · One home per fact.** A caveat lives on its strongest slide only; the appendix holds the full version. Main-line notes point to the appendix slide that answers the likely objection.
- **D-5 · Boundary thesis is primary; measurement serves it.** The deck still argues one thing — own the human-AI boundary because that *is* delivery ownership. The measurement thread deepens that hole and enriches the recovery; it is never a co-equal second argument.
- **D-6 · Version badge → v3.0.0.** Full re-audit version; prior scorecards do not carry.

---

## Slide-count reconciliation (why the math shifts +5/−3/−2, still net 0)

Aria's approved math was +4 / −3 / −1 = net 0, treating the two proposed frameworks as **one** slide. Rex S3 and the framework design both require the attention budget and the token budget to be **separate** slides (the weaker proposal must not ride the stronger). That makes the frameworks **+2**, so additions become **+5**.

To hold Larry's ceiling — main line at or below v2.1.0's 21 body slides — one further compression is required: **fold the "agent = acts" statement (old slide 04) into the loop slide's framing line** (old 06). Both ideas survive on one slide; nothing is dropped — the same move Aria already applied to 09+10. Net result:

- **+5** new main-line slides: strong-middle · velocity-decoupled · sensors-vs-decisions · attention budget · token budget
- **−3** moved to appendix (full, no claim dropped): autonomy ladder · bolt-on <40% · governance gap 84/49
- **−2** compressed: (09+10 → one) · (agent-acts folded into the loop)
- **Net 0.** Main line = **24 slides total → 21 body slides** (excluding title, CTA, credits). At the ceiling, not over it.

This +1/−1 delta from Aria's exact figure is purely the consequence of splitting the frameworks per Rex S3. Flagged, not silent — see Open Items.

---

## Main line (24 slides)

Legend: **CARRY** = content unchanged from v2.1.0 · **EDIT** = copy changes in place · **NEW** · **COMPRESS** · **REFRAME**.

---

### 01 · Title — CARRY (`t-title`, f-orange)
- **Headline:** "The Iteration Manager in the Age of Agents" (unchanged).
- **Change:** version badge → **v3.0.0**.
- **Note gist:** the question is not whether AI changed your job — it did — but whether you design that change or it gets designed around you; this deck argues the IM/DM is the natural locus for that design work, with evidence.
- **Appendix ref:** —

### 02 · Hook — REFRAME in place (`t-evidence`, f-paper)
- **Headline (claim):** "Your developers have never shipped more. Your squad's delivery hasn't moved."
- **Key content:** the decoupling *is* the hook — individual output up sharply while squad delivery stays flat. **Big number: 441%** (PR review time), framed as "the smallest part of the story." One tight reconciliation line, mandatory: **"Velocity didn't break today — agents just made gaming it free."** Do NOT use "less predictably" (no predictability metric exists in the research); the grounded claim is the decoupling — the squad converts less of its rising output into delivered, durable value. Keep the on-slide caveat that 441% is one triangulating signal, not the whole case.
- **`src`:** `Faros AI, "AI Engineering Report 2026" (22,000 devs, 4,000+ teams) — telemetry, not the DORA survey`
- **Note gist:** open here. The number a delivery manager can check in their own data is the shape, not the single figure — a velocity chart climbing while cycle-time and the review queue flatten. 441% is Faros's own telemetry (a common misattribution is DORA); it is the smallest part — the real story is that individual output and delivered value have come apart. Velocity was already a soft number before agents; agents didn't break it, they made inflating it free.
- **Appendix ref:** decoupling deep-dive (26); Jeffries lineage (27).
- **Budget flag (Iris):** `t-evidence .ctx` is ≤2 lines. Priority if space is tight: (1) decoupling claim, (2) the "gaming free" reconciliation line, (3) the 441 caveat. If all three won't fit `.ctx`, the reconciliation line becomes the headline's second sentence — do not drop it (it is what makes the Jeffries pre-concession on slide 08 amplify the hook rather than contradict it).

### 03 · Locate yourself — CARRY (`t-compare`, orange/paper)
- **Headline / tag:** "Locate Yourself" (unchanged).
- **Key content:** squad-is / you-are split; "that gap is the opportunity — you close it from inside the team, not by waiting for a mandate."
- **`src`:** —
- **Note gist:** recognition, not precision — most managers see their squad on the left and themselves on the right; the rest of the deck shows how to close the gap from inside.
- **Appendix ref:** wide-not-deep 83/55 (30).

### 04 · The loop (agent = acts, folded in) — COMPRESS (`t-figure`, f-paper)
- **Headline (claim):** "An agent doesn't stop when you stop typing. It loops until it hits a gate you designed."
- **Key content:** the agentic-loop diagram (`assets/images/slide-09-agentic-loop.png`). The old "agent = acts" statement folds in as the framing lead: a year ago "agent" meant a chatbot you prompt; now it means something that acts on its own, and the loop is what makes it different in kind. The gate — the human-in-the-loop decision point — is where the IM's governance sits.
- **`src`:** —
- **Note gist:** a chatbot stops when you stop typing; an agent receives a trigger, thinks, acts, observes, and decides whether to loop again — it runs until the task is done or it hits a gate you designed. That gate is the IM's opening. How far agents climb the autonomy spectrum is a fuller ladder (appendix).
- **Appendix ref:** autonomy ladder (33); chat-vs-agent anatomy (34).

### 05 · The strong middle — NEW (A) (`t-cards` cols-3, f-paper)
- **Headline (claim):** "Humans frame it. Agents build the middle. Humans judge what's good."
- **Key content:** a clean three — **Frame** (humans: the what and why — planning, intent), **Collapse** (agents: construction — the middle of the work, compressed), **Judge** (humans: what's good enough to ship). The mechanism for why the middle collapsed but the ends did not: on familiar work, the construction step is near-free; the binding constraint moved to judgment/review.
- **`src`:** `METR, "…Early-2025 AI on Experienced OS Developer Productivity" (July 2025 RCT) · shape: synthesis of SDLC-phase / human-sandwich / 80%-problem framings`
- **Note gist:** this is the best-triangulated idea in the research — four independent framings converge on the same shape. The point is the division of labour: agents own the construction middle; humans still own the framing at the front and the judgment at the end. That shape is what puts delivery back on the human-judgment boundary. Present METR's 19%-slower finding as one RCT's context-bound result on experienced devs and familiar code — not a fixed industry constant.
- **Appendix ref:** strong-middle / METR detail (29).

### 06 · First-person trust beat — CARRY (`t-statement`, f-ink)
- **Headline (claim):** "The first boundary I owned was one nobody was watching."
- **Key content:** the release-note-with-a-customer-name story; the fix wasn't more proofreading — it was naming who signs off before an agent ships.
- **`src`:** —
- **Note gist:** judgment shown, not cited. Presenter: swap in your own real boundary-ownership moment — a routine output handed to an agent, the one decision nobody owned, what it cost, the gate you designed in response. Under 30 seconds; it earns the argument that follows.
- **Appendix ref:** —

### 07 · Pivot question — CARRY (`t-question`, f-orange)
- **Headline (claim):** "What actually happens when a delivery team runs *with* AI — not beside it?"
- **Key content:** hold for a beat; the distinction is the argument.
- **`src`:** —
- **Note gist:** beside it = AI as a productivity tool in individual tasks (what most teams do); with it = the workflow redesigned so AI is a participant in the delivery system. The next slides give the performance evidence.
- **Appendix ref:** —

### 08 · Velocity decoupled / the broken metric — NEW (B) (`t-compare` has-head + has-annot, orange/paper)
- **Headline / seam-head (claim):** "Output and value came apart. Velocity now measures the wrong one."
- **Key content — the decoupling on the slide face (non-negotiable):**
  - LEFT (f-orange) "Individual output — up": PRs/dev **+98% (2025)**, tasks/dev **+21% (2025) / +33.7% (2026)**.
  - RIGHT (f-paper) "Squad delivery — flat or worse": incidents/PR **+242.7%**, bugs/dev **+54%**.
  - **annot-line (both reconciliations, mandatory):** "Different levels, same story — METR's 2025 RCT found experienced devs *19% slower* on familiar code. Velocity didn't break today; agents made gaming it free — Ron Jeffries said the number was soft back in 2012."
- **`src`:** `Faros AI telemetry (cite year) · METR (July 2025 RCT) · Scrum.org, "From Velocity to 'Agent Efficiency'" (2026) · Ron Jeffries / #NoEstimates (2012)`
- **Note gist:** the load-bearing claim is the decoupling, not "more code versus slower code." METR and Faros measure different levels — one is experienced devs on familiar repos in a controlled trial, the other is aggregate telemetry; both point at the same thing, the unit of work has come apart from delivered value. Velocity was already a soft number (Jeffries, who helped invent story points, said so); agents didn't create the flaw, they made inflating the number free — an agent produces points at near-zero cost, so the gaming goes vertical. Do not present 19% as a constant.
- **Appendix ref:** decoupling deep-dive incl. FORGE '26 (26); Jeffries lineage (27).
- **Budget flag (Iris):** the annot-line runs long. If it will not fit two lines cleanly, split its content: the METR level-reconciliation stays in the annot; the "gaming free / Jeffries" line moves up to sit under the seam-head. Both must remain on the slide face (this is the exact failure pattern the review is guarding against — a multi-source stack whose reconciliation hides in the notes).

### 09 · The advantage is real — and conditional on task type — COMPRESS 09+10 (`t-stat-grid`, f-paper)
- **Headline (claim):** "For complex, generative work the upside is real — and it is conditional on task type."
- **Key content (all four items must survive on the main line):**
  1. one upside stat with the qualifier **welded to it**: **+40%** quality uplift, human+AI vs solo — *for complex, generative work*.
  2. the Malone counter as the *source* of the conditional: **90%** of the 106 studies tested decision/classification tasks — exactly where human+AI underperforms the best solo performer.
  3. the explicit "real **and** conditional" statement (a highlighted card).
  4. pointer to the full reconciliation.
- **`src`:** `BCG RCT · Organization Science 2026 (n=758) · Malone et al. · Nature Human Behaviour 2024 (106 studies)`
- **Note gist:** surfacing the counter-evidence proactively is a credibility signal. The reconciliation is the task-type split: BCG/P&G measured generative, open-ended work (the ~10%); Malone's meta-analysis is mostly decision and classification tasks (the 90%), where adding AI degrades the call. Both are correct in their own domain. If you drop the "for complex, generative work" qualifier, the Malone challenge cannot be answered. Full breakdown in the appendix.
- **Appendix ref:** Malone in full (28).

### 10 · Generating vs governing — CARRY (`t-compare` has-annot, orange/paper)
- **Headline / tag:** "What's Happening Now" — "The automation is here. The governance gap is where the IM gets bypassed."
- **Key content:** left = what agents generate now (drafts, stories, tracking, reports); right = what nobody governs (design choices, risk thresholds, approval gates, production calls).
- **`src`:** —
- **Note gist:** the left column is demonstrable today; the right column is the accountability gap. If nobody governs the right column, the tech lead fills it de facto because they own the tooling — that is quiet erosion of the IM's standing, and it is the IM's opening if they occupy it.
- **Appendix ref:** governance gap 84/49 (31); bolt-on <40% (32).

### 11 · The boundary — CARRY (`t-compare` has-annot, orange/paper)
- **Headline / tag:** "The Boundary" — "The boundary is not permanent. The job is to own it right now."
- **Key content:** agents generate (drafts, tracking, analysis, coverage) / agents cannot decide (risk tolerance, approval gates, production, competing stakeholders, ethical edge cases).
- **`src`:** —
- **Note gist:** the hinge. "Not permanent" disarms the objection that AI will eventually cross this line too — yes, it will; the argument is about right now. The right column is what requires human judgment today, and that is the IM's accountability.
- **Appendix ref:** —

### 12 · Sensors aren't decisions — NEW (C) · the crux (`t-compare` has-head + has-annot, orange/paper)
- **Headline / seam-head (claim):** "Agents didn't retire your job. They moved it from the metric to the decision the metric forces."
- **Key content — the sensors/decisions cut on the slide face:**
  - LEFT (f-paper) "Engineering reads the signals": incidents/PR, code churn, durability, review latency — the telemetry, on the tech lead's dashboards.
  - RIGHT (f-orange) "You own the decisions the signals force": what counts as *done*; planned review capacity; WIP caps; what the sprint commits to; the stakeholder reporting contract.
  - **annot-line (the warrant, explicit):** "Whoever owns the delivery outcome owns these calls — and capping flow to a moving constraint has always been delivery-management craft, not tooling."
- **`src`:** `Signals: Faros AI, GitClear · the decisions are flow control — Reinertsen / Theory of Constraints (mechanism, decades-old)`
- **Note gist:** the split is the whole point. Engineering owns the sensors — the health readouts live in their dashboards, and that is fine. What the IM owns is the operating decisions those readouts force: what the squad calls done, how much review capacity is planned, where WIP is capped, what gets reported to stakeholders and how. Those are delivery-management decisions, not engineering read-outs. And the discipline that governs them — capping work to the binding constraint — is decades-old flow control; the constraint moved from developer hours to human review capacity, but the craft is the IM's home turf. Rebuilding what the squad measures is a delivery job, not a tooling job.
- **Appendix ref:** attention budget detail (39); decoupling deep-dive (26).
- **Design note:** this slide carries the whole spine's weight. It must *establish* the sensors/decisions line on the face — do not soften the annot-line into notes. No "resolved/addressed" language anywhere; the slide does the work by drawing the line cleanly.

### 13 · Centaur teams — CARRY (`t-compare` has-head + has-annot, orange/paper)
- **Headline / seam-head (claim):** "Weak human + machine + better process beat the grandmaster."
- **Key content:** human (judgment, accountability, context, sign-off) / AI (speed, throughput, pattern-matching, draft generation); "process design is the variable — that is the IM's job."
- **`src`:** `Kasparov · NYRB 2010 · 2005 Freestyle Chess Championship`
- **Note gist:** protect this as a moment. Teams of amateurs with computers beat both grandmasters alone and computers alone — the winning teams had the best *process* for combining judgment with calculation, not the strongest players or machines. Same pattern in code review and development.
- **Appendix ref:** —

### 14 · HITL patterns — CARRY (`t-cards` cols-3, f-paper)
- **Headline (claim):** "You decide which pattern. The agent can't."
- **Key content:** AI drafts → human reviews (define the review gates in the DoD); human steers → AI executes (maintain the backlog agents pull from); AI monitors → human intervenes (set escalation thresholds). Workflow design, set before the agent runs — architecture, not in-task judgment.
- **`src`:** `HITL taxonomy — LangGraph / DEV Community / Anthropic agent guidelines`
- **Note gist:** the tech lead designs the agent; the IM decides which human-in-the-loop pattern governs how that agent participates in delivery. Selecting the pattern is a design decision made before the work begins — not a decision made augmented by AI inside the task, which is the case the counter-evidence warns about.
- **Appendix ref:** five collisions (35).

### 15 · The fork — CARRY (`t-compare` has-annot, orange/paper)
- **Headline / tag:** "The Fork" — "one accountable owner beats handoffs between separate specialists."
- **Key content:** fragmentation path (tech lead absorbs the workflow; a new governance specialist takes the risk; no single owner; the role dissolves into its parts) / evolution path (you own the workflow architecture, the HITL patterns, risk at the boundary; the role expands).
- **`src`:** —
- **Note gist:** the emotional pivot — evolve or dissolve. Fragmentation is real and will happen in some orgs. The structural case for evolution is handoff cost: splitting workflow architecture and human-AI risk across a tech lead and a separate specialist creates new coordination seams where today there is one owner. Prioritisation is deliberately not shown as a fragmentation outcome — that is legitimately the product manager's job.
- **Appendix ref:** —

### 16 · Three capabilities — CARRY (`t-cards` cols-3, f-paper)
- **Headline (claim):** "Three capabilities. One survival argument."
- **Key content:** workflow architecture · agentic governance · risk at the boundary.
- **`src`:** —
- **Note gist:** these are the practical skills to govern the HITL patterns — acquirable through daily delivery practice, not a one-time workshop. An IM who governs one agent workflow this sprint knows more than a colleague who attended a training.
- **Appendix ref:** credentials (Appendix D, 41-adjacent — see appendix list).

### 17 · The attention budget — NEW (D1) · primary framework (`t-cards` cols-3 or `t-content`, f-paper)
- **Headline (claim):** "A proposal: budget the scarce thing. It isn't hours anymore — it's judgment."
- **Key content — the three struts, on the face:**
  1. **The need is real:** AI saves ~11 hrs/week; ~6.4 of them go straight back to supervising the agent (~58% of the saving, derived) — 69% admit shipping unverified work. Review capacity is the scarce resource.
  2. **The mechanism is proven:** cap work-in-progress to the binding constraint — Reinertsen / Theory-of-Constraints flow control, 15+ years old. Only the constraint moved: from developer hours to human review capacity.
  3. **The synthesis is the proposal:** name human-review capacity as the *explicitly budgeted, planned WIP limit* of a hybrid squad — the attention budget. Open territory; presented as Adnan's proposal.
- **`src`:** `Need: Glean Work AI Institute, "Work AI Index" (n=6,000, US/UK/AU, Dec 2025–Jan 2026) · Mechanism: Reinertsen / Theory of Constraints WIP · Synthesis: proposed here`
- **Note gist:** this is a proposal, and saying so is the strength, not a hedge — no published framework budgets human attention yet. The "58%" is derived from the two Glean numbers (6.4 of 11 hours), not a stated figure — show the two raw numbers and let the erosion be a visible callout. If asked "what *is* my attention budget — three hours a day?", do not invent a number; own the open-territory position — the mechanism is old and the synthesis is mine, and the number is what a pilot establishes. This also answers sustainable pace and WIP in one move — the scarce resource is judgment, and flow discipline under a moving constraint is your home turf, not the tech lead's.
- **Appendix ref:** attention budget full detail (39).
- **Design note:** NO invented attention-budget number on the slide (Vera S6). The Glean hours are grounded; the budget figure is not.

### 18 · The token budget — NEW (D2) · subordinate framework (`t-cards` cols-3, f-paper)
- **Headline (claim):** "A proposal: plan agent spend like capacity — read against what shipped, not how much."
- **Key content — three parts + three struts, compressed:**
  - Parts: a per-role **rate card** ($/sprint per squad member, tuned by the squad); **breach = a decision trigger** (top-up, descope, or downgrade tier — logged, never an automatic halt); **reports at sprint review, next to judged outcomes** (shipped, verified work) — never next to raw output.
  - Struts: **need** — enterprise AI spend is climbing (per-dev agent spend commonly $150–250/month, heavy shops far more; Gartner expects >40% of agentic projects canceled by end-2027 on cost/value/risk); **mechanism** — WIP breach semantics + the established $X/dev allocation practice; **synthesis** — whole-squad, role-rated scope paired with *judged outcomes*, companion to the attention budget.
- **`src`:** `Need: enterprise-spend + Gartner (2026) · Mechanism: Reinertsen breach semantics + $X/dev industry practice · Synthesis: proposed here`
- **Note gist:** subordinate to the attention budget — attention is the binding constraint, tokens are the purchasable one. The "who else uses this?" answer: nobody yet — the mechanism is 15 years old, the synthesis is mine, and I'm running the pilot. Dollars are the ledger because they survive tokenizer and model changes and speak to stakeholders. The budget is a constraint, not a score — under-spend isn't a virtue, over-spend isn't a sin; unexplained variance is what triggers questions.
- **`src` guard (Iris):** do **not** cite Scrum.org as precedent for the token budget — the verification gate confirmed Scrum.org's article contains no token-budget recommendation. This synthesis is Adnan's.
- **Appendix ref:** token budget full detail (40).
- **Design note:** the $/dev figures may appear as labeled ranges with their source; no invented squad budget number on the slide.

### 19 · The ceremony survives; the metric doesn't — REFRAME (`t-cards` cols-2 dense, f-paper)
- **Headline (claim):** "The ceremony survives as a judgment ritual. The metric inside it does not."
- **Supporting line:** "This is the opposite of an AI sticker. Shrink each ceremony to the human-judgment call it now exists for — then rebuild what it measures: velocity and story points *out*; flow of judged, durable outcomes, attention budget, and agent cost *in*."
- **Key content:** the VERDICT pillar→ritual scaffold underneath (Validation→DoD, Evidence→Daily Scrum, Runtime control→stop-the-line, Decisions→retro, Identity→working agreements, Cost & compliance→sprint review, Transparency→stakeholder reporting). **Pillar C copy FIX (mandatory):** "Track agent spend and compliance next to velocity" → **"Read agent spend against judged outcomes — shipped and verified — never against velocity."** Velocity does not appear as a live metric anywhere on this slide.
- **`src`:** `VERDICT governance model · Srivastav & Saxena (2026, practitioner framework)`
- **Note gist:** the opposite of slapping AI onto old practice. Each ceremony shrinks to the one judgment call it now protects, and the number inside it gets rebuilt — the sprint review reads agent spend against what actually shipped and was verified, the Daily Scrum reads agent logs for deviations. VERDICT is a practitioner scaffold; borrow its credibility from the incidents on the next slide, and present it as an actionable checklist.
- **Appendix ref:** governance maturity ladder (36); incidents (37).

### 20 · Failure modes — CARRY (`t-cards` cols-3, f-paper)
- **Headline (claim):** "No owner at the boundary. Here is what that looks like."
- **Key content:** Replit (July 2025 — agent deleted a production DB during a code freeze; missing approval gate); Meta (Dec 2024 — sensitive data posted to a public forum; missing authorization check); the context-leak pattern (data in the context window becomes data the agent acts on).
- **`src`:** `Fortune · The Register · AI Incident Database #1152 (Replit) · SecurityBrief Asia · AI Magazine (Meta)`
- **Note gist:** both incidents were engineering deployments, not delivery-management contexts — the inference is structural: they show what happens when no one designs the approval gate. They are workflow-design failures, not security failures; the agent had legitimate access in both cases.
- **Appendix ref:** governance incidents — primary sources (37).

### 21 · Squad audit + the measurement question — EDIT (`t-list`, f-paper)
- **Headline (claim):** "Start with a question, not a plan."
- **Key content:** the five audit questions, plus one reframed/added: **"What does your squad count as *done* — and does that number still mean anything now an agent can produce it in seconds?"** The audit takes one sprint and tells you where to put governance before someone else decides for you.
- **`src`:** —
- **Note gist:** the IM's first governance act — no permission from a CoE required, just a delivery manager understanding their own team's workflow. The output is a governance map and an honest read on what "done" now means. It feeds the next slide's path.
- **Appendix ref:** governance maturity ladder (36).

### 22 · The 12-month path — CARRY (`t-cards` cols-3, f-paper)
- **Headline (claim):** "The 12-month path."
- **Key content:** this quarter (map one workflow, design one gate) → this year (three or four workflows governed, HITL patterns in the DoD) → success (the role has not fragmented; the governance layer moves with the engineers).
- **`src`:** —
- **Note gist:** delivery practice, not change management. The alternative — wait for a central CoE, hire a consultant, form a committee — is the mandate-driven rollout that stalls. The IM who acts in the work closes the gap from inside; the one who waits gets bypassed.
- **Appendix ref:** —

### 23 · CTA — EDIT (`t-cta`, f-orange)
- **Headline (claim):** "Own the decisions agents can't make."
- **Key content — de-risked two-move close (Vera S6):**
  - **Homework (low-risk):** run the five-question squad audit, and track **one** honest metric beside velocity for one sprint — cycle-time of judged outcomes, review-queue depth, or 30-day code survival.
  - **Invitation (opt-in, not an assignment):** "…or pilot the attention budget with me." Speak to Adnan after the session.
- **`src`:** —
- **Note gist:** the closing line ties the two ladders together — agent capability keeps climbing on its own; the governance gap only closes when someone owns it. Keep the baseline as the safe homework and the framework pilot as an explicit invitation — do not make betting a real squad on an unproven instrument the audience's action item. If a CFO hears "measure judgment" as "ship less," the answer is that judged flow ships *more* delivered value, because the old vanity number was hiding a rework and incident tax.
- **Appendix ref:** frameworks detail (39, 40); primary-source list (41).

### 24 · The team — CARRY (`t-team-avatars`, f-paper)
- **Headline (claim):** "The team behind this deck."
- **Key content:** the human-AI credits grid (the ONE slide where specialist names appear legitimately).
- **`src`:** —
- **Note gist:** produced by a human-AI team using the myPKA system; the team slide models the centaur collaboration the deck argues for.
- **Appendix ref:** —

---

## Appendix (generous — grows freely; serves solo readers expanding detail AND Adnan in live Q&A)

Everything moved off the main line lands here in full. Each entry answers a specific likely objection; the main-line notes point to these.

### 25 · Divider — CARRY (`t-divider`, f-ink)
Reference material — navigate here only when a question needs it.

### 26 · Decoupling deep-dive: the controlled triangulation — NEW (`t-stat-grid`, f-paper)
- **Headline:** "Output up, activity flat — measured twice, two ways."
- **Content:** the FORGE '26 study (peer-reviewed track): team-level **completed story points +59.1%** (281→447) while developer **activity — committed lines of code — showed no significant change (p=0.928)**; perceived speed up (~82% reporting faster), satisfaction high but strongly task-dependent (low on complex integration work). Paired with the Faros individual-vs-squad reconciliation: individual output up (+98% PRs/dev 2025, +16.2% 2026; tasks/dev +21%/+33.7%) while squad quality degrades (incidents/PR +242.7%, bugs/dev +54%). Carry the authors' own caveats: FORGE is 3 teams at one consulting firm over 13 months and cannot fully separate the gain from team maturation.
- **`src`:** `Tomaz et al., FORGE '26 (arXiv:2602.13766) · Faros AI, "AI Engineering Report 2026"`
- **Answers:** slides 02, 08 — "is the decoupling real or one vendor's number?" (Now: one controlled academic study + one large telemetry set agree.)

### 27 · Jeffries / #NoEstimates lineage — NEW (`t-quote` or `t-content`, f-paper)
- **Headline:** "Velocity was soft before agents. Agents only made gaming it free."
- **Content:** Ron Jeffries — "I may have invented story points, and if I did, I'm sorry now"; #NoEstimates (2012); Goodhart's law. The pre-concession, in full: the flaw predates agents; what changed is the cost of inflating the number fell to near zero.
- **`src`:** `Ron Jeffries (co-originator, story points) · #NoEstimates (2012)`
- **Answers:** the Scrum-purist objection that "velocity was never in the Scrum Guide, so agents didn't break it" — correct, and that is the deck's own point.

### 28 · Malone in full — CARRY (was Appendix A) (`t-stat-grid`, f-paper)
- **Headline:** "Malone et al. in full — why BCG and P&G results reconcile."
- **Content:** 106 studies, 370 effect sizes; 90% decision/classification (where human+AI underperforms), 10% generative/creative (where BCG and P&G live).
- **`src`:** `Malone et al. · Nature Human Behaviour 2024`
- **Answers:** slide 09 — the BCG/P&G-vs-Malone challenge. **Must remain intact** (it is the reconciliation the compressed slide 09 points to).

### 29 · Strong-middle / METR detail — NEW (`t-content` or `t-stat-grid`, f-paper)
- **Headline:** "The strong-middle shape — four framings, one RCT."
- **Content:** the SDLC-phase compression table, the human-sandwich (Frame→Collapse→Judge), the 80%-problem (Osmani); METR's 2025 RCT in detail — 16 experienced devs, 246 real issues, randomized per-task, 19% slower — with METR's own generalizability caveats (self-selected, small-N, specific repos) and the note that the 2026 follow-up is selection-biased per METR itself and not a stable re-measurement.
- **`src`:** `METR (July 2025 RCT) · SDLC-phase / human-sandwich / 80%-problem framings`
- **Answers:** slide 05 — "is 19% a real constant?" (No — one context-bound RCT; the *shape* is what triangulates.)

### 30 · Wide, not deep (83/55) — CARRY (was slide 27) (`t-compare`, orange/paper)
- **Content:** 83% of practitioners use AI tools / 55% spend ≤10% of work time with AI. "Wide. Not deep."
- **`src`:** `AI4Agile Practitioners Report 2026 (n=289)`
- **Answers:** slide 03 — the second adoption data point behind the hook.

### 31 · Governance gap (84/49) — MOVED from main line (was slide 13) (`t-compare`, orange/paper)
- **Content:** 84% of agile teams use AI tools / 49% have governance guardrails. The 35-point gap is where the risk — and the role — lives.
- **`src`:** `Digital.ai · 18th State of Agile 2025 (n=350)`
- **Answers:** slide 10 — the on-slide governance number, kept available for questions.

### 32 · Bolt-on (<40%) — MOVED from main line (was slide 11) (`t-evidence`, f-paper)
- **Content:** <40% of businesses report measurable profit gains from AI — they layer AI on legacy workflow; the workflow never changes.
- **`src`:** `McKinsey MGI · AI adoption research`
- **Answers:** slide 10 / slide 19 — the "no AI sticker" evidence, now carried in Adnan's voice on the reframe.

### 33 · Autonomy ladder (5 rungs) — MOVED from main line (was slide 05) (`t-list` labels, f-paper)
- **Content:** Assisted → Augmented → Collaborative → Orchestrated → Autonomous; the human's role climbs from operate → govern.
- **`src`:** `Synthesis; autonomy framing after Feng, McDonald & Zhang (Univ. of Washington, 2025); cf. SAE J3016, Cloud Security Alliance 2026`
- **Answers:** slide 04 — "how far do agents climb?"

### 34 · Chat vs agent — CARRY (was slide 26) (`t-figure`, f-paper)
- **Content:** the four things an agent has that chat doesn't — Context, Connections, Capabilities, Cadence.
- **Answers:** slide 04 — the "what is an agent" primer for a room that needs it.

### 35 · The five collisions — CARRY (was slide 28) (`t-list`, f-paper)
- **Content:** pull-vs-push lifecycle, learning-vs-execution, state-transition mismatch, handoff ambiguity, shared-context gaps.
- **`src`:** `Webframp practitioner analysis`
- **Answers:** slide 14 — why agents collide with a sprint cadence unless composed.

### 36 · Governance maturity ladder — CARRY (was slide 29) (`t-cards` cols-2 dense, f-paper)
- **Content:** Unseen → Observed → Controlled (the target) → Autonomous.
- **`src`:** `VERDICT governance model · Srivastav & Saxena 2026`
- **Answers:** slides 19, 21 — the ladder the audit's "where do we sit?" question maps to.

### 37 · Governance incidents — primary sources — CARRY (was Appendix C) (`t-cards` cols-1 dense, f-paper)
- **Content:** Replit (#1152), Meta (Dec 2024), Gartner 40%-decommissioned-by-2027, with root causes and sources.
- **Answers:** slide 20 — full incident timelines for challenge.

### 38 · Wave 1 dissolution — CARRY (was Appendix B) (`t-stat-grid`, f-paper)
- **Content:** SM enrollment 49% (2020) → <5% (2024); Agile Coach demand. Dormant Q&A backup (the main line does not use the Wave narrative).
- **`src`:** `Wolpers enrollment data · Scrum Alliance 2024`
- **Answers:** "has a delivery role dissolved before?" — historical precedent on request only.

### 39 · Attention budget — full detail — NEW (`t-content` or `t-cards`, f-paper)
- **Content:** the WIP/ToC mechanism in full; the Glean botsitting math (11 saved − 6.4 supervised, ~58% erosion derived); review-queue health as the reportable signal (pickup time, % merged unreviewed); how the budget is set and breached (stop pulling agent work when review capacity is spent).
- **`src`:** `Glean Work AI Institute, "Work AI Index" · Reinertsen / Theory of Constraints`
- **Answers:** slides 12, 17 — "how do I actually run an attention budget?"

### 40 · Token budget — full detail — NEW (`t-cards` cols-2 or `t-content`, f-paper)
- **Content:** the rate-card structure (role → tier → $/sprint; squad budget = Σ headcount × role rate); breach semantics (top-up / descope / downgrade, logged, visible at sprint review); the review contract (burn vs budget next to judged outcomes; constraint-not-score Goodhart guard; dollars as the ledger); the growth path (cost-per-judged-outcome, routing rules, eval-gated top-ups — not day one).
- **`src`:** `Enterprise-spend + Gartner (need) · Reinertsen breach semantics + $X/dev practice (mechanism) · synthesis proposed here`
- **`src` guard:** do not cite Scrum.org as precedent (verified: no token-budget recommendation there).
- **Answers:** slide 18 — the full instrument for a pilot, and the "who else uses this?" recovery.

### 41 · Primary-source list + credential landscape — NEW/MERGE (`t-sources` + `t-cards`, f-paper)
- **Content:** the load-bearing citations with their exact attributions from the verification gate (Faros 441%/242.7%; METR RCT; GitClear; Glean; FORGE '26; Scrum.org; Malone; BCG/P&G; Kasparov; Digital.ai; McKinsey; AI4Agile). Fold in the credential landscape (PSM-AI, PMI AI-in-Agile-Delivery, IAPP AIGP as the curated three, mapped to deck capabilities; the rest as the fuller list).
- **Answers:** slide 23 and any sourcing challenge — one place to check every number.
- **Budget flag (Iris):** this may need to split into two appendix slides (sources; credentials) if the `t-sources` ≤12-entry budget is exceeded — the appendix can absorb the extra slide freely.

---

## Build eval checklist (pre-merge greppable rejects)

A pre-merge check should scan the built HTML **excluding the credits slide (24)** and reject any of the following. These are the pipeline-meta patterns Adnan ruled out of slide copy and speaker notes:

**Hard reject (case-insensitive) anywhere outside slide 24:**
- Specialist names as standalone words: `Rex`, `Vera`, `Aria`, `Pax`, `Nolan`, `Silas`, `Penn`, `Mack`, `Iris`, `Coda`, `Larry`
- Attribution-of-process phrases: `per Rex`, `per Vera`, `per Aria`, `Rex's`, `Vera's`, `Aria's`
- Confidence / audit-trail language: `Source confidence`, `confidence:`, `High confidence`, `Medium-High`, `audit trail`, `scorecard`, `pre-mortem`, `premortem`, `steelman`, `motivated opponent`, `contradiction-map`, `gap-register`, `re-audit`
- Gap / condition codes as tokens: `G-NEW`, `G-1`…`G-9`, `A2`, `A5`, `B1`, `C1`, `S1`…`S6`, `M1`…`M4`, `N1`…`N6` (match with word boundaries — see note)
- Argument-plumbing jargon: `warrant W`, `entailment`, `the A2`, `Blocker`, `Significant (`, `GO-WITH-CONDITIONS`
- Build hygiene: `TODO`, `FIXME`, `flagged`, `flag to`, `XXX`, `Lorem`

**Notes for the checker:**
- Slide 24 (credits) legitimately contains `Pax`, `Rex`, `Aria`, `Vera`, `Coda`, `Iris`, `Larry`, `Nolan` — scope the name checks to exclude that `<section>`.
- Gap-code tokens (`A2`, `B1`, `S1`, `C1`, etc.) collide with legitimate strings — enforce word-boundary matching and eyeball hits; the intent is to catch bare code references, not substrings inside real words or asset paths.
- **Legitimate deck vocabulary that must NOT be rejected:** `approval gate`, `review gate`, `HITL`, `boundary`, `governance`, `VERDICT`, `judged outcomes`, `attention budget`, `token budget` — these are the deck's own language, not pipeline meta.
- The 441% `src` line must read Faros, never DORA-as-source (a `grep -i "DORA 2025" | grep -v "not the DORA"` should return nothing).

---

## Conditions coverage map (for reviewers — NOT for any slide)

| Condition | Source | Where addressed |
|---|---|---|
| **B1** — don't build as "A2 resolved"; state warrant explicitly; back "why the IM" with the flow-discipline/WIP strut | Rex | Slide 12 (sensors-vs-decisions): warrant on the annot-line; flow-control-is-IM-craft strut pulled forward; no "resolved" language. D-5 subordinates measurement to the boundary thesis. |
| **S1** — VERDICT pillar C contradicts "velocity out" | Rex | Slide 19: pillar C rewritten to "read agent spend against judged outcomes, never velocity"; velocity removed as a live metric. |
| **S2** — frameworks need the three struts; token budget under-grounded, don't present as equal | Rex | Slides 17 & 18 each carry grounded-need / proven-mechanism / explicit-synthesis; slide 18 is subordinate; Scrum.org dropped as token precedent. |
| **S3** — slide-D overload; subordinate or split | Rex | Split into two slides (17 primary, 18 subordinate); attention budget carries WIP + sustainable pace, token budget separate. |
| **S4** — keep the task-type conditional welded to the upside; name Malone's split on the main line; Appendix A intact | Rex | Slide 09: qualifier welded to +40%; 90%/decision-task split named on-slide; Appendix 28 intact. |
| **S5** — verify Faros / Scrum.org before they land as pillars | Rex | Verification gate closed both; all figure `src` lines use the gate's exact strings (D-3). |
| **M1** — subordinate the measurement thread to the boundary thesis | Rex | D-5; slide 12 frames measurement rebuild as a delivery job = boundary ownership. |
| **M2** — METR as point-in-time RCT, not a constant | Rex | Slides 05, 08 notes and Appendix 29 present METR as one context-bound RCT. |
| **M3** — governance-evidence thinning as 84/49 moves off | Rex | Slides 10 + 11 carry it qualitatively; number available at Appendix 31. |
| **M4** — label proposed metrics as synthesis | Rex | "30/60/90-day survival" and both budgets framed as proposals (17, 18, 23). |
| **C1** — establish on-slide why delivery-outcome measurement is the IM's decision, not the tech lead's telemetry; separate sensors from decisions; cut "the tech lead does not contest this" | Vera | Slide 12 is built entirely on the sensors (engineering reads) vs decisions (IM owns) cut; the "does not contest" sentence does not appear. |
| **S1 (Vera)** — replace ungrounded "predictably" | Vera | Slide 02 headline/ctx use the grounded decoupling, not "predictably". |
| **S2 (Vera)** — slide B carries METR/Faros level-reconciliation on its face | Vera | Slide 08 annot-line carries the reconciliation; budget flag ensures it stays on-face. |
| **S3 (Vera)** — hook carries "agents made gaming free" so the pre-concession amplifies | Vera | Slide 02 mandatory reconciliation line; echoed on slide 08; Jeffries lineage at Appendix 27. |
| **S4 (Vera)** — concrete reportable metrics on the measurement slides; "ships more value" rebuttal in notes | Vera | Slides 12, 17, 23 name reportable metrics (review-queue depth, cycle-time of judged outcomes, 30-day survival); rebuttal in slide 23 note. |
| **S5 (Vera)** — every retired instrument gets an IM-owned replacement on-slide | Vera | Slide 12 (velocity→judged-flow decisions), slide 17 (sustainable pace→attention budget), slide 19 (metric-inside-the-ceremony rebuilt). |
| **S6 (Vera)** — de-risk the CTA; no invented attention-budget number; open-territory recovery in notes | Vera | Slide 23 baseline=homework / pilot=invitation; slides 17 & 18 carry no invented budget number; recovery lines in notes. |
| **L1/L2/L3 (Vera)** — keep on-slide anchors, don't overload the climb, don't present 19% as a constant | Vera | Numbers kept on main-line slides 08/09/12; frameworks split to ease climb load; METR framed as one RCT (M2). |
| Slide-count ceiling (≤ v2.1.0 body) | Larry/Aria | 24 total / 21 body — at the ceiling (see reconciliation section). |
| Generous appendix | Larry | 17 appendix slides incl. the new deep-dives (26, 27, 29, 39, 40, 41) and the 3 moved slides (31, 32, 33). |

---

## Open items for Larry / Adnan (couldn't fully reconcile unilaterally)

1. **The +1/−1 delta from Aria's math.** Splitting the frameworks (Rex S3) makes additions +5, so I compressed a second slide — the "agent = acts" statement folds into the loop (slide 04) — to hold the 21-body ceiling. This lands exactly at the ceiling and drops no claim, but it edits Aria's "stays unchanged" list (04 and 06 were both to stay). Aria should confirm the fold, or nominate a different −1 (e.g. moving the loop's ladder pointer, or a fourth appendix move). If Aria prefers to keep 04 standalone, the deck runs at 22 body — one over the ceiling — and Larry decides which constraint yields.
2. **Slide 08 and slide 02 copy density.** Both must carry multiple reconciliations on the slide face (Vera S2/S3). I've specified priority orders and fallbacks so nothing critical drops to notes, but if Iris finds the annot-line/ctx genuinely can't hold the mandatory lines within the layout budget, that comes back to Larry before we shrink or split — not resolved by shrinking fonts.
3. **No score, no research change made.** This plan does not alter any figure, add any claim beyond the approved spine, or score any dimension. Where a figure was uncertain, it uses the verification gate's exact attribution; nothing rests on model memory.
