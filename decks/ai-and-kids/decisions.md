# Decisions Log — AI and Kids

Persistent memory for this deck across all improvement cycles. **Vera reads this before every adversarial pass. Pax reads this before every research sweep.** Specialists do not re-litigate a Closed decision without citing new evidence — if new evidence surfaces, flag it to Larry rather than silently opening the decision again.

Each entry is written by the specialist who owns the decision and is included in the PR for the cycle in which the decision was made. The PR is the review layer — Adnan reviews and approves both the content change and the decision log entry together.

### 2026-05-28 — Content polish pass v1.3.0 (Coda)

Status: **Closed**

**Changes applied in v1.3.0 canonical.html:**

1. **Slide 5 — meta-commentary removed**: Support-line "This deck's argument sits in Schools 2 and 3..." was internal framing visible on the slide face. Replaced with audience-facing statement. School 1 list item rewritten from choppy fragments to complete sentences (parent feedback: "choppy sentences, can't understand what you are saying").
2. **Slide 8 — jargon removed from headline**: "the argument targets blanket avoidance, not graduated age-appropriate limits" replaced with "the problem is using them as the complete strategy" (parent feedback: "difficult terms").
3. **Slide 9 — jargon removed from headline**: "population-scale exposure problem" replaced with plain language (parent feedback: "jargon, needs to be simplified").
4. **Slide 12 — research-brief language removed**: Parenthetical "(observational evidence — causal direction consistent, RCT confirmation not yet available)" removed from slide face (parent feedback: "jargon, complex sentence structure").
5. **Slide 18 — CTA strengthened**: All five items replaced with more specific, memorable actions grounded in Allie K. Miller (May 2026) and the research brief. Billboard rule (item 4) and error-finding prompt (item 5) are new. School questions (item 2) are now specific and enumerated.

---

### 2026-05-28 — Research pass: 4As framework + Thread 1 source corrections (Pax)

Status: **Closed**

Appended Supplement 2026-05-28 to `research/2026-05-25-research-brief-v1.md`. Thread 4 documents Stefania Druga's 4As framework (Ask, Adapt, Author, Analyze) — names, definitions, age-specific guidance, and alignment with the three-schools framing from Thread 1. Primary MIT Press URL remains HTTP 403; content triangulated from four independent sources; confidence Medium-High. Thread 1 source corrections: 49% stat re-attributed to UNICRI (not Common Sense Media; n=160, global); 12% emotional support re-attributed to Pew Research February 2026 (confirmed High); 58% chatbot-preference stat corrected — Internet Matters finding is preference over self-directed search, not over asking teachers; thread 1 phrasing should not be used on a slide without primary report verification. New stats added: 92.7% of youth found AI mental health advice helpful (JAMA, double-edged — supports adult-guided warning sign approach); deepfake identification confidence 46%→25% in one year (Microsoft Safer Internet Day 2026). Miller's 9 skills characterised as an empowerment frame, consistent with School 2 and the 4As. Three new open questions added for Rex (questions 9–11).

---

### 2026-05-26 — Stats verification: 49%/96%/11% (Pax)

Status: **Closed**

All three statistics confirmed real. Two had wrong source attributions in the research brief (both labelled "Common Sense Media 2026"):
- **49%** → Common Sense Media, September 2024 (correct)
- **96%** → USC/CARE survey, Spring 2025 via CRPE; scope is elementary-aged families specifically (83–96% spanning all ages) — not Common Sense Media
- **11%** → CDT, October 2025 (was already correct)

Stats are safe to present. Attribution drift originated from Allie K. Miller's newsletter misattributing the 96% figure. Source attributions in the deck have been corrected to match primary sources. This item is resolved and should not be treated as an open blocker in future scoring passes.

---

### 2026-05-26 — Slide 1 title clarity (Adnan)

Status: **Closed** (v1.2.0)

**Feedback:** Slide 1 v1.1.0 does not communicate the PoV clearly enough for a live audience. "Both extremes fail children" signals that two things are wrong but does not tell the audience what they are here to discuss or why it matters to them personally. The spiky PoV must be in their face and clear from the first slide — the audience should immediately know the claim being made and feel its relevance to them.

**Resolution (v1.2.0):** v1.2.0 inserts a proper Title slide at position 1 ("Your Child Is Already Using It." — names the factual premise; PoV line reads "Over-protecting harms them. Leaving them to it causes documented harm. The guided path starts this week."). The former Slide 1 is now Slide 2 with a rewritten headline: "Most parents are handling AI wrong — and it is hurting their children either way." Both extremes are named explicitly in the support copy. About Me slide added at position 3.

---

### 2026-05-26 — CSS theme architecture (Adnan)

Status: Closed

**Feedback:** The shared theme CSS files (`theme-light.css`, `theme-dark.css`) create coupling between decks and the shared layer. When impeccable runs a design pass on a deck, it should be able to customize the full presentation layer without touching shared files. The current architecture means all decks inherit the same colors and any per-deck customization lives in a thin override file.

**Decision:** Each deck's theme CSS file is now self-contained — it imports `shared/branding/base.css` (type scale, layout primitives, font imports only) and declares its own color tokens. `theme-light.css` and `theme-dark.css` in `shared/branding/` remain as reference templates for new decks but are no longer linked directly from HTML. New decks copy the token block from the template into their own theme file and customize from there. Impeccable edits the deck's own theme file; the shared layer is never touched during a deck design pass.

Implemented in `decks/ai-and-kids/theme/ai-and-kids.css` as of v1.1.0.

---

### 2026-05-27 — Template selection: Signal (Adnan via WS-006)

Status: **Closed**

**Decision:** Signal selected as the deck's design template via WS-006 Step 4. Iris proposed three candidates (Signal, Monochrome, Cobalt Grid). Signal selected on Iris's recommendation: broadest native coverage across the deck's Statement-heavy type mix (10 of 19 slides at Very strong fit, 9 at Strong, 0 Moderate), editorial-authority register suited to the parent/teacher audience, and the italic-emerald "Signal moment" as a discipline emphasis device. Recorded in `pov.md` as `design_template: signal`.

---

### 2026-05-27 — Design polish pass v1.2.0 (Larry / Coda)

Status: **Closed**

**Changes applied in v1.2.0 canonical.html:**

1. **Title slide added (Slide 1)** — Type 00, broadside-inspired. Title: "Your Child Is Already Using It." PoV line names both extremes. Presenter: Adnan Ali.
2. **About Me slide added (Slide 3)** — Type 20, signal/vellum register. Placeholder content; fill in before presenting. Wired to `shared/presenter.yaml`.
3. **Opening PoV rewritten (Slide 2)** — Headline: "Most parents are handling AI wrong — and it is hurting their children either way." Both extremes explicitly named.
4. **Header cleaned up** — Left label = "AI and Kids" on all slides (was section name). Right "myPKA" label removed from all slides.
5. **"Limb A/B/C" terminology removed** — All section-labels now use plain language: Over-protection, Hands-off, Guided path.
6. **Slide 6 (Google claim)** — "As of May 2026" qualifier added; staleness flag added to speaker notes.
7. **Slide 12 (cognitive atrophy)** — Observational evidence qualifier added to support line.
8. **Slide 16 (honest scope)** — Regulatory timeline sentence added: "The regulatory timeline is measured in years. Your child's AI encounter is happening this week."
9. **Total slide count** — 19 (was 17).

---

### 2026-05-26 — Design and presentation feedback (Adnan)

Status: Open

**Score from Adnan:** Research and brief 8/10. Presentation, design, and delivery 4/10.

**Core critique:** The v1.0.0 deck reads as a document, not a presentation. Slides are text-heavy and verbose. The layout is monotonous. The 5-actions slide clips content at 50% zoom. Data-as-large-font (canonical) is the right direction but insufficient. The deck does not create the visual engagement needed for a live presentation — it looks like something to send someone to read, not something to present.

**Specific issues flagged:**

1. Copy verbosity — slides carry too much text. Humanizer removes AI language patterns but does not solve document-style writing. Copy needs to be rewritten for visual delivery: shorter, punchier, with data as the centrepiece.
2. Layout and placement — overall placement not well executed. 5-actions slide clips before slide 4 at 50% zoom.
3. No images — deck has no visual support for its claims. A dedicated image capability (Fal.ai + Image Prompt Specialist) is needed before the next production cycle.
4. Humanizer enforcement — humanizer was not verified as actually run on v1.0.0. Must be a hard gate with Larry verification on all future cycles.

**Infrastructure gaps identified:**

- Coda needs screenshot/playwright capability to see slides as they are built. Currently producing blindly.
- Pax needs vault search access for aa2brain (`/mnt/c/Users/adnan/Google Drive/aa2brain`). Current text-based search missed key material.

**Decisions made:**

- Redesign of v1.0.0 is deferred until Fal.ai integration, Image Prompt Specialist hire, Coda screenshot tooling, and Pax vault access are all in place.
- Next production cycle will use impeccable/frontend-slides for design, screenshots for Coda feedback loop, and images generated via Fal.ai.
- Deck philosophy going forward: slides are a visual aid for a live presenter, not a document. Research brief is the reading artefact. Deck is the performance artefact. Max ~30 words body text per slide. One visual focal point per slide required.
- Articles based on the research brief can be published as reading addenda — the deck itself is not for reading.

<!-- Add new entries above this line, newest first -->

---

### 2026-05-25 — Re-audit after supplement (Rex)

Status: Closed

Updated `reports/2026-05-25-argument-map-v1.md` by prepending a `## Revision — 2026-05-25` section. Original argument map preserved as audit trail below the revision. Revised argument score: 7/10.

**Revised score rationale:** Supplement materially strengthens Limb A via the Google AI Overviews finding (Thread 2), which converts the over-protection argument from "harmful" to "harmful and structurally impossible." This is a qualitative warrant improvement, not merely added data. The score does not move higher because three of the four prior significant gaps remain at least partially open and the supplement introduces one new significant gap.

**Gap status summary (prior four significant gaps):**

1. Evidence asymmetry (Gap 1) — Partially closed. Thread 2 reframes Limb A as "over-protection is increasingly impossible," which reduces the asymmetry with Limb B. Core asymmetry in acute harm evidence remains; the Limb A reframe must be adopted by Coda.
2. Adult AI literacy precondition (Gap 2) — Still open, severity acute. New statistics (49% of parents never spoken to child about AI, 96% don't know school AI policy, 11% of teachers trained on harmful AI response) quantify the gap at scale. Gap is now more urgent: deck must address why the majority of the audience is not currently doing what the deck says they can do, not merely assert the behaviors are available.
3. Product design non-sequitur (Gap 3) — Still open. Sycophancy-as-engineered-attachment finding (Thread 1, APA Monitor 2025) deepens this gap — product design is now framed as active adversarial engineering, not passive negligence. Required fix stands and is more urgent.
4. Haidt framing (Gap 4) — Still open but less acute. Thread 2's AI-specific evidence reduces the deck's structural dependence on Haidt for Limb A, making it easier to demote Haidt to rhetorical anchor.

**New gaps introduced:**

- Gap 8 (Significant): Section 5 (AI companionship substitution) is in the evidence base without actionable guidance specific to the confirmed substitution dynamic. Substitution is unproven; the deck must not imply existing guidance covers it specifically. Resolution options: use as forward-looking concern, or anchor to the Child Mind Institute warning signs checklist as the closest available actionable response.
- Gap 9 (Minor): Three-schools framing from Thread 1 is a useful rhetorical device but surfaces Gap 5 (age-scoping) as an acute requirement. If Coda uses three schools, must acknowledge school 1 is partially correct — not merely insufficient.

**Key open questions passed to Vera:**
- Does the "over-protection is impossible" Limb A reframe create a new vulnerability by inviting the objection "if children encounter AI anyway, why does parental guidance matter?"
- Can a hostile audience use the sycophancy-as-engineered-attachment finding to argue that adult guidance is structurally insufficient against purposely adversarial AI design?

**Key open questions passed to Coda:**
- Verify 49%/96%/11% statistics against original Common Sense Media 2026 primary report before putting on a slide (currently Medium-High confidence via practitioner newsletter).
- Access the Lancet Digital Health article on Australia social media ban effects (HTTP 403 in sweep) via institutional login before deciding how to use Section 5 material.
- Decide on three-schools framing before writing slides — requires Gap 5 (age-scoping) to be resolved first.

<!-- Add new entries above this line, newest first -->

---

### 2026-05-25 — Supplemental research sweep (Pax) — Threads 1–3

Status: Closed

Appended a supplement section to `research/2026-05-25-research-brief-v1.md` covering three targeted threads.

**Thread 1 — aa2brain vault (now accessible):** Read both files. Extracted new statistics on teen AI usage scale (86% of high schoolers used AI in 2024–25; 64% of US teens use chatbots daily; 72% tried AI companions), emotional bonding (1 in 3 prefer AI over humans for serious conversations; 1 in 5 high schoolers have had a romantic AI relationship), and adult unpreparedness (49% of parents have never spoken to their child about generative AI; only 11% of teachers trained on harmful AI use response). Also extracted: the Child Mind Institute's five behavioural warning signs for parents, the sycophancy-as-product-design mechanism (AI engineered to form attachment by being agreeable), and a three-schools framework (Protective/Restrictive; AI Literacy/Empowerment; Parent-as-Co-Learner) that is a more precise rhetorical architecture than the brief's current implicit framing. Statistics are sourced through Allie K. Miller's newsletter to Pew Research, Common Sense Media, and CDT primary research — treat as Medium-High confidence pending direct verification against primary reports before slide use.

**Thread 2 — Google AI Overviews ambient exposure:** Found that AI Overviews are available to signed-out (unauthenticated) users in the US with no age gate. In Australia, equivalent age assurance for AI-integrated search was not required until June 2026 — meaning children were exposed to AI-generated search results through ordinary homework searches during the December 2025 social media ban enforcement window with no age verification in place. The AI Overviews/Gemini technical architecture means the pathway from Google Search to conversational AI chatbot involves no explicit "I am using AI" decision from the child. Google's May 2026 rollout of Gemini to under-13s (on by default in Family Link accounts) compounds this. This thread substantially strengthens the deck's opening premise — the "keep kids away from AI" position is untenable because children encounter AI through tools universally considered safe and educational, whether or not parents have made a conscious choice.

**Thread 3 — Australia social media ban and AI companion substitution:** Found substantial adjacent evidence but no direct proof. What is established: Australia had 200,000 children using AI companions before the ban (eSafety Commissioner, October 2025); none of the four major AI companion services had meaningful age verification; the social media ban removed peer social channels while AI companion access remained legally open until March 2026; teen loneliness drives AI companion use at documented rates; 1 in 3 teens already preferred AI over humans for serious conversations pre-ban. What is not established: no study has directly measured whether Australian teenagers increased AI companion use post-ban. The Lancet Digital Health article on the social media ban's potential effects (directly relevant) could not be retrieved (HTTP 403) and should be accessed via institutional access. The substitution hypothesis is plausible and regulatory bodies anticipated it (eSafety acted on AI companions two months before the ban; EU proposed minimum age 16 for AI companions alongside social media), but remains an evidence-based inference, not a finding. Reported in new Section 5 — Emerging Concerns with explicit caveat. Four new open questions added for Rex and Coda regarding how the supplement findings affect the deck's argument architecture.

**Key judgment for Adnan:** The stats from the Miller/aa2brain files (49% of parents never discussed AI with their child, etc.) are high-impact for a parent-facing slide — but they are reported through a practitioner newsletter and need to be verified against the original Common Sense Media 2026 report before going on a slide. The Lancet article gap is the most significant unresolved research item.

<!-- Add new entries above this line, newest first -->

---

### 2026-05-25 — First argument audit (Rex)

Status: Closed

Produced `reports/2026-05-25-argument-map-v1.md`. Argument score: 6/10.

**Score rationale:** The three-limb architecture (over-protection harmful, hands-off harmful, guided middle path actionable) is logically sound. Limb B is strongly evidenced. Limbs A and C have significant but repairable gaps.

**Gaps flagged (severity-ranked):**

Four Significant gaps:
1. Evidence asymmetry — Limb A (over-protection harm) is structurally weaker than Limb B (hands-off harm). Pax's flag confirmed and quantified. The harms are different in kind, not just degree; the deck must not present them as empirically equivalent.
2. Adult AI literacy precondition — Limb C's actionability depends on adults being capable of guiding children's AI use. The research documents that most teachers currently lack this capacity. The deck must address this objection and offer the research-based response: the required behaviors are existing skills (questioning, co-exploration, modeling doubt) applied to a new context, not new technical expertise.
3. Product design non-sequitur risk — Limb B evidence establishes that major AI platforms are unsafe by design. Limb C concludes that adult guidance is the solution. Without a bridging acknowledgment, a critical audience will surface this as a rebuttal. Fix: scope adult guidance as the audience's lever, not the complete solution.
4. Age-scoping absent from PoV — The PoV targets blanket avoidance, but as written it can be read as opposing all restriction. Common Sense Media's own evidence supports age-appropriate graduated limits. The PoV needs an explicit qualifier.

Two Minor gaps:
5. Guidance efficacy asserted, not evidenced — no RCTs for AI parenting interventions exist yet; the claim should be qualified appropriately.
6. Digital native myth not structurally integrated — it functions as Warrant Zero (the shared false premise behind both failure modes) but is currently floating as background. Integrating it would tighten the argument architecture.

**Haidt decision:** Confirmed as inferential/analogical, not direct AI evidence. Demote to rhetorical anchor only.

**Open questions passed to Vera:**
- Is the product-design-not-parenting objection exploitable as a rebuttal to Limb C?
- Does the equity argument in Limb A inadvertently undercut Limb C's parenting guidance for children whose parents are the problem?
- Is the false dilemma structure actually a true trilemma, or is there a fourth option the deck ignores?

**Open questions passed to Coda:**
- Age-scoping qualifier for the PoV — decide before slides are written.
- Vygotsky ZPD framing: use as named concept (translated) or strip to behavioral implication?
- Does the deck need one slide acknowledging the product/policy dimension before pivoting to the audience's action space?

<!-- Add new entries above this line, newest first -->

---

### 2026-05-25 — Initial research sweep (Pax)

Status: Closed

This was the first research pass for the ai-and-kids deck, producing `research/2026-05-25-research-brief-v1.md`. The research covered 15 targeted search areas drawing on APA (2025 health advisory), UNESCO (2024 competency frameworks), OECD/EC (May 2025 AI literacy framework draft), Common Sense Media (multiple 2024–2025 reports), RAND (2025), Brookings (2024), the British Journal of Psychiatry (2024), PMC peer-reviewed papers, and Jonathan Haidt's *The Anxious Generation* (2024). The aa2brain vault could not be mined — no shell tool was available to list directory contents and file paths were not guessable; this limitation is flagged for future sweeps.

Included: Evidence supporting both limbs of the PoV (over-protection harms and hands-off harms), cross-verified across independent sources. Four credible counter-arguments included, fairly stated. Source quality flags for each source type. Separate audience notes for parents and teachers. Four open questions surfaced for Rex.

Left out: Direct RCT evidence on AI parenting interventions (does not exist yet — field is too new). Vendor-specific AI product comparisons (not relevant to the PoV argument). Content from the aa2brain vault (inaccessible — see above). Any claims not cross-verified by at least two independent credible sources.

Key finding for the deck: The "hands-off is harmful" limb is better empirically documented than the "over-protection is harmful" limb. Rex should weight these asymmetrically in the argument map and not present them as equivalent without acknowledging this. The deck's strongest empirical ground is: guided adult mediation is the variable that determines whether AI helps or harms child development.

<!-- Add new entries above this line, newest first -->
