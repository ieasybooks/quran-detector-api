<div align="center">
  <a href="https://pypi.org/project/quran-detector-api" target="_blank"><img src="https://img.shields.io/pypi/v/quran-detector-api?label=PyPI%20Version&color=limegreen" /></a>
  <a href="https://pypi.org/project/quran-detector-api" target="_blank"><img src="https://img.shields.io/pypi/pyversions/quran-detector-api?color=limegreen" /></a>
  <a href="https://pepy.tech/project/quran-detector-api" target="_blank"><img src="https://static.pepy.tech/badge/quran-detector-api" /></a>

  <a href="https://github.com/ieasybooks/quran-detector-api/actions/workflows/kamal-run.yml" target="_blank"><img src="https://github.com/ieasybooks/quran-detector-api/actions/workflows/kamal-run.yml/badge.svg" /></a>
</div>

<div align="center">

  [![ar](https://img.shields.io/badge/lang-ar-brightgreen.svg)](README.md)
  [![en](https://img.shields.io/badge/lang-en-red.svg)](README.en.md)

</div>

# quran-detector-api

Production-friendly **FastAPI** service that exposes the
[`quran-detector`](https://github.com/ieasybooks/quran-detector) Python package over HTTP.

Public URL: https://quran-detector-api.ieasybooks.com/

## OpenAPI / Docs

- OpenAPI: `/openapi.json`
- Swagger UI: `/docs`
- ReDoc: `/redoc`

## Features

- Detect endpoints: `POST /v1/detect`.
- Annotate endpoints: `POST /v1/annotate`.
- Health checks: `/v1/healthz` and `/v1/readyz`.
- Warm startup: initializes the detector engine at startup.
- Explicit request/text limits.
- Optional CORS for direct browser usage.

## Requirements

- Python **3.12+**
- `uv` recommended
- `mise` optional (for local setup matching this repo)

## Quickstart

Requirements: `mise` (Python 3.12) and `uv`.

```bash
cd quran-detector-api
mise trust
mise install
uv sync
uv run quran-detector-api
```

Default listen address: `http://127.0.0.1:8000`

## API

Base path: `/v1`

### Health

- `GET /v1/healthz` → `{"status":"ok"}` (process is up)
- `GET /v1/readyz` → `{"status":"ok"}` (engine initialized)

### Detect

`POST /v1/detect`

Request body:

```json
{
  "text": "string (1..5000 chars)",
  "settings": {
    "find_errors": true,
    "find_missing": true,
    "allowed_error_pct": 0.25,
    "min_match": 3,
    "delimiters": "optional override"
  }
}
```

Response body:

```json
{
  "matches": [
    {
      "surah_name": "الإخلاص",
      "verses": ["قل هو الله احد"],
      "errors": [[]],
      "start_in_text": 0,
      "end_in_text": 4,
      "aya_start": 1,
      "aya_end": 1
    }
  ]
}
```

### Annotate

`POST /v1/annotate`

Request body:

```json
{
  "text": "string (1..5000 chars)",
  "settings": {
    "find_errors": true,
    "find_missing": true,
    "allowed_error_pct": 0.25,
    "min_match": 3,
    "delimiters": "optional override"
  }
}
```

Response body:

```json
{ "annotated_text": "..." }
```

## Limits

- Maximum accepted text length: `5000` characters (enforced).
- Maximum request body size: `QD_API_MAX_BODY_BYTES` (default `65536`).

## Configuration

Environment variables (all optional):

- `QD_API_HOST` (default: `127.0.0.1`)
- `QD_API_PORT` (default: `8000`)
- `QD_API_WORKERS` (default: `1`)
- `QD_API_LOG_LEVEL` (default: `info`)
- `QD_API_CORS_ORIGINS` (default: empty; comma-separated list, or `*`)
- `QD_API_ROOT_PATH` (default: empty; set when serving behind a proxy path prefix)
- `QD_API_DOCS_ENABLED` (default: `true`)
- `QD_API_MAX_TEXT_LENGTH` (default/max: `5000`)
- `QD_API_MAX_BODY_BYTES` (default: `65536`)

## Development

Auto-reload:

```bash
uv run uvicorn quran_detector_api.main:app --reload
```

## Deployment

Run with multiple workers (tune for CPU/core count):

```bash
uv run uvicorn quran_detector_api.main:app --host 0.0.0.0 --port 8000 --workers 2
```

### Docker

Build image:

```bash
docker build -t quran-detector-api .
```

Run:

```bash
docker run --rm -p 8000:8000 quran-detector-api
```

