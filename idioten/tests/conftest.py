"""
Module for keeping fixtures.
"""


import pytest
from idioten.application.idioten_deck import create_deck
from idioten.application.idioten_empty_row import empty_row


@pytest.fixture
def boards_fixture():
    """ Dict holding all boards. """
    boards = {
        "empty_board_single": [
            empty_row()
        ],
        "empty_row_double": [
            empty_row(),
            empty_row()
        ],
        "void": [

        ],
        "populated_single_OK_pre": [
            ['TD', '2C', '3S', 'KD']
        ],
        "populated_single_OK_post": [
            ['- ', '2C', '3S', 'KD']
        ],
        "populated_single_NOK": [
            ['TH', '2C', '3S', 'KD']
        ],
        "populated_double_OK": [
            ['5C', '4H', 'KC', 'QS'],
            ['TD', '2C', '3S', 'KD']
        ]
    }
    return boards


@pytest.fixture
def rows_fixture():
    """ Method containing rows for testing. """
    rows = {
        "void":                 [],
        "empty_row":            ['- ', '- ', '- ', '- '],
        "populated_OK_1":       ['TD', '3C', '2H', 'KD'],
        "populated_OK_2":       ['TD', '3C', '5C', '2C'],
        "populated_NOK_1":      ['TS', '3C', '2H', 'KD'],
        "populated_NOK_4":      ['TD', '3C', '2H', 'KD'],
        "position_empty_2":     ['TD', '- ', '2H', 'KD'],
        "royals":               ['JS', 'QS', 'KS', 'AS']
    }
    return rows


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
def empty_row_fixture():
    """ Empty row. """
    bench_board = ['- ', '- ', '- ', '- ']
    return bench_board
