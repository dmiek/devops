""" Test cases to test the OK_to_remove-functionality. """

from pytest_bdd import scenario, given, when, then
from idioten.application.idioten_ok_to_move import ok_to_move


@scenario(
    "features/idioten_ok_to_move.feature",
    "Cards can only be moved to an empty location",
    example_converters=dict(startstate=str, inputvalue=str, endstate=int)
)
def test_moving_card():
    """ Tests that no card is removed if board is empty. """


@given("a board consisting of <start_board>")
def start_board(boards_fixture, start_board):
    """ Setup a board to test. """
    boards_fixture["play"] = boards_fixture[start_board]
    assert isinstance(boards_fixture["play"], list)


@when("moving a card is attempted from <fr> position to <to> position")
def move_a_card(boards_fixture, fr, to):
    """ Attempt to move a card. """
    boards_fixture["play"] = ok_to_move(boards_fixture["play"], fr, to)


@then("board is according to <end_board>")
def end_board(boards_fixture, end_board):
    """ Assess card move valid or not. """
    assert boards_fixture["play"] == boards_fixture[end_board]
