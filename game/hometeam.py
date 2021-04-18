import random

class HomeTeam:
    def __init__(self, name, *players):
        self.name = name
        self.players = list(players)


Kalin = HomeTeam("FC Kalin", "Kalin", "Ivan", "Georgi")


AWAY_TEAMS = random.choice([Kalin])
home_team = AWAY_TEAMS.name