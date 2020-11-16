""" Test cases to test the OK_to_remove-functionality. """

from pytest_bdd import scenario, given, when, then
from idioten.application.idioten_OK_to_remove import ok_to_remove
from idioten.application.idioten_input_modifier import input_modifier

@scenario(
    "features/idioten_OK_to_remove.feature",
    "Test if card is OK to remove or not",
    example_converters=dict(startstate=str, inputvalue=str, endstate=int)
)
def test_empty_board_removal():
    """ Tests that no card is removed if board is empty. """


@given("a <start_row> of cards")
def start_row_def(rows_fixture, start_row):
    """ Assert initial row's properties. """
    assert isinstance(rows_fixture[start_row], list) == 1
    assert len(rows_fixture[start_row]) <= 4


@when("a card at <pos> position is requested to be removed")
def remove_a_card(rows_fixture, start_row, pos):
    """ Attempt to remove a card at a given postion. """
    pos = input_modifier(pos)
    rows_fixture["status"] = ok_to_remove(rows_fixture[start_row], pos)


@then("the <end_status> is set accordingly")
def end_status_def(rows_fixture, end_status):
    """ Assert "OK to remove"-status is set accoridingly. """
    assert rows_fixture["status"] == int(end_status)
