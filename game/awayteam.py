class AwayTeam:
    def __init__(self, name, *players):
        self.name = name
        self.players = list(players)


Liverpool = AwayTeam("Liverpool", "Kalin", "Ivan", "Georgi")
RealMadrid = AwayTeam("Real Madrid")
BayernMunich = AwayTeam("Bayern Munich")

AWAY_TEAMS = [Liverpool, RealMadrid, BayernMunich]
