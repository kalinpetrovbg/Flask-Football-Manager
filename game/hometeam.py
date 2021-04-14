class HomeTeam:
    def __init__(self, name, *players):
        self.name = name
        self.players = list(players)

Barcelona = HomeTeam("Barcelona", "Kalin", "Ivan", "Georgi")
