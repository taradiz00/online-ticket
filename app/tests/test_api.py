import pytest
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

@pytest.fixture(scope="function")
def anon_client():
    client = TestClient(app)
    yield client


def test_login_invalid_data_response_401(anon_client):
    payload = {
        "Username":"eli",
        "Password":"eli12",
        "Email":"eli@yahoo.com"
    }
    response = anon_client.post("/users/login", json=payload)
    assert response.status_code == 401



def test_login_invalid_data_422(anon_client):
    payload = {
        "Username":"eli10",
    }
    response = anon_client.post("/users/login", json=payload)
    assert response.status_code == 422



def test_login_response_200(anon_client):
    payload = {
        "Username": "eli10",
        "Password": "Eli123"
    }
    response = anon_client.post("/users/login", json=payload)
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "refresh_token" in response.json()



def test_register_response_201(anon_client):
    payload = {
        "Username":"abdi80",
        "Password":"abdi80A",
        "Password_Confirm":"abdi80A",
        "Email":"abdi80@yahoo.com",
    }
    response = anon_client.post("/users/register", json=payload)
    assert response.status_code == 201
    assert response.json()["detail"] == "User registered successfully"



def test_register_invalid_data_422(anon_client):
    payload = {
        "Username":"eli10",
        "Password":"Eli123",
        "Password_confirm":"Eli123"
    }
    response = anon_client.post("users/register", json=payload)
    assert response.status_code == 422



def test_register_password_mismatch_422(anon_client):
    payload = {
        "Username":"eli10",
        "Password":"Eli123",
        "Password_confirm":"eli123",
        "Email":"eli10@yahoo.com"
    }
    response = anon_client.post("users/register", json=payload)
    assert response.status_code == 422

