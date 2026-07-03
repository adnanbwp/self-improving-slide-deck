# Research Brief: External Corroboration — "Both Axes" Agentic Engineering Base Deck
**Version:** v1
**Date:** 2026-07-03
**Prepared by:** Pax, Senior Research Specialist
**For:** Agentic Engineering base deck — Larry / Adnan Ali
**Scope:** Light *external* corroboration pass. Internal primary sources (Google 5-whitepaper "Vibe Coding" series + aa2brain VERDICT/ladder wiki) are already grounded and cited. This brief tests whether the deck's single-source governance spine holds up against established external frameworks, verifies the two hard statistics, and checks 2026 currency. It does **not** re-derive the internal material.

---

## Executive Summary

The deck's two-axis thesis survives external scrutiny well, and its most-at-risk element — the single-source VERDICT framework — is *substantively* corroborated by four independent, authoritative bodies (NIST, OWASP, Google SAIF, EU AI Act) even though the *named* "VERDICT" model remains one-source. The strongest finding: **Google's own SAIF 2.0 agent principles (human controllers · limited powers · observable actions) map almost one-to-one onto VERDICT's Identity · Validation · Evidence/Transparency pillars** — three of VERDICT's seven pillars were already public in Google's earlier SAIF (SAIF 2025 predates the 2026 VERDICT session). The Knight Capital statistic ($440M / 45 min) is verified and citable to the SEC. The "silent time-bomb / shadow agent" claim is strongly corroborated by IBM's 2025 breach data and multiple 2025–2026 shadow-AI surveys. Two things force a caveat: (1) VERDICT is a single-agent operating model and **under-weights multi-agent / inter-agent risk**, which OWASP-2026 and the EU AI Act now treat as first-class; (2) the deck's Day-4 "Google 7-pillar security ≈ VERDICT 7 pillars" symmetry is an *internal construction*, not an externally validated identity — SAIF has 6 domains + 3 agent principles, not 7 — so it must be presented as "our mapping," not "Google says." **Overall confidence in the two-axis claim after external checking: High** (the orthogonality of build-verification vs runtime-governance is independently reflected in every framework reviewed).

---

## Target 1 — Corroborate or challenge VERDICT

**Claim under test:** VERDICT's runtime-governance thesis — "traditional pre-deployment governance can't see agents; you need runtime validation, kill-switch, identity, logging, spend caps, transparency" — and its 7 pillars.

**Finding 1a — The core thesis (traditional governance wasn't built for agents; runtime is the missing axis) is independently confirmed.**
Multiple 2024–2026 sources note that the incumbent governance frameworks — **NIST AI RMF, ISO/IEC 42001, and the EU AI Act — contain no references to "agent," "agentic," or autonomous AI systems**, and that agents "act on external systems, access tools dynamically, execute multi-step plans where errors cascade, maintain persistent memory, and delegate across agent boundaries in ways that fragment accountability." This is exactly the gap VERDICT names. The Cloud Security Alliance is now drafting an **Agentic Profile for the NIST AI RMF** adding *runtime behavioral governance, tool-use risk, and delegation-chain accountability* — the same runtime pillars VERDICT asserts.
- NIST AI RMF Generative AI Profile (NIST-AI-600-1), 2024-07-26 — https://www.nist.gov/itl/ai-risk-management-framework ; https://airc.nist.gov/
- CSA, "NIST AI RMF: Agentic Profile v1" (2025–2026) — https://labs.cloudsecurityalliance.org/agentic/agentic-nist-ai-rmf-profile-v1/

**Finding 1b — Google SAIF 2.0 (2025) already contained a subset of what VERDICT (2026) later named.** SAIF 2.0's *three core principles for agents* are: (1) agents must have **well-defined human controllers**, (2) their **powers must be carefully limited**, (3) their **actions and planning must be observable**. Its three agent controls are **Agent Permissions** (least privilege as a hard ceiling), **Agent User Control** (human approval for any state-changing action), **Agent Observability** (log actions, tool calls, and reasoning). This is a near one-to-one match to VERDICT's **Identity (I)**, **Validation (V)**, and **Evidence/Transparency (E/T)** — arrived at by a different author for a different purpose.
- Google SAIF "Focus on Agents" — https://saif.google/focus-on-agents ; Google security blog — https://blog.google/technology/safety-security/ai-security-frontier-strategy-tools/ (2025)

**Finding 1c — OWASP gives VERDICT its control-level vocabulary.** OWASP Top 10 for LLM Apps (2025) already lists **LLM06 Excessive Agency** (over-permissioned agents). OWASP's **Top 10 for Agentic Applications (2026)**, peer-reviewed by 100+ experts, centres on *goal misalignment, tool misuse, delegated trust, inter-agent communication, persistent memory, and emergent autonomous behavior*; the OWASP Agentic Security Initiative guide (Feb 2025) uses a taxonomy of Agent Design · Memory · Planning & Autonomy · Tool Use · Deployment & Operations. Practitioner guidance explicitly recommends "use OWASP as the control-level vocabulary **inside** higher-order frameworks like NIST AI RMF and ISO/IEC 42001" — precisely VERDICT's positioning as an *operating model*, not a checklist.
- OWASP Top 10 for Agentic Applications 2026 — https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- OWASP Top 10 for LLM Apps 2025 — https://genai.owasp.org/llm-top-10/

**Finding 1d — EU AI Act encodes the runtime pillars into law (from Aug 2, 2026).** Article 14 requires a human overseer able to **override, disregard, and halt** the system (= VERDICT **R**, Runtime Control / kill-switch). Article 12 requires **logging integrated into core design** and ≥6-month retention (= VERDICT **E**, immutable evidence). Article 26 assigns deployer accountability, and Recitals 99–100 extend the compliance boundary across **multi-agent chains** (= VERDICT **I**, Identity/ownership).
- EU AI Act Art. 14 — https://artificialintelligenceact.eu/article/14/ ; Art. 26 — https://artificialintelligenceact.eu/article/26/ ; official framework — https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai

**Finding 1e — MITRE ATLAS + CoSAI cover the adversarial/threat-modeling flank.** MITRE ATLAS (16 tactics / 84 techniques; Spring 2025 added 19 GenAI techniques incl. RAG poisoning, impersonation, AI supply-chain compromise, targeting "orchestration and execution layers") and the OASIS **Coalition for Secure AI (CoSAI) Risk Map** provide the attack-technique layer that feeds VERDICT's Validation/Evidence pillars. These are *complements*, not competitors — they model threats; VERDICT governs the response.
- MITRE ATLAS — https://atlas.mitre.org/ ; CoSAI Risk Map — https://github.com/cosai-oasis/secure-ai-tooling

**Where external sources ADD to / pressure VERDICT:**
- **Multi-agent / inter-agent risk** is a first-class concern for OWASP-2026 and EU AI Act (Recitals 99–100) but is only lightly implied in VERDICT's 7 (single-agent-centric) pillars. **This is a genuine gap.**
- **Data/model-supply-chain integrity** (OWASP LLM03/04; NIST data poisoning; ATLAS supply-chain compromise) sits outside VERDICT's oversight-centric pillars. VERDICT governs the *agent*, not the *model/data pipeline*.

**Confidence + caveats:** *Substance of VERDICT — High* (four independent authoritative bodies converge on its pillars). *VERDICT as a named/standard framework — Low-Medium* (still one source: Srivastav & Saxena, one Maven session, 2026-05-24). The honest frame is: **VERDICT is a useful synthesis/mnemonic of an industry consensus that is forming in public — not itself the standard.**

**What this means for the deck:** VERDICT can carry the governance axis with confidence *if framed as a synthesis*. Slide 14 (7 pillars) should footnote the external convergence (NIST Agentic Profile, SAIF 2.0, OWASP Agentic, EU AI Act) — this converts the deck's biggest liability (single source) into a strength (VERDICT = the mnemonic for what four bodies are independently saying). Add one line acknowledging multi-agent risk as the frontier VERDICT's pillars under-cover.

---

## Target 2 — Verify the Knight Capital statistic ("≈$440M in ≈45 minutes")

**Verified. Citable.** On **August 1, 2012**, a deployment error at Knight Capital Group (only 7 of 8 servers received the new code; a dormant 2003 "Power Peg" routine reactivated on the 8th) sent **~4 million unintended orders / 397 million shares across ~154 securities in ~45 minutes**, producing a **~$440M pre-tax loss** and **$7B in transient positions**; the stock fell ~75% in two days and the firm was effectively taken over. The **SEC's own enforcement action** (its *first-ever* under the Market Access Rule 15c3-5) confirms the incident and its cause: "did not have adequate safeguards … failed to prevent the entry of millions of erroneous orders."
- **Primary (regulator):** SEC Press Release 2013-222, "SEC Charges Knight Capital With Violations of Market Access Rule," 2013-10-16 — https://www.sec.gov/newsroom/press-releases/2013-222 (settled for a $12M penalty).
- **Secondary corroboration:** CIO, "Software Testing Lessons Learned From Knight Capital" — https://www.cio.com/article/286790/software-testing-lessons-learned-from-knight-capital-fiasco.html ; Henrico Dolfing case study — https://www.henricodolfing.ch/en/case-study-4-the-440-million-software-error-at-knight-capital/

**Confidence + caveats:** *High.* Triangulated across the SEC action and 6+ independent write-ups. Minor precision note: the SEC penalty was $12M; the **$440M is the firm's trading loss**, widely and consistently reported (a few sources round to ~$460M pre-tax). The deck's "$440M in 45 minutes" is accurate and defensible.

**What this means for the deck:** Use it as-is on slides 4 and 17. Cite the SEC release (not a blog) for authority. Keep the framing the wiki already uses — Knight Capital *predates* AI agents but is *structurally identical* to a broad-permission agent with no kill-switch (the R and C pillars). One sober caveat for a sophisticated audience: it was an *automated trading* failure, not an *AI/agentic* one — present it as an analogy for the failure mode (speed × no runtime control), not as an AI incident.

---

## Target 3 — The "silent time-bomb / shadow agent" claim (agentic × Unseen)

**Strongly corroborated.** The claim — a tested agent nobody knows is running, and "most orgs are L1 Unseen without realising" — is backed by 2025–2026 primary and survey data:

**Finding 3a — IBM Cost of a Data Breach 2025 (the strongest source).** Breaches involving **shadow AI cost ~$670K more** than standard breaches (~$4.63M avg); **13%** of orgs reported breaches of AI models/apps and **97% of those lacked AI access controls**; **63%** of breached orgs had **no AI governance policy**; shadow-AI breaches took longer to detect (247 vs 241 days) and disproportionately exposed customer PII.
- IBM/Ponemon, "Cost of a Data Breach 2025," 2025-07-30 — https://www.ibm.com/reports/data-breach ; https://newsroom.ibm.com/2025-07-30-ibm-report-13-of-organizations-reported-breaches-of-ai-models-or-applications,-97-of-which-reported-lacking-proper-ai-access-controls

**Finding 3b — Inventory / oversight gap is real and measured.** ~**43% of organizations cannot produce an AI inventory** (a baseline requirement under EU AI Act / NIST AI RMF / ISO 42001); a 2026 Gravitee survey found only **24.4% have full visibility into which AI agents talk to each other**; **~79% lack formal security policies for autonomous tools**. Gartner projects **30% of new enterprise AI apps will use agent architectures by 2026**, and MCP adoption reportedly grew 400%+ in 2025 — mostly outside formal security review.
- CSA, "The Shadow AI Agent Problem in Enterprise Environments," 2026-04-28 — https://cloudsecurityalliance.org/blog/2026/04/28/the-shadow-ai-agent-problem-in-enterprise-environments
- Airia, "Shadow AI Statistics 2026" — https://airia.com/shadow-ai-statistics-key-data-points-every-ciso-needs-in-2026/
- Forbes Councils, "Agentic AI Sprawl" — https://councils.forbes.com/blog/agentic-ai-sprawl-audit-approve-kill-autonomous-workflows-before-they-multiply

**Finding 3c — The internal "5 known → 12 discovered shadow agents" anecdote (Saxena) is now a documented pattern**, not a one-off — the shadow-AI literature treats undiscovered agent sprawl as the default enterprise state.

**Confidence + caveats:** *Phenomenon — High* (IBM primary + convergent surveys). *Specific secondary percentages (43%, 24.4%, 79%) — Medium* — several come from vendor/aggregator blogs (Airia, itecsonline, Gravitee) rather than the primary survey PDFs; cite the *direction*, and prefer IBM for any hard number on a slide.

**What this means for the deck:** This is the deck's most externally-defensible emotional beat. Slide 4/17 "silent time-bomb" can now carry a real 2025–2026 datapoint (IBM's +$670K, or "43% can't inventory their AI"). It strongly validates the ladder claim "most orgs are L1 without realising." Prefer IBM's figures for on-slide stats; treat the vendor percentages as supporting texture.

---

## Target 4 — 2026 currency: "vibe coding → agentic engineering" for production

**Corroborated, and the deck is on-trend — with one framing nuance.** The vibe → structured → agentic spine is mainstream in mid-2026:

- **Karpathy himself** coined "vibe coding" (Feb 2025) and by 2026 says that era is *ending* — "entering the age of agentic engineering: orchestrating agents against detailed specifications with human oversight." The deck's exact arc, from the person who named both poles.
- **Addy Osmani** (a Google "Vibe Coding" whitepaper co-author) — "Vibe coding is not the same as AI-assisted engineering" — https://medium.com/@addyosmani/vibe-coding-is-not-the-same-as-ai-assisted-engineering-3f81088d5b98
- **Wes McKinney (MotherDuck)** — "Vibe Coding Is Dangerous, Agentic Engineering Isn't" — https://motherduck.com/blog/vibe-coding-dangerous-agentic-engineering-wes-mckinney/
- **Towards Data Science / DeepLearning.AI** — "From Vibe Coding to Spec-Driven Development" — the verification-into-artifacts climb is the consensus story — https://towardsdatascience.com/from-vibe-coding-to-spec-driven-development/

**Newer framing the deck should acknowledge (currency):** In mid-2026 the ascendant label for the disciplined pole is increasingly **"spec-driven development" (SDD)** — GitHub Spec Kit, AWS Kiro, DeepLearning.AI's SDD course — arguably more current than "agentic engineering" for the *same* right-hand pole. The deck already lands here on Day 5 (specs declare policy); worth a one-liner naming SDD as the industry term so the deck reads current, not behind.

**Counter-argument to pre-empt:** The spectrum is **task-dependent, not a maturity ladder** — "more agentic" is not universally "better." Multiple sources (and the aa2brain spectrum note's own "East" challenge) stress choosing the right point for the stakes; a weekend prototype should stay vibe-coded. If the deck's readiness map implies "always climb to agentic," sophisticated readers will push back.

**Confidence + caveats:** *High* — the framing is corroborated by the term's originator, a whitepaper co-author, and independent practitioners.

**What this means for the deck:** The spine is safe and current. Add one line naming **spec-driven development** as the 2026 industry term for the right pole (currency signal). On the readiness map, make explicit that the target cell is stakes-dependent — "production-ready for high-stakes/autonomous work," not "everything must be agentic" — to inoculate against the task-dependency counter-argument.

---

## Target 5 — Red-flag check on the hypothesis (§2)

1. **"Google 7-pillar security ≈ VERDICT 7 pillars" (Day 4, slide 10) is an internal construction, not an external fact.** Google's public agent security posture (SAIF 2.0) is **6 domains + 3 agent principles**, not seven pillars. The neat 7≈7 symmetry comes from the Google *course* material, mapped by hand onto VERDICT. **Red flag:** present slide 10 as *"our mapping of Google's security guidance onto VERDICT,"* never as "Google's seven pillars equal VERDICT's seven." The mapping is defensible and useful — but it is synthesis, and the deck's own honesty rule requires labeling it as such. *(Medium confidence this needs a wording change — High that it should not be stated as external identity.)*

2. **VERDICT's single-source status must stay visible.** The deck already flags this on slide 21 — keep it, and upgrade the frame from "single-source, treat with caution" to "single-source *name* for a multi-source *consensus*" (Target 1). *(High.)*

3. **Multi-agent risk is under-covered by VERDICT's pillars** (Target 1). If the deck claims VERDICT is *complete*, that overclaims. Add a caveat: VERDICT is strong on single-agent oversight; inter-agent/delegation risk is the live frontier (OWASP-2026, EU AI Act Recitals 99–100). *(High.)*

4. **"Production-ready = agentic × L3" can over-generalize.** Correct for high-stakes/autonomous work; but a well-governed *structured* (not agentic) workflow can be production-ready for lower-stakes tasks. The map's top-right is the target for the *hard* cases, not a universal mandate. Small wording guard on slides 4/17/19. *(Medium.)*

5. **Knight Capital is pre-AI** (Target 2) — fine as an analogy, mislabeled if called an "AI incident." *(High.)*

**Nothing in §2 is contradicted by external sources.** The two-axis orthogonality (build-verification ⊥ runtime-governance) is *reflected* in every framework reviewed: NIST/SAIF/OWASP all separate "is the output correct/verified" (evals, testing, assurance) from "can we control it while it runs" (permissions, human-in-the-loop, kill-switch, observability). The deck's central claim is the strongest-standing part of the whole argument.

---

## Methodology

**Vault first (aa2brain, `rg`):** searched `VERDICT`, `shadow AI/agent`, `Knight Capital`, `NIST/OWASP/SAIF/MITRE/EU AI Act/ISO 42001`, `vibe coding/agentic engineering/spec-driven`, `runtime governance`, `agent inventory`. Read the internal primaries in full: `entities/knight-capital-incident.md`, `comparisons/traditional-governance-vs-agentic-governance-needs.md`, `concepts/vibe-coding-to-agentic-engineering-spectrum.md`, plus the VERDICT concept notes and the `7-steps-govern-ai-agents-maven-2026-05-24.md` course capture. Confirmed the vault has only *passing* external-framework mentions (one NIST RMF question; one OWASP MCP Top 10 reference) — external corroboration was a genuine gap, now filled.

**External (10 targeted WebSearch passes):** NIST AI RMF GenAI/Agentic Profile; OWASP LLM & Agentic Top 10; Google SAIF 2.0 agents; EU AI Act agentic obligations; MITRE ATLAS / CoSAI; Knight Capital + SEC action; IBM 2025 breach / shadow AI; vibe→agentic 2026 currency + critique. Prioritized primary/authoritative sources (NIST, OWASP, Google, EU official text, SEC, IBM) over aggregator blogs.

**Triangulation:** every load-bearing claim verified across ≥2 independent sources. VERDICT's substance triangulated across four bodies (NIST, OWASP, SAIF, EU AI Act). Knight Capital triangulated to the SEC action + multiple write-ups. Shadow-AI anchored on IBM's primary report with survey corroboration.

## Limitations

- **VERDICT as a named framework remains single-source** — external work corroborates its *content*, not the specific "VERDICT" packaging or the exact 7-pillar cut. Do not present VERDICT as an industry standard.
- **Some shadow-AI percentages (43%, 24.4%, 79%) are vendor/aggregator-sourced**, not read from primary survey PDFs. Direction is solid; treat specific numbers as Medium and prefer IBM for on-slide stats.
- **The Day-4 "7≈7" mapping was not externally validatable** — SAIF is 6 domains + 3 principles. It is a defensible internal synthesis, flagged accordingly.
- **MITRE ATLAS / CoSAI covered lightly** — they are threat-modeling complements, not governance operating models; not central to the deck's argument.
- **Fast-moving space:** EU AI Act high-risk enforcement (Aug 2, 2026) and SAIF/OWASP/NIST agentic profiles are all evolving in 2026; re-check before any dated claim ships.

## Recommendations (for Coda / Iris)

1. **Turn the single-source liability into a strength:** footnote slide 14 (VERDICT pillars) with the four-body convergence (NIST Agentic Profile · SAIF 2.0 · OWASP Agentic 2026 · EU AI Act) — the deck's honesty about VERDICT then *reads as rigor*.
2. **Re-label slide 10** as an explicit *mapping* of Google's security guidance onto VERDICT, not an external equivalence.
3. **Add one currency line** naming *spec-driven development (SDD)* as the 2026 industry term for the agentic/right pole.
4. **Guard the readiness map** so "agentic × L3" reads as the target for high-stakes work, not a universal mandate (pre-empts the task-dependency counter-argument).
5. **Add one frontier caveat:** VERDICT is strong on single-agent oversight; multi-agent/inter-agent risk is the live edge it under-covers.
6. **On-slide hard stats to prefer:** Knight Capital → cite SEC 2013-222; shadow AI → cite IBM 2025 (+$670K, or "43% can't inventory their AI").
