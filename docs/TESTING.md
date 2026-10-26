# Testing

## Run the suite

```bash
pip install -r requirements.txt
pytest -q
```

## Current coverage goals
- Health endpoint responds successfully.
- Reading ingestion validates and persists a sensor reading.
- Out-of-range sensor values are rejected.
- Intrusion event ingestion persists event details.
- Irrigation recommendation changes when moisture is below the configured threshold.

The database path can be overridden with `SFA_DB_PATH` to isolate test data. Tests use a temporary database.

## Before field deployment
Add tests for malformed device messages, duplicate/out-of-order timestamps, sensor dropout, gateway reconnects, notification retries, database recovery, and pump safety interlocks. Test camera models using a labelled dataset and report precision, recall, and false-positive rate across lighting and weather conditions.
