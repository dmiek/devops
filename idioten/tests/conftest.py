"""
Module for keeping fixtures.
"""


import pytest
from idioten.application.idioten_deck import create_deck


@pytest.fixture
def decks_fixture():
    """ Fixture for card deck. """
    cards = {"current": create_deck()}
    assert len(cards["current"]) == 52
    assert isinstance(cards["current"], list)
    return cards


@pytest.fixture
def input_fixture():
    """ Fixture for creating input object. """
    inputs = {"keyboard": '', "status": 'unknown'}
    assert len(inputs) == 2
    assert len(inputs["keyboard"]) == 0
    assert inputs["status"] == 'unknown'
    return inputs


@pytest.fixture()
def board_fixture():
    """ Creating initial board. """
    test_board = {"void": [], "pop": ['TD', 'AS', '9H', '3C']}
    return test_board

@pytest.fixture()
def empty_row_fixture():
    """ Empty row. """
    bench_board = ['- ', '- ', '- ', '- ']
    return bench_board