"""
Test module to test board setup.
"""


from pytest_bdd import scenario, given, when, then
from idioten.application.idioten_setup import game_setup


@scenario(
    'features/idioten_setup.feature',
    'Verify deck is set up regardless of state',
    example_converters=dict(start_deck=str, end_deck=str)
)
def test_different_start_decks():
    """ Tests that different types of decks can be restored and shuffled. """


@scenario(
    "features/idioten_setup.feature",
    "Game setup clears boards",
    example_converters=dict(board_start=str, board_end=str)
)
def test_board_clearing():
    """ Tests that all kinds of boards are cleared. """


@given('different types of <start_deck>')
def decks_not_set_up(decks_fixture, game_fixture, start_deck):
    """ Tests that previous and partial decks can be restored and shuffled. """
    game_fixture["deck"] = decks_fixture[start_deck]


@given("<board_start>")
def board_populated(boards_fixture, board_start, game_fixture):
    """ Populating with different boards """
    game_fixture["board"] = boards_fixture[board_start]


@when('game is set up')
def setup_board(game_fixture):
    """ Module sets up game. """
    game_setup(game_fixture)


@then('<end_deck> contains 52 cards')
def deck_sizes_ok(decks_fixture, game_fixture, end_deck):
    """ Asserts that deck is of correct size. """
    assert len(game_fixture["deck"]) == len(decks_fixture[end_deck])


@then('<board_end>')
def board_is_empty(boards_fixture, board_end, game_fixture):
    """ Asserts that board is set up. """
    assert game_fixture["board"] == boards_fixture[board_end]
