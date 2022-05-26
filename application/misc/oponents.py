"""Dict for building teams data and used for listing as a table."""

from collections import defaultdict

from application.db import Players


def teams_data(teams):
    """Generate dict with all teams."""

    data = defaultdict()

    for team in teams:
        players = Players.query.filter_by(team_id=team.id).all()
        stats = {
            "name": team.name,
            "logo": team.logo,
            "league": team.league,
            "id": team.id,
            "ovr": team.overall,
            "att": team.attack,
            "mid": team.middle,
            "def": team.defence,
            "count": len(players),
        }
        data[team] = stats

    return data
