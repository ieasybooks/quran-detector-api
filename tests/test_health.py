from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check_success():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": "v1"}


def test_health_wrong_method():
    response = client.post("/api/health")
    assert response.status_code == 405
