# Supplementary Research Brief — hybrid-delivery v3

**Date:** 2026-06-07
**Builds on:** `decks/hybrid-delivery/research/2026-05-30-research-brief-v2.md` (and v1, 2026-05-29)
**Prepared by:** Pax, Senior Research Specialist
**For:** hybrid-delivery deck v1.4.0 → v1.5.0 — Larry / Adnan Ali
**Trigger:** Adnan slide-by-slide feedback (`reports/2026-06-07-feedback-v1.4.0.md`), not a scheduled sweep.

---

## Scope note (WS-005 lens applied, but reframed)

This is a **confirm-and-source** task, not a "did the world change" significance sweep. Adnan has already committed to both frameworks for two specific slides. My job: ground them in the most credible available sources, recommend the best-fit version, and **surface any credibility problems** before they go on a slide. The WS-005 threshold (new independent source + claim impact + recency) is met for both deliverables — all sources below are new to the deck's evidence base except the VERDICT material already captured in v1.

Two deliverables:
1. **Agent Capability Maturity model** for the NEW opening Slide 3.
2. **VERDICT AI-governance framework** for the Slide 20 rewrite.

---

# DELIVERABLE 1 — Agent Capability Maturity Model (new Slide 3)

## Executive summary

The exact five-rung ladder Adnan named — **augmented → assisted → collaborative → orchestrated → autonomous** — is **NOT an established, canonical framework**. It is a **synthesis** (Adnan's own ordering of terms that float around the agentic-maturity literature). The closest single published source that uses all five words (Adaline Labs) orders them differently and pins them to generic level numbers, not to those words as the rung labels. **Confidence that "those five named rungs in that order" is canonical: Low (it is not).**

However, the *underlying idea* — a 5-level autonomy spectrum where the human's role changes as autonomy rises — is **well-established and convergent across multiple credible sources**, including a peer-reviewed-track academic working paper, an industry-standards body (Cloud Security Alliance), and major vendors (Microsoft, Salesforce, Gartner). **Confidence in the underlying 5-level autonomy concept: High.**

**Recommendation for an Iteration Manager audience:** Keep Adnan's five evocative labels as the *spectrum's surface vocabulary*, but anchor the slide's substance — and its citation — on the **University of Washington "Levels of Autonomy for AI Agents" paper (Feng, McDonald & Zhang, 2025)**, which frames each level by **what the human does** (Operator → Collaborator → Consultant → Approver → Observer). That human-role framing is exactly the angle Adnan asked for, it is the most defensible citation, and it maps directly to an IM's "where do I add value" question. Present it explicitly as a **synthesis** on the slide, not as "the" framework — that protects the deck from a "where did this come from?" challenge.

## Key findings

### Finding 1.1 — Adnan's exact five-rung ladder is a synthesis, not a canonical model. **Confidence: High (that it's a synthesis).**

I searched for the precise ordered set "augmented → assisted → collaborative → orchestrated → autonomous" across academic, standards-body, analyst, and vendor sources. No single authoritative source publishes those five words, in that order, as named maturity rungs. The terms each appear in the agentic-maturity discourse, but no one canonical framework strings them together this way. This is a **strength to be managed, not a flaw**: the labels are vivid and audience-friendly. They just must not be presented as a cited external framework — they are Adnan's articulation of a real, well-supported spectrum.

### Finding 1.2 — The single source closest to Adnan's wording (Adaline Labs) uses a different order. **Confidence: High.**

Adaline Labs, "The 5 Levels of Agentic AI" (Nilesh Barla, Jun 2025, updated Jan 2026) is the one widely-circulated piece that uses **augmented, assisted, orchestrated, collaborative, autonomous**. Critically:
- Its order is **augmented → assisted → orchestrated → collaborative → autonomous** — it places *orchestrated* (L3, single-agent multi-step) **before** *collaborative* (L4, multi-agent deliberation). Adnan has collaborative before orchestrated.
- The article's own *level names* are actually "Basic Responder / Router & Co-Pilot / Tool-Using Agents / Multi-Agent Systems / Fully Autonomous AGI" — the augmented/assisted/etc. words are descriptive overlays, not the rung labels.
- It is a **vendor blog** (Adaline is an LLM-eval tooling company), self-described framework, citing ReAct, MCP, MetaGPT, ARC-AGI as technical underpinnings. Credibility: Medium — coherent and well-written, but not authoritative.

**Implication:** If Adnan wants the *collaborative-before-orchestrated* order, he is making a defensible pedagogical choice (human-to-human-style collaboration feels "closer in" than full multi-agent orchestration) but it diverges from the one source that uses his vocabulary. Flag on the slide as a deliberate synthesis.

### Finding 1.3 — The best-sourced, best-fit backbone for an IM audience is the UW "Levels of Autonomy" paper. **Confidence: High.**

**Feng, K.J.K., McDonald, D.W., & Zhang, A.X. "Levels of Autonomy for AI Agents." University of Washington, Jun 14, 2025.** Working paper, to be published by the Knight First Amendment Institute (Columbia) — i.e. academic-track, not a vendor blog. Its organizing question is *"What is the role of the user when interacting with the agent?"* — and autonomy is defined as the degree to which the agent operates without user involvement. Five levels, each defined by the human's role:

| Level | Human's role | One-line definition |
|---|---|---|
| L1 | **Operator** | Agent gives on-demand support; the human owns long-term planning and decisions. |
| L2 | **Collaborator** | Human and agent jointly plan and execute, with frequent communication; human can take control anytime. |
| L3 | **Consultant** | Agent plans and executes; human supplies expertise/preferences via indirect feedback. |
| L4 | **Approver** | Agent runs autonomously but requests human sign-off on consequential or blocked actions. |
| L5 | **Observer** | Fully autonomous agent; human can only monitor logs and hit an emergency kill-switch. |

Key throughline (also stated by Sean Falconer and CSA below): **as autonomy rises, the human's job shifts from proactive gatekeeping to reactive auditing.** That single sentence is the load-bearing insight for an IM slide — it reframes the IM's evolution, not its elimination.

**Why this fits the IM audience best:** it is the only framework keyed entirely to *the human's role*, which is the deck's central argument ("the roles that survive will own what agents can generate but can't decide"). It is also the most academically defensible citation.

### Finding 1.4 — The autonomy-spectrum idea triangulates across three more independent, credible sources. **Confidence: High.**

| Source | Levels | Human-role framing | Credibility |
|---|---|---|---|
| **Cloud Security Alliance** — Jim Reavis, "Autonomy Levels for Agentic AI," Jan 28 2026. Explicitly maps to SAE J3016 driving levels. | 6 (L0–L5): No Autonomy → **Assisted** → Supervised → Conditional → High → Full | Executor → Approver → Plan Approver → Boundary Setter → Monitor → Executive Oversight | **High** — industry standards body; SAE analogy is the one Adnan gestured at. Notes L5 is "not appropriate for enterprise deployment today." |
| **Sean Falconer (AI @ Confluent), "The Practical Guide to the Levels of AI Agent Autonomy," Nov 2025** — synthesizes HuggingFace's 5-level model + the UW interaction model + SAE J3016 + Parasuraman/Sheridan/Wickens (aviation) + NIST ALFUS (robotics). | 5 (L0–L4) HuggingFace + UW overlay | Complete control → Router → Tool-caller → Supervisor → Observer | **Medium-High** — practitioner synthesis but explicitly grounds itself in the established cross-domain autonomy literature (aviation, robotics, automotive). Uses "augment," "collaborative," "centaur." Best single bibliography to cite for "this idea has deep roots." |
| **arXiv 2506.12469 = the UW paper above** (same authors) | 5 | as Finding 1.3 | **High** |

The SAE-driving-levels analogy Adnan reached for is real and is used explicitly by CSA and Falconer. It is a legitimate framing device.

### Finding 1.5 — Major vendors all publish agentic-maturity models, but **none uses Adnan's five words as rungs**, and most are org-adoption maturity (CMM-style), not human-role autonomy. **Confidence: High.**

These are useful to *name* on the slide (shows the concept is industry-wide) but **not** to adopt as the rung labels:

- **Microsoft Learn — "Agentic AI adoption maturity model"** (updated May 2026). Five levels, explicitly built on the **Capability Maturity Model (CMM)**: Initial (100) → Repeatable (200) → Defined (300) → Capable (400) → Efficient (500). This is *organizational adoption* maturity across five capability pillars — NOT a human-role autonomy spectrum. Good precedent for the slide title "Agent **Capability** Maturity" (CMM heritage) but wrong content for Adnan's rungs.
- **Salesforce — "The Agentic Maturity Model: A 4-Step Roadmap for CIOs"** (2025). Four levels: Information-Retrieval Agents → single-domain orchestration → multi-domain concierge → multi-agent ecosystem ("no one has gotten there"). Vendor/Agentforce-marketing. Does not use Adnan's words.
- **Gartner** — has its own 5-level agentic maturity framing (per 2026 Hype Cycle for Agentic AI) plus the widely-cited prediction that **40% of agentic AI projects will be canceled by end of 2027** (already in the deck via v1/v2 governance findings). Analyst-grade; specifics paywalled.

## Recommendation for Slide 3

1. **Keep Adnan's five evocative labels** (augmented / assisted / collaborative / orchestrated / autonomous) as the spectrum's surface vocabulary — they are memorable and audience-friendly.
2. **Anchor each rung on "what the human does"** using the UW Operator → Collaborator → Consultant → Approver → Observer framing. This is the citable backbone and the IM-relevant angle.
3. **Label the slide an explicit synthesis** — e.g. a small source line: *"Synthesis; autonomy-level framing after Feng, McDonald & Zhang (Univ. of Washington, 2025); cf. SAE J3016, Cloud Security Alliance 2026."* This pre-empts "where's this from?" and is honest.
4. **Mirror the slide title's CMM heritage** ("Agent **Capability** Maturity") — defensible via Microsoft's CMM-based model. Keeps it cleanly distinct from Slide 22's *AI Governance* Maturity ladder (VERDICT), per Adnan's resolved open-decision #4.
5. **The one-sentence takeaway to put on the slide:** *as agent autonomy rises, the human's role shifts from doing the work, to steering it, to governing it — gatekeeping becomes auditing.* That is the line every credible source agrees on, and it's the deck's whole thesis in one breath.

### Suggested rung table for the slide (synthesis, human-role anchored)

| Rung (Adnan's label) | Human's role | One line |
|---|---|---|
| **Augmented** | Operator | Human does the work; AI speeds up discrete steps (autocomplete, draft, summarize). |
| **Assisted** | Collaborator | Human and AI work side by side; AI suggests, human decides and can grab the wheel anytime. |
| **Collaborative** | Consultant | AI plans and executes a task; human supplies judgment and preferences, not keystrokes. |
| **Orchestrated** | Approver | Multiple agents run a workflow; human sets the gates and signs off on consequential actions. |
| **Autonomous** | Observer | Agents run end-to-end; human monitors, audits, and holds the kill-switch. |

(Note: this puts *collaborative* before *orchestrated* per Adnan's order. If he wants to match the one source that uses his exact words verbatim, swap them — but the human-role logic above reads cleanly in his order, so I'd keep it and label it a synthesis.)

## Deliverable 1 — primary source URLs

- UW "Levels of Autonomy for AI Agents" (Feng, McDonald, Zhang, 2025): https://arxiv.org/html/2506.12469v1 — **primary, recommended citation**
- Cloud Security Alliance, "Autonomy Levels for Agentic AI" (Reavis, Jan 2026, SAE J3016 mapping): https://cloudsecurityalliance.org/blog/2026/01/28/levels-of-autonomy
- Sean Falconer, "The Practical Guide to the Levels of AI Agent Autonomy" (Nov 2025, best cross-domain bibliography): https://seanfalconer.medium.com/the-practical-guide-to-the-levels-of-ai-agent-autonomy-ac5115d3af26
- Adaline Labs, "The 5 Levels of Agentic AI" (closest to Adnan's exact words, different order): https://labs.adaline.ai/p/the-5-levels-of-agentic-ai
- Microsoft Learn, "Agentic AI adoption maturity model" (CMM-based, supports the "Capability" title): https://learn.microsoft.com/en-us/agents/adoption-maturity-model/
- Salesforce, "The Agentic Maturity Model: A 4-Step Roadmap for CIOs": https://www.salesforce.com/news/stories/agentic-maturity-model/

## Credibility red flags — Deliverable 1

- **The named five-rung ladder in Adnan's order is not externally citable as a framework.** Present it as a synthesis or it invites a challenge. (High confidence.)
- The single source using his exact vocabulary (Adaline) is a vendor blog and orders two rungs differently. Don't cite it as the authority.
- Do not conflate the two distinct families on the same slide: **autonomy-level / human-role** models (UW, CSA, Falconer — the right one here) vs **organizational-adoption CMM** models (Microsoft, Salesforce). They answer different questions.

---

# DELIVERABLE 2 — VERDICT AI-Governance Framework (Slide 20 rewrite)

## Executive summary

VERDICT is a **7-pillar runtime-governance operating model for AI agents**: **V**alidation, **E**vidence, **R**untime Control, **D**ecisions, **I**dentity, **C**ost & Compliance, **T**ransparency. It is the work of two named practitioners — **Niharika Srivastav and Sanjay Saxena** — introduced in a **Maven live session ("7 Steps to Govern AI Agents," May 24 2026)** that doubles as marketing for their 6-week paid AI Governance Practitioner cohort.

**Credibility verdict: this is a single-source practitioner/consultant heuristic, not an academic or independently-validated framework.** There is **no book yet** (one is ~7 months into writing), no peer review, no independent adoption, and the entire evidence base traces to **one course recording in Adnan's own vault**. The deck's own v1 brief already flagged this correctly: *"consultant/practitioner framework from Maven live session; not independently validated or peer-reviewed. Useful heuristic but should not be cited as research."* That assessment stands. **Confidence in the VERDICT content as captured: High** (fully documented in the vault). **Confidence in VERDICT as an authoritative external framework: Low.**

**Recommendation:** It is fine to use VERDICT as a memorable *organizing scaffold* for Slide 20 — the seven pillars are internally coherent and each maps cleanly to a real IM cadence (mapping below). But **attribute it honestly** ("a practitioner governance model, Srivastav & Saxena, 2026") and **lean its credibility on the documented incidents it explains** (Knight Capital, Replit, Meta — all independently sourced in v2) rather than on VERDICT's own authority. Do not present VERDICT as established or research-backed.

## Key findings

### Finding 2.1 — VERDICT = the seven pillars, fully documented. **Confidence: High (content); Low (authority).**

Source: aa2brain vault — `entities/verdict-framework.md`, `raw/courses/7-steps-govern-ai-agents-maven-2026-05-24.md` (the full session transcript/brief). The canonical breakdown:

| Letter | Pillar | Problem it solves | Control |
|---|---|---|---|
| **V** | Validation | Agents execute unapproved actions | Pre-execution validation gates with policy enforcement |
| **E** | Evidence | No audit trail of what the agent did or why | Immutable, timestamped action logs with decision rationale (audit-ready) |
| **R** | Runtime Control | Governance applied only pre-deployment, not during execution | Live policy enforcement + kill-switch |
| **D** | Decisions | Agents make choices with no explainability | Decision logging with reasoning captured at each step |
| **I** | Identity | Agents act with no clear ownership/accountability | Agent identity registry with assigned human owners + access scopes |
| **C** | Cost & Compliance | Unchecked spend and regulatory violations | Automated spend caps, regulatory guardrails, usage monitoring |
| **T** | Transparency | Agents operate as black boxes | Real-time dashboards, stakeholder reporting, explainable outputs |

Headline framing from the source: *"VERDICT doesn't prevent AI. It prevents AI from going unchecked."* And: *"Not a checklist. Not a policy document. A repeatable governance operating model."*

### Finding 2.2 — Authorship, nature, and credibility. **Confidence: High.**

- **Authors:** Niharika Srivastav (AIGP-certified; 30+ yrs Bank of America / Charles Schwab / Blue Shield; Stanford Exec Leadership; co-author *Visual Guide to Cybersecurity*) and Sanjay Saxena (Chief AI Officer & founder, CyberEdx; 30+ yrs Deloitte / KPMG / CVS Health / Kaiser Permanente; Harvard MBA; CISSP). Both are credentialed, senior, credible *individuals*.
- **Nature:** A **practitioner/consultant heuristic**, delivered in a Maven course that funnels to a paid 6-week cohort + AIGP exam prep. By the authors' own admission a **book is still ~7 months from existing** ("we are working on a book to introduce this framework to the world"). No textbook, no peer review, no standards-body status.
- **Independent validation:** **None found.** The framework appears only in the authors' own Maven session and Adnan's vault notes derived from it. It does not appear in academic literature, analyst reports, or third-party adoption that I could locate. (Searched: vault full-text + web orientation. The web turned up the generic agentic-governance discourse, not VERDICT specifically.)

### Finding 2.3 — VERDICT is internally coherent and explains real, independently-documented incidents. **Confidence: Medium-High.**

The framework maps its pillars onto three real failures (the source's own table):

| Incident | VERDICT pillars implicated |
|---|---|
| Knight Capital, $440M in 45 min, 2012 (runaway trading algo, no kill-switch) | R + C |
| Claude Code misuse for data extortion, 2025 (no runtime monitoring) | R + E + D |
| "OpenClaw" third-party-skill tool attack | I + R + T |

Two of the deck's already-verified incidents (Replit production-DB deletion Jul 2025; Meta agent data leak Dec 2024 — both fully triangulated in v2) slot naturally into the same pillars: Replit = missing **V**alidation + **R**untime kill-switch; Meta = **I**dentity/authorization + **T**ransparency gap. **This is the move that makes VERDICT safe to use:** the pillars are credible *because the failures they name are independently documented*, not because VERDICT is authoritative.

### Finding 2.4 — VERDICT ships with two companion models already in the deck/vault. **Confidence: High.**

- **AI Governance Maturity Ladder** (Slide 22): Unseen 👻 → Observed 👁 → Controlled 🔒 → Autonomous Governance 🖥. "Most enterprises are between Level 1 and 2; VERDICT gets you to Level 3." This is the *same authors* — so Slides 20 and 22 share a single source. Worth noting for Adnan's "keep complementary with Slide 22" instruction: they are complementary by construction (same framework family), but that also means **both slides rest on one un-validated source.** Consider whether that concentration is acceptable.
- **Implementation phases:** EXPOSE → BIND → ENFORCE → SELF-GOVERN (a 4-phase rollout sequence).

## Mapping VERDICT to an Iteration Manager's cadences (for the Slide 20 rewrite)

This is the synthesis Slide 20 needs — each pillar mapped to a concrete IM activity or agile ceremony. This mapping is **my construction** (Pax synthesis), grounded in the pillar definitions; VERDICT's authors do not themselves map to agile ceremonies. Flag as synthesis on the slide.

| Pillar | IM cadence / daily activity | What the IM actually does |
|---|---|---|
| **V — Validation** | **Definition of Done / Sprint Planning** | Bake "which agent actions require a human gate before execution" into the DoD and acceptance criteria. The IM owns *where the gates live*, not the code. |
| **E — Evidence** | **Daily Scrum + sprint records** | Ensure agent actions are logged and visible in the same places human work is tracked (board, PR history). An undocumented agent contribution is an invisible risk. |
| **R — Runtime Control** | **Backlog refinement / WIP limits / "stop-the-line"** | Define escalation thresholds and the team's kill-switch protocol — who can halt an agent mid-run, under what trigger. The IM owns the team's circuit breaker. |
| **D — Decisions** | **Retrospective** | Make agent decision-rationale a retro input: when an agent chose a path, was the reasoning inspectable? Retros are where "we couldn't explain why the agent did X" surfaces and gets fixed. |
| **I — Identity** | **Team working agreements / RACI** | Assign every agent a named human owner on the team. The IM maintains the "who owns which agent" registry the same way they maintain team capacity. |
| **C — Cost & Compliance** | **Sprint review / capacity & cost reporting** | Track agent spend and compliance alongside velocity. The IM surfaces the hidden cost line (cf. the $447 overnight-cricket-book anecdote) that pure velocity metrics miss. |
| **T — Transparency** | **Stakeholder reporting / sprint review** | Make agent activity legible to stakeholders — a dashboard line, not a black box. The IM is the translation layer between agent activity and stakeholder trust. |

This mapping reinforces the deck's core thesis (the IM owns *governance and workflow design*, not execution) and complements the HITL-pattern-selector argument from v2 Finding 2.

## Deliverable 2 — primary source URLs / provenance

- **Primary source (vault, original):** Maven live session "7 Steps to Govern AI Agents," Srivastav & Saxena, May 24 2026 — captured at `/mnt/c/Users/adnan/Google Drive/aa2brain/raw/courses/7-steps-govern-ai-agents-maven-2026-05-24.md` and `entities/verdict-framework.md`. The session deck was built in Gamma (`gamma.app/docs/Govern-6op3p4abw2buo0d`, referenced in the recording) and emailed to attendees; I could not independently retrieve a public canonical URL for VERDICT.
- **Authors (for attribution):** Niharika Srivastav (niharikas@gmail.com), Sanjay Saxena (CyberEdx, sanjay@cyberedx.com).
- **No public, independent, third-party source for VERDICT was found.** This is itself the headline credibility finding.

## Credibility red flags — Deliverable 2 (READ THIS)

- 🚩 **Single-source.** Every datum about VERDICT traces to one Maven course in Adnan's vault. No independent adoption, no peer review, no published book yet. (High confidence.)
- 🚩 **Marketing-coupled.** The framework is the hook for a paid cohort + AIGP exam-prep funnel. That doesn't make it wrong, but it means it's a sales artifact, not a neutral standard. (High confidence.)
- 🚩 **Source concentration across two slides.** Slides 20 *and* 22 both rest on this one source (VERDICT + its maturity ladder are the same authors). If the audience challenges VERDICT, two slides wobble together. (High confidence.)
- 🚩 **The agile-cadence mapping is Pax synthesis, not VERDICT's own claim.** The authors never mapped pillars to Sprint Planning / Retro / etc. Present the mapping as the deck's contribution, not theirs. (High confidence.)
- ✅ **Mitigations available:** (1) attribute honestly as a practitioner model; (2) borrow credibility from the *independently-documented incidents* (Knight Capital, Replit, Meta) the pillars explain; (3) frame the seven pillars as a useful *checklist scaffold* an IM can act on, not as validated research. With these, VERDICT is safe to keep — Adnan has committed to it and it is internally sound — but it must not be over-claimed.

---

## Methodology

**Vault first (per standing instruction).** Full-text ripgrep across `/mnt/c/Users/adnan/Google Drive/aa2brain` for both topics.
- *VERDICT:* rich hit — 17 files including the original course transcript, entity notes for the framework and both authors, the maturity-ladder and implementation-phase concept notes, and a synthesis query. Deliverable 2 is sourced almost entirely from the vault (the authoritative primary source for VERDICT *is* in the vault).
- *Maturity model:* searched for the exact rung terms and SAE-style autonomy taxonomies. **No match** for Adnan's five-rung ladder; confirmed it is not in his notes. Deliverable 1 is therefore sourced externally.

**External search.** 4 web searches (orientation) + 5 WebFetch deep-reads of the highest-value sources: the UW arXiv autonomy paper, Adaline Labs five-levels, Cloud Security Alliance autonomy levels, Sean Falconer practitioner guide, and Microsoft Learn maturity model. Salesforce's pages returned 403 to WebFetch; its 4-level structure was captured via search snippet instead.

**Triangulation.** The autonomy-spectrum concept is verified across four independent sources (UW paper, CSA, Falconer, Adaline) plus two vendor models (Microsoft, Salesforce) — High confidence on the concept, High confidence that Adnan's specific labeling is a synthesis. VERDICT is single-source by nature; I triangulated its *credibility* (vault provenance + deck's own v1 assessment + absence of any external footprint) rather than its content, which only one source provides.

## Limitations

- **Deliverable 1:** I could not find a single authoritative source that publishes Adnan's exact five-rung ladder; the recommendation is to present it as a sourced synthesis. The UW paper is a working paper (academic-track, Knight Institute forthcoming) — strong, but not yet a final peer-reviewed publication. Gartner's and Salesforce's full models sit behind partial paywalls; their level *names* are captured but not every sub-detail.
- **Deliverable 2:** VERDICT cannot be independently validated — by design, it is one practitioner team's coinage. I could not retrieve a public canonical URL; the authoritative source is the vault course capture. The agile-cadence mapping is my synthesis and should be labeled as such. The "40% of agentic AI projects canceled by 2027" Gartner stat that VERDICT leans on is already independently verified in the deck's v1/v2 briefs.
- **Both:** This was a confirm-and-source pass, not an exhaustive landscape sweep. Other maturity/governance frameworks exist (e.g. NIST AI RMF, EU AI Act risk tiers, IMDA Singapore) that could substitute for or complement VERDICT if Adnan ever wants a higher-credibility governance anchor — noted as a future option, out of scope here.

## Recommendations / next steps

1. **Slide 3:** adopt the human-role rung table above; cite the UW paper; label it a synthesis. (Pax confidence: High this is the strongest available grounding.)
2. **Slide 20:** use the seven-pillar → IM-cadence mapping; attribute VERDICT honestly as a practitioner model; borrow credibility from the documented incidents.
3. **Decision for Adnan / Larry:** accept that Slides 20 and 22 both rest on one un-validated source. If that concentration is uncomfortable, consider anchoring Slide 22's *governance maturity* ladder on a higher-credibility source (NIST AI RMF tiers or the CSA autonomy levels) and keeping VERDICT to Slide 20 only. Flagged, not decided — Adnan owns this call.
4. **Bookmark:** UW Levels-of-Autonomy paper and CSA autonomy-levels post are the two most durable, citable references that emerged; worth adding to the vault for future agentic decks.
