---
agent_id: larry
session_id: repo-structure-fixed-standalone-git
timestamp: 2026-05-25T09:32:36Z
type: close-session
linked_sops: []
linked_workstreams: []
linked_guidelines: []
---

# Git repo structure corrected — self-improving-slide-deck now standalone

## Context

Continuation of session 3 after the first close. Adnan noticed uncommitted files in the working directory and flagged that each folder under `/home/aali/learning/claude/` should be its own git repo, not tracked by a parent repo.

## What we did

- Larry fixed the parent repo (`/home/aali/learning/claude/`) — created `.gitignore` listing all subfolders (self-improving-slide-deck/, anthropic-managed-agents-tutorial/, claude-video/, lifeOS/, linear/, myPKA/), ran `git rm --cached -r self-improving-slide-deck/` to stop tracking it, committed.
- Larry initialized `self-improving-slide-deck/` as a standalone git repo by cloning the existing GitHub history (`.git` dir) into the working directory — preserving all prior commits without a force push.
- Larry updated `.gitignore` to also exclude `.claude/` and `myPKA/` (which has its own git).
- Larry committed `CLAUDE.md`, `docs/` (adversarial-review-architecture-v1.md, deck-folder-spec.md, engine-decisions.md, mission-and-objectives.md), and the updated `.gitignore` to the standalone repo and pushed to GitHub.
- Local working tree is now clean; `git status` shows nothing to commit.

## Decisions made

- **Each folder under `/home/aali/learning/claude/` is its own standalone git repo.** Parent repo ignores all subfolders via `.gitignore`.
- **`.claude/` and `myPKA/` are gitignored in self-improving-slide-deck.** `.claude/` is local tool config; `myPKA/` has its own git.
- **`docs/` (non-superpowers) is tracked and pushed.** Project reference docs (mission, decisions, specs) belong on the remote alongside `shared/` and `decks/`.

## Insights

- Cloning the GitHub repo's `.git` dir into the working directory is cleaner than `git init` + `git fetch` + `git reset --hard` when you want to adopt an existing remote's history without touching working files.

## Realignments

- **Parent repo was tracking self-improving-slide-deck/ files.** This was an artefact of the project starting inside a parent learning repo. Corrected by untracking and gitignoring.

## Open threads

- [ ] WS-004 bootstrap for AI & Kids not yet triggered — this is the first action for the next session.
- [ ] `shared/branding/logo.svg` is still a placeholder — replace with Adnan's actual mark when available.
- [ ] Teenagers audience deferred to a later improvement cycle (by design).

## Next steps

- Adnan triggers WS-004 bootstrap for AI & Kids when ready.
- Larry briefs Pax to mine aa2brain for existing AI-and-kids research before the external sweep.

## Cross-links

- [[2026-05-25-09-17_larry_engine-infrastructure-built-github-live]] — immediately prior close; full infrastructure build and initial GitHub setup
- [[2026-05-25-larry-adversarial-resolved-team-complete]] — session 2: adversarial objections resolved
