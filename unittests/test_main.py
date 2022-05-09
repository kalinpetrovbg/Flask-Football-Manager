"""Unit tests for main.py file."""

from unittests.fixures.base_fixture import client


def test_landing(client):
    landing = client.get("/")
    html = landing.data.decode()

    assert landing.status_code == 200

