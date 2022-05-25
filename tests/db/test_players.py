"""Unit tests for Players model."""


def test_if_players_are_crated_correctly(app_with_player):
    player = app_with_player

    assert player.first_name == "Cristiano"
    assert player.last_name == "Ronaldo"
    assert player.position == "ATT"
    assert player.overall == 50
    assert player.__repr__() == "Cristiano"
