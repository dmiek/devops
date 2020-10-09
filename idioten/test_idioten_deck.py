from pytest_bdd import scenario, given, when, then
from idioten_deck import create_deck

game_active = False

@scenario('feature_idioten_deck.feature', 'Create a proper deck for the game')
def test_create_deck():
    pass

@given('no active round')
def no_active_round():
    previous_deck = create_deck()

@when('new deck generated')
def new_round_generated():
    new_deck = create_deck()

@then('deck contains only allowed colours')
def test_create_deck_allowed_colour():
    # Check that deck only contains allowed colours.
    new_deck = create_deck()
    allowed_colour = ["D","S","C","H"]
    for i in new_deck:
        assert i[1] in allowed_colour

@then('Deck contains only allowed ranks')
def test_create_deck_allowed_ranks():
    # Check that deck contains only allowed ranks.
    new_deck = create_deck()
    allowed_ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    for i in new_deck:
        assert i[0] in allowed_ranks

@then('new deck is different from previous deck')
def test_new_deck_previous_deck():
    previous_deck = create_deck()
    new_deck = create_deck()
    assert new_deck != previous_deck
