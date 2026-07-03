"""Fail-open media-API cost telemetry (WS7.2).

emit_cost_span(provider, units, unit_type, model=None, asset_slug=None) computes a dollar
figure from costs.yaml (same dir, or $COSTS_YAML) and emits ONE OTel span to Phoenix
(project `media-costs`). The whole body is wrapped: any failure — missing deps, missing
prices, Phoenix down — returns silently and the TTS/image call proceeds (continuity rule 1).

Canonical copy: ~/projects/template/telemetry/. Vendored copies: tasveer/scripts/,
animated-video/pipeline/, self-improving-slide-deck/scripts/ (brand-kit-style copy,
re-sync from template).
"""
import os
from pathlib import Path

_DEFAULT_ENDPOINT = (
    "http://phoenix:6006/v1/traces" if os.path.exists("/.dockerenv")
    else "https://life-os-vps.tailf48c4d.ts.net:9443/v1/traces"
)


def _price(costs, provider, unit_type, units, model):
    if provider == "elevenlabs" and unit_type == "chars":
        return units / 1000.0 * float(costs["elevenlabs"]["tts_per_1k_chars_usd"])
    if provider == "fal" and unit_type == "images":
        per = costs["fal"].get(model) or costs["fal"]["default_per_image_usd"]
        return units * float(per)
    return None


def emit_cost_span(provider, units, unit_type, model=None, asset_slug=None):
    """Fail-open: never raises, never blocks. Returns computed cost or None."""
    try:
        import yaml
        from opentelemetry import trace
        from opentelemetry.sdk.resources import Resource
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import SimpleSpanProcessor
        from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

        costs_path = os.environ.get("COSTS_YAML") or str(Path(__file__).parent / "costs.yaml")
        costs = yaml.safe_load(open(costs_path))
        cost = _price(costs, provider, unit_type, units, model)
        endpoint = os.environ.get("PHOENIX_OTLP_ENDPOINT", _DEFAULT_ENDPOINT)
        provider_tp = TracerProvider(resource=Resource.create({
            "service.name": "media-costs",
            "openinference.project.name": "media-costs",
        }))
        provider_tp.add_span_processor(
            SimpleSpanProcessor(OTLPSpanExporter(endpoint=endpoint, timeout=5)))
        tracer = provider_tp.get_tracer("cost-span")
        with tracer.start_as_current_span(f"{provider}.{unit_type}") as span:
            span.set_attribute("openinference.span.kind", "TOOL")
            span.set_attribute("cost.provider", provider)
            span.set_attribute("cost.units", units)
            span.set_attribute("cost.unit_type", unit_type)
            if model:
                span.set_attribute("cost.model", model)
            if cost is not None:
                span.set_attribute("cost.usd", round(cost, 6))
            slug = asset_slug or os.environ.get("ASSET_SLUG")
            if slug:
                span.set_attribute("asset_slug", slug)
        provider_tp.force_flush()
        provider_tp.shutdown()
        return cost
    except Exception:
        return None


if __name__ == "__main__":
    # ponytail: assert-based self-check — price math only, no network.
    import yaml as _y
    costs = _y.safe_load(open(Path(__file__).parent / "costs.yaml"))
    assert abs(_price(costs, "elevenlabs", "chars", 1000, None)
               - costs["elevenlabs"]["tts_per_1k_chars_usd"]) < 1e-9
    assert _price(costs, "fal", "images", 2, "fal-ai/flux/schnell") == 0.006
    assert _price(costs, "fal", "images", 1, "unknown-model") == costs["fal"]["default_per_image_usd"]
    assert _price(costs, "other", "x", 1, None) is None
    print("cost_span self-check OK")
