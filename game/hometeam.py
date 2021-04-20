import random

from players.defender import Defender
from players.keeper import Keeper
from players.midfielder import Midfielder
from players.winger import Winger
from players.forward import Forward


class HomeTeam:
    def __init__(self, name, *players):
        self.name = name
        self.players = list(players)
        self.midfield = 38   # later to be calculated


Kalin = HomeTeam("FC Kalin", Keeper("Yannic Banfi"), Defender("Gasem Al-Marwani"), Midfielder("Jan Eger"),
                 Winger("Vasil Gorbanov"), Forward("Juraj Trška"))


HOME_TEAMS = random.choice([Kalin])
home_team = HOME_TEAMS.name
home_team_players = [player.name for player in HOME_TEAMS.players]
print(', '.join(home_team_players))
