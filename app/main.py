from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from pathlib import Path
from . import db
from .models import ReadingIn, EventIn

app = FastAPI(title="SMART FARM ASSISTANT API", version="0.1.0", description="Educational prototype; sample values may be simulated.")

@app.on_event("startup")
def startup(): db.init_db()

@app.get("/", response_class=HTMLResponse)
def dashboard():
    return (Path(__file__).parent / "dashboard.html").read_text(encoding="utf-8")

@app.get("/api/health")
def health(): return {"status":"ok", "project":"SMART FARM ASSISTANT", "mode":"prototype"}

@app.get("/api/readings")
def get_readings(limit: int = Query(50, ge=1, le=500)): return db.list_readings(limit)

@app.post("/api/readings", status_code=201)
def post_reading(reading: ReadingIn): return db.add_reading(reading.model_dump())

@app.get("/api/events")
def get_events(limit: int = Query(50, ge=1, le=500)): return db.list_events(limit)

@app.post("/api/events", status_code=201)
def post_event(event: EventIn): return db.add_event(event.model_dump())

@app.get("/api/irrigation/recommendation")
def irrigation_recommendation(threshold: float = Query(30, ge=0, le=100)):
    rows = db.list_readings(1)
    if not rows: return {"recommendation":"no_data", "message":"Submit a soil reading before requesting a recommendation.", "threshold_pct":threshold}
    moisture = rows[0]["soil_moisture"]
    return {"recommendation":"check_irrigation" if moisture < threshold else "no_irrigation_suggested", "soil_moisture_pct":moisture, "threshold_pct":threshold, "message":"Moisture is below the configured threshold; inspect the field before watering." if moisture < threshold else "Moisture is at or above the configured threshold. This is advisory only."}
