"""Crate fixture for the app."""

import pytest

from app import app


@pytest.fixture
def test_app():
    test_app = app
    test_app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(test_app):
    return app.test_client()


@pytest.fixture()
def runner(test_app):
    return app.test_cli_runner()



def test_request_example(client):
    response = client.get("/")
    assert response.status_code == 200