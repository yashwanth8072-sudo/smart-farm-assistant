import os, sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = os.getenv("SFA_DB_PATH", "smart_farm_assistant.db")

def connect():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con

def init_db():
    with connect() as con:
        con.execute('''CREATE TABLE IF NOT EXISTS readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT, device_id TEXT NOT NULL,
            soil_moisture REAL NOT NULL, temperature_c REAL NOT NULL,
            humidity_pct REAL NOT NULL, ph REAL, timestamp TEXT NOT NULL)''')
        con.execute('''CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT, device_id TEXT NOT NULL,
            event_type TEXT NOT NULL, confidence REAL, zone TEXT, timestamp TEXT NOT NULL)''')

def add_reading(data: dict):
    with connect() as con:
        cur = con.execute("INSERT INTO readings(device_id,soil_moisture,temperature_c,humidity_pct,ph,timestamp) VALUES(?,?,?,?,?,?)",
            (data["device_id"], data["soil_moisture"], data["temperature_c"], data["humidity_pct"], data.get("ph"), str(data["timestamp"])))
        row = con.execute("SELECT * FROM readings WHERE id=?", (cur.lastrowid,)).fetchone()
        return dict(row)

def list_readings(limit=100):
    with connect() as con:
        return [dict(r) for r in con.execute("SELECT * FROM readings ORDER BY id DESC LIMIT ?", (limit,)).fetchall()]

def add_event(data: dict):
    with connect() as con:
        cur = con.execute("INSERT INTO events(device_id,event_type,confidence,zone,timestamp) VALUES(?,?,?,?,?)",
            (data["device_id"], data["event_type"], data.get("confidence"), data.get("zone"), str(data["timestamp"])))
        return dict(con.execute("SELECT * FROM events WHERE id=?", (cur.lastrowid,)).fetchone())

def list_events(limit=100):
    with connect() as con:
        return [dict(r) for r in con.execute("SELECT * FROM events ORDER BY id DESC LIMIT ?", (limit,)).fetchall()]
