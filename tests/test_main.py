"""Unit tests for main.py file."""

from app import app


def test_login_page():
    client = app.test_client()
    url = "/login.html"
    response = client.get(url)

    assert response.status_code == 200

