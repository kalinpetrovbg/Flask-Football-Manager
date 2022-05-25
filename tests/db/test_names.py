"""Unit tests for db.names file."""
from db.names import spanish_f_names, spanish_l_names


def test_spanish_names():
    first_names = spanish_f_names
    last_names = spanish_l_names

    assert "Santiago" in first_names
    assert "Laurentino" in last_names
