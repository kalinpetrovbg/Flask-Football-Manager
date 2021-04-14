class AwayTeam:
    def __init__(self, name, *players):
        self.name = name
        self.players = list(players)

a = AwayTeam("Liverpool", "Kalin", "Ivan", "Georgi", "Dobri")
