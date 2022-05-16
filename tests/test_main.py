"""Unit tests for main.py file."""

from app import app


def test_login_page():
    client = app.test_client()
    url = "/"
    response = client.get(url)

    # Todo

    assert response.status_code == 200

