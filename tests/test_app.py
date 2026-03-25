from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    r = client.get("/")
    assert r.status_code == 200