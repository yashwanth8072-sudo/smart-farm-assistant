"""Insert a few synthetic demo records into the local SQLite database."""
from datetime import datetime, timezone
from app import db

def main():
    db.init_db()
    now = datetime.now(timezone.utc).isoformat()
    samples = [
        {"device_id":"soil-node-01","soil_moisture":27.5,"temperature_c":29.2,"humidity_pct":64.0,"ph":6.4,"timestamp":now},
        {"device_id":"soil-node-02","soil_moisture":38.0,"temperature_c":28.4,"humidity_pct":67.0,"ph":6.6,"timestamp":now},
    ]
    for sample in samples: db.add_reading(sample)
    db.add_event({"device_id":"gate-cam-01","event_type":"possible_animal_intrusion","confidence":0.82,"zone":"north-boundary","timestamp":now})
    print("Inserted synthetic demo readings and event.")

if __name__ == '__main__': main()
