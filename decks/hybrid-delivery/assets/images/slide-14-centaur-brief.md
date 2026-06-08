# Image Brief — Slide 14 Centaur Argument (hybrid-delivery)

- **Date:** 2026-05-30
- **Deck slug:** hybrid-delivery
- **Slide:** 14 — Structural Model ("Weak human + machine + better process beat the grandmaster")
- **HTML source:** Not yet wired — brief precedes placement
- **Research brief:** Supplied inline via Larry dispatch
- **Argument map:** Supplied inline via Larry dispatch

---

## Style thread

Editorial monochrome: high-contrast black-and-white photography or graphite-toned illustration, with visible grain or texture. The register is NYRB or Magnum Photos — ideas made legible through material detail, not symbolic gesture. No colour except warm cream tones where a background wash is needed; no digital-art smoothness; no motivational-poster composition.

---

## Argument justification

This image supports the centaur warrant — the core structural claim of the deck — that process design, not raw human or machine capability alone, determines outcomes in human+AI collaboration. The Kasparov 2005 Freestyle Chess Championship is the load-bearing evidence: amateur players with computers and better process beat grandmasters playing solo. A human hand at a chess board, with a machine presence implied through reflected screen light or a laptop visible at the edge of frame, makes the human+AI partnership concrete without over-explaining it. The editorial B&W aesthetic matches the NYRB source and signals intellectual seriousness appropriate to the IM/DM audience. The image does not carry the argument — the large display quote does — but it anchors the metaphor in physical reality so the audience reads the claim as grounded, not abstract.

---

## Recommended Fal.ai model

**`fal-ai/flux/dev`**

Rationale: FLUX Dev produces the highest-fidelity photorealistic detail in the Fal.ai stack and handles monochrome editorial photography well when the style is specified precisely in the prompt. It resolves fine material texture (chess piece grain, keyboard keys, board squares) without the over-smoothed look of SDXL. Preferred over `fal-ai/stable-diffusion-v3-medium` for this brief because the subject is documentary/photographic, not illustrative.

---

## Primary prompt

```
Black and white editorial photograph, close-up of a wooden chess board mid-game, pieces scattered in an unresolved mid-game position. A single human hand — relaxed, precise, not theatrical — hovers just above a knight or bishop, about to move. In the background, soft-focus: the edge of an open laptop screen, its light casting a faint rectangular reflection across the chess board squares. No human face visible. No artificial lighting effects. Shot as if by a documentary photographer for a serious literary journal: high contrast, fine grain, shallow depth of field, the chess board sharp and the background gently blurred. Mood: concentrated intellect, partnership, precision. Monochrome, warm shadow tones, not cold.
```

---

## Negative prompt

```
color, colour, vibrant, saturated, red, blue, green, yellow, orange, purple, bright, neon, glowing, robot, android, cyborg, mechanical hand, prosthetic, circuit board, binary code, hologram, digital overlay, floating text, HUD, interface graphics, stock photo composition, symmetrical framing, motivational poster, hands shaking, smiling face, any face, portrait, corporate office background, generic businessperson, cheesy, kitsch, AI art cliche, smooth plastic texture, over-processed, HDR, lens flare, watermark, blurry chess pieces in foreground
```

---

## Generation parameters

| Parameter | Value | Notes |
|---|---|---|
| width | 1792 | 16:9 landscape |
| height | 1024 | 16:9 landscape |
| num_inference_steps | 50 | Higher step count for photorealistic detail |
| guidance_scale | 7.5 | Balanced adherence vs. quality |
| seed | 2005 | Mnemonic: year of the Freestyle Championship |

---

## Alternative prompt A — tighter crop, board only

Use if primary generates an awkward hand or the laptop reflection reads as a distraction.

```
Black and white editorial photograph, extreme close-up of a chess board mid-game. Several pieces visible — knight, bishop, pawns — in a contested position. Across one or two board squares, a faint rectangular highlight: the reflected glow of an off-frame laptop screen. No hands. No faces. Shot with a macro lens, fine grain, high contrast. The board surface shows age and use — worn squares, slightly scuffed pieces. Mood: analytical calm, two kinds of intelligence at work in the same space. Monochrome, warm shadow tones.
```

---

## Alternative prompt B — two hands, human and geometric

Use if Larry or the design review wants a more direct visual expression of the partnership. Use only if the abstract geometry reads as elegant, not kitschy.

```
Black and white editorial illustration, graphite and ink style. A human hand and a second hand rendered in precise geometric line-work — not robotic, not mechanical, but architectural, like a technical drawing come to life — both reaching toward the same chess piece on a board, neither touching it yet. The human hand has natural skin texture and shadow; the geometric hand has clean constructed lines and cross-hatching. Composition: symmetrical from below, looking up at the two hands converging. Mood: precision, collaboration, intellectual tension. No colour. No faces. The board is implied by its pattern of squares beneath the hands.
```

---

## Coda placement notes

Two placement options are recommended; Coda should assess both against the final layout:

**Option 1 — Right panel (preferred)**
Place the image in the right 45% of the slide as a framed panel, with the left 55% carrying the display quote, sub-claim, and human/AI column layout. Apply a very light cream wash (#F8F5EE at ~15% opacity) over the image to integrate it with the slide background. This keeps the image as a visual anchor without competing with the typographic hierarchy. The image should bleed to the top and bottom edges of the right panel.

**Option 2 — Full-bleed background**
Use the image as a full-bleed background at 20–25% opacity over the cream background, with the text layout centred over it. This is the lower-risk option if the image composition is too busy at full panel size. Apply a cream gradient overlay (left edge fully opaque at #F8F5EE, fading to 40% opacity at the right edge) so the left-side text remains fully legible.

In both options: do not add a drop shadow or border to the image. The monochrome image should feel continuous with the slide's warm cream/charcoal palette, not framed as a separate element.

---

## Brief rationale

The Kasparov Freestyle Chess claim is the structural fulcrum of the hybrid-delivery deck's centaur argument. It is the one piece of evidence that makes the "IM/DM as process designer" conclusion feel earned rather than asserted. An image that grounds this claim in physical material — a real chess board, a human hand in thought, a machine presence at the periphery — does two things text cannot: it makes the human+AI collaboration feel like an observable practice rather than a metaphor, and it signals to the IM/DM audience that this is serious intellectual territory, not a trend deck. The editorial B&W register matches the source (NYRB) and the audience's professional self-image. The explicit avoidance of robotic or android imagery prevents the image from reducing the argument to "humans vs. machines," which is the opposite of the centaur claim.
