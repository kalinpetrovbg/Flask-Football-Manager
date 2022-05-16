"""Unit tests for stadium folder."""

from stadium.stadium import Stadium
from stadium.stadium import STADIUM_NAMES
from weather.weather import Sunny, Rainy


def test_if_stadium_exist_in_list_with_stadiums():
    stadium_name = "Camp Nou"

    assert stadium_name in STADIUM_NAMES


def test_stadium_initialization():
    stadium = Stadium()

    stadium.name = "Camp Nou"
    stadium.capacity = 99000

    assert stadium.__str__() == 'Stadium "Camp Nou" with 99000 capacity.'


# def test_generate_stadium():
#     stadium = Stadium()
#
#     for key, value in STADIUM_NAMES.items():
#         if key == "Camp Nou":
#
#             stadium.name = key
#             stadium.capacity = value
#
#             generated_stadium = list(STADIUM_NAMES)
#
#     assert stadium.name == "Camp Nou"
#     assert stadium.capacity == 99354


def test_generate_visitors():
    sunny = Sunny()

    stadium = Stadium()

    stadium.name = "Camp Nou"
    Stadium.capacity = 99000

    stadium.generate_visitors(sunny)

    assert sunny.coefficient == 0.85
    assert Stadium.spectators == 84150


def test_generate_message_if_sunny():
    sunny = Sunny()

    stadium = Stadium()

    Stadium.name = "Camp Nou"
    Stadium.capacity = 99000
    Stadium.spectators = Stadium.capacity * sunny.coefficient

    message = Stadium.generate_message(sunny)

    assert message == 'It was an exceptionally hot day for the crowd of 84150 that came out to "Camp Nou".'


def test_generate_message_if_rainy():
    rainy = Rainy()

    Stadium.name = "Camp Nou"
    Stadium.capacity = 99000
    Stadium.spectators = Stadium.capacity * rainy.coefficient

    message = Stadium.generate_message(rainy)

    assert message == 'It had rained all day, but 44550 hardy fans still made it out to "Camp Nou".'