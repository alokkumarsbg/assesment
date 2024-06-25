from fastapi.testclient import TestClient
from view import app
from unittest.mock import ANY

client = TestClient(app)

def test_add_lists_success():
    response = client.post("/api/add", json={"batchid":"test01","lists": [[1, 2], [3, 4]]})
    assert response.status_code == 200
    assert response.json() == {"batchid":"test01","results": [3, 7], "status": "complete","started_at":ANY,"completed_at":ANY}

def test_add_empty_list():
    response = client.post("/api/add", json={"batchid":"test02","lists": [[]]})
    assert response.status_code == 200
    assert response.json() == {"batchid":"test02","results": [0], "status": "complete","started_at":ANY,"completed_at":ANY}

def test_add_lists_with_negative_numbers():
    response = client.post("/api/add", json={"batchid":"test03","lists": [[-1, -2], [-3, 4]]})
    assert response.status_code == 200
    assert response.json() == {"batchid":"test03","results": [-3, 1], "status": "complete","started_at":ANY,"completed_at":ANY}

def test_add_lists_with_invalid_data():
    response = client.post("/api/add", json={"batchid":"test04","lists": [[1, 2], "invalid"]})
    assert response.status_code == 422  # Unprocessable Entity

def test_add_lists_with_large_numbers():
    response = client.post("/api/add", json={"batchid":"test05","lists": [[1e6, 2e6], [3e6, 4e6]]})
    assert response.status_code == 200
    assert response.json() == {"batchid":"test05","results": [3000000.0, 7000000.0], "status": "complete","started_at":ANY,"completed_at":ANY}
