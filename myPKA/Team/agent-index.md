# Team - Agent Index

Routing table for the six specialists shipped on day one. Larry reads this on every request to decide who handles what.

| Specialist | Role | Folder | Routes to them when |
|---|---|---|---|
| Larry | Orchestrator, Librarian, Session-Log Author | [[Team/Larry - Orchestrator/AGENTS]] | Every request lands here first. Larry never executes domain work; he routes, then synthesizes. |
| Nolan | HR | [[Team/Nolan - HR/AGENTS]] | User wants to hire a new specialist, retire one, or audit team hygiene. Default owner of [[SOP-001-how-to-add-a-new-specialist]]. |
| Pax | Researcher | [[Team/Pax - Researcher/AGENTS]] | User asks a question that needs cross-source verification, fact-checking, or structured intelligence. |
| Penn | Journal Writer | [[Team/Penn - Journal Writer/AGENTS]] | User shares thoughts, screenshots, voice notes, photos, or anything that needs to land in the Journal or PKM. See [[WS-001-daily-journaling]]. |
| Mack | Automation Specialist | [[Team/Mack - Automation Specialist/AGENTS]] | API integrations, MCP servers, webhooks, OAuth flows, automation scripts. Connection layer for external imports — fetches the bytes, hands off to Silas. Wires up external image generators when local image-gen isn't available. |
| Silas | Database Architect | [[Team/Silas - Database Architect/AGENTS]] | External knowledge imports — primary executor of [[WS-002-import-external-knowledge-base]]. Default owner of [[SOP-002-convert-mypka-to-sqlite]]. Frontmatter integrity audits, schema drift, GL-002 compliance. |
| Coda | Deck Author | [[Team/Coda - Deck Author/AGENTS]] | Deck version needs to be produced or updated from Pax's research brief and Rex's argument map; audience variants needed; final production step before the PR. |
| Rex | Logic Auditor | [[Team/Rex - Logic Auditor/AGENTS]] | Deck argument score needed; gap, non-sequitur, or missing warrant suspected; Definition of Done audit gate. |
| Vera | Adversarial Critic | [[Team/Vera - Adversarial Critic/AGENTS]] | Deck adversarial score needed; pre-mortem or red-team pass on an argument or architecture decision; Definition of Done audit gate. |
| Aria | Audience Persona & Narrative Specialist | [[Team/Aria - Audience Persona/AGENTS]] | Narrative spine needed before the slide plan (`/tactics` SHAPE); deck narrative or persuasion score needed; new audience version being created; CTA needs definition; Definition of Done audit gate. |
| Iris | Image Prompt Specialist | [[Team/Iris - Image Prompt Specialist/AGENTS]] | Deck needs an image brief after Coda produces HTML slides; research brief and argument map are on file; Mack needs structured prompts to execute via Fal.ai. |

## Bootstrap rule

If this table shrinks below 3 rows, Larry switches to Bootstrap Mode and prompts the user to hire replacements via Nolan.

## Adding a new specialist

Follow [[SOP-001-how-to-add-a-new-specialist]]. Nolan owns this procedure.
