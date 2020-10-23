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
def accepted_values(valid_input):
    """ Fixture for allowed values. """
    allowed_input = valid_input
    return allowed_input


@pytest.fixture
def rejected_values(invalid_input):
    """ Fixture for allowed values. """
    rejected_input = invalid_input
    return rejected_input


@pytest.fixture
def input_fixture():
    """ Fixture for creating input object. """
    inputs = {"keyboard": '', 'status': 'unknown'}
    assert len(inputs) == 2
    assert len(inputs["keyboard"]) == 0
    assert inputs["status"] == 'unknown'
    return inputs
