"""
Module for keeping fixtures.
"""


from code.idioten_deck import create_deck
import pytest


@pytest.fixture
def decks():
    """ Fixture for card deck. """
    cards = {"current": create_deck(), "new": create_deck()}
    assert len(cards["current"]) == 52
    return cards
