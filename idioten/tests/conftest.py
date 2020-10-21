"""
Module for keeping fixtures.
"""


import pytest
from ..code.idioten_deck import create_deck


@pytest.fixture
def decks():
    """ Fixture for card deck. """
    cards = {"current": create_deck()}
    assert len(cards["current"]) == 52
    assert isinstance(cards["current"], list)
    return cards
