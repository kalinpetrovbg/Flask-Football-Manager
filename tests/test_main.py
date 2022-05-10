"""Unit tests for main.py file."""

from app import app

def test_index_page():
    client = app.test_client()
    url = "/"

    response = client.get(url)
    # html = landing.data.decode()

    assert response.status_code == 200

