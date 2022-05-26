"""Unit tests for stadium folder."""

import random

from application.stadium import STADIUM_NAMES
from application.stadium import Stadium
from application.weather.weather import Sunny, Rainy, PartiallyCloudy, Cloudy, Storm


def test_if_stadium_exist_in_list_with_stadiums():
    stadium_name = "Camp Nou"

    assert stadium_name in STADIUM_NAMES


def test_stadium_initialization():
    stadium = Stadium()

    stadium.name = "Camp Nou"
    stadium.capacity = 99000

    assert stadium.__str__() == 'Stadium "Camp Nou" with 99000 capacity.'


def test_generate_stadium():
    stadium = Stadium()

    generated = Stadium.generate_stadium()
    STADIUM_NAMES = {"Camp Nou": 99354}

    generated_stadium = random.choice(list(STADIUM_NAMES.items()))
    Stadium.name, Stadium.capacity = generated_stadium

    assert stadium.name == "Camp Nou"
    assert stadium.capacity == 99354
    assert generated.name == "Camp Nou"
    assert generated.capacity == 99354


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


def test_generate_message_if_partially_cloudy():
    weather = PartiallyCloudy()

    Stadium.name = "Camp Nou"
    Stadium.capacity = 99000
    Stadium.spectators = Stadium.capacity * weather.coefficient

    message = Stadium.generate_message(weather)

    assert message == '99000 spectators arrived at "Camp Nou",where weather conditions were pretty good for football.'


def test_generate_message_if_cloudy():
    weather = Cloudy()

    Stadium.name = "Camp Nou"
    Stadium.capacity = 99000
    Stadium.spectators = Stadium.capacity * weather.coefficient

    message = Stadium.generate_message(weather)

    assert message == 'Clouds darkened the skies at "Camp Nou" as 79200 spectators turned up for the match.'


def test_generate_message_if_stormy():
    weather = Storm()

    Stadium.name = "Camp Nou"
    Stadium.capacity = 99000
    Stadium.spectators = Stadium.capacity * weather.coefficient

    message = Stadium.generate_message(weather)

    assert message == 'The storm has almost emptied "Camp Nou" but there are still 19800 enthusiasts today.'
