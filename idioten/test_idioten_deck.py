from pytest_bdd import scenario, given, when, then
from idioten_deck import create_deck

@scenario('feature_idioten_deck.feature', 'New deck is different from previous one')
def test_create_deck():
    pass

@given('no deck')
def no_deck():
    deck = []
    assert type(deck) == list

@given('existing deck')
def existing_deck():
    previous_deck = create_deck()
    assert len(previous_deck) == 52

@when('deck shuffled')
def new_deck_generated():
    new_deck = create_deck()
    assert type(new_deck) == list

@then('deck contains only allowed colours')
def test_create_deck_allowed_colour():
    # Check that deck only contains allowed colours.
    allowed_colour = ["D", "S", "C", "H"]
    for i in new_deck:
        assert i[1] in allowed_colour

@then('deck contains only allowed ranks')
def test_create_deck_allowed_ranks():
    # Check that deck contains only allowed ranks.
    allowed_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    for i in new_deck:
        assert i[0] in allowed_ranks

@then('new deck is different from previous deck')
def test_new_deck_previous_deck():
    previous_deck = create_deck()
    new_deck = create_deck()
    assert new_deck != previous_deck

@then('deck is of the correct type')
def test_deck_type():
    assert type(new_deck) == list

@then('deck contains no duplications')
def test_unique_card():
    unique_card = []
    assert len(new_deck) == 52
    for i in range(len(deck)):
        assert deck[i] not in unique_card
        unique_card.append(deck[i])