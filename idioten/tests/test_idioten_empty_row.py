"""
Testing the empty_row functionality.
"""
from idioten.application.idioten_empty_row import empty_row
from pytest_bdd import scenario, given, when, then


@scenario('features/idioten_empty_row.feature', 'Empty void board')
def test_reset_void_board():
    """ Test the resetting of an empty board. """


@scenario('features/idioten_empty_row.feature', 'Empty populated board')
def test_reset_pop_board():
    """ Test the resetting of a populated board. """


@given('board is completely empty')
def board_is_void(rows_fixture):
    """ Given an void board. """
    assert rows_fixture["void"] == []
    assert len(rows_fixture["void"]) == 0


@given('board is populated by current row')
def board_is_populated(rows_fixture):
    """ Given a populated board. """
    assert rows_fixture["populated_OK_1"] != []
    assert len(rows_fixture["populated_OK_1"]) == 4


@when('empty row is put on void board')
def empty_row_on_void_board(rows_fixture):
    """ Empty row is place on board. """
    rows_fixture["void"] = empty_row()


@when('empty row is put on populated board')
def empty_row_on_pop_board(rows_fixture):
    """ Populated row is place on board. """
    rows_fixture["populated_OK_1"] = empty_row()


@then('void board is empty and prepared for playing')
def board_void_prepared_and_empty(rows_fixture, empty_row_fixture):
    """ Board is empty but prepared for playing. """
    assert rows_fixture["void"] == empty_row_fixture
    assert len(rows_fixture["void"]) == 4


@then('populated board is empty and prepared for playing')
def board_pop_prepared_and_empty(rows_fixture, empty_row_fixture):
    """ Board is empty but prepared for playing. """
    assert rows_fixture["populated_OK_1"] == empty_row_fixture
    assert len(rows_fixture["populated_OK_1"]) == 4
