# Image Brief — Slide 08 Chat vs Agent (hybrid-delivery)

- **Date:** 2026-06-01
- **Deck slug:** hybrid-delivery
- **Slide:** 08 — "Chat vs Agent" (new slide, Section: "The Shift")
- **HTML source:** Not yet wired — brief precedes Coda placement (Coda writing HTML in parallel)
- **Research brief:** /home/aali/learning/claude/self-improving-slide-deck/decks/hybrid-delivery/research/2026-05-30-research-brief-v2.md
- **Argument map:** Supplied inline via Larry dispatch (v2 file not yet present on disk; claim grounded in research brief v2 Claim Impact Summary and HITL patterns section)

---

## Style thread

Clean, editorial flat-design diagram on cream paper (#F5F1E8 approximately). Near-black ink for structural lines and body text, jade accent (#3D7A5E approximately) for headers and connective arrows. Geometric and precise — the register is "smart whiteboard diagram," the kind a thoughtful systems thinker would draw with deliberate care. Whitespace is a first-class design element: resist filling every corner. No decorative flourishes, no gradients, no drop shadows. Consistent across all slides in this brief.

---

## Argument justification

This image supports the deck's foundational structural claim — that agents represent a categorically different paradigm from LLM chat — which is the conceptual prerequisite for every downstream claim in the deck. The HITL patterns argument (slides 15–17), the five workflow-agent collision points, and the IM/DM governance role all rest on the audience understanding that agents are not smarter chatbots but systems with persistent context, external connections, scheduled execution, and multi-step capability. Without this foundation, the collision points feel abstract and the governance argument feels like over-engineering. A split-panel diagram makes the structural difference visible in a single glance: left panel shows the stateless, single-turn simplicity of chat; right panel shows the connected, multi-directional richness of an agent. The visual asymmetry between the two panels does the argumentative work — the audience perceives the complexity differential before reading a word.

---

## Recommended model

**`fal-ai/nanobanana-2`**

Rationale: This slide requires legible text labels rendered directly inside the image — panel headers ("LLM Chat", "Agent"), flow step labels ("User", "LLM", "Response"), caption text ("Stateless · Single turn · No memory"), and the four compass-point labels with sub-labels ("Context / memory · knowledge", etc.). nanobanana-2 is specified by Adnan specifically for its superior text rendering inside generated images. No other Fal.ai model should be substituted here.

---

## Primary prompt

```
Editorial flat-design diagram, cream paper background (#F5F1E8), near-black ink. A clean vertical dividing line splits the image into two panels.

LEFT PANEL — header text "LLM Chat" in jade green near the top. Below: a simple three-step linear flow diagram with three boxes connected by right-pointing arrows in sequence: box labeled "User" → box labeled "LLM" → box labeled "Response". Below the flow, small caption text in near-black: "Stateless · Single turn · No memory". The left panel has generous white space — minimal, sparse, intentionally simple.

RIGHT PANEL — header text "Agent" in jade green near the top. In the center of the panel: a circle labeled "LLM (Brain)" in jade. From this center circle, four lines radiate outward in four cardinal directions, each ending in a small rectangle. TOP rectangle: bold label "Context" with sub-label text "memory · knowledge". RIGHT rectangle: bold label "Connections" with sub-label text "tools · APIs". BOTTOM rectangle: bold label "Capabilities" with sub-label text "skills · actions". LEFT rectangle: bold label "Cadence" with sub-label text "schedules · triggers". The right panel feels visually richer and more connected than the left panel.

All text is clean geometric sans-serif. Jade accent color on the panel headers, the LLM center circle, and the four radiating lines. Near-black for all labels and body text. Cream background throughout. No decorative elements. No gradients. No drop shadows. Precise, geometric, smart whiteboard aesthetic.
```

---

## Negative prompt

```
photorealistic, photography, 3D render, robot, android, circuit board, binary code, hologram, glow effects, neon, vibrant color, color gradients, drop shadows, decorative borders, rounded corners on dividing line, speech bubbles, emoji, icons, illustrations of people, hands, faces, corporate stock photo aesthetic, cluttered layout, small unreadable text, overlapping elements, curved or organic shapes, watermark, blurry text, pixelated text, distorted letters
```

---

## Generation parameters

| Parameter | Value | Notes |
|---|---|---|
| width | 1792 | 16:9 landscape |
| height | 1024 | 16:9 landscape |
| num_inference_steps | 50 | Higher step count for text legibility and layout precision |
| guidance_scale | 7.5 | Balanced prompt adherence vs. quality |
| seed | 2608 | Mnemonic: 26 = 2026, 08 = slide number |

---

## Alternative prompt A — simplified right panel

Use if the primary generates an overcrowded right panel where the four compass labels compete with each other visually.

```
Editorial flat-design diagram, cream paper background, near-black ink. Vertical dividing line splits the composition.

LEFT PANEL: header "LLM Chat" in jade. Three-step linear flow: "User" → "LLM" → "Response" with right-pointing arrows. Caption below: "Stateless · Single turn · No memory". Sparse, minimal.

RIGHT PANEL: header "Agent" in jade. Center circle: "LLM (Brain)". Four labeled spokes extending outward at top, right, bottom, left positions. Top spoke: "Context". Right spoke: "Connections". Bottom spoke: "Capabilities". Left spoke: "Cadence". Each spoke terminus has a small label only — no sub-labels. A note below the diagram in small text: "memory · tools · skills · schedules". Jade lines for spokes. Near-black text throughout.

Flat, geometric, whiteboard diagram aesthetic. Cream background. No decorative elements.
```

---

## Coda placement notes

Two placement options for Coda to assess against the final layout:

**Option 1 — Full-bleed background (preferred)**
Place the diagram as a full-bleed background image filling the entire slide canvas. The image is already designed at 1792×1024 to match 16:9 slide proportions. No additional text overlay is needed — the image itself carries all labels. Coda should ensure the HTML slide has no conflicting text elements positioned over the image panels.

**Option 2 — Centered panel at 85% width**
Place the image centered horizontally at 85% of slide width, with equal cream margins at top and bottom, anchored to a cream slide background (#F5F1E8). This creates a slight breathing margin around the diagram and allows a small section-label badge ("The Shift") in the top-left corner of the slide without it overlapping the diagram content.

In both options: do not apply CSS filters, opacity reductions, or color overlays to the image. The diagram is designed to integrate with the slide's cream-and-jade palette natively.

---

## Brief rationale

The "Chat vs Agent" distinction is not incidental to the hybrid-delivery deck — it is the conceptual gateway through which every subsequent claim must pass. The deck's audience (IMs and Delivery Managers) has extensive experience with LLM chat tools (Microsoft 365 Copilot in chat mode, per the research brief) but is only beginning to encounter agents (31% of engineers are using agents per Stack Overflow 2025; the practitioner equivalent is lower). Without a clear visual model of what makes an agent structurally different, the audience will frame the entire deck through the lens of chatbot behavior they already know — and the collision points, HITL patterns, and governance failure modes will all seem like overreactions to a tool they are already comfortable with. The split-panel diagram resolves this framing risk in the span of a single slide. The left panel validates the audience's existing mental model (chat is exactly as simple as they think); the right panel reveals the structural complexity that makes agents a different category requiring different governance. The visual asymmetry does not need to be explained — it is perceptible before the text labels are read.
