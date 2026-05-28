#!/usr/bin/env python3
"""
generate-image.py — Fal.ai image generation for slide deck assets.

Usage (deck asset):
    python scripts/generate-image.py \
        --prompt "A child using a tablet with a curious expression" \
        --deck ai-and-kids \
        --version v1.1.0 \
        --output hero.png \
        --aspect-ratio landscape_16_9 \
        --model fal-ai/flux-pro/v1.1

Usage (shared/arbitrary path):
    python scripts/generate-image.py \
        --prompt "..." \
        --output-path shared/assets/avatars/larry.png \
        --aspect-ratio square_hd \
        --model ultra

Usage (image-to-image):
    python scripts/generate-image.py \
        --prompt "..." \
        --input-image shared/assets/AdnanAli-Headshot.png \
        --output-path shared/assets/avatars/adnan.png \
        --model fal-ai/nano-banana-2/edit
"""

import argparse
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# Auto-load .env from repo root (no dependency on python-dotenv)
_env_path = Path(__file__).parent.parent / ".env"
if _env_path.exists():
    for _line in _env_path.read_text().splitlines():
        _line = _line.strip()
        if _line and not _line.startswith("#") and "=" in _line:
            _k, _, _v = _line.partition("=")
            os.environ.setdefault(_k.strip(), _v.strip())


# --- Model aliases -----------------------------------------------------------

MODEL_ALIASES = {
    "schnell": "fal-ai/flux/schnell",
    "ultra": "fal-ai/flux-pro/v1.1-ultra",
    "nanobanan2": "fal-ai/nano-banana-2",
    "nanobanan2-edit": "fal-ai/nano-banana-2/edit",
}

ULTRA_MODEL = "fal-ai/flux-pro/v1.1-ultra"

# Models that use `image_size` parameter
IMAGE_SIZE_MODELS = {"fal-ai/flux-pro/v1.1", "fal-ai/flux/schnell", "fal-ai/nano-banana-2", "fal-ai/nano-banana-2/edit"}

# Mapping from landscape_16_9 style to aspect_ratio string for ultra
ASPECT_RATIO_MAP = {
    "landscape_16_9": "16:9",
    "portrait_9_16": "9:16",
    "square_hd": "1:1",
    "square": "1:1",
    "landscape_4_3": "4:3",
    "portrait_3_4": "3:4",
    "landscape_3_2": "3:2",
    "portrait_2_3": "2:3",
}


# --- Helpers -----------------------------------------------------------------

def log(record: dict) -> None:
    """Write a single structured JSON line to stdout."""
    print(json.dumps(record), flush=True)


def resolve_model(raw: str) -> str:
    return MODEL_ALIASES.get(raw, raw)


def build_arguments(model: str, prompt: str, aspect_ratio: str) -> dict:
    args = {"prompt": prompt}
    if model == ULTRA_MODEL:
        mapped = ASPECT_RATIO_MAP.get(aspect_ratio)
        if mapped is None:
            print(
                f"ERROR: unknown aspect_ratio '{aspect_ratio}' for ultra model. "
                f"Known: {list(ASPECT_RATIO_MAP.keys())}",
                file=sys.stderr,
            )
            sys.exit(1)
        args["aspect_ratio"] = mapped
    else:
        args["image_size"] = aspect_ratio
    return args


def download_file(url: str, dest: Path) -> None:
    with urllib.request.urlopen(url) as response:
        dest.write_bytes(response.read())


# --- Main --------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate an image via Fal.ai.")
    parser.add_argument("--prompt", required=True, help="Image generation prompt.")
    parser.add_argument(
        "--aspect-ratio",
        default="landscape_16_9",
        dest="aspect_ratio",
        help="Aspect ratio / image size token (default: landscape_16_9).",
    )
    parser.add_argument("--output", default=None, help="Output filename (e.g. hero.png). Required without --output-path.")
    parser.add_argument("--deck", default=None, help="Deck slug (e.g. ai-and-kids). Required without --output-path.")
    parser.add_argument("--version", default=None, help="Version string (e.g. v1.1.0). Required without --output-path.")
    parser.add_argument(
        "--output-path",
        default=None,
        dest="output_path",
        help="Absolute or repo-relative output path. Overrides --deck/--version/--output when set.",
    )
    parser.add_argument(
        "--model",
        default="fal-ai/flux-pro/v1.1",
        help=(
            "Model ID or alias. Aliases: schnell → fal-ai/flux/schnell, "
            "ultra → fal-ai/flux-pro/v1.1-ultra, "
            "nanobanan2 → fal-ai/nano-banana-2, "
            "nanobanan2-edit → fal-ai/nano-banana-2/edit. "
            "Default: fal-ai/flux-pro/v1.1."
        ),
    )
    parser.add_argument(
        "--input-image",
        default=None,
        dest="input_image",
        help="Path to input image for image-to-image models (absolute or repo-relative).",
    )
    args = parser.parse_args()

    if args.output_path is None and not all([args.deck, args.version, args.output]):
        parser.error("Either --output-path or all of --deck, --version, and --output are required.")

    # --- Validate credentials before any network call -----------------------
    fal_key = os.environ.get("FAL_KEY", "").strip()
    if not fal_key:
        print(
            "ERROR: FAL_KEY environment variable is not set. "
            "Copy .env.example to .env and add your key.",
            file=sys.stderr,
        )
        sys.exit(1)

    model = resolve_model(args.model)

    # --- Resolve output path ------------------------------------------------
    repo_root = Path(__file__).parent.parent
    if args.output_path:
        output_path = Path(args.output_path)
        if not output_path.is_absolute():
            output_path = repo_root / output_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
    else:
        assets_dir = repo_root / "decks" / args.deck / "versions" / args.version / "assets"
        assets_dir.mkdir(parents=True, exist_ok=True)
        output_path = assets_dir / args.output

    try:
        log_output = str(output_path.relative_to(repo_root))
    except ValueError:
        log_output = str(output_path)

    # --- Idempotency check --------------------------------------------------
    if output_path.exists():
        log({
            "service": "fal.ai",
            "model": model,
            "output": log_output,
            "skipped": True,
            "reason": "file already exists",
            "ts": datetime.now(timezone.utc).isoformat(),
        })
        sys.exit(0)

    # --- Import fal_client after env check so the missing-key error is clear -
    try:
        import fal_client  # noqa: PLC0415
    except ImportError:
        print(
            "ERROR: fal-client is not installed. Run: pip install fal-client",
            file=sys.stderr,
        )
        sys.exit(1)

    # --- Upload input image if provided (image-to-image) --------------------
    input_image_url = None
    if args.input_image:
        input_image_path = Path(args.input_image)
        if not input_image_path.is_absolute():
            input_image_path = repo_root / input_image_path
        if not input_image_path.exists():
            print(f"ERROR: input image not found: {input_image_path}", file=sys.stderr)
            sys.exit(1)
        input_image_url = fal_client.upload_file(str(input_image_path))
        log({"event": "input_image_uploaded", "url": input_image_url, "ts": datetime.now(timezone.utc).isoformat()})

    # --- Submit request -----------------------------------------------------
    arguments = build_arguments(model, args.prompt, args.aspect_ratio)
    if input_image_url:
        arguments["image_urls"] = [input_image_url]
    result = fal_client.run(model, arguments=arguments)

    # --- Extract image URL and seed -----------------------------------------
    images = result.get("images") or []
    if not images:
        print(f"ERROR: no images returned from fal.ai. Full response: {result}", file=sys.stderr)
        sys.exit(1)

    image_url = images[0].get("url")
    if not image_url:
        print(f"ERROR: image entry has no url field. Entry: {images[0]}", file=sys.stderr)
        sys.exit(1)

    seed = result.get("seed")

    # --- Download binary to disk (do not store the URL) ---------------------
    download_file(image_url, output_path)

    # --- Emit structured log ------------------------------------------------
    log({
        "service": "fal.ai",
        "model": model,
        "output": log_output,
        "seed": seed,
        "ts": datetime.now(timezone.utc).isoformat(),
    })


if __name__ == "__main__":
    main()
