from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from app.main import app
from app.services import weaviate_client

def mock_get_client():
    mock = MagicMock()
    # Customize mock here if needed, like:
    # mock.some_method.return_value = ...
    return mock

app.dependency_overrides[weaviate_client.get_client] = mock_get_client

client = TestClient(app)

def test_health_check():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}  # Match the actual return value
