"""
Test module to test board setup.
"""


from pytest_bdd import scenario, given, when, then
from idioten.application.idioten_setup import game_setup


@scenario('features/idioten_setup.feature', 'Verify board set up and empty when setup')
def test_board_set_up():
    """
    Scenario for testing that board is empty after setup.
    """

@scenario(
    "features/idioten_setup.feature",
    "Game setup clears boards",
    example_converters=dict(board_start=str, board_end=str)
)
def test_board_clearing():
    """ Tests that all kinds of boards are cleared. """


@given('board not set up')
def board_not_setup(boards_fixture, game_fixture):
    """ Tests that a void board can be set up. """
    game_fixture["board"] = boards_fixture["void"]
    assert game_fixture["board"] != boards_fixture["empty_board_single"]


@given("<board_start>")
def board_populated(boards_fixture, board_start, game_fixture):
    """ Populating with different boards """
    game_fixture["board"] = boards_fixture[board_start]
    assert game_fixture["board"] != boards_fixture["empty_board_single"]


@given('board already empty')
def board_already_empty(boards_fixture, game_fixture):
    """
    Tests that an already empty board does not cause any issues when setting up game.
    """
    game_fixture["board"] = boards_fixture["empty_board_single"]
    assert game_fixture["board"] == boards_fixture["empty_board_single"]


@when('game is set up')
def setup_board(game_fixture):
    """ Module sets up game. """
    game_setup(game_fixture)


@then('board is empty')
def board_is_set_up(boards_fixture, game_fixture):
    """ Asserts that board is set up. """
    assert game_fixture["board"] == boards_fixture["empty_board_single"]


@then('<board_end>')
def board_is_empty(boards_fixture, board_end, game_fixture):
    """ Asserts that board is set up. """
    assert game_fixture["board"] == boards_fixture[board_end]
