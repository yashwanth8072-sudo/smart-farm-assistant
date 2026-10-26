# Architecture

## Scope
This repository implements a software-only educational prototype. Real sensors, LoRa gateways, pump relays, and trained computer-vision models require separate integration and field validation.

## Logical data flow

```text
Soil/environment sensors ─┐
Camera/motion detector ────┼─> Edge controller / gateway ─> FastAPI service ─> SQLite
                           │                                      │
LoRa / Wi-Fi / cellular ───┘                                      ├─> Browser dashboard
                                                                  └─> Irrigation advisory
```

## Components
- **Sensors:** soil moisture, temperature, humidity, and optional pH; readings should be calibrated.
- **Intrusion detector:** future camera/motion subsystem; current API stores event reports but does not classify images.
- **Gateway:** future integration point for LoRa nodes and IP connectivity.
- **FastAPI:** validates input models, exposes REST endpoints, and provides OpenAPI documentation.
- **SQLite:** local persistence for prototype readings and events.
- **Dashboard:** static browser UI that fetches API data.
- **Irrigation advisory:** compares latest soil moisture with a user-configurable threshold; it does not actuate a pump.

## Data and trust boundaries
Sensor nodes and browsers are untrusted inputs. Validate ranges and device identifiers. For deployment, add authentication, TLS, rate limits, audit logging, backups, and per-device authorization. Never expose an unauthenticated control endpoint directly to a pump relay.

## Suggested production evolution
1. Add authenticated device ingestion and device provisioning.
2. Introduce a message broker for intermittent LoRa gateway connectivity.
3. Add model versioning and confidence thresholds for image classification.
4. Add alert delivery with retry and acknowledgement.
5. Implement hardware-in-the-loop tests and fail-safe pump control.
6. Evaluate detection precision/recall, false alarms, latency, energy consumption, and water-use outcomes in field trials.
