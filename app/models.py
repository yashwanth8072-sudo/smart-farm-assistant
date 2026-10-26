from datetime import datetime, timezone
from pydantic import BaseModel, Field

class ReadingIn(BaseModel):
    device_id: str = Field(min_length=1, max_length=80)
    soil_moisture: float = Field(ge=0, le=100, description="Percent")
    temperature_c: float = Field(ge=-30, le=80)
    humidity_pct: float = Field(ge=0, le=100)
    ph: float | None = Field(default=None, ge=0, le=14)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Reading(ReadingIn):
    id: int

class EventIn(BaseModel):
    device_id: str = Field(min_length=1, max_length=80)
    event_type: str = Field(default="possible_animal_intrusion", min_length=1, max_length=80)
    confidence: float | None = Field(default=None, ge=0, le=1)
    zone: str | None = Field(default=None, max_length=80)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Event(EventIn):
    id: int
