"""Unit tests for main.py file."""


def test_login_page(client):
    url = "/"
    response = client.get(url)

    assert b"<title>Python Manager</title>" in response.data

