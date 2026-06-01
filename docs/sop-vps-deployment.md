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
