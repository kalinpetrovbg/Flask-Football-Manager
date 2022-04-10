"""Classes for the home and away teams in a game."""


class HomeTeam:
    """Build the home team properies."""

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __str__(self):
        return f"Home team {self.name} with power {self.power}."


class AwayTeam:
    """Build the away team properies."""

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __str__(self):
        return f"Away team {self.name} with power {self.power}."
