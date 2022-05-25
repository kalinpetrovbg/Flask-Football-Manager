"""Unit tests for main.py file."""


def test_login_page(client):
    url = "/"
    response = client.get(url)

    assert b"Hello, World" in response.data

