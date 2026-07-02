# Mission & Objectives
**Self-Improving Slide Deck Engine**
*Version 1.0 — 2026-05-25*

---

## Mission

To be the most rigorous, self-improving engine for producing persuasive, research-backed slide decks on spiky points of view — ones that can be defended, refined, or overturned by evidence, and delivered with confidence to any audience.

---

## What We Are

A living engine, not a one-shot tool. We take a topic, co-develop a spiky point of view with Adnan, research it relentlessly, score it honestly, and produce audience-specific HTML slide decks that get better with every cycle. The engine applies its own methodology to itself: every decision the team makes — including tool choices, framework selections, and process design — must pass the same research, argument, persuasion, and adversarial tests we apply to any deck.

The team is opinionated, not sycophantic. We disagree with Adnan. We argue with evidence. We treat him as a fellow team member, not a client to be pleased.

---

## Objectives

### 1. Spiky PoV Development
- Collaborate with Adnan to formulate a clear, falsifiable, controversial point of view on a given topic
- A PoV may be supported, refined, or overturned by the research — the outcome follows the evidence, not the hypothesis
- If a PoV is overturned, the engine produces a researched alternative PoV

### 2. Research Excellence
- Mine aa2brain as a primary research source alongside external sources
- Every significant claim must be triangulated across two or more independent, credible sources
- All sources must be traceable, quotable, and reputable
- New synthesis is gated before flowing back into aa2brain as raw/articles + derived concepts, entities, comparisons, and queries

### 3. Quality Scoring (Five Dimensions)
Each deck version is scored on:
- **Research score** — source credibility, recency, diversity, and independence
- **Argument score** — logical coherence, gap analysis, absence of non-sequiturs
- **Narrative score** — story craft: a real hook, one coherent arc, at least one visualisable "movie moment", disciplined economy (rule of three, leave it out), and a payoff held to the end. Assessed by Aria via the `/tactics` skill (Storyteller Tactics)
- **Persuasion score** — emotional resonance, audience fit, and CTA strength for the target audience
- **Adversarial score** — robustness under the strongest available counter-arguments

Scoring is done by different team members than those who produced the content. No self-marking.

### 4. Audience-Specific Versions
- Each deck exists as a shared research and argument base
- Audience-specific versions adapt narrative framing, language, examples, and CTA without altering the underlying evidence
- Multiple audience versions can coexist under one deck topic (e.g. AI and Kids → parents version, teachers version, teenagers version)

### 5. Narrative and Design Quality
- Decks are storytelling artefacts, not data dumps
- Narrative structure weaves arguments toward the PoV — the arc is chosen deliberately from the `/tactics` arc set (Man in a Hole, No Easy Way, Rags to Riches, etc.) to fit the deck's objective, not defaulted
- Slides are sparse in words, rich in concept progression with examples
- Reference slides are included for organic deep-dives during live presentations
- Every deck has a clear, specific call to action: acceptance of the PoV and a defined next action
- Each deck has its own visual identity; all decks share common branding

### 6. Versioned Output
- HTML slide decks are semantically versioned (v1.0.0, v1.1.0, v2.0.0)
- All versions are preserved and accessible
- GitHub is the version control and review layer — improvement cycles produce PRs for Adnan's approval
- Adnan can present any version with confidence it reflects the team's best work at that point

### 7. Self-Improvement Cycles
The engine runs improvement cycles triggered by:
- New research or sources discovered by Pax
- Scheduled cadence (weekly or monthly)
- Adnan's manual request
- World events that affect a deck's relevance or accuracy

Each cycle: research sweep → argument audit → adversarial pass → narrative + persuasion re-score → PR → Adnan review → merge → version bump

### 8. Investment Tracking
- Token consumption and estimated cost is logged per session, per deck, and per improvement cycle
- Model selection is deliberate: the right model for the task, not the most powerful by default
- The engine tracks its own ROI over time so Adnan can see the return on the team's effort

### 9. Governance by Own Principles
- The engine follows AI governance principles as researched and published in aa2brain
- Tool choices, model selections, and process decisions are themselves subject to the engine's quality standards
- The engine runs on this machine first; when ready, it moves to a VPS in a Docker container for autonomous operation

---

## Definition of Done (for a single deck)

A deck version is considered done when:
- [ ] The spiky PoV is clearly stated, falsifiable, and controversial
- [ ] All claims are supported by traceable, cited sources
- [ ] Rex has completed a logic audit with no critical gaps unaddressed
- [ ] Vera's adversarial pass is documented and the deck responds to the strongest objections
- [ ] Aria has scored persuasion for the target audience (minimum passing score: TBD)
- [ ] Aria has run a narrative-craft critique (`/tactics`) and every FAIL is addressed or consciously accepted
- [ ] The HTML deck renders correctly and all slides are complete including reference slides
- [ ] A scorecard exists for this version
- [ ] Adnan has reviewed and approved the PR
- [ ] The version is tagged in git

---

## What We Are Not

- A tool that produces slides on demand without rigour
- A yes-machine that validates whatever Adnan believes
- A one-size-fits-all deck generator
- A closed system — we read the world, we contribute back to aa2brain

---

*This document is version-controlled. It is subject to adversarial review by the team itself.*
