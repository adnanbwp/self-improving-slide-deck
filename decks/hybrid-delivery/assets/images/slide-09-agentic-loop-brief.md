# Image Brief — Slide 09 The Agentic Loop (hybrid-delivery)

- **Date:** 2026-06-01
- **Deck slug:** hybrid-delivery
- **Slide:** 09 — "The Agentic Loop" (new slide, Section: "The Loop")
- **HTML source:** Not yet wired — brief precedes Coda placement (Coda writing HTML in parallel)
- **Research brief:** /home/aali/learning/claude/self-improving-slide-deck/decks/hybrid-delivery/research/2026-05-30-research-brief-v2.md
- **Argument map:** Supplied inline via Larry dispatch (v2 file not yet present on disk; claim grounded in research brief v2 HITL patterns section and Anthropic Trustworthy Agents findings)

---

## Style thread

Clean, editorial flat-design diagram on cream paper (#F5F1E8 approximately). Near-black ink for structural lines and body text, jade accent (#3D7A5E approximately) for headers and connective arrows. Geometric and precise — the register is "smart whiteboard diagram," the kind a thoughtful systems thinker would draw with deliberate care. Whitespace is a first-class design element: resist filling every corner. No decorative flourishes, no gradients, no drop shadows. Consistent with slide-08-chat-vs-agent in the same deck.

---

## Argument justification

This image supports the HITL warrant — specifically the claim that "human-in-the-loop" means the human enters the agent's reasoning cycle at a designed gate point, not that the human supervises every micro-step. The research brief (v2, Finding 2) establishes that Anthropic's own research found agents ask for clarification 16.4% of turns on complex goals while humans interrupt only 7.1% of the time — meaning agents are better calibrated than humans at knowing when to pause. The IM/DM's job is to design the system so those pauses land at the right decision points. This argument only lands if the audience can visualize the loop that the pauses interrupt. Without the loop diagram, "human-in-the-loop" sounds like a vague promise of oversight; with it, the HITL patterns on the subsequent slides have a concrete mechanical referent — the human enters at DECIDE or at ACT, depending on the pattern selected. The loop diagram also sets up the governance failure modes: the Replit incident (production database deleted) is precisely the failure case where the loop ran to ACT without a human gate at DECIDE. Showing the loop makes the governance argument mechanically legible rather than anecdotal.

---

## Recommended model

**`fal-ai/nanobanana-2`**

Rationale: This slide requires multiple legible text labels rendered directly inside the image — five step labels ("RECEIVE", "THINK", "ACT", "OBSERVE", "DECIDE"), five sub-labels ("input / trigger arrives", "LLM reasons & plans", "use tools & connections", "read results & context", "done? or loop again"), two fork-path labels ("complete ✓", "continue"), and a center circle label ("LLM"). nanobanana-2 is specified by Adnan specifically for its superior text rendering inside generated images. No other Fal.ai model should be substituted here.

---

## Primary prompt

```
Editorial flat-design circular loop diagram, cream paper background (#F5F1E8), near-black ink and jade green accent.

Center of the composition: a filled circle in jade green labeled "LLM" in white or cream text.

Five rectangular step boxes arranged in a clockwise circle around the center circle, connected by curved arrows forming a continuous loop. The steps in clockwise order starting from the top-left position:

Step 1 — box labeled "RECEIVE" in bold near-black, sub-label text below: "input / trigger arrives"
Step 2 — box labeled "THINK" in bold near-black, sub-label text below: "LLM reasons & plans"
Step 3 — box labeled "ACT" in bold near-black, sub-label text below: "use tools & connections"
Step 4 — box labeled "OBSERVE" in bold near-black, sub-label text below: "read results & context"
Step 5 — box labeled "DECIDE" in bold near-black, sub-label text below: "done? or loop again"

At the DECIDE box, a fork: one arrow exits the loop pointing outward (away from center) labeled "complete ✓" in jade text. A second arrow curves back inward toward the THINK box labeled "continue" in near-black.

All curved loop arrows are jade green with clear arrowheads indicating clockwise direction. The arrows feel dynamic and directional. The LLM center circle is jade filled. Step boxes have thin near-black borders on cream fill. All text is clean geometric sans-serif. Generous whitespace between elements — the diagram breathes, it does not crowd.
```

---

## Negative prompt

```
photorealistic, photography, 3D render, robot, android, circuit board, binary code, hologram, glow effects, neon, vibrant color, color gradients, drop shadows, decorative borders, speech bubbles, emoji, icons, illustrations of people, hands, faces, corporate stock photo aesthetic, cluttered layout, small unreadable text, overlapping elements, watermark, blurry text, pixelated text, distorted letters, counter-clockwise arrows, overlapping step boxes, boxes touching the center circle, flat arrows without arrowheads, spiral shape, gear shape, infinity symbol
```

---

## Generation parameters

| Parameter | Value | Notes |
|---|---|---|
| width | 1792 | 16:9 landscape |
| height | 1024 | 16:9 landscape |
| num_inference_steps | 50 | Higher step count for text legibility and circular layout precision |
| guidance_scale | 7.5 | Balanced prompt adherence vs. quality |
| seed | 2609 | Mnemonic: 26 = 2026, 09 = slide number |

---

## Alternative prompt A — simplified loop, no sub-labels

Use if the primary generates overcrowded step boxes where sub-labels compete with step names for legibility.

```
Editorial flat-design circular loop diagram, cream paper background, jade and near-black.

Center: jade circle labeled "LLM".

Five boxes in a clockwise ring, connected by jade curved arrows with arrowheads. Boxes labeled only: "RECEIVE", "THINK", "ACT", "OBSERVE", "DECIDE". Bold near-black text, cream fill, thin border.

At DECIDE, two arrows fork: one exits the loop labeled "done ✓", one curves back to THINK labeled "loop".

Clean, geometric, whiteboard aesthetic. Generous whitespace. No sub-labels. No decorative elements.
```

---

## Coda placement notes

Two placement options for Coda to assess against the final layout:

**Option 1 — Full-bleed background (preferred)**
Place the diagram as a full-bleed background image filling the entire slide canvas. The image is already designed at 1792×1024 to match 16:9 slide proportions. No additional text overlay is needed — the image carries all labels. Coda should ensure no conflicting HTML text elements are positioned over the loop structure. A section-label badge ("The Loop") may be placed in the top-left corner outside the diagram's active area if the composition permits.

**Option 2 — Centered panel at 80% width**
Place the image centered on a cream slide background (#F5F1E8) at 80% width. The equal cream margins at all edges give the circular diagram visual breathing room and allow the slide number and section label to occupy the periphery without overlapping the diagram. This is the safer option if the generated image has a tight circular composition that would be cropped awkwardly at full bleed.

In both options: do not apply CSS filters, opacity reductions, or color overlays. The diagram is designed to integrate with the slide's cream-and-jade palette natively. The jade arrows must remain at full saturation to maintain directionality — do not wash them out.

---

## Brief rationale

The agentic loop diagram is the mechanical substrate for the deck's HITL argument. The research brief (v2, Finding 2, HITL section) establishes that the IM/DM's governance role is specifically to decide which actions in this loop require a human gate and which can proceed autonomously — the DEV Community source states directly that "you encode this classification in your agent's action manifest, not in the agent's prompt." That classification decision — where the human enters the loop and at which step — is the concrete, actionable definition of the IM/DM's new role. Without seeing the loop, the audience cannot locate where they are supposed to act. With the loop visible, the HITL patterns become a question of "at which step do I insert a gate?" rather than an abstract governance principle. The loop also makes the governance failure modes mechanically legible: the Replit production database deletion (Finding 5, v2 brief) is the failure case where ACT executed without a gate at DECIDE. The Meta data leak is the failure case where ACT executed without a context-scope check before the action. Both incidents map to specific loop positions, making the governance argument concrete rather than cautionary-anecdotal.
