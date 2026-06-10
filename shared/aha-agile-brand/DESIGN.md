---
name: Aha Agile
colors:
  surface: '#131410'
  surface-dim: '#131410'
  surface-bright: '#3a3935'
  surface-container-lowest: '#0e0e0b'
  surface-container-low: '#1c1c18'
  surface-container: '#20201c'
  surface-container-high: '#2a2a26'
  surface-container-highest: '#353530'
  on-surface: '#e5e2db'
  on-surface-variant: '#e2bfb4'
  inverse-surface: '#e5e2db'
  inverse-on-surface: '#31312c'
  outline: '#a98a80'
  outline-variant: '#5a4139'
  surface-tint: '#ffb59d'
  primary: '#ffb59d'
  on-primary: '#5d1800'
  primary-container: '#f4612c'
  on-primary-container: '#511400'
  inverse-primary: '#ac3400'
  secondary: '#cec6b3'
  on-secondary: '#343023'
  secondary-container: '#4b4738'
  on-secondary-container: '#bcb5a3'
  tertiary: '#cac6c1'
  on-tertiary: '#32302d'
  tertiary-container: '#93908c'
  on-tertiary-container: '#2b2a26'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbd0'
  primary-fixed-dim: '#ffb59d'
  on-primary-fixed: '#390b00'
  on-primary-fixed-variant: '#832600'
  secondary-fixed: '#eae2cf'
  secondary-fixed-dim: '#cec6b3'
  on-secondary-fixed: '#1f1b10'
  on-secondary-fixed-variant: '#4b4738'
  tertiary-fixed: '#e6e2dc'
  tertiary-fixed-dim: '#cac6c1'
  on-tertiary-fixed: '#1d1b18'
  on-tertiary-fixed-variant: '#484743'
  background: '#131410'
  on-background: '#e5e2db'
  surface-variant: '#353530'
typography:
  mega-display:
    fontFamily: Archivo
    fontSize: 180px
    fontWeight: '900'
    lineHeight: '0.78'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Archivo
    fontSize: 90px
    fontWeight: '900'
    lineHeight: '0.84'
    letterSpacing: -0.04em
  headline-lg-mobile:
    fontFamily: Archivo
    fontSize: 56px
    fontWeight: '900'
    lineHeight: '0.88'
    letterSpacing: -0.03em
  section-h2:
    fontFamily: Archivo
    fontSize: 32px
    fontWeight: '900'
    lineHeight: '1.1'
  body-mono:
    fontFamily: Space Mono
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.55'
  label-caps:
    fontFamily: Space Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.2em
  meta-small:
    fontFamily: Space Mono
    fontSize: 10px
    fontWeight: '400'
    lineHeight: '1.4'
spacing:
  micro: 4px
  small: 8px
  standard: 16px
  gutter: 24px
  section: 64px
  hero: 140px
---

## Brand & Style

The design system is rooted in a **Swiss-Brutalist** and editorial philosophy. It is defined by a "State it, then stop" approach—prioritizing brevity, clarity, and intentional restraint. The visual narrative is dry, deadpan, and "unbothered," evoking the atmosphere of a high-end independent architecture or design publication.

The aesthetic relies on high-contrast duotone fields, massive typographic scales, and heavy whitespace. It rejects unnecessary decoration in favor of raw structural elements, like hard horizontal seams and "redaction bars" that serve as rhythmic markers rather than masks. The overall tone is professional, authoritative, and avant-garde.

## Colors

The palette is built on a "Field Locking" logic, now optimized for a high-impact **dark mode** environment. Layouts are split by hard edges between primary fields, creating a nocturnal editorial feel.

- **Burnt Orange & Ink**: In this dark-themed iteration, the deep "Ink" tones serve as the primary canvas, with "Burnt Orange" providing aggressive, high-visibility accents and structural seams.
- **Paper & Bone**: These lighter tones are now reserved for high-contrast typography, inverse structural elements, and specific UI accents that need to "pop" against the dark background.
- **Tint Logic**: `orange-tint` is used exclusively on `orange` backgrounds. `paper-tint` is used exclusively on `paper` backgrounds. This maintains tonal purity within each field even in a dark context.

## Typography

Typography is the primary engine of the design system, characterized by the tension between a heavy, tight-leading Grotesque and a dry, technical Monospace.

- **Archivo (Black/900)**: Reserved for headlines and oversized background numerals. It must be used large. Leading should be extremely tight to create a "blocky" text effect. In dark mode, these blocks often appear as high-contrast "knock-out" text.
- **Space Mono**: Used for all reading copy, labels, and metadata. 
- **Formatting**: Use all-caps with high tracking for labels and kickers. Use italics for annotations and "asides" only. Avoid using Archivo for any body text.

## Layout & Spacing

The layout treats the screen like a physical poster or an editorial spread. It follows a **fixed grid** philosophy with a maximum content width of 1080px.

- **Seams**: Use hard horizontal divisions between background colors.
- **Bleed**: Large display numerals should intentionally bleed off the edges of containers or the screen.
- **Whitespace**: Space is used as a functional element to isolate statements. 
- **Breakpoints**: 
  - **Desktop**: 12-column grid with 48px margins.
  - **Mobile**: Single-column stack with 24px margins. Typography scales fluently using clamp functions to maintain impact across devices.

## Elevation & Depth

This system is predominantly flat. Hierarchy is created through color blocking and layering rather than shadows.

- **Tonal Layers**: Use the dark `background` and `surface` variables as the base backdrop to ground the "poster" fields (Orange/Ink).
- **Glassmorphism**: Limited to interactive controls. Use a `control-glass` background with a 4px backdrop blur to distinguish UI elements from the editorial content. This is particularly effective in dark mode to suggest depth.
- **Texture**: Apply a subtle SVG "Paper Grain" turbulence filter to all primary fields to create a tactile, archival feel, even on dark surfaces.
- **Shadows**: Shadows are discouraged, except for the "Badge" or the primary poster element to create a slight lift from the backdrop.

## Shapes

The primary layout and structural components use **sharp (0px)** corners to reinforce the brutalist aesthetic. 

Controlled roundedness is used only for specific functional motifs:
- **Redaction Bars**: 7px radius.
- **UI Controls**: 22px radius.
- **The Badge/Pills**: Full pill-shape (999px).

## Components

- **The Badge**: A circular dark disc with a "Bone" hairline ring. It contains the central brand mark.
- **Redaction Bars**: Rounded blocks (`7px` radius) used in `orange-tint` or `paper-tint`. These are used to create visual rhythm or horizontal rules.
- **Buttons & Controls**: Circular or highly rounded surfaces using the `control-glass` style. Icons should be 20px centered in a 44px container.
- **Input Fields**: Monospace-heavy, defined by a `1.5px` high-contrast border (hairline) at the bottom or as a full ghost-border.
- **Cards**: Flat containers with 0px radius. Use "Bone" or "Ink" hairlines for separation.
- **Annotations**: Technical metadata labels in all-caps Space Mono, occasionally paired with hand-drawn SVG arrows for an "editorial markup" feel.