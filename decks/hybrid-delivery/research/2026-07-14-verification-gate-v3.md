---
date: 2026-07-14
author: Pax
purpose: "Verification gate for hybrid-delivery v3.0.0 — primary-source confirmation of load-bearing figures (Rex S5 / brief v4 flags)"
status: complete
---

# Verification Gate — hybrid-delivery v3.0.0

Scope: six items from Larry's brief, primary sources only (WebFetch on actual pages/PDFs; search-engine snippets used only where noted and flagged as such). No claim below rests on model memory.

---

## 1. The 441% PR-review-time figure — **CORRECTION REQUIRED to existing v2.1.0 deck**

**Verdict: VERIFIED — the figure is Faros AI's own telemetry, NOT the DORA 2025 primary report. The current deck's attribution is wrong.**

- Fetched `dora.dev/dora-report-2025` directly: it is a landing page (not the full report); none of 441%, 242.7%, 33.7%, 98%, 54% appear anywhere on it. It links out to a gated PDF download (email-gated via Swarmia/Google Cloud mirrors — could not retrieve the PDF itself; tried `dora.dev/research/2025/dora-report/2025_dora_report.pdf` directly, 404).
- Fetched `faros.ai/blog/key-takeaways-from-the-dora-report-2025` directly: the article's own text distinguishes its two data sources explicitly. Quote: *"In July 2025, Faros released groundbreaking telemetry analysis from over 10,000 developers"* (2025 dataset) and *"Our AI Engineering Report 2026, drawn from two years of telemetry across more than 4,000 teams"* (2026 dataset, later corrected elsewhere in the same piece to "22,000 developers"). The article states plainly: *"Median time in PR review is up 441%, compared to 91% in our 2025 dataset"* — "our" referring to Faros's own telemetry, not DORA's survey. DORA's own contribution is cited separately in the same piece as the adoption-rate finding ("95% of developers now use AI tools").
- Cross-checked against the existing STORM research (`2026-07-13-storm-lens-researcher-economist.md`, R1/R4) and skeptic-lens pass (`2026-07-13-storm-lens-skeptic-historian.md`, S1), both of which independently flagged the same attribution problem before this gate ran — three independent passes now agree.

**Correction needed:** `versions/v2.1.0/canonical.html` line ~84 currently reads *"The 441% PR review time figure is from DORA 2025"* — this is incorrect and should be corrected in the current deck, not just avoided going forward.

**Exact slide-ready attribution string:** `Faros AI, "AI Engineering Report 2026" (22,000 developers, 4,000+ teams) — telemetry, not the DORA survey`

**Confidence: High** on misattribution; **Medium-High** on the 441% figure itself being accurately reported by Faros (single-vendor proprietary telemetry, internally consistent, directionally corroborated by CircleCI/LinearB per the existing STORM pass, but the exact number rests on one commercial vendor).

**Same-item figures, same source, same correction:**
- Incidents per PR +242.7% — Faros 2026 telemetry (same article, same quote). Attribution string: as above.
- Individual output: tasks/dev — Faros 2025 telemetry: **+21%**; Faros 2026 telemetry: **+33.7%** (brief's "21-34%" range is verified, but note these are two different reporting years, not a single range from one dataset — cite the year).
- PRs merged/dev — Faros 2025: **+98%**; Faros 2026: **+16.2%** (brief's "up to 98%" is verified but is the 2025 figure specifically, not current — flag this on-slide if using the bigger number, since the more recent 2026 figure is much smaller).

---

## 2. Scrum.org "From Velocity to Agent Efficiency"

**Verdict: PARTIALLY VERIFIED — body retrieved via reader-proxy (not raw WebFetch, page is JS-gated); core claims confirmed, one claim from the brief (token/compute budgets) NOT found in this specific article.**

- Direct WebFetch of `scrum.org/resources/blog/velocity-agent-efficiency-evidence-based-management-ai-era` returns an empty/JS-shell page (confirmed gated, as flagged in the brief).
- Retrieved via `r.jina.ai` reader proxy (strips JS, renders text) — this got past the gate. Confirmed and quoted directly from the article:
  - **Velocity as vanity metric:** *"Velocity becomes a vanity metric (though it was earlier too)."*
  - **Don't story-point agent work:** not a verbatim standalone sentence, but the article's structural argument and conclusion directly support it: *"Rather than counting story points, organizations should adopt outcome-focused metrics aligned with Evidence-Based Management principles."* And separately: *"Agile has never been about points. It has always been about the sustainable delivery of value."*
  - **EBM as substitute:** *"To maintain Empiricism, we must retire Velocity in favor of metrics that measure the friction between your silicon workforce (Agents) and your carbon workforce (Humans)."* The article's own proposed replacement metrics are named "Agent Efficiency Score (AES)" and "Human-Agent Handoff Time" — not generic EBM language, but explicitly framed as within the EBM/Empiricism tradition.
  - **Token/compute budgets for agent capacity: NOT FOUND.** I searched the retrieved text specifically for "token," "compute budget," "compute cost" — none appear. This is a correction to the brief, which stated Scrum.org "gestures at" token/compute budgets — that claim does not hold for this specific article. I also checked the companion post, "Beyond Velocity Metrics: How to Measure AI-Agile Synchronization" (`scrum.org/resources/blog/beyond-velocity-metrics-how-measure-ai-agile-synchronization`) — same result, no token/compute-budget language found there either.

**Exact slide-ready attribution string:** `Scrum.org, "From Velocity to 'Agent Efficiency'" (2026)`

**Recommended slide treatment:** use the "vanity metric" and "silicon workforce / carbon workforce" quotes verbatim (both confirmed). Drop the token/compute-budget claim from this citation — if the deck wants that idea, source it as the team's own original proposal (which the brief's §Proposals section already frames it as), not as something Scrum.org states.

**Confidence: Medium-High** on the quotes (retrieved via a reader-proxy rather than a direct browser render, so there is a small residual risk of proxy misparsing — recommend a manual spot-check by opening the URL in a browser before the deck goes final, per the brief's own flag).

---

## 3. METR 19% figure and 2026 follow-up caveat

**Verdict: VERIFIED.**

- Fetched `metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/` directly. Exact on-slide-safe sentence: *"When developers are allowed to use AI tools, they take 19% longer to complete issues—a significant slowdown that goes against developer beliefs and expert forecasts."* Study design confirmed: 16 experienced developers, 246 real issues (~2 hrs avg each), RCT (randomized per-task AI allow/disallow), screen-recorded.
- The authors' own caveats on generalizability (worth keeping in reserve for Q&A, not the slide): the paper explicitly does NOT claim AI fails to speed up most developers, or fails in domains other than software — sampling was self-selected, small-N, specific repos.
- Fetched `metr.org/blog/2026-02-24-uplift-update/` directly for the follow-up. Exact selection-bias framing: *"30% to 50% of developers told us that they were choosing not to submit some tasks because they did not want to do them without AI."* METR's own interpretation: *"Together, these effects make it likely that our estimate reported above is a lower-bound on the true productivity effects of AI on these developers."* And explicitly: *"because of the selection effects in our experiment, our data is only very weak evidence for the size of this increase."*

**Exact slide-ready attribution string:** `METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity" (RCT, July 2025)` — cite only this study; if the 2026 follow-up is mentioned at all, caveat it explicitly as "selection-biased per METR's own admission — not a stable re-measurement."

**Confidence: High** (primary source, direct fetch of both posts, RCT design, quotes verbatim).

---

## 4. GitClear figures (refactoring 21%→3.8%, duplication +81%, churn +15%)

**Verdict: PARTIALLY VERIFIED.**

- Fetched `gitclear.com/the_ai_code_quality_maintainability_gap` directly. Confirmed:
  - **Refactoring:** 21% (2022) → 3.8% (2026). GitClear's own definition, as extracted: refactoring is measured as **"the percentage of moved code"** as a share of changed lines (code that was relocated/restructured rather than freshly duplicated).
  - **Duplication:** +81% increase, specifically 40.3 duplicated blocks per million changed lines (2023 baseline) → 73.0 per million changed lines (2026 year-to-date). Definition: **"Duplicated code blocks (regions of five or more consecutive repeated meaningful lines)."**
  - **Sample:** 623 million analyzed changes, 2023-2026 — confirmed this range applies to the whole report ("623 million analyzed changes from 2023-2026, tracking eight quality signals as AI authorship reaches record volume").
  - **Two-week code churn +15%:** figure confirmed present on the page, but **GitClear's precise methodology for this metric was not retrievable** — the definition sits behind the full whitepaper PDF, which is gated behind an email-registration form I could not complete. Treat the +15% figure as confirmed-but-undefined; do not put a specific methodological claim about what counts as "churn" on the slide without the primary definition.

**Exact slide-ready attribution string:** `GitClear, "The AI Code Quality Maintainability Gap" (623M changes, 2023-2026)`

**Confidence: High** on refactoring and duplication figures and definitions (both directly quoted from the primary page); **Medium** on the churn figure (number confirmed, exact definition not obtained — recommend the caption avoid over-specifying what "churn" measures, or drop that one figure if precision is required).

---

## 5. Glean Work AI Index botsitting figures

**Verdict: VERIFIED.**

- Fetched the primary Glean report page directly: `glean.com/work-ai-institute/reports/work-ai-index-report`. Confirmed:
  - **11 hrs/week saved:** *"Workers say AI automation saves them roughly 11 hours a week."*
  - **6.4 hrs/week lost to "botsitting":** *"Workers spend 6.4 hours a week botsitting."*
  - **58% erosion:** not a directly quoted percentage on the page — it is the **derived** figure (6.4 ÷ 11 = 58.2%). The brief's "~58% erosion" framing is a calculation from the two primary figures, not a Glean-stated percentage. Recommend the slide either show the two raw numbers (11 hrs saved, 6.4 hrs lost) and let the ~58% be a visibly-derived callout, or caption it "(derived)".
  - **69% shipping unverified work ("botshitting"):** confirmed verbatim — *"69% of AI users admit to botshitting at work."*
  - **Survey n and geography confirmed:** 6,000 full-time (30+ hrs/week) digital workers — US (n=3,000), UK (n=1,500), Australia (n=1,500); fielded December 2025–January 2026. Co-authored with Stanford, UC Berkeley, Emory, UC Santa Barbara, UNC Charlotte, University College London, University of Notre Dame researchers per the CIO.com secondary coverage (cross-checked, consistent with the primary page).

**Exact slide-ready attribution string:** `Glean Work AI Institute, "Work AI Index" (n=6,000; US/UK/Australia, Dec 2025–Jan 2026)`

**Confidence: High** (primary source directly fetched, exact figures and sample confirmed; only the 58% is a derived-not-stated number, flagged above).

---

## 6. FORGE '26 paper (arxiv 2602.13766) — numeric findings

**Verdict: VERIFIED — full text obtained this pass (previous passes got methodology only; the PDF rendered fully this time).**

Actual numeric findings (previously an unresolved SOURCE GAP in the brief — now closed):

- **Study:** 3 agile teams (21 professionals), a large IT consulting firm, 13 months (Oct 2023–Nov 2024), comparing historical (pre-adoption) vs. research (post-adoption) sprints, using GitHub Copilot + an internal GPT tool. SPACE framework (Satisfaction, Performance, Activity, Communication, Efficiency).
- **Headline finding — the "P-A-E divergence":** team-level **completed story points rose 59.1%** (Case J: 281 → 447) between historical and research periods, and **planned story points rose ≈150%** (447 → 1,155) — statistically significant (planned: p=4.94e-07, Cohen's d=0.49; remaining: p=6.15e-10, d=0.53) — **while developer Activity (committed lines of code) showed no significant change** (p=0.928, ~456K lines across 349 commits). Perceived Efficiency/speed rose (~82% reporting increased speed); Satisfaction was high overall (3.78/5.0 mean) but strongly task-dependent (low for complex integration work — API/ETL/legacy-Kafka tasks under 25-50% positive).
- **Direct relevance to the deck's velocity argument:** this is the closest thing found in the literature to a controlled, real-world confirmation that **story-point throughput can rise sharply even while raw activity stays flat** — i.e., independent empirical support for "construction-output volume and delivered value have decoupled," the deck's central claim (mirrors the Faros individual-output-vs-team-outcome divergence, but from a controlled academic study rather than vendor telemetry — good triangulation pairing).
- **Caveat the authors themselves state and the deck should carry:** the study explicitly cannot fully separate the 59.1% gain from team maturation/project-familiarity effects over the 13-month window (acknowledged limitation), and it is 3 teams at one consulting firm (external validity/selection-bias risk, early-adopter teams). Does not measure "story-point validity" in the sense of whether a point still costs the same effort — it measures throughput and activity divergence, not estimation accuracy per se.

**Exact slide-ready attribution string:** `Tomaz et al., "Impacts of Generative AI on Agile Teams' Productivity" (FORGE '26, arXiv:2602.13766)`

**Confidence: High** (peer-reviewed-track paper — FORGE 2026, 3rd ACM conference — full text obtained and read directly, not a search summary).

---

## Slide-ready attribution table

| Figure | Exact src-line text |
|---|---|
| 441% PR review time increase | `Faros AI, "AI Engineering Report 2026" (22,000 devs, 4,000+ teams) — telemetry, not DORA` |
| Incidents/PR +242.7% | `Faros AI, "AI Engineering Report 2026"` |
| Tasks/dev +21% (2025) / +33.7% (2026) | `Faros AI telemetry — cite year, do not merge into one range` |
| PRs merged/dev +98% (2025) / +16.2% (2026) | `Faros AI telemetry — cite year; 2025's 98% is the larger, older figure` |
| Velocity "vanity metric" / silicon-vs-carbon workforce | `Scrum.org, "From Velocity to 'Agent Efficiency'" (2026)` |
| METR 19% slower (RCT) | `METR, "Measuring the Impact of Early-2025 AI on Experienced OS Developer Productivity" (July 2025 RCT)` |
| Refactoring 21%→3.8%; duplication +81% | `GitClear, "The AI Code Quality Maintainability Gap" (623M changes, 2023-2026)` |
| Two-week churn +15% | `GitClear, "The AI Code Quality Maintainability Gap" — figure confirmed, definition not primary-sourced; caption cautiously or drop` |
| 11 hrs saved / 6.4 hrs botsitting / 69% shipping unverified | `Glean Work AI Institute, "Work AI Index" (n=6,000, US/UK/AU, Dec 2025-Jan 2026)` |
| ~58% erosion | same as above, but label "(derived: 6.4÷11)" — not a Glean-stated percentage |
| Story points +59.1% with flat activity | `Tomaz et al., FORGE '26 (arXiv:2602.13766)` |

---

## Methodology

Search/fetch order: (1) direct WebFetch of every primary URL named in the brief (dora.dev, faros.ai, metr.org ×2, gitclear.com, glean.com, arxiv.org, scrum.org); (2) where a primary page returned a JS-gated shell (scrum.org only), retried via `r.jina.ai` reader-proxy, which rendered readable text — flagged explicitly as a proxy fetch, not a raw browser fetch, with a recommendation for a manual spot-check; (3) for the FORGE '26 PDF, the raw WebFetch tool returned only encoded PDF structure — the underlying binary was recovered and read directly with the Read tool, which parses PDFs natively, yielding full text including all tables; (4) WebSearch used only as a fallback to locate an alternate URL (e.g., a scrum.org search snippet, Google Cloud/Swarmia DORA PDF mirrors) — snippet-only content is marked "search-engine snippet, not fetched" wherever used and was not treated as sufficient on its own (the scrum.org search snippet was superseded by the successful proxy fetch, so no claim rests on snippet-only evidence in the final verdicts above).

## Limitations

- The DORA 2025 primary PDF itself was never obtained (bot/email-gated on all mirrors tried: dora.dev direct link, Google Cloud, Swarmia). This does not block the verdict on item 1, because the correction rests on Faros's own article explicitly distinguishing its telemetry from DORA's survey — but if Adnan wants the DORA report's own figures for any other claim, that gate is still closed and needs a manual download.
- GitClear's precise "two-week churn" methodology remains unconfirmed (gated behind full-whitepaper registration).
- The Scrum.org quotes rest on a reader-proxy fetch, not a raw browser render; functionally reliable but flagged for a manual spot-check before verbatim quoting in a public-facing deck.
- Confidence on "441%" being numerically accurate is capped at Medium-High because it is single-vendor proprietary telemetry, however the misattribution finding (not from DORA) is High confidence regardless of whether the number itself is precisely right.

---

## Addendum — slide 18 figures (M-V2 follow-up)

Scope: two figures on slide 18 (token-budget slide) of hybrid-delivery v3.0.0, flagged by Rex as outside the original six-item gate above. Same discipline: primary sources via direct WebFetch/WebSearch, triangulated, confidence levels stated.

### 7. Claude Code per-developer spend ($150-250/month typical; heavy-shop range)

**Verdict: PARTIALLY VERIFIED — the core figures are Anthropic's own primary-sourced disclosure; the "heavy-automation shops $500-2,000/month" range is NOT an Anthropic figure and should not be attributed to them.**

- Fetched Anthropic's own live documentation directly: `docs.anthropic.com/en/docs/claude-code/costs` (301-redirects to `code.claude.com/docs/en/costs`, same first-party Anthropic property, not gated). Exact quote: *"Across enterprise deployments, the average cost is around \$13 per developer per active day and \$150-250 per developer per month, with costs remaining below \$30 per active day for 90% of users."* This is a primary, first-party source — not a secondary citation of Anthropic.
- Cross-checked against two independent tech-press pieces covering Anthropic's April 2026 update to this same page: `briefs.co` ("Anthropic Just Doubled Its Claude Code Cost Estimate to \$13 a Day," confirms the page previously said ~\$6/day before an April 15, 2026 refresh, and confirms the same \$150-250/month figure) and corroborating coverage on Yahoo Finance/AOL syndicating the same story. All agree on \$13/day average, \$150-250/month, <\$30/day for 90% of users, and that this is Anthropic's own disclosed enterprise-deployment data (not modeled/estimated by a third party).
- **The "$500-2,000/engineer/month heavy-automation shops" range in the original STORM brief (E1) does NOT trace to Anthropic.** Fetched two of the specific secondary blog sources that carry similar-sounding heavy-user figures: `finout.io/blog/claude-code-pricing-2026` states *"Approximate API-equivalent cost is \$300-500/month before caching"* for a "Full-time engineer, Opus-heavy, daily use" scenario — explicitly the article's own calculation, not attributed to Anthropic. `verdent.ai/guides/claude-code-pricing-2026` states *"Estimated API cost: \$20-60+/day → \$400-1,200+/month"* for heavy users — again the article's own estimate, plus one anecdotal case (\$15,000 over 8 months for one developer). Neither source states \$500-2,000, and neither attributes its heavy-user estimate to Anthropic. WebSearch aggregation independently produced yet a third range ("\$500 to \$2,000") when summarizing across several SEO/content-mill pricing-guide sites, but no single primary or first-party source states that specific range — it appears to be an artifact of search-summary aggregation across inconsistent secondary sources, not a real figure with a stable citation.
- The CIO.com and The Register articles originally cited in the STORM brief (E1) as sourcing the Anthropic figures were re-fetched directly for this addendum and **do not, in fact, mention Anthropic, Claude, or Claude Code by name at all** — both are about AI coding agent costs generically, citing Gartner analyst commentary (Nitish Tyagi) with different, vendor-agnostic numbers ("\$20 to \$100 to \$2,000-\$5,000/developer/month," extreme cases to "\$20,000"). The STORM brief's attribution of the \$150-250/\$13-per-day figures to these two articles was **incorrect** — those figures are real and Anthropic's own, but the correct citation is Anthropic's docs page, not CIO.com/The Register (which cover a different, generic industry claim that happens to share the "\$20,000 outlier" flavor).

**Exact slide-ready attribution string:** `Anthropic, Claude Code Docs — "Manage costs effectively" (code.claude.com/docs/en/costs; refreshed April 2026) — $13/dev/active-day avg, $150-250/dev/month typical across enterprise deployments, <$30/day for 90% of users`

**Recommended slide treatment:** keep "$150-250/month" as-is (verified, primary). For the heavy-shop clause, the built slide's current wording — *"heavy shops far more"* (no specific number) — is the right call and needs no correction; it is defensible where a specific "$500-2,000" figure is not. If a specific heavy-user number is wanted later, it would need to be sourced as a third-party estimate (e.g., finout.io or verdent.ai, each with a different range) and clearly labeled as such, not as an Anthropic-disclosed figure.

**Confidence: High** on $13/day, $150-250/month, <$30/day-for-90% (first-party Anthropic doc, corroborated by two independent tech-press pieces covering the same page update). **Low** on any specific "$500-2,000/month heavy shop" figure — no primary or consistent secondary source supports that exact range; treat as unverified if it appears anywhere on the slide (it currently does not — the built deck's hedge language avoids the problem).

---

### 8. Gartner: >40% of agentic AI projects canceled by end of 2027

**Verdict: VERIFIED (via triangulated syndication; Gartner's own site remains bot-gated).**

- Direct WebFetch of the original Gartner URL (`gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027`) again returned **HTTP 403** (bot-blocked) — same result as the prior gate pass; this remains unresolved at the source itself.
- Retrieved a **new, previously untried non-gated syndication** this pass: `predictiveanalyticsworld.com/machinelearningtimes` (Machine Learning Times), fetched directly and successfully. It explicitly headers the piece "Originally published on Gartner, June 25, 2025" and reproduces verbatim: *"Over 40% of agentic AI projects will be canceled by the end of 2027, due to escalating costs, unclear business value or inadequate risk controls."*
- Cross-checked against **Gartner's own official X/Twitter account** (`x.com/Gartner_inc/status/1937674605193220161`), which posted the identical headline: *"Gartner Newsroom: Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027 #GartnerNewsroom"* — this is Gartner's own first-party channel confirming the release is genuine and dated correctly, even though the newsroom page itself is bot-gated.
- HPCwire syndication (already cited in the original STORM pass) was re-attempted directly this pass and returned HTTP 403 as well (previously it had been accessible via search-snippet only) — do not rely on HPCwire as a directly-fetched source going forward; treat it as search-snippet-corroborated only.
- Net: three independent points of confirmation now line up on the exact wording — (a) predictiveanalyticsworld.com's direct verbatim republication with explicit "originally published on Gartner" attribution, (b) Gartner's own X account posting the identical headline, (c) the original STORM pass's HPCwire/AgentMarketCap search-snippet corroboration. No single source is the gated primary page itself, but three independent channels (one of them Gartner's own account) agree on identical wording, which is a stronger triangulation than the prior gate pass had.

**Exact prediction wording confirmed:** *"Over 40% of agentic AI projects will be canceled by the end of 2027, due to escalating costs, unclear business value or inadequate risk controls."* — issued by Gartner, June 25, 2025.

**Exact slide-ready attribution string:** `Gartner, "Over 40% of Agentic AI Projects Will Be Canceled by End of 2027" (press release, June 25, 2025) — cost, unclear business value, inadequate risk controls; gartner.com bot-gated, verified via Gartner's own X account + Machine Learning Times verbatim republication`

**Recommended slide treatment:** the built slide's wording — *"Gartner expects >40% of agentic projects canceled by end-2027"* — is an accurate compression of the verified quote and needs no correction. Slide 32's paraphrase — *"More than 40% of agentic deployments predicted to be decommissioned by end-2027 on uncontrolled cost, unclear value, or governance failures"* — is a reasonable paraphrase (not verbatim: "deployments"/"decommissioned"/"governance failures" vs. the original "projects"/"canceled"/"inadequate risk controls") but does not misstate the finding; if verbatim precision is wanted for a skeptical audience, swap in the exact wording above.

**Confidence: Medium-High** (unchanged from the original gate — the primary page itself is still unobtained, but corroboration strengthened from two secondary syndications to three, including Gartner's own first-party social account).

---

## Addendum methodology

Search/fetch order: (1) direct WebFetch of Anthropic's own docs page (docs.anthropic.com/en/docs/claude-code/costs, followed 301 redirect to code.claude.com/docs/en/costs) — succeeded, first-party source; (2) direct WebFetch retry of the original Gartner press-release URL — still 403; (3) WebSearch to locate a new non-gated syndication of the Gartner release, then direct WebFetch of that syndication (predictiveanalyticsworld.com) — succeeded; (4) direct WebFetch of the two secondary press articles (CIO.com, The Register) originally cited in the STORM brief for the Anthropic spend figures, to check whether they actually support the attribution — they do not (they don't mention Anthropic/Claude at all); (5) direct WebFetch of two SEO/blog pricing guides (finout.io, verdent.ai) to check whether the "$500-2,000 heavy shop" figure has any traceable source — neither supports that specific range, and neither attributes its own estimate to Anthropic.

## Addendum limitations

- Gartner's newsroom page remains fully bot-gated on every URL tried across both gate passes (gartner.com direct, HPCwire direct-refetch). The verdict rests on triangulated syndication plus Gartner's own social account, not the primary page itself — if a fully primary citation is required (e.g., for a skeptical client audience), this would need a manual, human-browser retrieval of the Gartner page.
- The exact provenance of the "$500-2,000/month heavy-automation shop" figure that appeared in the original STORM brief (E1) could not be traced to any single consistent source — it appears to be a search-aggregation artifact rather than a real, citable figure. This is a correction to the STORM brief's E1 entry, not just a gap: the STORM brief should not be treated as having verified that specific sub-range.
- Did not re-verify the "$234B enterprise application software spend at risk" Gartner figure mentioned in the STORM brief (E1) — out of scope for this addendum (not one of the two flagged slide-18 figures).
