import pytest
from fastapi.testclient import TestClient
from app import app


client = TestClient(app)


def test_get_user_1():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Alice", "age": 30}

def test_get_user_2():
    response = client.get("/users/2")
    assert response.status_code == 200
    assert response.json() == {"name": "Bob", "age": 25}

def test_get_user_not_found():
    response = client.get("/users/3")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}


def test_create_user_success():
    response = client.post("/users/?user_id=3&name=Olivia&age=40")
    assert response.status_code == 200
    assert response.json() == {"name": "Olivia", "age": 40}

def test_create_user_already_exists():
    response = client.post("/users/?user_id=1&name=Alice&age=30")
    assert response.status_code == 400
    assert response.json() == {"detail": "User already exists"}