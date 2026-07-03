# SOP: VPS Slide Deck Deployment

## Overview

Slides are served by an nginx container (`slides-hosting-slides-1`) on the VPS at `178.105.51.174:8080`. The container mounts `/root/slides → /usr/share/nginx/html`.

Files are pushed via `scripts/push.py`.

---

## What Gets Pushed

| Source | Destination | Script step |
|---|---|---|
| `shared/` | `/root/slides/shared/` | Step 1 |
| `decks/{slug}/theme/` | `/root/slides/decks/{slug}/theme/` | Step 2 |
| `decks/{slug}/assets/` | `/root/slides/decks/{slug}/assets/` | Step 2b |
| `decks/{slug}/versions/{current}/` | `/root/slides/decks/{slug}/versions/{current}/` | Step 3 |
| Other-version `assets/` | `/root/slides/decks/{slug}/versions/{v}/assets/` | Step 3b |
| Thumbnail PNG | `/root/slides/decks/{slug}/thumbnail.png` | Step 4 |
| `hosting/index.html` | `/root/slides/index.html` | Step 6 |

**Push command:**
```bash
cd /home/aali/learning/claude/self-improving-slide-deck
python3 scripts/push.py
```

---

## HTML Path Assumptions

From `versions/v1.x.x/canonical.html`:

| Asset | Relative path | Resolves to |
|---|---|---|
| Deck images/diagrams | `../../assets/images/` | `decks/{slug}/assets/images/` |
| Deck diagrams | `../../assets/diagrams/` | `decks/{slug}/assets/diagrams/` |
| Theme CSS | `../../theme/{name}.css` | `decks/{slug}/theme/` |
| Shared lib (reset, reveal) | `../../../../shared/lib/` | `shared/lib/` |
| Shared avatars | `../../../../shared/assets/avatars/` | `shared/assets/avatars/` |

---

## Diagnosing Image/Style Issues

**Images not showing:**
1. SSH in: `ssh root@178.105.51.174`
2. Check: `ls /root/slides/decks/{slug}/assets/` — if missing, the deck-level assets weren't pushed
3. Fix: `rsync -az decks/{slug}/assets/ root@178.105.51.174:/root/slides/decks/{slug}/assets/`

**Fonts or styling broken (wrong font-family, sizes):**
1. Check: `ls /root/slides/decks/{slug}/theme/` — if missing, theme wasn't pushed
2. Fix: `rsync -az decks/{slug}/theme/ root@178.105.51.174:/root/slides/decks/{slug}/theme/`

**Quick full re-push for one deck:**
```bash
# From repo root — re-run push.py (it's idempotent)
python3 scripts/push.py
```

---

## Container / Port

| Detail | Value |
|---|---|
| Container | `slides-hosting-slides-1` |
| Host port | `8080` |
| Mount | `/root/slides → /usr/share/nginx/html` |
| Gallery URL | `http://178.105.51.174:8080/` |

---

## Known Past Issues

- **2026-06-01**: `decks/{slug}/assets/` was never synced by push.py — images 404'd. Fixed in commit `2248b7b`.
- **2026-06-01**: `decks/{slug}/theme/` was not on VPS (likely pushed before that step was added) — fonts and colors fell back to browser defaults.
- **2026-07-03**: a `portable.html` placed in `versions/{version}/` got picked up by `push.py`'s variant discovery and rendered as a broken gallery tile (name/version on one card, thumbnail-less "portable" link on another). **Rule: the portable build lives at the deck root** (`decks/{slug}/{slug}-vX.Y.Z-portable.html`), never in `versions/`. It's a download-only artifact — `push.py` deploys only `versions/{current}/` + `shared/`, so the deck-root portable never touches the gallery.
- **2026-07-03**: `pov.md` `current_version` was stale (`v0.1.0` while the deck was built at `v1.0.0`) — `push.py` skips a deck whose `current_version` dir doesn't exist. **Sync `pov.md current_version` to the actual `versions/` dir before every push.**
- **2026-07-03**: `find_thumbnail()` didn't match the default `slide-01.png` name, so the gallery card showed a placeholder. **Name the thumbnail `{version}*canonical*slide1*.png`** under `decks/{slug}/screenshots/` (or the repo-root `screenshots/`), e.g. `v1.0.0-canonical-slide1.png`, so it's found.
