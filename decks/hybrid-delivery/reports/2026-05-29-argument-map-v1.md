# Argument Map: Hybrid Delivery Deck
**Version:** v1
**Date:** 2026-05-29
**Auditor:** Rex, Logic Auditor
**Research brief audited against:** `decks/hybrid-delivery/research/2026-05-29-research-brief-v1.md`

---

## Argument Score: 5 / 10

Rationale: The argument is built on genuinely strong empirical anchors for two of its five load-bearing claims, but contains one fatal logical gap (the performance hierarchy claim uses a universal quantifier the deck's own counter-evidence directly refutes), one fatal non-sequitur (the role dissolution threat is asserted without bridging evidence connecting general knowledge-worker data to the IM/DM population specifically), and two significant gaps where the argument relies entirely on medium-confidence practitioner opinion rather than evidence. The arc's internal progression is coherent in direction but earns its later sections on rhetorical momentum rather than logical necessity.

---

## 1. Core Claim

**As stated in the PoV:**
"Human+AI hybrid teams consistently outperform both AI-only and human-only teams for the generative, iterative knowledge work that delivery teams do — but the advantage is structural, not automatic; iteration managers who learn to architect the collaboration, govern agentic workflows, and own the risk at the human-AI boundary will define what delivery leadership looks like for the next five years, while those who don't will find the role dissolved around them."

**Reformulated as a single falsifiable assertion:**
Structured human+AI collaboration produces measurably superior outcomes for the generative knowledge work of delivery teams, and the IM/DM who develops three specific capabilities — workflow architecture, agentic governance, and human-AI risk ownership — will secure a durable career position while those who do not will have the role absorbed or eliminated.

This is a compound claim with two logically independent halves. The first half is partially supported. The second half is the deck's actual thesis and is the weaker of the two.

---

## 2. Reconstructed Argument Chain

```
P1. AI adoption is now pervasive and irreversible — the workforce question is
    how to collaborate, not whether AI will be present.
        |
        v
P2. Human+AI hybrid teams outperform both solo conditions for the specific
    task type delivery teams do (generative, iterative knowledge work),
    but only when the collaboration is structured correctly.
        |
        v
P3. "Structured correctly" requires specific design decisions — workflow
    composition, semi-synchronous coordination, shared agents — that are
    currently human-owned and non-trivial.
        |
        v
P4. The IM/DM role is the natural locus for this structuring work, because
    the same skills that govern delivery (risk, coordination, ways of working)
    map directly onto the skills that govern hybrid team architecture.
        |
        v
P5. AI governance (token costs, agentic workflows, risk at the human-AI
    boundary) adds a new, durable, hard-to-replicate skill surface that
    further anchors the IM/DM role.
        |
        v
C.  IMs/DMs who acquire the three capabilities will define the next
    generation of delivery leadership; those who do not risk role dissolution.
```

This is a valid logical chain in skeleton form. Each premise earns the next in principle. The gaps are evidentiary, not structural — the chain is sound but several links are unsupported or misdirected.

---

## 3. Toulmin Decomposition of the Five Load-Bearing Claims

### Claim 1: Human+AI outperforms both solo conditions for delivery-type work

| Toulmin element | Content |
|---|---|
| Claim | Human+AI hybrid teams consistently outperform AI-only and human-only for the generative knowledge work delivery teams do |
| Data | BCG RCT (758 consultants, Organization Science 2026): 12.2% more tasks, 25.1% faster, 40% quality uplift. P&G RCT (776 professionals, NBER 2025): teams with AI 3x more likely to produce top-10% solutions. |
| Warrant | Consulting and product development work is structurally similar to delivery management work — therefore findings generalize |
| Backing | Both studies involved complex, iterative, knowledge-creation tasks with professional populations |
| Qualifier | Only for tasks inside the AI capability frontier; on tasks outside the frontier, AI users were 19% *less* likely to produce correct solutions (BCG finding) |
| Rebuttal | Malone et al. meta-analysis (Nature Human Behaviour 2024, 106 studies): on average human+AI combinations do NOT outperform the best solo performer; decision tasks especially show degradation |

**Gap assessment:**
The warrant (consulting work = delivery management work) is unstated and unearned. The inference requires an explicit bridge argument that does not currently exist. The word "consistently" is a universal quantifier that the evidence cannot support — Malone shows the average is negative; the deck's evidence shows specific conditions under which the result is positive.

**Severity: FATAL** — "consistently outperform" must be replaced with a conditional framing.

---

### Claim 2: The performance advantage is structural, not automatic

| Toulmin element | Content |
|---|---|
| Claim | The hybrid performance advantage depends on specific structural design choices, not on simply adding AI to a team |
| Data | McKinsey MGI: <40% of businesses report measurable profit gains because they bolt AI onto legacy workflows. Dell'Acqua: tasks outside the frontier show 19% *worse* performance with AI. Webframp: five workflow collision points between team and agent lifecycles. |
| Warrant | If AI integration without redesign produces failure, then redesign is the differentiating variable |
| Backing | Multiple independent sources (McKinsey primary research, BCG peer-reviewed study, practitioner analysis) converge on the same failure mode |
| Qualifier | The specific design choices that produce the advantage are described at medium-confidence practitioner level, not validated by RCTs |

**Gap assessment:**
This is the strongest claim in the deck. McKinsey + BCG frontier-failure finding + practitioner pattern converge from high-confidence independent sources. The gap is in the transition to Arc 3: the specific structural prescriptions don't inherit the evidentiary weight.

**Severity: SIGNIFICANT** — bridge from "structure matters" to specific prescriptions needs explicit acknowledgment of confidence grade shift.

---

### Claim 3: The IM/DM is the natural locus of hybrid team architecture

| Toulmin element | Content |
|---|---|
| Claim | The IM/DM role is the right human to own workflow architecture, governance, and risk at the human-AI boundary |
| Data | McKinsey MGI: manager role shifts from supervising people to orchestrating people, agents, and robots. Microsoft New Future of Work: human expertise matters more — humans shift to guiding, critiquing, improving AI work. |
| Warrant | The skills required for hybrid team architecture (coordination, risk, ways of working) are the same skills the IM/DM already owns |
| Backing | Multiple practitioner sources describe the evolved SM/IM role in terms that map to current IM/DM accountabilities |
| Qualifier | No controlled study has directly measured IM/DM outcomes before and after AI integration |
| Rebuttal | The role fragments across tech lead + PM + new AI specialist (acknowledged counter-claim, not addressed in arc) |

**Gap assessment:**
The warrant (IM/DM skill set maps onto hybrid architecture skills) is asserted, not demonstrated. The alternative path — role fragmentation — is acknowledged in the research brief but not addressed in the arc. This is a false dilemma risk.

**Severity: SIGNIFICANT** — the bridge from general manager role evolution to IM/DM specifically is inferential; the dissolution counter-claim requires explicit handling.

---

### Claim 4: AI governance is a durable career moat for the IM/DM

| Toulmin element | Content |
|---|---|
| Claim | Governing agentic workflows is a new, durable, hard-to-replicate skill surface that anchors the IM/DM's career position for five years |
| Data | Singapore IMDA framework (High). Anthropic agent safety framework (High). Token cost analysis: $110K+/month exposure for 20-person team running agents inefficiently (Medium-High). AIGP salary data ($141K–$170K median). |
| Warrant | Intersection of "understands agents" and "understands risk/compliance" is thin → scarcity → value |
| Backing | VERDICT framework (Medium). AI governance maturity data showing most enterprises at Level 1–2. |
| Qualifier | Counter-claim 2: as autonomous AI governance (Level 4) matures, the human governance layer shrinks — the moat has a timer |
| Rebuttal | "Five years" has no empirical basis |

**Gap assessment:**
Regulatory grounding (IMDA, Anthropic) is high confidence. Token cost exposure is directionally credible. The "durable" claim overstates — the moat has a timer that must be explicitly acknowledged.

**Severity: SIGNIFICANT** — acknowledge the timer explicitly rather than asserting durability.

---

### Claim 5: Those who don't evolve will find the role dissolved

| Toulmin element | Content |
|---|---|
| Claim | IM/DMs who do not develop the three capabilities will have their role dissolved |
| Data | Itamar Gilad: pure delivery PO is most vulnerable archetype (Medium). Digital.ai: 42% of orgs use hybrid approaches (role fragmentation underway). "Gradual hollowing" concept (Medium — YouTube-sourced). |
| Warrant | If AI absorbs low-leverage facilitation work and IM/DM doesn't move to higher-leverage work, organizational value justification fails |
| Backing | Practitioner convergence (theagileforum, scrum.org, rethinkyourunderstanding) |
| Qualifier | No longitudinal study tracks actual IM/DM headcount trends before and after AI adoption |
| Rebuttal | All cited evidence covers knowledge workers generally — none is IM/DM-specific |

**Gap assessment:**
The dissolution claim is the deck's primary motivating claim and rests on zero IM/DM-specific empirical evidence. Brynjolfsson's 14% gain in customer support and McKinsey's general manager evolution do not earn a conclusion about IM/DM roles specifically. The CAD/draftsmen analogy is evocative but is an analogy, not evidence.

**Severity: FATAL** — most important single finding. The dissolution claim is the primary call to action for the target audience and is entirely unsupported by IM/DM-specific evidence.

---

## 4. Logical Gaps Register

| # | Gap | Type | Severity |
|---|---|---|---|
| G1 | "Consistently outperform" uses a universal quantifier directly refuted by Malone et al. Must be conditional: for generative knowledge work, under structured conditions. | Overstatement / unsupported universal | FATAL |
| G2 | Role dissolution claim has no IM/DM-specific empirical evidence — all cited evidence covers knowledge workers generally or unrelated domains. | Missing evidence for load-bearing claim | FATAL |
| G3 | Warrant that consulting/product development work generalizes to delivery management work is unstated and unearned. | Unstated warrant / generalization gap | SIGNIFICANT |
| G4 | IM/DM as "natural locus" for hybrid architecture is asserted, not demonstrated. The role-fragmentation alternative is not addressed. | False dilemma / missing rebuttal | SIGNIFICANT |
| G5 | Arc 3's structural prescriptions rest entirely on medium-confidence practitioner sources. Evidence grade mismatch with Arc 2. | Evidence grade mismatch | SIGNIFICANT |
| G6 | "Durable career moat" overstates the governance claim. Five-year framing is right but the timer must be confronted explicitly. | Overstatement / missing qualifier | SIGNIFICANT |
| G7 | Arc 6 (actionable closing) is a resource catalogue, not an argument. No warrant connecting "governance is the risk surface" to "here are the certifications." | Non-sequitur (minor) | MINOR |
| G8 | "Five years" framing has no empirical basis. Functions as rhetorical anchoring. | Unsupported quantifier | MINOR |
| G9 | Vigilance decay connection to IM/DM governance role is asserted rather than demonstrated. | Underdeveloped warrant | MINOR |

---

## 5. Non-Sequiturs

**Arc 6 (actionable closing):** The deck establishes why governance and hybrid architecture matter; it does not establish why these specific certifications are the correct response to the identified skill gap. Needs a brief warrant: "these credentials directly address the three capabilities identified in Arc 5."

Minor non-sequitur — audience will accept practical utility even without the explicit bridge, but the gap is real.

---

## 6. Strength Assessment

**Strongest:**
1. Claim 2 (structural not automatic) — McKinsey + BCG frontier-failure + practitioner pattern from independent high-confidence sources. The intellectual center of the argument.
2. Arc 5 governance evidence — strong regulatory grounding (IMDA, Anthropic), plausible economic stakes. Most novel part of the deck.
3. The PoV's conditional framing ("structural not automatic," "those who don't will find the role dissolved") is logically superior to unconditional versions.

**Most vulnerable:**
1. The dissolution claim — zero IM/DM-specific evidence; audience most entitled to push back.
2. "Consistently outperform" — will not survive encounter with Malone et al.
3. "Natural locus" for IM/DM — assertion without explicit warrant; the skill-overlap argument needs to be made, not implied.

---

## 7. Assessment of the Malone et al. Complication

The PoV's scoping to "generative, iterative knowledge work" is the correct logical move. The reconciliation is sound: Malone covers mostly decision/classification tasks (90%); BCG/P&G cover creation-adjacent work and are post-GPT-4. However, "consistently outperform" is directly contradicted even within the scoped task type. Fix: remove "consistently" and replace with "for generative, iterative knowledge work under structured conditions, human+AI combinations produce meaningfully better outcomes than either solo condition."

The deck would be stronger for surfacing and resolving the Malone counter-evidence explicitly in Arc 2 — for an analytically oriented IM/DM audience, this is a credibility move.

---

## 8. Arc Coherence Assessment

- Arc 1 → Arc 2: Clean. Establishing AI adoption is irreversible earns "how do you structure the collaboration?"
- Arc 2 → Arc 3: Works directionally; evidence grade mismatch (G5) will be noticed by analytical audience.
- Arc 3 → Arc 4: Weakest transition. "Delivery requires these design skills" → "IM/DM owns those skills" — asserted by proximity, not argued.
- Arc 4 → Arc 5: Clean. If IM/DM owns the workflow, they own the governance surface.
- Arc 5 → Arc 6: Non-sequitur (G7). Needs explicit bridge.

Overall: coherent in direction, narratively driven rather than logically necessary from Arc 3 forward.

---

## Summary

**Argument score: 5 / 10**
**Gap count: 2 Fatal / 4 Significant / 3 Minor**

**Most important single finding:** The dissolution claim — the deck's primary motivating claim — rests on zero IM/DM-specific empirical evidence. A knowledgeable IM/DM will correctly challenge whether general knowledge-worker productivity findings justify role-specific dissolution claims, and the deck currently has no answer.

**Second most important finding:** "Consistently outperform" is a universal quantifier that Malone et al. directly refutes. One wording change fixes this.
