"""
Module for testing the cleaning of empty rows from the board.
"""

from pytest_bdd import scenario, given, when, then
from idioten.application.idioten_clean_board import clean_board


@scenario("features/idioten_clean_board.feature", "Remove empty lines from board")
def test_clean_board():
    """ Scenario creation for testing the clean board-feature. """


@given("an <existing> board")
def existing_board(boards_fixture, existing):
    """ Given an existing board of different appearances. """
    boards_fixture["board"] = boards_fixture[existing].copy()
    assert isinstance(boards_fixture["board"], list) is True


@when("empty rows are cleaned from existing board larger than 1 row")
def remove_empty_rows(boards_fixture):
    """ When board is cleaned. """
    clean_board(boards_fixture)


@then("board is according to <end> board")
def verify_board(boards_fixture, end):
    """ Verify board is according to end board. """
    assert boards_fixture["board"] == boards_fixture[end]
