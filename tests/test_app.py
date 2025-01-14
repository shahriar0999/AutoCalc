import pytest
from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

def test_homePage():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to our Calculator App"}

def test_add():
    response = client.post("/add", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_subtract():
    response = client.post("/subtract", json={"a": 10, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"result": 6}

def test_multiply():
    response = client.post("/multiply", json={"a": 6, "b": 7})
    assert response.status_code == 200
    assert response.json() == {"result": 42}

def test_divide():
    response = client.post("/divide", json={"a": 20, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"result": 4.0}

def test_divide_by_zero():
    response = client.post("/divide", json={"a": 20, "b": 0})
    assert response.status_code == 200
    assert response.json() == {"error": "Division by zero is not allowed"}

def test_square():
    response = client.post("/divide", json={"a": 0, "b": 0})
    assert response.status_code == 200
    assert response.json() == {"result": 1}