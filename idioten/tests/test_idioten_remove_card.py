"""
Tests the "remove card"-functionality.
"""


from pytest_bdd import given, when, then, scenario
from idioten.application.idioten_remove_card import remove_card
from idioten.application.idioten_empty_row import empty_row


empty_ref_board = empty_row()


@scenario(
    "features/idioten_remove_card.feature",
    "No card is removed if board is empty",
    example_converters=dict(startstate=str, inputvalue=str, endstate=str)
)
def test_empty_board_removal():
    """ Tests that no card is removed if board is empty. """


@given("a board consisting of <start_board>")
def empty_board(boards_fixture, start_board):
    """ Setup a board to test. """
    boards_fixture["play"] = boards_fixture[start_board]
    assert type(boards_fixture["play"]) == list


@when("a card removal is attempted at <x> position")
def card_removal_attempted(boards_fixture, x):
    """ Card is removed from board. """
    boards_fixture["play"] = remove_card(boards_fixture["play"], x)


@then("board is according to <end_board>")
def board_after_removal(boards_fixture, end_board):
    """ Assert board is modified accordingly. """
    assert boards_fixture["play"] == boards_fixture[end_board]
