""" Test cases to test the OK_to_remove-functionality. """

from pytest_bdd import scenario, given, when, then
from idioten.application.idioten_OK_to_remove import OK_to_remove
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
    pass


@when("a card at <x> position is requested to be removed")
def remove_a_card(rows_fixture, start_row, x):
    pos = input_modifier(x)
    rows_fixture["status"] = OK_to_remove(rows_fixture[start_row], pos)


@then("the <end_status> is set accordingly")
def end_status_def(rows_fixture, end_status):
    assert rows_fixture["status"] == int(end_status)
