from fastapi.testclient import TestClient
from app.main import app
from app.auth import create_access_token
from datetime import timedelta

client = TestClient(app)

# Создание токена для тестового пользователя
def get_auth_header(username: str):
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": username}, expires_delta=access_token_expires
    )
    return {"Authorization": f"Bearer {access_token}"}

def test_add_note():
    response = client.post(
        "/notes/",
        json={"title": "Test", "content": "This is a test note"},
        headers=get_auth_header("example_user")
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test"

def test_list_notes():
    response = client.get("/notes/", headers=get_auth_header("example_user"))
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_note_without_auth():
    response = client.post("/notes/", json={"title": "Test", "content": "This is a test note"})
    assert response.status_code == 401

def test_list_notes_without_auth():
    response = client.get("/notes/")
    assert response.status_code == 401

def test_add_note_with_spelling_errors():
    response = client.post(
        "/notes/",
        json={"title": "Tset", "content": "This is a tset note"},
        headers=get_auth_header("example_user")
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Tset"

def test_list_notes_for_different_user():
    response = client.get("/notes/", headers=get_auth_header("another_user"))
    assert response.status_code == 200
    assert response.json() == []

def test_invalid_token():
    response = client.get("/notes/", headers={"Authorization": "Bearer invalid_token"})
    assert response.status_code == 401