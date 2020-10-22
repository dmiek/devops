"""
Module for keeping fixtures.
"""


import pytest
from idioten.application.idioten_deck import create_deck


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
    allowed_input = ('d', 'e', 'n', '1', '2', '3', '4')
    return allowed_input
