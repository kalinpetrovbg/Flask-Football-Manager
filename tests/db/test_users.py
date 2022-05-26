"""Unit tests for Users model."""
from application.db.users import AnonymousUser


def test_if_user_is_added_in_db_correctly(app_with_user):
    new_user = app_with_user

    assert new_user.username == "kalin_petrov"
    assert new_user.password == "0Ury@gaj82"
    assert new_user.team_id == 1000
    assert new_user.is_authenticated
    assert new_user.is_active
    assert not new_user.is_anonymous


def test_annonymouse_user_if_it_has_no_team():
    new_guest_user = AnonymousUser()

    assert new_guest_user.team_id is None
    assert not new_guest_user.is_authenticated
    assert new_guest_user.is_anonymous


def test_annonymouse_user_with_a_new_team():
    new_guest_user = AnonymousUser()

    new_guest_user.team_id = 1001

    assert new_guest_user.team_id == 1001
    assert new_guest_user.is_anonymous
