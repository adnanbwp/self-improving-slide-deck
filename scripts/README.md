# scripts/

## Scripts

### generate-image.py

Generates a single image via Fal.ai and saves the binary to
`decks/<deck>/versions/<version>/assets/<output>`.

Idempotent: re-running with the same `--output` path logs a skip and exits 0 —
no duplicate API calls.

Emits a JSON log line to stdout on every run:
`{"service": "fal.ai", "model": "...", "output": "...", "seed": ..., "ts": "..."}`.

## Install dependencies

```
pip install fal-client
```

## Setup

Copy `.env.example` to `.env` and fill in your key:

```
cp .env.example .env
# edit .env and set FAL_KEY=<your key from fal.ai/dashboard>
```

Then export it into your shell before running the script:

```
export $(grep -v '^#' .env | xargs)
```

## Smoke test

Once `FAL_KEY` is set, run:

```
python scripts/generate-image.py \
  --prompt "A child using a tablet, warm illustration style" \
  --deck ai-and-kids \
  --version v1.1.0 \
  --output smoke-test.png \
  --model schnell
```

Expected output (one JSON line):

```json
{"service": "fal.ai", "model": "fal-ai/flux/schnell", "output": "decks/ai-and-kids/versions/v1.1.0/assets/smoke-test.png", "seed": 12345, "ts": "2026-05-26T..."}
```

The file will be at `decks/ai-and-kids/versions/v1.1.0/assets/smoke-test.png`.

## Model aliases

| Alias | Resolves to | Size param |
|---|---|---|
| (default) | `fal-ai/flux-pro/v1.1` | `image_size` |
| `schnell` | `fal-ai/flux/schnell` | `image_size` |
| `ultra` | `fal-ai/flux-pro/v1.1-ultra` | `aspect_ratio` |

## Aspect ratio tokens

For `image_size` models (default, schnell): `landscape_16_9`, `portrait_9_16`,
`square_hd`, `square`, `landscape_4_3`, `portrait_3_4`.

For `ultra`: the script maps `landscape_16_9` to `16:9` automatically.
