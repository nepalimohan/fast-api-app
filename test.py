from fastapi.testclient import TestClient
from main import app, get_db

app.dependency_overrides[get_db] = lambda: {"connection": "Mocked connection", "items": [{"id": 1, "name": "Item 1"}]}

client = TestClient(app)

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "Item 1"}]
