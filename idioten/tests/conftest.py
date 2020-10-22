"""
Module for keeping fixtures.
"""


import pytest
from idioten.application.idioten_deck import create_deck
from idioten.application.idioten_input import VALID_INPUT


@pytest.fixture
def decks():
    """ Fixture for card deck. """
    cards = {"current": create_deck()}
    assert len(cards["current"]) == 52
    assert isinstance(cards["current"], list)
    return cards


@pytest.fixture
def allowed_values():
    """ Fixture for allowed values. """
    allowed_input = VALID_INPUT
    return allowed_input


@pytest.fixture
def input_fixture():
    inputs = {"keyboard": ''}
    assert len(inputs) == 1
    assert len(inputs["keyboard"]) == 0
    return inputs
