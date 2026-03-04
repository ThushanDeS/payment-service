import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_fares():
    response = client.get("/api/fares/")
    assert response.status_code == 200

def test_create_fare():
    fare_data = {"price": 250.00, "code": "ECONOMY"}
    response = client.post("/api/fares/", json=fare_data)
    assert response.status_code == 200
