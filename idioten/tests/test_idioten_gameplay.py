"""
Module for testing the gameplay.
"""

from pytest_bdd import scenario, given, when, then

@scenario(
    "features/idioten_gameplay.feature",
    "Initiate gameplay"
)
def test_initiate_gameplay():
    """
    Tests the initiating of a new game.
    """


@given("deck is complete")
def no_game_running(boards_fixture):
    """ Verify no game is running. """
    assert len(boards_fixture["deck"]) == 52


@when("new game is started")
def new_game_started():
    return


@then("four cards are dealt from the deck")
def four_cards_dealt():
    return