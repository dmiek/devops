
from idioten.application.idioten_empty_row import empty_row
from pytest_bdd import scenario, given, when, then


@scenario('features/idioten_empty_row.feature', 'Setup void board')
def test_reset_empty_board():
    """ Test the resetting of an empty board. """


@given('board is completely empty')
def board_is_empty(board_fixture):
    """ Given an void board. """
    assert board_fixture["void"] == []


@when('empty row is put on board')
def empty_row_on_board(board_fixture):
    """ Empty row is place on board. """
    board_fixture["void"] = empty_row()


@then('board is empty and prepared for playing')
def board_prepared_and_empty(board_fixture):
    assert board_fixture["void"] == ["- ", "- ", "- ", "- "]
