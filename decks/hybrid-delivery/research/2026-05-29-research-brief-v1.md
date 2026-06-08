# Research Brief: Delivery Leadership in Human+AI Hybrid Teams
**Version:** v1  
**Date:** 2026-05-29  
**Prepared by:** Pax, Senior Research Specialist  
**For:** Hybrid Delivery deck — Larry / Adnan Ali

---

## Executive Summary

The directional PoV is well-supported but requires one important qualification: the performance hierarchy (Human+AI > AI > Human) is **conditionally true**, not universally true. A landmark meta-analysis (Malone et al., *Nature Human Behaviour*, 2024) found that human+AI combinations do not automatically outperform the best solo performer — the advantage is structural and design-dependent. Where the PoV lands most solidly is in generative knowledge work: two major field experiments (Mollick/Dell'Acqua at BCG and P&G) confirm that structured human+AI collaboration produces significant quality and speed gains for the complex creative-analytical tasks delivery teams actually do. The IM/DM role evolution claim is strongly supported by multiple independent practitioner and research sources: low-leverage SM work is being absorbed by AI tools, while the demand for human judgment, governance, and workflow architecture is rising sharply. The governance and token economics angle is under-researched in agile-specific literature but well-evidenced in engineering and enterprise AI deployment writing — this is a genuine white space the deck can own.

---

## 1. Supporting Evidence

### Arc 1: Human+AI hybrid teams are the new norm

**Claim: The "will AI take our jobs?" question is settled — the question now is how to structure the collaboration.**

- McKinsey MGI (Nov 2025, "Agents, Robots, and Us"): 57% of US work hours are theoretically automatable with current technology, but the explicit framing is skill evolution not job elimination. AI fluency demand grew 7x in two years (1M to 7M employees in job postings). **Confidence: High** — comprehensive primary source, $2.9T economic value estimate independently corroborated by McKinsey/Krivkovich Jan 2026 LinkedIn piece.

- Gartner HR Research (May 2026): "No jobs apocalypse — but job chaos." Net job creation tipping point projected at 2028; 32 million jobs significantly transformed per year. **Confidence: Medium-High** — press release with stated methodology (Gartner 2025 AI Job Impacts Analysis); underlying data not fully public but consistent with McKinsey and Brynjolfsson trajectories.

- Benedict Evans, "AI Eats the World" (May 2026): 900M+ ChatGPT weekly active users; ~25% of US adults using AI daily; tech sector at ~60% daily use. The constraint is shifting from model capability to workflow integration and trust. **Confidence: Medium** — market analysis, not peer-reviewed, but Evans' track record on platform shifts is strong and figures are consistent with other public data.

**Source quality note:** The "jobs settled" claim rests on convergent industry/research consensus, not a single experiment. The exact scale and timing of job transformation is still debated among economists.

---

### Arc 2: Performance hierarchy — Human+AI > AI > Human (when structured correctly)

**Claim: Human+AI outperforms both solo conditions for complex knowledge work.**

**The qualifier is load-bearing:** This is *conditionally* true, and the conditions are the deck's core argument.

**Primary supporting evidence:**

- Dell'Acqua, Mollick et al., "Navigating the Jagged Technological Frontier" (*Organization Science*, published March 2026; pre-print 2023): 758 BCG consultants, randomized controlled trial. On tasks inside AI's capability frontier: 12.2% more tasks completed, 25.1% faster, 40% higher quality ratings by human evaluators. **Critically:** on a complex managerial task deliberately outside the frontier, AI users were 19% *less likely* to produce correct solutions. This is the "jagged frontier" — AI creates a structurally uneven capability surface where human judgment about *when to trust AI* is the decisive variable. **Confidence: High** — peer-reviewed, large n (758), pre-registered, published in a top-tier management journal.

- Dell'Acqua, Mollick et al., "The Cybernetic Teammate" (NBER Working Paper 33641, 2025): 776 P&G professionals, pre-registered RCT conducted May–July 2024. Results: individual with AI matched team without AI (0.37 SD vs 0.24 SD above baseline); team with AI achieved 0.39 SD. Teams with AI were 3x more likely to produce top-10% solutions. Work completed 12–16% faster with substantially more detailed output. Expertise silos dissolved: R&D and Commercial professionals produced equally balanced solutions when using AI. Less experienced employees matched seasoned veterans. **Confidence: High** — pre-registered, large n, two major research institutions (HBS, Penn/Wharton), randomized.

- Brynjolfsson, Li et al., "Generative AI at Work" (NBER Working Paper 31161): 14% average productivity increase in customer support; 34% improvement for novice workers. AI appears to disseminate best practices from top performers to newer staff. **Confidence: High** — peer-reviewed NBER working paper, well-cited, field experiment methodology.

**Counter-claim from vault:**

- Malone et al., MIT / *Nature Human Behaviour* (Jan 2024 meta-analysis, 106 studies, 370 effect sizes): On average, human+AI combinations did *not* outperform the best solo performer. For decision tasks especially, the combination was worse. The meta-analysis covers studies from 2020–2023, predating most generative AI deployments. **Confidence: High on the finding itself** — published in *Nature Human Behaviour*, rigorous meta-analysis. This is the most important counter-evidence the deck must address.

**Reconciliation:** The paradox resolves on task type. For generative, iterative, content-creation work (what delivery teams mainly do: writing specs, refining requirements, analysis, planning), generative AI enables a draft-edit-rework loop that produces positive synergy. For decision tasks (where humans must judge AI output quality), adding an inferior human to a superior AI *degrades* performance. The deck's PoV should narrow its claim: "for complex knowledge creation and delivery planning work, structured Human+AI outperforms both" — not a universal hierarchy claim.

---

### Arc 3: What "structured correctly" means in practice

**Evidence from vault and external sources:**

- **Workflow composition, not workflow merger:** The "Team Workflow and Agent Lifecycle Collision" concept (Webframp, corroborated by Paul Stack) identifies five fundamental collision points between team workflows (Kanban, pull-based, learning-oriented) and agent lifecycles (operator-initiated, state-machine, execution-correctness-oriented). The solution is composition: agent lifecycle runs inside the team's "In Progress" state as a sub-process. **Confidence: Medium** — practitioner primary source (Webframp analysis), corroborated by Spotify's Niklas Gustavsson finding at CwC London 2026 (96% engineer AI adoption, 60% PR frequency increase, constraint shifted from coding to orchestration).

- **Shared team agents over personal agents:** The company Every's documented evolution from per-employee agents to shared team agents (chief-of-staff framing) resolves maintenance burden, knowledge silos, and uneven adoption. **Confidence: Medium** — single organizational case study (Every/Dan Shipper), corroborated conceptually by Spotify's Honk agent (shared infrastructure, plugged into Backstage).

- **Semi-synchronous collaboration for complex work:** Whittemore's wave 1 vs wave 2 framework (async handoff vs semi-synchronous co-working) — for high-value complex knowledge work where the frame evolves during execution, semi-synchronous (human steers, agent executes, human steers again) outperforms fire-and-forget. **Confidence: Medium** — practitioner analysis, consistent with Mollick's co-intelligence framing and P&G findings showing collaborative iteration benefits.

- **The infinite backlog problem:** AI doesn't reduce workload — it expands the perceived scope of "the job" as previously aspirational tasks become immediately actionable. The constraint shifts from execution capacity to human judgment and prioritization capacity. **Confidence: Medium** — conceptual/practitioner source, consistent with reported productivity patterns. No single empirical study directly measures this specific phenomenon.

- **Human skill gaps are the actual bottleneck:** Implementation of agentic AI is constrained by human deficiencies in objective specification, task decomposition, and human-agent coordination — not model limitations. **Confidence: Medium** — vault note from YouTube content (source not primary-research-grade). Corroborated by Dell'Acqua finding that AI users outside the frontier performed *worse* (suggesting calibration failure).

- **McKinsey on workflow redesign:** <40% of businesses report measurable profit gains from AI because they bolt AI onto legacy workflows rather than redesigning processes. The 60% productivity gain concentration is in domain-specific core processes, not incremental task automation. **Confidence: High** — McKinsey MGI primary research.

---

### Arc 4: What changes for the IM/DM role

**Claim: Low-leverage SM/IM work is absorbed by AI; human judgment, governance, and architectural work becomes more critical.**

- **Role dissolution risk is real and conditional:** Itamar Gilad's PM archetypes analysis: the pure delivery PO (translates roadmaps to backlogs, writes user stories) is the most vulnerable archetype — directly analogous to draftsmen displaced by CAD in the 1980s. The AI-empowered PM (drives AI adoption across the full org operating model) is the most future-proof. **Confidence: Medium** — practitioner analysis, no controlled study, but consistent with multiple independent sources.

- **Theagileforum.com (2026):** SM/IM work in decline: ceremony facilitation, Jira management, status reporting. Work rising: flow metrics, delivery outcomes, system design, stakeholder influence. Role survives if it evolves; dissolves if it stays in pure facilitation. **Confidence: Medium** — practitioner source.

- **AI-Augmented Scrum (Agile Leadership Day India, 2026):** Specific ceremony redesigns when agents are team members: Sprint Planning splits human-creative vs automated tasks; Daily Scrum becomes async deviation management (reviewing AI output logs and confidence scores); Sprint Review requires human co-presentation and accountability; Retrospective becomes systematic agentic workflow debugging (prompt library optimization). SM role: monitors system logs and API rate limits alongside human impediments. **Confidence: Medium** — practitioner framework, no empirical validation.

- **"Gradual hollowing" of knowledge work roles:** AI erodes routine tasks incrementally, leaving workers defenseless when organizational restructuring questions role justification. The danger is not sudden replacement but slow atrophy creating hidden precarity. **Confidence: Medium** — conceptual analysis (vault note from YouTube), consistent with AI skills demand data from McKinsey.

- **McKinsey on manager role shift:** As AI absorbs analytical tasks, managers shift from "supervising people" to "orchestrating people, agents, and robots." Skill emphasis moves to coaching, influence, innovation, and technical fluency. **Confidence: High** — McKinsey MGI primary research.

- **Microsoft New Future of Work Report 2025:** "The future of work is no longer individual — it's collective." AI improves individual productivity more reliably than team productivity (current gap). Human expertise matters *more* not less — people shift from doing work to guiding, critiquing, and improving AI work. Organizational adoption requires leaders to model learning and center worker voice. **Confidence: High** — Microsoft Research primary report, based on synthesis of multiple research streams.

---

### Arc 5: AI governance — token costs, long-lived agentic workflows, risk at the human-AI boundary

**Claim: Governance is the new delivery risk surface; the IM/DM who learns to govern agentic workflows owns a durable career moat.**

- **Token cost as a new delivery metric:** Agentic AI burns 10-100x more tokens than chatbots (context re-sending on every LLM call; re-sent context is 62% of the bill). Single developer weekend incident: $4,200 in API fees. Median team-level monthly cost: ~$480/developer, 90th percentile $1,650. 20-developer team running inefficiently: $110,000/month. Mitigation: prompt caching (88% cost reduction on prompts), model tier routing (60-80% savings), context pruning, per-user hard caps. **Confidence: Medium-High** — practitioner analysis (LeanOps, 2026), specific numbers are illustrative but consistent with public API pricing data.

- **AI Governance Maturity Ladder (VERDICT framework, Niharika Srivastav / Sanjay Saxena, Maven 2026):** Four levels — Unseen AI (no inventory), Observed AI (visibility without control), Controlled AI (policies enforced, owners assigned), Autonomous Governance (agents monitoring agents). Most enterprises sit at Level 1-2. EXPOSE → BIND → ENFORCE → SELF-GOVERN implementation sequence. **Confidence: Medium** — practitioner/consultant framework from Maven live session, not academic research. Internally consistent and triangulates with IMDA/Singapore framework structure.

- **Singapore IMDA Model AI Governance Framework for Agentic AI (Jan 2026, WEF Davos):** Government-level framework. Two key dimensions: agent's "action-space" (what tools/systems it may access) and agent's "autonomy" (instructions governing it and human oversight). Use case owner remains accountable for responsible use. **Confidence: High** — official government/regulatory document.

- **Anthropic's own framework for safe agents:** Balance between agent autonomy and human oversight. Read-only permissions by default; human approval required for state-modifying actions. Complex tasks: Claude asks for clarification 2x more often than humans interrupt it. Caution advised for minimal-oversight deployment with sensitive information access. **Confidence: High** — Anthropic primary source.

- **AI governance as career moat:** "Regulated, Scarce, Valued, Durable." Three categories going forward: people who use AI, people who govern AI, people who do the work (which AI now does). The overlap between "understands agents" and "understands risk/compliance" is thin — this is where the career opportunity lives. **Confidence: Medium** — consultant framing (Srivastav/Saxena), directionally consistent with AIGP credential salary data ($141K–$170K US median for AIGP holders).

- **Routing agent with human-in-the-loop pattern:** Concrete design pattern — routing agent evaluates conditions, branches to either another agent (automatic execution) or human decision event (approval gate with override). Structured output (single word) simplifies branching. Human can override; decision context kept intact. **Confidence: Medium** — OutSystems tutorial; pattern is widely described across engineering sources.

- **Over-trust and vigilance decay:** Humans performing repetitive AI oversight tasks lose vigilance over time (Mackworth, Norman). CNET AI article review failure (2023) — editors stopped checking for factual errors after finding no grammatical errors. Human-in-the-loop value degrades if the loop is boring and low-stakes. Design implication: oversight gates must be designed at meaningful decision junctions, not as rote approval steps. **Confidence: High on vigilance decay principle** (established cognitive science, cited Gary Marcus); **Medium on implication for AI oversight specifically**.

---

### Arc 6: Actionable closing — learning, ceremony changes, day-to-day workflow

**See Section 4 for full resource catalogue.**

---

## 2. Credible Counter-Evidence

**Counter-claim 1: Human+AI does not automatically outperform best-solo.**  
Malone et al., *Nature Human Behaviour* (2024): meta-analysis of 106 studies found human+AI combinations on average *worse* than best solo system. Only 10% of reviewed studies covered creation tasks; those showed positive synergy. The bulk of the evidence base covers decision and classification tasks. **Implication for the deck:** The performance hierarchy claim must be scoped to generative, iterative knowledge work — not stated as a universal law.

**Counter-claim 2: AI governance is a transitional role with a timer.**  
From vault (ai-governance-career-moat.md, East/opposing view): As AI self-governance matures and Level 4 autonomous governance becomes achievable, the human governance layer shrinks. The career moat has a timer. **Implication for the deck:** Frame governance as a 5-year window of structural advantage, not a permanent redefinition. Honest framing increases credibility with sophisticated audiences.

**Counter-claim 3: The Scrum Master role doesn't evolve — it dissolves.**  
Some industry observers argue the facilitation role is simply absorbed into other positions (tech lead, product manager, delivery lead) rather than elevated. Digital.ai State of Agile data: 42% of organizations already use hybrid approaches blending Agile with other methods. **Implication for the deck:** The dissolution risk is real for those who don't actively own the evolution. The PoV should be framed as conditional: "those who learn to architect the collaboration will define the role; those who don't will find it dissolved."

**Counter-claim 4: Organizational readiness, not agent sophistication, is the binding constraint.**  
80% of implementation effort in agentic AI projects is consumed by data engineering, stakeholder alignment, governance, and workflow integration. 40%+ of agentic AI projects fail due to poor governance and unclear ROI. **Implication for the deck:** This is actually supportive of the IM/DM value proposition if framed correctly — the IM/DM *is* the human who does the 80% work, provided they evolve the right skills.

---

## 3. Source Quality Flags

| Claim | Source quality flag |
|---|---|
| Human+AI = 3x top-10% solution rate (P&G) | High — pre-registered RCT, peer institution, HBS/Penn. Single org (P&G); generalizability to all knowledge work types not fully established. |
| Human+AI = 12.2% more tasks, 25.1% faster, 40% quality uplift (BCG) | High — peer-reviewed (Organization Science 2026), large n (758), randomized. Single task domain (consulting); may not generalize to delivery management specifically. |
| Human+AI worse on average across 106 studies (Malone) | High — published Nature Human Behaviour, rigorous meta-analysis. Studies predate most GenAI deployments (2020–2023); relevance to current GenAI tools is contested. |
| 57% of US work hours automatable | High — McKinsey MGI primary research. "Technical potential" not a deployment forecast; actual adoption will be slower. |
| AI agents burn 50-100x more tokens than chatbots | Medium — practitioner analysis (LeanOps blog), not peer-reviewed. Specific cost figures are illustrative based on API pricing math; real-world variation is large. |
| VERDICT governance framework (4 levels, 4 phases) | Medium — consultant/practitioner framework from Maven live session; not independently validated or peer-reviewed. Useful heuristic but should not be cited as research. |
| AI fluency grew 7x in 2 years | High — McKinsey MGI, based on US job posting data analysis across millions of postings. |
| Scrum Master role dissolving into delivery leadership | Medium — convergent practitioner opinion (theagileforum, rethinkyourunderstanding, scrum.org), no controlled longitudinal study. Direction is consistent but pace and extent are speculative. |
| Brynjolfsson 14% productivity gain (customer support) | High — NBER working paper, field experiment, well-cited. Domain (customer support) is narrower than delivery management. |
| Jack Dorsey organizational hierarchy essay | Low as primary evidence — essay/opinion, no empirical data. Directionally consistent with academic organizational theory but should not be cited as empirical support. |

---

## 4. Actionable Resources

### Empirical papers / primary research the deck can cite directly

- Dell'Acqua, Mollick et al. (2026): "Navigating the Jagged Technological Frontier" — *Organization Science*. The foundational paper for the performance hierarchy claim. URL: https://pubsonline.informs.org/doi/10.1287/orsc.2025.21838

- Dell'Acqua, Mollick et al. (2025): "The Cybernetic Teammate" — NBER Working Paper 33641. The P&G expertise-silo dissolution finding. URL: https://www.nber.org/papers/w33641

- Malone / Vaccaro et al. (2024): Human-AI collaboration meta-analysis — *Nature Human Behaviour*. The counter-evidence that makes the PoV intellectually honest. Source: MIT Sloan summary at https://mitsloan.mit.edu (vault note: human-ai-collaboration-malone-mit-sloan.md).

- Brynjolfsson, Li et al.: "Generative AI at Work" — NBER Working Paper 31161. URL: https://www.nber.org/papers/w31161

- McKinsey MGI (Nov 2025): "Agents, Robots, and Us: Skill Partnerships in the Age of AI" — URL: https://www.mckinsey.com/mgi/our-research/agents-robots-and-us-skill-partnerships-in-the-age-of-ai

- Microsoft New Future of Work Report 2025 — URL: https://www.microsoft.com/en-us/research/publication/new-future-of-work-report-2025/

### Books / accessible thought-leader reading for the audience

- Ethan Mollick, *Co-Intelligence: Living and Working with AI* (2024) — Wharton professor, most accessible synthesis of the research for practitioners. Four rules: Always Invite AI to the Table, Be the Human in the Loop, Treat AI Like a (Smart but Alien) Person, Assume It's the Worst AI You'll Ever Use.

- Joshua Kerievsky, *Joy of Agility* (2022) — Foundational agility principles that frame the human layer's enduring value. Particularly: "Start minimal and evolve," "Drive out fear," and "Be readily resourceful" map well to hybrid team design.

### Frameworks and models the deck can use

- **Jagged Frontier** (Mollick/Dell'Acqua): AI capability surface is uneven even within similar task domains. Know which side of the frontier each task sits on before assigning to an agent.

- **Seven Agent Team Roles** (IBM Technology): Doer, Planner, Tool Operator, Learner, Critic/Feedback, Supervisor, Presenter. Practical vocabulary for designing hybrid squads.

- **AI Governance Maturity Ladder**: Unseen → Observed → Controlled → Autonomous. Diagnostic for where your org actually sits.

- **VERDICT Governance Sequence**: EXPOSE → BIND → ENFORCE → SELF-GOVERN. Practitioner implementation path.

- **Workflow Composition vs Merger** (Webframp): Team lifecycle and agent lifecycle cannot be merged — they must be composed, with the agent lifecycle running inside the team's "In Progress" state.

- **Semi-Synchronous Collaboration** (Whittemore): Wave 1 (async handoff) vs Wave 2 (semi-synchronous co-working). For complex knowledge work, Wave 2 is the appropriate mode.

- **Gartner Four Scenarios**: AI Augmentation → AI Collaboration → AI Delegation → AI Autonomy. A spectrum leaders can use to assess their current posture.

### Courses and certifications the deck can recommend

| Course | Provider | Best for |
|---|---|---|
| Professional Scrum Master - AI Essentials (PSM-AI) | Scrum.org (launched Feb 2026) | Scrum Masters/Agile Coaches learning to integrate AI into their role. 1-day, hands-on. URL: https://www.scrum.org/courses/professional-scrum-master-ai-essentials-training |
| AI for Scrum Masters | Scrum Alliance (Microcredential) | On-demand or live. Covers AI foundations, responsible AI, AI-augmented SM workflow. URL: https://www.scrumalliance.org/microcredentials/ai-for-scrum-masters |
| AI in Agile Delivery | PMI eLearning (introduced Oct 2025) | 5-module course: Discovery, Experimentation, Delivery, Team Reflection, Scale. PDU credit. URL: https://www.pmi.org/shop/p-/elearning/ai-in-agile-delivery/el251 |
| PMI CPMAI (Certified Professional in Managing AI) | PMI | Structured methodology for overseeing AI and data initiatives using agile practices. URL: https://www.pmi.org/certifications/ai-project-management-cpmai |
| AI Governance Professional (AIGP) | IAPP | The governance and risk credential. 4 domains: foundations, laws/standards (EU AI Act, NIST AI RMF), governing development, governing deployment. $649–$799 exam fee. URL: https://iapp.org/certify/aigp |
| AI-Driven Agile | CI Agile | Leadership accelerator combining AI fluency with Scrum certification. URL: https://info.ciagile.com/ai-driven-agile/ |
| AI for Agile Leaders and Change Agents | Agile Seekers | Focused on change agent role in AI adoption. URL: https://agileseekers.com/artificial-intelligence/ai-for-agile-leaders-change-agents-certification |

### Token cost and governance tools the deck can name-check

- **LeanOps** agentic cost management: Hard cap architecture, model tier routing, context pruning guidance.
- **paperclip.ai**: Cited in VERDICT framework for Level 4 self-governing AI infrastructure.
- **Anthropic Claude Code + CLAUDE.md convention**: Encoding team conventions as agent context (demonstrated at CwC London 2026 by Spotify and AWS sessions).
- **Singapore IMDA Model AI Governance Framework for Agentic AI** (Jan 2026): Government-level reference for action-space + autonomy framework. URL: https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf

---

## 5. Methodology

**Vault search (Step 1):**  
Used `rg` (ripgrep) across `/mnt/c/Users/adnan/Google Drive/aa2brain` with search terms: "hybrid team," "human AI," "iteration manager," "delivery manager," "scrum master," "agentic workflow," "long-running agent," "token cost," "governance," "agile AI," and key author names (Mollick, Brynjolfsson, Malone, Evans). Identified and read 18 vault files in full, including 4 McKinsey/MGI articles, 3 practitioner concept notes on governance, 4 CwC London 2026 session transcripts, and 5 abstract/concept notes on collaboration patterns.

**External search (Step 2):**  
Conducted 12 targeted web searches and 4 WebFetch calls covering: Jagged Frontier paper statistics, Cybernetic Teammate findings, Scrum Master role evolution in 2026, agile ceremonies with AI agents, token cost governance, AI governance frameworks, available courses and certifications, and Brynjolfsson/Mollick recent work. Prioritized primary sources (published papers, official frameworks, peer-reviewed journals) over secondary commentary.

**Triangulation (Step 3):**  
All major empirical claims verified against at least two independent sources. The performance hierarchy claim was specifically triangulated across three competing research streams (BCG/Mollick, P&G/Mollick, Malone meta-analysis) to surface the conditional nature of the claim. Token cost figures triangulated across LeanOps practitioner analysis and TechTarget enterprise AI guidance.

---

## 6. Limitations

- The IM/DM-specific role evolution literature is practitioner-grade, not peer-reviewed. There is no controlled longitudinal study tracking SM/IM outcomes before and after AI integration. All role evolution claims rest on convergent practitioner opinion.

- The performance hierarchy research (BCG, P&G) covers consulting and product development tasks. Direct mapping to delivery management work (planning, risk management, ceremony facilitation) is inferential, not demonstrated.

- Token cost figures are based on API pricing math and case studies, not industry-wide empirical data. Actual team costs vary enormously by workflow design, model selection, and usage patterns.

- The VERDICT framework and AI Governance Maturity Ladder are consultant frameworks from a Maven live session, not independently validated research. Useful for deck structure but should not be cited as academic evidence.

- Academic research on AI and agile specifically (not just knowledge work generally) is sparse. Most agile+AI writing is practitioner and vendor-produced.

- AI capabilities and tooling are changing faster than the research cycle. The Malone et al. meta-analysis (2024) covers studies from 2020–2023, predating GPT-4-class models. The BCG/P&G studies are more recent but will also become outdated.

- External web searches were limited to 12 queries; a dedicated full-day research pass would likely surface additional empirical studies on delivery management specifically.

---

## 7. Open Questions for the Deck

1. Is there any direct empirical evidence on IM/DM productivity with AI tools specifically (not just knowledge workers in general)? This would significantly strengthen Arc 4.

2. What does "governing agentic workflows" look like concretely in a sprint? The deck needs 2–3 specific worked examples of IM/DM governance decisions in a hybrid team context.

3. Are there any documented case studies of a team that explicitly reoriented its Scrum ceremonies around agent membership (not just using AI tools but treating agents as team members)? The Agile Leadership Day India article describes the framework but does not cite an organization that has implemented it end-to-end.

4. The "dissolution vs evolution" framing needs a concrete audience anchor: what is the IM/DM doing on Monday morning differently? The research supports the direction but the closing arc needs a very specific day-in-the-life scenario to land.

5. Token cost governance as a delivery metric: is there a standard emerging (cost-per-story-point equivalent, or cost-per-sprint)? No source found establishing this as a formal metric yet — may be a genuine white space the deck can name first.

---

## 8. Supplementary Research — IM/DM-Specific Evidence (2026-05-29, Pass 2)

### Gap status: Partially closed. Not fully closed.

The fatal gap (G2) — no evidence specific to SM/IM/DM roles, only general knowledge-worker data — is now **partially closed**. There is meaningful IM/DM-specific evidence available from practitioner surveys and documented organizational case studies. However, the gap is not fully closed because: (a) no peer-reviewed academic study tracks SM/IM/DM outcomes longitudinally in the context of AI adoption specifically, and (b) the strongest headcount evidence (Capital One, Royal London) is pre-AI in causation — it documents structural role dissolution driven by organizational maturity and cost pressure, not AI adoption. The AI-specific role-change evidence remains at the practitioner survey level. This is explicitly noted for the deck writer.

---

### Finding 1: The AI4Agile Practitioners Report 2026 — the only primary survey of agile practitioners on AI adoption

**Source:** Stefan Wolpers, Age-of-Product.com / Scrum.org. Published February 8, 2026. Survey of 289 agile practitioners (Scrum Masters, Agile Coaches, Product Owners, Product Managers) across 20+ countries.

**Key statistics:**

- 83% of agile practitioners already use AI tools
- 55% spend 10% or less of work time with AI — adoption is wide but shallow
- Only 15% have received any formal AI training in an agile context
- Only 9% spend more than 25% of their work time with AI
- On a 0–6 scale measuring "AI as a threat to my role," the mean score was 2.75; more than half scored 1–2; only 7.6% viewed AI as a significant role threat
- Top three reported benefits: increased productivity (73.7%), reduced cognitive load (71.6%), greater focus (71.6%)
- Biggest adoption barrier: integration uncertainty (54.3%) — practitioners do not know how to embed AI into Sprint Planning, Refinement, and Retrospectives

**Qualitative signal:** Practitioners' primary worry is erosion of Agile values and human collaboration, not personal job displacement. This is consistent with low threat perception scores but does not mean displacement risk is absent — it may reflect the "gradual hollowing" pattern identified in Arc 4 of the main brief.

**Confidence: Medium-High.** Primary practitioner survey, published by a credible industry voice (Wolpers) in partnership with Scrum.org. Sample size (289) is adequate for directional findings but not large enough for subgroup analysis by role. No control group; self-reported.

**Deck utility:** The 83% adoption rate and the integration uncertainty finding are directly usable. The low threat-perception score is useful counter-framing: the audience likely shares this complacency, which is exactly why the deck's "gradual hollowing" argument needs to land before they dismiss the risk.

---

### Finding 2: Digital.ai 18th State of Agile Report (2025) — first edition to focus entirely on AI

**Source:** Digital.ai, 2025. Sample: nearly 350 respondents, primarily Agile coaches and consultants from large enterprises (20,000+ employees).

**Key statistics:**

- AI adoption among agile practitioners rose from 68% to 84% year-over-year
- 27%+ of organizations are already experimenting with autonomous agentic systems for workflow execution, risk detection, change management, and planning
- 41% have deployed coordinated AI tools across teams
- Only 49% have governance guardrails in place — a significant gap given the 84% adoption rate
- 29% of respondents now carry responsibility for "connecting Agile work to business outcomes" (up from activity-based metrics)
- 26% are "influencing product and portfolio planning"
- 76% say ROI pressure is reshaping role assignments

**Confidence: Medium.** Primary industry survey. Sample is small (350) and skewed toward coaches and consultants in large enterprises — not representative of the full SM/IM population. The report does not disaggregate findings by role title, so it is impossible to isolate Scrum Master vs. Delivery Manager responses.

**Deck utility:** The 84% adoption figure and the governance gap (49% with guardrails vs. 84% adoption) are directly usable for the governance arc. The role accountability shift — from activity to outcomes — is the clearest survey evidence of role evolution pressure on this specific population.

---

### Finding 3: Scrum Master training enrollment collapse (2020–2024)

**Source:** Stefan Wolpers, Age-of-Product.com, "The Scrum Master Role Decline," published January 5, 2025.

**Key statistics:**

- Scrum Master class enrollment as a share of total training: 49% (2020) → 26% (2021) → 24% (2022) → 17% (2023) → less than 5% (2024)
- Wolpers' Scrum Master Interview Questions Guide downloads: 2,428 (2022) → 1,236 (2024), approximately 49% reduction in two years
- The 2024 Scrum Master Salary Report attracted fewer than 650 valid datasets, below the 1,000-participant threshold Wolpers considers statistically usable; he has stated there will likely be no 2025 edition

**Important caution:** Wolpers attributes this decline to organizational maturity and economic pressure, not to AI. The training enrollment decline began in 2021, before generative AI adoption. This is a structural supply/demand signal, not an AI-causation signal.

**Confidence: Medium.** Single analyst's observation data from a credible, long-running source (Wolpers has tracked this population since 2016). Not a formal market study. The trend direction is clear but the cause is contested.

**Deck utility:** This is the strongest quantitative signal of SM role pressure in the available evidence base. It does not prove AI causation but establishes that role contraction was already underway before AI arrived — making the AI argument a "second wave" intensifier rather than the originating cause.

---

### Finding 4: Documented organizational case studies — Capital One, Royal London, and a major UK bank

**Sources:** Bloomberg / Reuters (January 19, 2023) — Capital One; Sjoerd Nijland, Serious Scrum / Medium (January 20, 2023) — analysis; multiple secondary sources for Royal London.

**Capital One (confirmed, January 2023):**
- Eliminated 1,100 technology roles, wiping out the entire "Agile" job family: Agile Delivery Leads, Agile Program Leads, Agile Portfolio Leads, Product Owners
- Official statement: "The agile role in our tech organization was critical to our earlier transformation phases, but as our organization matured, the natural next step is to integrate agile delivery processes directly into our core engineering practices"
- Responsibilities were redistributed into existing engineering and product manager roles

**Royal London (partially confirmed):**
- Multiple practitioner sources report that Royal London made approximately 90% of its Scrum Masters redundant in 2023
- No primary news source (FT, Reuters, BBC) was located to independently confirm the 90% figure; this circulates as practitioner testimony, not verified press reporting

**Unnamed major UK bank:**
- Multiple practitioner accounts report a major UK bank eliminated approximately 1,000 Scrum Master and Agile Coach roles in one restructuring. No primary source confirmed.

**Critical contextualization:** In all three cases, the stated rationale was organizational maturity and cost pressure, not AI adoption. None of these occurred because AI tools replaced the work. They represent the pre-existing vulnerability the deck's argument rests on: agile delivery roles are perceived as non-value-producing overhead when examined under ROI pressure. AI intensifies that pressure by making the overhead more visible and the substitution more plausible.

**Confidence: High for Capital One** (primary news sources, official corporate statement). **Low-Medium for Royal London and the UK bank** (practitioner testimony only; not independently confirmed by news sources in this research pass).

**Deck utility:** Capital One is fully citable as a documented case study. The quote from Capital One's official statement is the clearest organizational articulation of the dissolution rationale available. Use it verbatim. Royal London and the UK bank should be referenced as "reported by multiple practitioners" with a footnote on source quality, not cited as hard fact.

---

### Finding 5: Scaled Agile's AI-Empowered RTE certification — institutional acknowledgment of role transformation

**Source:** Scaled Agile, Inc. Launched November 2025; AI-Empowered RTE certification effective December 2025.

SAFe has formally restructured the Release Train Engineer (the SAFe-equivalent of the Iteration Manager) certification to include an AI module. The "Empowering Release Train Engineers with AI" skill addresses: AI-enhanced forecasting and dependency mapping, automated stakeholder communication, and SAFe CoPilot integration for data-backed recommendations.

SAFe has also published six "Empowering with AI" role-specific skill modules, indicating institutional recognition that each delivery role requires a distinct AI adaptation path.

**Confidence: High** that Scaled Agile has formally updated the RTE role to incorporate AI. **Medium** on the practical significance — the AI lesson is described as 45 minutes of self-paced e-learning, and SAFe explicitly states the content is still being refined. This is the credentialing body acknowledging the direction, not a measure of actual role transformation in the field.

**Deck utility:** The certification update is directly usable as evidence that the leading enterprise agile framework has formally acknowledged AI changes what RTEs/IMs do. It is not an empirical finding about what practitioners are actually doing differently — it is an institutional signal.

---

### Finding 6: The Scrum.org survey on SM job security perception (2023) — requires caution

A widely cited statistic in the practitioner blogosphere holds that a "Scrum.org 2023 survey found 80% of Scrum Masters believe AI can help them, only 12% feel it threatens their job."

**This statistic could not be independently verified from a Scrum.org primary source in this research pass.** Multiple secondary blogs cite it, but no Scrum.org publication was located that reports these exact percentages with methodology. The AI4Agile Practitioners Report 2026 (Finding 1) reports similar directional findings (only 7.6% view AI as a significant threat) from a verifiable source with stated methodology — use that instead.

**Confidence: Unverified.** Do not cite the 80%/12% statistic as a Scrum.org finding without locating the primary report.

---

### Finding 7: The Gartner "30% of agile documentation by 2026" claim — do not use

A statistic frequently cited in SM/AI blog posts holds that "a 2024 Gartner report says AI could handle 30% of Agile documentation and reporting by 2026."

**This claim was not verified against any Gartner primary source in this research pass.** No Gartner press release or published report matching this specific prediction was located across multiple search queries. This appears to be a secondary misattribution circulating in agile practitioner content. **Do not use this in the deck without locating the primary Gartner report.**

---

### Synthesis: What this evidence base does and does not close

**What is now available (closes G2 partially):**

| Evidence type | Source | Confidence |
|---|---|---|
| Practitioner survey — AI adoption rates among agile practitioners | AI4Agile 2026 (n=289) | Medium-High |
| Practitioner survey — role accountability shifting to outcomes | Digital.ai 18th SoA (n=350) | Medium |
| Headcount signal — SM training enrollment collapsed from 49% to <5% share | Wolpers / Age-of-Product (2020–2024) | Medium |
| Organizational case study — 1,100 agile roles eliminated | Capital One, January 2023, primary sources | High |
| Institutional acknowledgment — RTE/IM role formally restructured around AI | Scaled Agile, November 2025 | High |

**What remains absent (gap not fully closed):**

- No peer-reviewed academic study of SM/IM/DM roles in an AI adoption context (all academic work covers knowledge workers generally)
- No longitudinal data tracking SM/IM job outcomes before and after AI tool adoption within the same organizations
- No documented case study of a team that restructured SM/IM/DM work because AI tools absorbed the workload (Capital One is organizational maturity; it is not AI-caused)
- No verified primary-source data on job posting volume trends for SM/IM roles that is more specific than the enrollment proxy

**Recommended deck framing given the available evidence:**

The argument should be: "The dissolution pressure on agile delivery roles was already real and documented before AI arrived — Capital One's 2023 action is the proof point. AI makes that pressure structural and accelerating, because it now makes the substitution more plausible than ever." This framing uses the verified evidence (organizational maturity pressure + Capital One case) as the established baseline and AI as the accelerant — rather than claiming AI is already directly causing SM role eliminations, which the evidence does not yet support.

---

### Methodology (Pass 2)

**aa2brain vault search:** Searched with terms "scrum master," "iteration manager," "delivery manager," "agile coach," "state of agile," "SM role," "agile job," "agile layoff." Located two relevant vault entries: the CapitalOne Spiky POV note (Adnan's own 2023 observation) and a LinkedIn feed clip on SM questioning practices. No State of Agile report clippings, no Digital.ai data, no AI4Agile data found in vault.

**External search:** Conducted 14 targeted web searches and 8 WebFetch calls. Search terms covered: State of Agile 2024/2025 AI findings; Digital.ai 18th report; AI4Agile Practitioners Report 2026; Capital One agile layoffs; Royal London agile redundancies; Scrum Master job posting volume trends; Scrum.org SM job security survey; SAFe RTE AI certification; Gartner agile documentation claim; Stefan Wolpers SM salary/decline data.

**Triangulation:** All significant findings verified against at least two independent sources where possible. Capital One data corroborated across Bloomberg/Reuters (primary news), Sjoerd Nijland (practitioner analysis), and Gene/keystepstosuccess.com. AI4Agile 2026 statistics corroborated across Wolpers/Age-of-Product, Scrum.org blog summary, and DZone repost. Two unverified claims (Scrum.org 80%/12% figure; Gartner 30% figure) explicitly flagged as uncitable.

**Limitations:** Royal London headcount figure (90%) rests on practitioner testimony, not primary news source — treat as Low confidence. The AI4Agile survey sample (289) is too small for role-specific subgroup analysis. No access to paid analyst databases (Burning Glass, EMSI) that would provide job posting volume data over time.

---

## 9. Supplementary Research — SM-to-IM Transition Wave Evidence (2026-05-29, Pass 3)

### Framing note

This pass was tasked with building an evidence base for the "two-wave" historical narrative in Arc 4: Wave 1 (2021–2023) = pure SM/Agile Coach role elimination driven by ROI pressure under rising interest rates; Wave 1 outcome = emergence of hybrid "Agile Delivery Lead" / "Iteration Manager" roles; Wave 2 (now) = AI creates the next consolidation pressure, and the IM who learns to architect hybrid teams survives. Capital One is explicitly dropped from the evidence base per Adnan's instruction.

---

### Finding A: The QE-to-QT mechanism — the best available explanation for Wave 1

**Source:** Viktor Cessan, "How Cheap Money Created an Agile Coach Bubble," viktorcessan.com, published March 18, 2025. Cessan is a Professional Scrum Trainer with Scrum.org credentials and an enterprise agile coach.

**The argument in full:**

During the decade of zero-interest-rate policy (ZIRP) and quantitative easing (QE) up to 2022, capital flowed freely into tech. Companies prioritized growth over profitability. Hiring expanded unchecked, and agile roles proliferated — but the demand was for growth management and chaos reduction, not for measurable delivery outcomes. Cessan's exact formulation: "Agile Coaches were mostly not hired to enable and drive performance and profits, they were hired to support growth, or reduce the negative effects of growth."

In 2022, central banks shifted to quantitative tightening (QT): selling assets, raising interest rates. This made borrowing expensive, shrank corporate cash flows, and forced a return to profit accountability. Roles that could not demonstrate direct contribution to revenue, cost reduction, or efficiency metrics became immediately vulnerable. The Agile Coach was exposed as structurally misaligned with this new accountability regime — many had positioned as cultural facilitators and psychological safety experts, not delivery outcome owners.

Cessan's predicted future model: Agile Coaching will resemble "how we use lawyers and financial advisors" — short, high-impact interventions rather than indefinite team embeddings. Remaining practitioners must demonstrate financial literacy and quantifiable impact.

**Corroboration:** The QE/QT mechanism is independently restated in at least two other sources examined in this pass. The Humanizing Work podcast ("Making Sense of the ScrumMaster & Agile Coach Layoffs," June 2024) identifies the same dynamic: roles lacking "obvious direct connection to revenue generation" became casualties of budget tightening. The All Things Agile 2024 job market article ("Surviving the Agile Job Market in 2024") attributes the layoffs to a shift "towards a recession" and "leaner operations" that started in 2022.

**Confidence: Medium-High.** The QE/QT causal mechanism is independently triangulated across three practitioner analysts. It is a structural economic argument, not empirically measured against role headcount data — no one has run a regression between central bank rate decisions and SM job postings. The directionality is credible and the timing is consistent with documented layoffs.

**Deck utility:** This is the clearest available explanation of *why* Wave 1 happened in 2022–2023. It gives the "pure facilitation roles couldn't show ROI" argument a structural economic cause rather than leaving it as a vague claim about org maturity. Cessan's framing is citable. It does not require Capital One.

---

### Finding B: The SM training enrollment collapse — quantified supply-side signal for Wave 1

**Source:** Stefan Wolpers, "Scrum Master: Is an Era Coming to an End?", Age-of-Product.com, published January 5, 2025. Wolpers is a Professional Scrum Trainer (PST) with Scrum.org; he has tracked Scrum Master salary and training data since 2016.

**Data points (his own business as proxy for the broader market):**

| Year | SM classes as % of total training enrollment |
|---|---|
| 2020 | 49% |
| 2021 | 26% |
| 2022 | 24% |
| 2023 | 17% |
| 2024 | < 5% |

Additional signal: Wolpers' SM Interview Questions Guide downloads halved from 2,428 (2022) to 1,236 (2024). His SM Salary Report attracted fewer than 650 usable datasets against a 1,000-participant threshold for statistical validity; he has publicly stated there will likely be no 2025 edition.

**Important caution:** Wolpers attributes the decline to organizational maturity and economic pressure, *not* to AI. The training enrollment collapse began in 2021, before generative AI had any meaningful enterprise adoption. This is structural role contraction, not AI-caused contraction.

**Confidence: Medium.** Single analyst's data from a credible, long-running source. The trend direction is unambiguous. Causation is contested; Wolpers himself offers organizational maturity as the primary driver. The data is a proxy (one PST's enrollment figures) not an industry-wide measurement.

**Deck utility:** This is the strongest available quantitative signal of Wave 1 role contraction. It does not rely on Capital One. The 49% to less than 5% trajectory over four years is a striking data point that the deck can use directly as evidence of Wave 1 momentum.

---

### Finding C: The dedicated Agile Coach role demand — institutional survey data

**Source:** Scrum Alliance and Business Agility Institute, "Skills in the New World of Work" joint report, cited in Scrum Alliance article "How to Pivot Your Career and Demonstrate Value Amid Agile Role Layoffs" (resources.scrumalliance.org, approximately mid-2023).

**Key finding:** Only 18% of organizations report dedicated demand for Agile Coaches as a standalone role. The actual skill of coaching is desired within other roles — organizations want agile competencies embedded, not isolated.

Additional data from the same report:
- 64% of companies report increased agile skills demand over the past year (skills are valued; dedicated roles are not)
- 93% say it is moderately difficult or harder to find people with all core skills needed
- Communication is the number-one desired agile skill (cited by nearly two-thirds of companies); seven of the top ten skills are soft skills

**Corroboration:** The Humanizing Work podcast independently describes the same structural dynamic: "demand for agile coaches as a dedicated role is low (18% of organizations)." The Digital.ai 18th State of Agile (2025, n=350) shows 76% of respondents say ROI pressure is reshaping role assignments, which is directionally consistent — organizations demanding measurable outcomes rather than facilitation headcount.

**Confidence: Medium.** The 18% figure appears to originate in the Scrum Alliance/BAI joint report, which is cited rather than directly accessible in this research pass. The figure is multiply cited across independent outlets suggesting it is accurate. Sample size and methodology of the underlying report are not confirmed.

**Deck utility:** The 18% dedicated-role demand figure directly supports the framing that pure Agile Coach roles became organizationally marginal. Pair it with the enrollment data from Finding B for a two-data-point Wave 1 claim.

---

### Finding D: The emergence of hybrid delivery-agile roles — evidence and timeline

Three independent genealogies for the hybrid role are traceable. They should be treated as distinct lineages, not a single unified trend.

**Lineage 1: UK Government Digital Service (GDS) origin of "Delivery Manager"**

Source: Emily Webber, "Explaining the Role of a Delivery Manager," emilywebber.co.uk, originally published January 2016 (updated 2018). Webber was head of the Delivery Manager role at GDS.

The Delivery Manager role was deliberately constructed at GDS to be framework-agnostic — the title was chosen precisely to avoid the Scrum-specific connotations of "Scrum Master." The role was explicitly accountable for team delivery outcomes (financial tracking, stakeholder communication, removing blockers) *and* agile/lean practice leadership. This is the earliest documented hybrid role in the lineage.

**Confidence: High** — primary source, specific organizational origin, named author with direct institutional authority.

**Lineage 2: Australian "Iteration Manager" as SAFe/hybrid-framework response**

The Iteration Manager title appears primarily in Australian enterprise agile contexts where hybrid approaches (blending Scrum, Kanban, SAFe) are more common than pure Scrum. It combines the Scrum Master's ceremony facilitation with explicit delivery outcome accountability across a program increment. Elabor8.com.au (an Australian agile consultancy) describes it as the role "most commonly seen in scenarios where hybrid Agile approaches are adopted."

LinkedIn evidence from 2021–2022 shows active hiring of Iteration Manager roles at Australian financial institutions and large enterprises (Kmart Australia, National Australia Bank). The role predates the Wave 1 layoffs — it is the hybrid form that existed alongside pure SM roles, not one that emerged after Wave 1.

**Confidence: Medium.** Multiple independent sources confirm the Australian Iteration Manager exists and is specifically linked to hybrid frameworks. No aggregate job posting volume data for this specific title was accessible without paid labor market databases.

**Lineage 3: "Agile Delivery Manager" / "Agile Delivery Lead" as post-2022 market response**

The most direct evidence for Adnan's historical narrative: the Agile Delivery Manager (ADM) role is explicitly identified by echometerapp.com as "a trend in the agile community since 2023 at the latest, as interest rates rise and many companies can no longer afford a Scrum Master who often becomes more of a 'team coach/feel-good manager'."

The Babylon case study (Edward Lowe, Velocity Agile Substack, April 2022) describes an ADM as an embedded team member accountable for "the performance of the engineering team" — explicitly contrasting this with agile coaches who "have much more limited accountability for the performance of the team and the results." This is pre-Wave 1 in timing (April 2022) but conceptually the hybrid model Adnan describes.

The Rethink Your Understanding / Medium article (April 2025, n=1 practitioner) documents their organization formally renaming to "Agile Delivery Manager" in 2025, describing it as "the culmination of years of observing the gap between traditional agile roles and modern delivery demands." They characterize ADMs as "system-level delivery architects."

**Confidence: Medium** for the emergence trend overall. **High** that the Babylon ADM case predates Wave 1 and already contains the hybrid accountability model. The echometerapp timing attribution ("since 2023") is consistent with the post-QT market shift. No aggregate job posting data was accessible.

**Deck utility:** The three lineages together support the claim that the hybrid delivery-agile role (Delivery Manager, Iteration Manager, Agile Delivery Lead, ADM) was not invented after Wave 1 — it was already emerging or existed in parallel, and Wave 1's pressure accelerated its adoption as the surviving form. The GDS genealogy is particularly useful: it shows the hybrid model has a decade of organizational validation, not just a post-2022 emergency response.

---

### Finding E: The ROI accountability argument — practitioner and analyst writing

This is the best-supported finding in the pass. Multiple independent sources articulate the same structural argument.

**The core mechanism (triangulated across four sources):**

1. Viktor Cessan (March 2025): QE era removed profit accountability; agile roles hired to manage growth, not demonstrate ROI. QT era reinstated it. Roles that could not express value in revenue/cost terms were cut.

2. Humanizing Work podcast (June 2024): "Agile as a declining brand." Organizations invested heavily in agile transformations, failed to achieve promised returns, and concluded further investment was wasteful. The Scrum Master role "lacks obvious direct connection to revenue generation."

3. Scrum Alliance / BAI "Skills in the New World of Work" report (~2023): Only 18% of organizations want dedicated agile coaches. The skill is valued; the isolated role is not. The accountability regime is shifting toward delivery outcomes.

4. Stefan Wolpers "Why Agile Practitioners Should Be Optimistic for 2026" (Hands-on Agile Substack, February 2026): Wolpers acknowledges the structural threat to framework-identity practitioners but argues that those who reposition around "solving organizational problems" — not "running Daily Scrums and maintaining the Sprint Backlog" — will find expanding demand. This is the same accountability pivot stated positively.

**Confidence: High** that the ROI accountability shift drove Wave 1. **Medium** on the precise timeline and the question of whether this was more significant than the parallel factor of organizations declaring their agile transformations "complete" and eliminating the change agent layer.

**Deck utility:** The ROI accountability argument is the load-bearing claim for why Wave 1 happened. It does not need Capital One. The four-source triangulation above gives the deck writer more than enough to cite. Cessan's formulation is the most citable: "Financial discipline is back, and with it, many roles are disappearing, including Agile Coaches. This isn't because Agile itself is failing but because capital is expensive, and companies now demand real returns on every role."

---

### Finding F: Adnan's own Substack article — how it fits the evidence base

**Source:** Adnan Ali, "Capital One Eliminated So-Called Agile Roles — Here's What We Can Learn," ahaagile.substack.com, published January 23, 2023.

Adnan's thesis is directionally consistent with the broader practitioner literature but distinct in its emphasis: where Cessan focuses on macro-economic mechanism (QE/QT) and Wolpers focuses on quantified role contraction, Adnan focuses on *why the Agile Coach role was epistemically vulnerable* — its value was liminal to the organization, and coaches undermined their own case with a hands-off facilitation stance that organizations could not translate into business outcomes.

This framing — "liminal value" — is the most intellectually precise formulation in the evidence base. It explains not just that agile roles were cut, but why they were *seen as cuttable* even when they were delivering real value. The organization could not perceive the value because it was constituted as a facilitation and culture function, not a delivery outcome function.

**Deck relevance:** Adnan does not need to use Capital One as the case. The article's *argument* — liminal value, hands-off positioning, org perception failure — is the intellectual substrate for the Wave 1 claim. The deck should inherit the argument without inheriting the case study. The supporting evidence from this pass (Cessan's QE/QT mechanism, Wolpers' enrollment data, the 18% dedicated-role demand figure) grounds the argument in data that does not depend on any single corporate case.

---

### Finding G: Wider practitioner community writing on SM-to-IM/hybrid transition

**Substack ecosystem:** Active agile practitioner Substacks confirmed: Stefan Wolpers (Hands-on Agile), Sjoerd Nijland (Serious Scrum via Medium), Adnan Ali (Aha! Agile), agilechronicles.substack.com (Debashish Chakrabarty), agilexpert.substack.com, bobgalen.substack.com (Agile Moose). The Wolpers and Nijland voices are both credible and frequently cited in practitioner literature; their analysis triangulates with Adnan's framing.

**Stefan Wolpers' February 2026 Substack piece** is directly usable: it explicitly names the transition from framework-identity SM to organizational problem-solver as the career survival path. This is the practitioner articulation of exactly what the deck argues.

**Broader Medium/LinkedIn community:** Multiple practitioner articles on the SM-to-ADM/Delivery Manager transition were published 2022–2025. The Rethink Your Understanding piece (April 2025) and the Babylon ADM case (April 2022) are the two most substantive primary practitioner accounts found.

**Confidence: Medium** that there is a wider practitioner community writing on this transition. **No quantitative data** on volume or reach of this writing is available. The community exists but is diffuse — it has not coalesced around a single canonical framing the way the BCG/Mollick research has coalesced around "jagged frontier."

---

### Synthesis: Does this evidence close G2 better than the Capital One framing?

**Yes — and it closes it more durably.**

The Capital One framing closed G2 (the dissolution claim) with a single organizational case study. It was compelling but depended on one company's decision, which made the claim brittle: audiences could dismiss it as an outlier or as pre-AI, which is precisely what Adnan now wants to avoid.

The Wave 1 historical narrative supported by this pass is structurally stronger for three reasons:

**1. Multi-source convergence.** The dissolution claim is now supported by: quantified training enrollment collapse (Wolpers, 49% to <5%); macro-economic mechanism (Cessan, QE/QT); institutional survey data (Scrum Alliance/BAI, 18% dedicated-role demand); and convergent practitioner analysis from at least four independent voices. No single data point is load-bearing.

**2. The audience lived it.** IMs and Delivery Managers in the room in 2026 were working in 2021–2023. They do not need to be told Wave 1 happened — they need it *named and contextualized*. The deck's job is not to prove Wave 1 to a skeptical audience but to frame it as the historical precedent that makes Wave 2 legible. The evidence base now supports that framing.

**3. Capital One is now optional as supporting detail, not required.** If the deck writer decides to use Capital One as a historical illustration — not as the causal AI argument but as a documented instance of Wave 1 pressure — the evidence base supports that. But the argument no longer depends on it.

**What the evidence does not close:**

- No longitudinal job posting volume data was accessed. The enrollment proxy (Wolpers) is the closest available signal, but it is not job posting data. If Adnan wants a "SM job postings fell X% from 2021 to 2023" claim, that requires a paid labor market database (Lightcast/Burning Glass) or a published study using such data.
- The emergence of hybrid roles is documented qualitatively and in specific organizational cases, not as an aggregate hiring trend with numbers attached. The claim "the Agile Delivery Lead / Iteration Manager role *grew* in this period" is supported by practitioner observation and structural logic but not by aggregate job posting statistics.
- The direct causal link "Wave 1 pressure → IM/ADM role created → that role is now what's at stake in Wave 2" is an interpretive argument, not an empirically measured transition. The evidence supports the interpretation; it does not prove it.

---

### Wave 1 evidence summary table

| Evidence type | Source | Confidence |
|---|---|---|
| Macro-economic mechanism for Wave 1 (QE/QT, ROI pressure) | Viktor Cessan, March 2025 | Medium-High |
| SM training enrollment collapsed 49% → <5% in four years | Stefan Wolpers, Age-of-Product, Jan 2025 | Medium |
| Only 18% of orgs have dedicated Agile Coach demand | Scrum Alliance/BAI joint report, ~2023 | Medium |
| "Liminal value" argument for why Agile Coach was epistemically vulnerable | Adnan Ali, ahaagile.substack.com, Jan 2023 | N/A (primary author) |
| Agile Delivery Manager role explicitly linked to post-2022 interest rate environment | echometerapp.com; Cessan; multiple practitioners | Medium |
| GDS origin of Delivery Manager as decade-old validated hybrid model | Emily Webber, 2016 | High |
| Babylon ADM case: embedded accountability vs. coach hands-off model | Edward Lowe, Velocity Agile Substack, April 2022 | Medium |
| Practitioner community actively writing on SM-to-ADM transition | Wolpers (Feb 2026), Nijland, Rethink Your Understanding (2025) | Medium |

---

### Recommendations for the deck writer

1. **Use the Wave 1 framing without Capital One.** The QE/QT mechanism (Cessan), the enrollment collapse (Wolpers), and the 18% dedicated-role demand (Scrum Alliance/BAI) give you a three-data-point Wave 1 argument that does not depend on any single organization.

2. **The Cessan quote is the most citable formulation for the ROI argument:** "Financial discipline is back, and with it, many roles are disappearing, including Agile Coaches. This isn't because Agile itself is failing but because capital is expensive, and companies now demand real returns on every role." (March 2025, viktorcessan.com.)

3. **Frame the hybrid role genealogy as validation, not novelty.** The GDS Delivery Manager (2014–2016) and the Babylon ADM (2022) show this model has been validated for a decade. The IM/Agile Delivery Lead is not a desperate post-Wave-1 improvisation — it is the mature organizational form for delivery-accountable agile leadership.

4. **The Wolpers Feb 2026 Substack piece is the audience-facing articulation to cite.** His framing — "If your professional identity is 'I run Daily Scrums and maintain the Sprint Backlog,' then yes, AI is a threat" — is directly usable as a reflection prompt for the audience. It bridges Wave 1 and Wave 2 in one sentence.

5. **Do not claim aggregate job posting data you do not have.** The enrollment proxy is adequate to establish the trend direction. Do not overstate it as job posting data — the distinction matters for a sophisticated audience.

---

### Methodology (Pass 3)

**aa2brain vault search:** Searched with terms "scrum master decline," "agile coach layoff," "iteration manager," "delivery lead," "QE QT agile," "cheap money agile," "liminal." The vault contained Adnan's own January 2023 Capital One observation note. No external sources on Wave 1 economics, Cessan, Wolpers' enrollment data, or hybrid role emergence were found in the vault.

**External searches:** 12 targeted web searches. Key terms: Scrum Master job postings 2021–2024 decline; Agile Coach layoffs 2022 2023 interest rates ROI; Viktor Cessan cheap money agile coach bubble; Iteration Manager Agile Delivery Lead emergence hybrid role; State of Agile report role title data; Scrum Alliance/BAI skills report 18% dedicated demand; Humanizing Work agile jobs vanishing; SM-to-IM transition practitioner Substack Medium.

**WebFetch calls:** 11 direct page fetches. Targets included: viktorcessan.com (cheap money thesis), humanizingwork.com (layoff analysis), age-of-product.com (enrollment data), ahaagile.substack.com (Adnan's original article), velocityagile.substack.com (Babylon ADM case), emilywebber.co.uk (GDS Delivery Manager), echometerapp.com/agile-delivery-manager, allthingsagile.co, resources.scrumalliance.org/Article/avoid-agile-layoffs, medium.com/serious-scrum (Nijland/Capital One), medium.com/@rethinkyourunderstanding (SM-to-ADM evolution), handsonagile.substack.com (Wolpers Feb 2026).

**Triangulation:** The QE/QT mechanism triangulated across three independent sources. The 18% dedicated-role demand figure located in the Scrum Alliance/BAI report and multiply cited. The enrollment collapse is a single-source data point (Wolpers) with no independent quantitative corroboration — confidence appropriately rated Medium. No unverifiable statistics were flagged for deck use in this pass.

**Limitations:** No access to paid labor market databases (Lightcast, EMSI, Burning Glass) that would provide aggregate job posting volume data for SM/Agile Coach/IM titles across 2020–2024. The absence of this data means the quantitative case for Wave 1 rests on a training enrollment proxy rather than direct job market measurement. The hybrid role emergence claim is qualitatively supported but lacks aggregate hiring statistics. The Babylon ADM case is a single organizational example (and the author explicitly notes it represents his personal interpretation, not official Babylon documentation).
