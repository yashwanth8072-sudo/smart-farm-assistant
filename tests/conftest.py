import os
import tempfile
import pytest
from fastapi.testclient import TestClient

@pytest.fixture()
def client(monkeypatch):
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    monkeypatch.setenv("SFA_DB_PATH", path)
    from app import db
    db.DB_PATH = path
    from app.main import app
    db.init_db()
    with TestClient(app) as test_client:
        yield test_client
    try: os.remove(path)
    except OSError: pass
