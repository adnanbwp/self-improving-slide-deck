#!/usr/bin/env python3
"""Push latest slide deck versions to VPS and regenerate the gallery index."""

import re
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
VPS = "root@178.105.51.174"
REMOTE_DIR = "/root/slides"


# ── helpers ──────────────────────────────────────────────────────────────────

def parse_pov(pov_path: Path) -> dict:
    text = pov_path.read_text()
    def field(key):
        m = re.search(rf'^{key}:\s*(.+)$', text, re.MULTILINE)
        return m.group(1).strip() if m else None
    return {'topic': field('topic'), 'version': field('current_version')}


def rsync(src: str, dst: str, delete=False):
    cmd = ['rsync', '-az', '--progress']
    if delete:
        cmd.append('--delete')
    cmd += [src, dst]
    subprocess.run(cmd, check=True)


def find_thumbnail(deck_dir: Path, version: str) -> Path | None:
    """Return first matching screenshot for the deck's latest version."""
    search_dirs = [
        PROJECT_ROOT / 'screenshots',
        deck_dir / 'screenshots',
    ]
    for d in search_dirs:
        if not d.exists():
            continue
        for pattern in [f'{version}*canonical*slide1*.png', f'{version}*.png']:
            hits = sorted(d.glob(pattern))
            if hits:
                return hits[0]
    return None


# ── index.html generation ────────────────────────────────────────────────────

def render_card(slug: str, topic: str, version: str, has_thumb: bool, variants: list[str]) -> str:
    thumb_html = (
        f'<img src="decks/{slug}/thumbnail.png" alt="{topic} opening slide" loading="lazy">'
        if has_thumb else
        '<div class="no-thumb"></div>'
    )
    variant_links = ''.join(
        f'<a href="decks/{slug}/versions/{version}/{v}.html" '
        f'class="variant" onclick="event.stopPropagation()">{v}</a>'
        for v in variants if v != 'canonical'
    )
    variants_block = f'<div class="variants">{variant_links}</div>' if variant_links else ''
    return f'''\
    <a class="card" href="decks/{slug}/versions/{version}/canonical.html">
      <div class="thumb">{thumb_html}</div>
      <div class="card-body">
        <h2>{topic}</h2>
        <span class="badge">{version}</span>
        {variants_block}
      </div>
    </a>'''


def generate_index(decks: list[dict]) -> str:
    cards = '\n'.join(render_card(**d) for d in decks)
    return f'''\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Slide Decks</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600;700&family=Barlow:wght@400;500&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{
      --bg: #0d0d0d;
      --surface: #1a1a1a;
      --border: #2a2a2a;
      --text: #e8e8e8;
      --muted: #888;
      --accent: oklch(65% 0.18 160);
    }}
    body {{
      background: var(--bg);
      color: var(--text);
      font-family: 'Barlow', sans-serif;
      min-height: 100vh;
      padding: 2rem;
    }}
    header {{
      max-width: 1200px;
      margin: 0 auto 2.5rem;
      border-bottom: 1px solid var(--border);
      padding-bottom: 1rem;
    }}
    header h1 {{
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 2rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      color: var(--accent);
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 1.5rem;
      max-width: 1200px;
      margin: 0 auto;
    }}
    .card {{
      display: flex;
      flex-direction: column;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 4px;
      text-decoration: none;
      color: inherit;
      overflow: hidden;
      transition: border-color 0.15s, transform 0.15s;
    }}
    .card:hover {{
      border-color: var(--accent);
      transform: translateY(-2px);
    }}
    .thumb {{ aspect-ratio: 16/9; overflow: hidden; background: #111; }}
    .thumb img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}
    .no-thumb {{ width: 100%; height: 100%; background: #111;
                  display: flex; align-items: center; justify-content: center; }}
    .no-thumb::after {{ content: '\\25B6'; font-size: 2rem; color: var(--border); }}
    .card-body {{ padding: 1rem 1.25rem 1.25rem; display: flex; flex-direction: column; gap: 0.5rem; }}
    .card-body h2 {{
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 1.3rem;
      font-weight: 700;
      letter-spacing: 0.02em;
      line-height: 1.2;
    }}
    .badge {{
      font-size: 0.72rem;
      font-family: monospace;
      background: var(--bg);
      border: 1px solid var(--border);
      color: var(--muted);
      padding: 0.2em 0.5em;
      border-radius: 2px;
      align-self: flex-start;
    }}
    .variants {{ display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.25rem; }}
    .variant {{
      font-size: 0.75rem;
      color: var(--accent);
      border: 1px solid var(--accent);
      padding: 0.2em 0.6em;
      border-radius: 2px;
      text-decoration: none;
      text-transform: capitalize;
    }}
    .variant:hover {{ background: var(--accent); color: #000; }}
  </style>
</head>
<body>
  <header><h1>Slide Decks</h1></header>
  <main class="grid">
{cards}
  </main>
</body>
</html>
'''


# ── main ─────────────────────────────────────────────────────────────────────

def main():
    decks_dir = PROJECT_ROOT / 'decks'
    deck_slugs = sorted(p.name for p in decks_dir.iterdir() if p.is_dir())

    if not deck_slugs:
        print("No decks found in decks/", file=sys.stderr)
        sys.exit(1)

    # 1. Sync shared assets
    print("→ Syncing shared/")
    rsync(str(PROJECT_ROOT / 'shared') + '/', f'{VPS}:{REMOTE_DIR}/shared/', delete=True)

    deck_data = []

    for slug in deck_slugs:
        deck_dir = decks_dir / slug
        pov_path = deck_dir / 'pov.md'

        if not pov_path.exists():
            print(f"  skip {slug}: no pov.md")
            continue

        info = parse_pov(pov_path)
        if not info['version'] or not info['topic']:
            print(f"  skip {slug}: missing topic or current_version in pov.md")
            continue

        version = info['version']
        version_dir = deck_dir / 'versions' / version

        if not version_dir.exists():
            print(f"  skip {slug}: version dir versions/{version}/ not found")
            continue

        print(f"→ Pushing {slug} {version}")

        # Ensure remote deck directory exists before rsyncing into subdirs
        subprocess.run(
            ['ssh', VPS, f'mkdir -p {REMOTE_DIR}/decks/{slug}/versions'],
            check=True,
        )

        # 2. Sync deck theme
        theme_dir = deck_dir / 'theme'
        if theme_dir.exists():
            rsync(str(theme_dir) + '/', f'{VPS}:{REMOTE_DIR}/decks/{slug}/theme/')

        # 3. Sync latest version folder only
        rsync(str(version_dir) + '/', f'{VPS}:{REMOTE_DIR}/decks/{slug}/versions/{version}/', delete=True)

        # 3b. Sync assets from all versions — HTML may reference sibling version assets
        #     via relative paths like ../v1.1.0/assets/
        for v_dir in sorted((deck_dir / 'versions').iterdir()):
            if v_dir == version_dir or not v_dir.is_dir():
                continue
            assets_dir = v_dir / 'assets'
            if assets_dir.exists() and any(assets_dir.iterdir()):
                subprocess.run(
                    ['ssh', VPS, f'mkdir -p {REMOTE_DIR}/decks/{slug}/versions/{v_dir.name}/assets'],
                    check=True,
                )
                rsync(str(assets_dir) + '/', f'{VPS}:{REMOTE_DIR}/decks/{slug}/versions/{v_dir.name}/assets/')

        # 4. Upload thumbnail if found
        thumb = find_thumbnail(deck_dir, version)
        has_thumb = False
        if thumb:
            print(f"   thumbnail: {thumb.name}")
            subprocess.run(
                ['scp', str(thumb), f'{VPS}:{REMOTE_DIR}/decks/{slug}/thumbnail.png'],
                check=True,
            )
            has_thumb = True
        else:
            print(f"   no thumbnail found for {slug} {version} (card will show placeholder)")

        # 5. Discover audience variants in this version
        variants = sorted(
            p.stem for p in version_dir.glob('*.html')
            if p.stem != 'canonical'
        )
        variants = ['canonical'] + variants

        deck_data.append({
            'slug': slug,
            'topic': info['topic'],
            'version': version,
            'has_thumb': has_thumb,
            'variants': variants,
        })

    if not deck_data:
        print("No decks were pushed.", file=sys.stderr)
        sys.exit(1)

    # 6. Generate and upload index.html
    print("→ Generating index.html")
    index_html = generate_index(deck_data)
    index_local = PROJECT_ROOT / 'hosting' / 'index.html'
    index_local.write_text(index_html)
    subprocess.run(
        ['scp', str(index_local), f'{VPS}:{REMOTE_DIR}/index.html'],
        check=True,
    )
    index_local.unlink()

    print(f"\n✓ Done. Open: http://178.105.51.174:8080/")


if __name__ == '__main__':
    main()
