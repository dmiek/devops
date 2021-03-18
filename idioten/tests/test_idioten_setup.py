"""
Test module to test board setup.
"""


from pytest_bdd import scenario, given, when, then
from idioten.application.idioten_setup import game_setup


@scenario('features/idioten_setup.feature', 'Verify board setup and empty when setup')
def test_board_set_up():
    """
    Scenario for testing that board is empty after setup.
    """

# @scenario(
#     "features/idioten_setup.feature",
#     "Game setup clears boards",
#     example_converters=dict(startstate=str, inputvalue=str, endstate=str)
# )
# def test_board_clearing():
#     """ Tests that all kinds of boards are cleared. """


@given('board not setup')
def board_not_setup(boards_fixture):
    boards_fixture["current"] = boards_fixture["void"]
    print(boards_fixture["current"])
    assert boards_fixture["current"] != boards_fixture["empty_board_single"]


# @given("<board_start>", board_start)
# def board_populated(boards_fixture, board_start):
#

@when('game is set up')
def setup_board(boards_fixture):
    boards_fixture["current"] = game_setup()


@then('board is empty')
def board_is_setup(boards_fixture):
    assert boards_fixture["current"] == boards_fixture["empty_board_single"]
