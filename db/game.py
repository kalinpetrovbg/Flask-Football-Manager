class HomeTeam:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __str__(self):
        return f"Home team {self.name} with power {self.power}."


class AwayTeam:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __str__(self):
        return f"Away team {self.name} with power {self.power}."