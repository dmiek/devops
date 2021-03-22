"""
Tests the "remove card"-functionality.
"""


from pytest_bdd import given, when, then, scenario
from idioten.application.idioten_remove_card import remove_card


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
    boards_fixture["board"] = boards_fixture[start_board].copy()


@when("a card removal is attempted at <player_input> position")
def card_removal_attempted(boards_fixture, player_input):
    """ Card is removed from board. """
    boards_fixture["player_input"] = player_input
    remove_card(boards_fixture)


@then("board is according to <end_board>")
def board_after_removal(boards_fixture, end_board):
    """ Assert board is modified accordingly. """
    assert boards_fixture["board"] == boards_fixture[end_board]
