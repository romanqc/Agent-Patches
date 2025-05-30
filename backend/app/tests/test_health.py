from fastapi.testclient import TestClient
from main import app  # Make sure this path matches your actual app import

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Agent Patches Backend is Live!"}
