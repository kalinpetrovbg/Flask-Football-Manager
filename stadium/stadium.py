STADIUM_NAMES = {
    "Camp Nou": 99354,
    "Wembley Stadium": 90000,
    "Croke Park": 82300,
    "Twickenham Stadium": 82000,
    "Signal Iduna Park": 81359,
                                        # Todo  add at least 30 stadiums
}


class Stadium:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def generate_stadium(self):
        pass

    def generate_number_visitors(self, weather):
        pass                                # Todo  based on weather generate num_visitors