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


@given("a board consisting of <a> <b> <c> <d>")
def empty_board(a, b, c, d):
    """ Create an empty board and verify it's empty. """
    board = [a, b, c, d]
    for n in range(len(board)):
        board[n] = board[n] + ' '
    assert type(board) == list
    assert type(empty_ref_board) == list
    assert board == empty_ref_board


@when("a card removal is attempted at <x> position")
def card_removal_attempted(x):
    pass


@then("board is according to <end_board>")
def board_after_removal(end_board):
    pass
