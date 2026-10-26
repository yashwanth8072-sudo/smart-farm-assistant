# SMART FARM ASSISTANT

An open-source educational prototype for IoT-based farm monitoring, intrusion-event logging, and soil-moisture-based irrigation recommendations.

> **Status:** prototype / simulation. Hardware drivers and a trained animal-detection model are not included. Sample readings are synthetic, not real farm measurements.

## Features
- FastAPI REST API for sensor readings and intrusion events
- SQLite persistence
- Browser dashboard
- Threshold-based irrigation recommendation
- Sample CSV and JSON data
- Automated API tests
- Architecture, API, and testing documentation

## Requirements
- Python 3.10+
- pip

## Quick start

```bash
git clone https://github.com/yashwanth8072-sudo/smart-farm-assistant.git
cd smart-farm-assistant
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000 for the dashboard and http://127.0.0.1:8000/docs for interactive API docs.

## Run tests

```bash
pytest -q
```

## Seed sample data

```bash
python scripts_seed_data.py
```

## API overview
- `GET /api/health` — service health
- `GET /api/readings` and `POST /api/readings` — sensor readings
- `GET /api/events` and `POST /api/events` — intrusion events
- `GET /api/irrigation/recommendation` — recommendation from latest soil moisture

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md), [`docs/API.md`](docs/API.md), and [`docs/TESTING.md`](docs/TESTING.md).

## Safety
Validate calibration, wireless coverage, weatherproofing, authentication, and electrical/pump safeguards before real deployment. Keep physical actuation disabled until safeguards are tested. Any animal deterrents must be humane and lawful.

## License
MIT — see [`LICENSE`](LICENSE).
