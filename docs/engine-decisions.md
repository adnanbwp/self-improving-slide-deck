# Engine Decisions Log

Persistent memory for architectural decisions about the engine itself (not per-deck). When a decision here is revisited, the existing entry must be updated with a superseding entry — not silently changed.

---

## HTML presentation framework — 2026-05-25 | Pax (research) + Adnan (decision)

**What was considered:** Reveal.js, Slidev, Marp, Impress.js, raw HTML+CSS

**What was decided:** Reveal.js

**Why:** Git-native HTML+CSS output. No mandatory build step (serves with `python -m http.server`). Audience variants via CSS swap — one HTML file, one base theme, one per-audience override stylesheet. Speaker notes, fullscreen, offline operation all native. Clean Docker path. Low dependency surface (one JS file). Raw HTML+CSS is a trivial fallback if needed — the exit cost is near zero.

**Options not taken:**
- *Slidev* — Vite + Vue build pipeline is overhead with no benefit when the engine (not a human) is the author. Every deck becomes an npm project. Audience variants require separate builds.
- *Marp* — ceiling is its floor: three built-in themes, minimal animation, no expressive per-deck visual identity. Works for quick technical slides, not controlled brand output.
- *Impress.js* — 3D spatial layout is unmaintainable at scale. No speaker notes. No PDF export. Disqualified.
- *Raw HTML+CSS only* — near-equivalent, but Reveal.js gives fullscreen API, keyboard navigation, and speaker notes for free. The escape hatch to raw HTML+CSS remains trivially available.

**Status:** `Closed`

---

## Specialist roster — initial nine — 2026-05-25 | Larry + Adnan

**What was considered:** myPKA base six (Larry, Nolan, Pax, Penn, Mack, Silas) plus Rex, Vera, Aria. Considered whether Penn and Nolan are needed in the engine context.

**What was decided:** Hire Rex (Logic Auditor), Vera (Adversarial Critic), Aria (Audience Persona Scorer). Penn scoped to PKM-side captures only — not part of engine workflows. Nolan active only when a new specialist is needed; not part of standard improvement cycles. A tenth specialist (Deck Author) identified as a critical gap and hired in the same session.

**Why:** The four-dimensional scoring system requires dedicated specialists per dimension. No existing team member could cover Rex, Vera, or Aria's roles without violating the no-self-marking rule. Penn's journal-writing role is orthogonal to deck production. Nolan's value is episodic (hire-on-demand), not continuous.

**Options not taken:**
- *Larry as deck writer* — violates the iron rule that Larry never executes domain work.
- *Penn repurposed as deck writer* — Penn's competency is journal capture and PKM. Slide deck production is a different craft requiring a different specialist.
- *Adnan as sole author* — would make the engine a reviewer rather than a producer; reduces autonomy and makes the `autonomous` engagement level impossible.

**Status:** `Closed`

---

## Deck Author hire — 2026-05-25 | Rex + Vera (gap identification) + Adnan (decision)

**What was considered:** Whether to hire a Deck Author, or have the engine generate slides programmatically from research briefs, or have Adnan author v1.0.0 with specialists improving it.

**What was decided:** Hire a dedicated Deck Author specialist.

**Why:** The engine's mission requires deck quality that improves across cycles. A named specialist who owns the craft of turning research + argument maps into persuasive slide narrative enforces accountability and maintains a consistent voice across versions. Programmatic generation without a named specialist makes quality ownership diffuse. Adnan-as-first-author is viable but limits the `autonomous` engagement mode.

**Options not taken:**
- *Programmatic generation* — not ruled out as a technique the Deck Author uses, but the role must be named and contracted so someone is accountable for the output quality.
- *Adnan as v1.0.0 author* — deferred for decks in `co-author` engagement mode, where this is natural. Not the default.

**Status:** `Closed` — Deck Author contract pending Pax research brief and Adnan approval.

---

## Aria scoped to scoring only — 2026-05-25 | Vera (gap identification) + Adnan (decision)

**What was considered:** Aria adapts decks for audiences AND scores them (original design) vs. Aria scores only vs. Rex scores audience fit.

**What was decided:** Aria scores only. The Deck Author writes and adapts. Aria evaluates the result.

**Why:** Mission states "scoring is done by different specialists than those who produced the content — no self-marking." Aria adapting and then scoring her own adaptation violates this directly. Rex scoring audience fit is outside Rex's methodology (argument logic ≠ persuasion psychology). Aria scoring what the Deck Author produced is clean.

**Options not taken:**
- *Aria adapts + scores* — direct self-marking violation.
- *Rex scores audience fit* — mismatch between Rex's logic-audit methodology and persuasion-psychology assessment.

**Status:** `Closed`

---

## Disagreement resolution — 2026-05-25 | Vera (gap identification) + Larry (decision)

**What was considered:** Larry resolves disputes internally vs. Larry escalates all disputes to Adnan via PR vs. a specialist hierarchy (e.g. Rex overrules Pax on argument claims).

**What was decided:** Larry documents both positions in the PR summary. Adnan resolves via PR review. Larry does not make content calls.

**Why:** Larry's iron rule prohibits domain execution. Making Larry a content arbitrator violates this. A specialist hierarchy would undermine the independence of the scoring layer. The PR is already the review layer — dispute documentation belongs there.

**Options not taken:**
- *Larry as content arbitrator* — violates iron rule.
- *Specialist hierarchy* — undermines scorer independence.

**Status:** `Closed`
