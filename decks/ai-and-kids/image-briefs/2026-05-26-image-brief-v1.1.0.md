# Image Brief — AI and Kids v1.1.0

- **Date:** 2026-05-26
- **Deck slug:** ai-and-kids
- **HTML sources:** `decks/ai-and-kids/versions/v1.1.0/canonical.html`
- **Research brief:** `decks/ai-and-kids/research/2026-05-25-research-brief-v1.md`
- **Argument map:** `decks/ai-and-kids/reports/2026-05-25-argument-map-v1.md`

---

## Style thread

All images in this deck are observational documentary photographs — the kind that look pulled from real family or classroom life, not staged or lit for advertising. The palette is warm but not saccharine: natural window light, everyday environments, no dramatic contrast or cinematic treatment. Every image must feel like a Tuesday afternoon, not a campaign.

---

## Per-slide entries

### Slide 1 — Both extremes fail children (title slide)

**Argument justification:** The deck's central claim is that adult presence — not restriction and not absence — is the deciding variable. The title slide must establish that emotional register before any argument begins. A warm, collaborative, calm image of an adult and a child at a screen together communicates "guided engagement" in a single frame in a way the headline alone cannot. It also counteracts the anxiety most parents feel when AI and children are mentioned in the same breath: the first thing the audience sees should be guidance-as-normal, not threat-as-normal.

**Prompt:** A parent and a child — the child looks approximately 10–12 years old — sitting side by side at a kitchen or dining table, both looking at a laptop screen together. The adult has turned slightly toward the child, relaxed posture, no urgency. The child is pointing at something on the screen. The room is lit by natural light from a window to one side; the light is warm and soft, afternoon quality, not harsh. The laptop screen is visible but its contents are indistinct — no specific text or logo is legible. Both faces are visible in a three-quarter angle; both expressions are engaged, curious, and calm. No phones in frame. The table has ordinary household objects — a cup, maybe a book — nothing stylised. Shot from roughly eye-level or slightly elevated, medium shot that includes both figures and the laptop. Style: observational photography, minimal depth-of-field blur (the background can be slightly soft but both figures must be sharp), no filters, no vignetting, no graphic overlay.

**Model recommendation:** `fal-ai/flux/dev` — photorealistic documentary photography with natural light; FLUX Dev handles subtle human warmth and domestic interiors without over-sharpening or artificial skin tone correction.

**Aspect ratio:** 1:1 — crops cleanly into the right column of the col-layout on Slide 1 without letterboxing.

**Style direction:** Observational documentary. Natural window light. Warm but not warmed — no orange grade. Real domestic environment.

**Negative constraints:** No stock-photo smiles (wide, teeth-forward, posed). No blue-toned "tech" lighting or screen glow as the primary light source. No AI branding, logos, or legible text visible on screen. No tablet or phone as the primary device — laptop only. No anxious or alarmed expressions. No dramatic framing (low angle, wide-angle distortion, cinematic flare). No children under approximately 8 or over approximately 14. No teachers or classroom setting — this slide is for the parent audience.

---

### Slide 2 — Both failure modes rest on the same false assumption — SKIPPED

**Reason:** The display-phrase typography ("Remove the adult. / Remove the risk. / Wrong.") is the entire rhetorical mechanism on this slide — an image would compete with the three-beat rhythm, not amplify it.

---

### Slide 3 — Three schools of thought — SKIPPED

**Reason:** Three-column card grid doing structural taxonomy work; the content is intellectual categorisation and an image would clutter rather than clarify.

---

### Slide 4 — The decision to keep your child from AI has already been made for you — by Google

**Argument justification:** This is the structural anchor of Limb A — the impossibility argument. The claim is factual: children encounter AI-generated content through ordinary Google homework searches without any parental decision to introduce AI. The argument's force depends on the audience recognising the ordinariness and inevitability of the exposure. The image makes the abstract structural claim ("AI is already in the homework tools you trust") concrete and immediately legible. Text alone describes the situation; the image makes the parent feel it. The existing `data-prompt-hint` correctly identifies the core scene; the full prompt below refines it to Iris-quality specificity.

**Prompt:** A child of approximately 11–13 years old sitting alone at a desk or kitchen table, working on what is clearly a homework task — a textbook or notebook is open beside the laptop. The laptop screen is visible from a slight angle and shows a Google Search results page: the top third of the screen has a distinct AI-generated summary box (styled in a rounded card format, slightly separated from the organic results below it). The AI summary box contains text — it does not need to be legible, but the visual structure of the Google AI Overview card format must be recognisable: distinct container, light background, a small icon, one or two short paragraphs. The organic search results appear below it in the familiar blue-link format. The child is reading the screen; their expression is neutral, focused — this is just homework, nothing unusual. The room is lit with ambient daylight from a window; the screen provides some additional illumination on the child's face. No adults are visible in the frame — the adult's absence is the point. Medium shot: the child, the desk surface, the screen. Style: observational documentary photography, slightly elevated angle looking at the screen over the child's shoulder or from a 45-degree side angle that shows both the child's face and the screen content. Shallow enough depth of field that the background is soft, but screen text structure remains visible.

**Model recommendation:** `fal-ai/flux/dev` — for maintaining photorealistic screen content legibility while keeping the human figure natural. Note to Mack: if the Google AI Overview card format is not rendering recognisably in the generated image, a second pass should be requested with explicit screen content composition or a composited screen mock-up.

**Aspect ratio:** 1:1 — fills the right column of the col-layout on Slide 4.

**Style direction:** Observational documentary. Same visual register as Slide 1 but with deliberate adult absence — colder in mood (only ambient/screen light), not warm window-light. The contrast with Slide 1 reinforces the argument: with adult versus without.

**Negative constraints:** No dramatic or alarmed expression on the child. No phone — laptop only. No AI branding other than Google Search UI structure. No adults in the frame. No obviously stylised or cinematic lighting. No text on screen that is legible enough to be read by the slide audience (screen structure visible, specific text indistinct). No child younger than approximately 10 or older than approximately 14. No classroom setting.

---

### Slide 5 — School AI bans don't prevent use — they just remove the only guided context — SKIPPED

**Reason:** The display phrase ("The ban protects / the students least at risk") carries the ironic charge of the argument. An image would illustrate rather than intensify it.

---

### Slide 6 — Some limits are right — SKIPPED

**Reason:** Age-limit list formatted as a structured reference — typographic content that functions as a table. No image serves a functional list.

---

### Slide 7 — This is not a marginal risk — population-scale exposure — SKIPPED

**Reason:** The 77% stat callout in the right column already provides visual contrast against the text. Adding an image would crowd the stat, which is the slide's single most important element.

---

### Slide 8 — AI companions are purposely engineered to form emotional attachment — SKIPPED

**Reason:** The pull-quote format ("Purposely programmed to be agreeable") achieves its impact through typography and restraint. Illustrating emotional manipulation risks cliché (child staring at phone, glowing screen). The argument lands harder without it.

---

### Slide 9 — The mental health harm is documented, not theoretical — SKIPPED

**Reason:** This slide documents mortality and clinical testing failures. Using an image here risks aestheticising harm or sensationalising a death. The statistical and testimonial evidence is more responsible without visual amplification.

---

### Slide 10 — AI boosts immediate output while degrading durable learning — SKIPPED

**Reason:** The two-line display phrase ("Better output. / Less thinking.") is a compression of the entire cognitive atrophy argument. An image of a student at a screen would be generic and would dilute the punch of the contrast.

---

### Slide 11 — The evidence on both sides is real — but not equivalent — SKIPPED

**Reason:** The contrast-pair grid layout is doing the rhetorical work of the evidence asymmetry disclosure. An image would interrupt the visual logic of the side-by-side comparison.

---

### Slide 12 — Adult guidance is the variable that determines whether AI helps or harms — SKIPPED

**Reason:** The three-line display phrase ("Same product. / Different adult. / Different outcome.") is the argumentative hinge of the deck. An image would give the audience something to look at other than those words. The words should land alone.

---

### Slide 13 — 49% of parents have never spoken to their child about AI — SKIPPED

**Reason:** The 49% stat callout in the right column is the confrontation; it needs no visual support. The statistic speaking to the audience directly is the intended effect.

---

### Slide 14 — Adult guidance is your lever — not the complete solution — SKIPPED

**Reason:** Display phrase + honest-scope argument slide. Argument content is the entirety of the slide; no image required.

---

### Slide 15 — Five warning signs — SKIPPED

**Reason:** Functional behavioral checklist for reference. Illustrating warning signs risks aestheticising distress or creating anxiety rather than equipping parents to act.

---

### Slide 16 — Five things you can do this week — SKIPPED

**Reason:** Numbered action list. A practical reference slide. An image would reduce the visual hierarchy of the list and distract from actions the audience should be scanning and retaining.

---

### Slide 17 — References — SKIPPED

**Reason:** Bibliography slide. No image appropriate.

---

## Summary

- **Slides briefed:** 2 (Slides 1 and 4)
- **Slides skipped:** 15
- **Style thread:** Observational documentary photography, natural/ambient light, warm but unglamourised domestic environments. Slide 1 warm window light (adult present); Slide 4 cooler ambient/screen light (adult absent) — the contrast is intentional and argumentative.
