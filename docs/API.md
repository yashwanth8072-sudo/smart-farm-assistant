# API Reference

Base URL for local development: `http://127.0.0.1:8000`. Interactive schema: `/docs`.

## `GET /api/health`
Returns service status and prototype mode.

## `GET /api/readings?limit=50`
Returns recent readings newest-first. `limit` must be 1–500.

## `POST /api/readings`
Example JSON:
```json
{"device_id":"soil-node-01","soil_moisture":27.5,"temperature_c":29.2,"humidity_pct":64,"ph":6.4}
```
Moisture and humidity are percentages; pH is optional. Values are range-validated.

## `GET /api/events?limit=50`
Returns recent intrusion-event reports.

## `POST /api/events`
Example JSON:
```json
{"device_id":"gate-cam-01","event_type":"possible_animal_intrusion","confidence":0.82,"zone":"north-boundary"}
```
`confidence` is optional and between 0 and 1. It is supplied by a caller; this API does not infer it from images.

## `GET /api/irrigation/recommendation?threshold=30`
Compares the latest soil-moisture percentage with the threshold. Returns an advisory recommendation only; no pump is activated. If no readings exist, the response is `no_data`.

## Production warning
The prototype has no authentication or transport encryption. Do not expose it publicly or connect it directly to physical equipment without adding appropriate safeguards.
