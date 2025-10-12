import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_endpoint():
    payload = {"query": "Where is the internal documentation?"}
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "Confluence" in data["answer"]  # depends on your doc content

def test_invalid_payload():
    payload = {"wrong_key": "test"}
    response = client.post("/predict", json=payload)
    assert response.status_code == 422  # FastAPI returns 422 for validation errors
