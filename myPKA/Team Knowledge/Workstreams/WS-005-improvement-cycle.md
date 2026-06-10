# WS-005 — Improvement Cycle

- **Type:** Workstream — recurring multi-agent composition. Runs on every active deck whenever a trigger fires.
- **Owners:** Larry (orchestration), Pax (research sweep), Rex (argument re-audit), Vera (adversarial re-pass), Aria (persuasion re-score), Coda (deck update)
- **References:** [[docs/deck-folder-spec]], [[docs/superpowers/specs/2026-05-25-engine-design]], [[WS-004-bootstrap-deck]], [[WS-006-slide-plan-design-selection]]
- **Trigger:** Weekly cron (default), Adnan manual request, or external process signal (future). Skips decks with `status: archived` or `status: overturned`.

---

## Purpose

Improve an existing deck version using new research, updated argument analysis, and re-scored outputs. Produces a new version (e.g. v1.0.0 → v1.1.0) only when improvement is warranted. Does not produce a PR if scores are flat and no PoV update is needed.

---

## Inputs

| Field | Description |
|---|---|
| `slug` | Deck folder name (e.g. `ai-and-kids`) |
| `current_version` | Read from `decks/<slug>/pov.md` |
| `trigger_type` | `scheduled` \| `manual` \| `external` |
| `engagement_level` | Read from `decks/<slug>/pov.md` — defaults to `autonomous` |

---

## Significance Threshold

Pax evaluates new research against three criteria. All three must be considered together:

1. **Source count** — at least one new independent credible source not present in the prior research brief
2. **Claim impact** — the new finding directly supports, challenges, or could overturn a specific claim in the current deck (not just tangentially related)
3. **Recency** — published or updated after the date of the prior research brief

**Below threshold:** one new source, weakly related to claims, or not more recent than existing sources. Log in `reports/` and stop — no cycle triggered.

**Above threshold:** two or more new independent sources with direct claim impact, or one highly credible source (e.g. peer-reviewed, major institution) with strong claim impact.

**Special rule — AI governance material:** Any finding that directly affects the engine's own governance principles (as documented in aa2brain) surfaces to Adnan for explicit go-ahead regardless of threshold level.

---

## Choreography

### Step 1 — Research Sweep (Pax)

Larry briefs Pax:

> "Research sweep for the `<topic>` deck (current version: `<current_version>`). Prior research brief: `decks/<slug>/research/YYYY-MM-DD-research-brief-vN.md`. Find: (1) new sources published or updated since that brief's date, (2) new developments relevant to the PoV in `decks/<slug>/pov.md`. Assess against the significance threshold in [[WS-005-improvement-cycle]]. Report your finding: threshold met or not, with evidence. If met, provide a new supplementary brief."

### Step 2 — Threshold Check (Larry)

| Condition | Action |
|---|---|
| Below threshold | Larry logs finding in `decks/<slug>/reports/YYYY-MM-DD-research-sweep-vN.md`. Cycle stops. |
| Above threshold + AI governance material | Larry surfaces to Adnan with Pax's finding. Wait for go-ahead before proceeding. |
| Above threshold, non-governance | Proceed autonomously to Step 3. |

### Step 3 — Re-audit (Rex, Vera, Aria — parallel)

Larry briefs all three in the same message, with links to Pax's new research and the current deck version.

**Rex brief:** "Re-audit the argument in `decks/<slug>/versions/<current_version>/canonical.html` against Pax's new research brief `decks/<slug>/research/YYYY-MM-DD-research-brief-vN.md`. Has the new evidence strengthened, weakened, or changed any claims? Updated argument score. File at `decks/<slug>/scorecards/<next_version>-argument.md`."

**Vera brief:** "Re-run adversarial pass on `decks/<slug>/versions/<current_version>/canonical.html` incorporating any new counter-evidence from Pax's research brief. Has the deck's resilience improved or weakened? Updated adversarial score. File at `decks/<slug>/scorecards/<next_version>-adversarial.md`."

**Aria brief (one per active audience):** "Re-score persuasion for `decks/<slug>/versions/<current_version>/<audience>.html` for a `<audience>` audience. Note any changes in emotional resonance, narrative clarity, or CTA strength relative to the prior persuasion scorecard. File at `decks/<slug>/scorecards/<next_version>-persuasion-<audience>.md`."

### Step 4 — Score Delta Check (Larry)

Larry compares all new scorecards against the prior version's scorecards.

| Condition | Action |
|---|---|
| All scores flat AND no PoV update warranted | Log in `reports/`. Cycle stops — no PR. |
| Any score changed OR PoV update warranted | Proceed to Step 5. |

### Step 5 — Slide Plan & Design Selection (WS-006)

Larry runs [[WS-006-slide-plan-design-selection]] with inputs:
- `slug`: `<slug>`
- `argument_map`: `decks/<slug>/reports/YYYY-MM-DD-argument-map-vN.md`
- `research_brief`: `decks/<slug>/research/YYYY-MM-DD-research-brief-vN.md`
- `pov_path`: `decks/<slug>/pov.md`
- `audiences`: active audiences from `pov.md`
- `prior_slide_plan`: `decks/<slug>/reports/YYYY-MM-DD-slide-plan-vN-1.md`

WS-006 applies carry-forward logic: Coda updates only rows where new evidence warrants a change. Design template carries forward from `pov.md` unless Adnan requests a redesign. If the delta has zero `type` and zero `purpose` changes, Larry may proceed without explicit approval. Proceed to Step 5a.

### Step 5a — Deck Update (Coda Pass 2)

Larry briefs Coda:

> "Update `decks/<slug>/versions/<current_version>/` to produce `decks/<slug>/versions/<next_version>/`. Approved slide plan: `decks/<slug>/reports/YYYY-MM-DD-slide-plan-vN.md`. Template system: the deck is on the aha agile system (`shared/templates/aha-agile/`) — build slides from the `t-*` layout catalogue in its README; content budgets and field rules are binding. If `<current_version>` pre-dates the aha agile system (Reveal.js or custom-engine deck), convert it per the conversion playbook in `shared/templates/aha-agile/README.md` as part of this cycle and bump the major version. Write each slide against its row in the slide plan. Update only what the new evidence warrants — do not rewrite slides that carry forward unchanged. Honour all Coda tips from the design proposal. After producing HTML, run the humanizer skill on all modified slide text and speaker notes."

Coda output: `versions/<next_version>/canonical.html` + all active audience variants.

### Step 5b — Image Brief (Iris)

Larry briefs [[Iris]] with links to the updated HTML files produced in Step 5, the research brief, and the argument map. Iris produces `decks/<slug>/image-briefs/YYYY-MM-DD-image-brief-vN.md` — one structured entry per slide that benefits from an image, each with prompt, model recommendation, aspect ratio, style direction, and negative constraints. Mack executes the brief via `scripts/generate-image.py`. Coda wires the generated image paths into the HTML files.

### Step 6 — Humanizer Pass (Coda)

Coda runs the humanizer skill on all modified text content in the updated HTML files. This step is complete when no remaining AI-writing patterns are flagged.

### Step 7 — PR Compilation (Larry)

Larry compiles a GitHub PR following the PR format in [[docs/superpowers/specs/2026-05-25-engine-design]].

Score delta table compares `<current_version>` → `<next_version>` across all four dimensions.

### Step 8 — Review and Merge (Adnan)

Adnan reviews PR → merges → Larry updates `pov.md`:

```yaml
current_version: <next_version>
```

---

## Version Bumping Convention

| Change type | Bump |
|---|---|
| New evidence strengthens or refines existing claims | `v1.0.0 → v1.1.0` (minor) |
| PoV refined (still same core claim, tighter framing) | `v1.1.0 → v1.2.0` (minor) |
| PoV significantly changed (still same topic, different claim) | `v1.2.0 → v2.0.0` (major) |
| New audience variant added | `v1.0.0 → v1.1.0` (minor) |
