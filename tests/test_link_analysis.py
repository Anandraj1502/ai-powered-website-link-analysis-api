import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.utils.validators import validate_url


client = TestClient(app)


# Test 1: Homepage should work
def test_homepage():
    response = client.get("/")

    assert response.status_code == 200
    assert "running" in response.json()["message"].lower()


# Test 2: Localhost should be blocked
def test_localhost_blocked():
    with pytest.raises(ValueError):
        validate_url("http://localhost")


# Test 3: Private IP should be blocked
def test_private_ip_blocked():
    with pytest.raises(ValueError):
        validate_url("http://127.0.0.1")


# Test 4: Invalid scheme should be blocked
def test_invalid_scheme_blocked():
    with pytest.raises(ValueError):
        validate_url("ftp://example.com")


# Test 5: Invalid URL should return an error
def test_invalid_url_api():
    response = client.post(
        "/link-analysis",
        json={"url": "ftp://example.com"}
    )

    assert response.status_code == 400