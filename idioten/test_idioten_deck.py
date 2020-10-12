import pytest
from pytest_bdd import scenario, given, when, then, parsers
from idioten_deck import create_deck

previous_deck = create_deck()


@pytest.fixture
def card_deck():
    deck = create_deck()
    assert len(deck) == 52
    return deck


@scenario("idioten_deck.feature", "Deck is of the correct type")
def test_correct_type():
    pass


@scenario("idioten_deck.feature", "Deck only contains allowed colours")
def test_allowed_colours():
    pass


@scenario("idioten_deck.feature", "Deck only contains allowed ranks")
def test_allowed_ranks():
    pass


@scenario("idioten_deck.feature", "Deck contains correct number of cards")
def test_correct_number_of_cards():
    pass


#@scenario("idioten_deck.feature", "Deck is different from previous deck")
#def test_new_deck_different():
#    pass


@given("existing deck", previous_deck)
def existing_deck():
    assert len(previous_deck) == 52
    assert type(previous_deck) == list


@when('deck shuffled')
def build_deck():
    card_deck = create_deck()
    assert type(card_deck) == list
    assert len(card_deck) == 52
    return card_deck


@then('deck is of correct type', card_deck)
def deck_type(card_deck):
    assert type(card_deck) == list
    assert len(card_deck) == 52


@then('deck contains only allowed colours', card_deck)
def allowed_colour(card_deck):
    # Check that deck only contains allowed colours.
    allowed_colours = ["D", "S", "C", "H"]
    for i in range(len(card_deck)):
        assert card_deck[i][1] in allowed_colours


@then('deck contains only allowed ranks', card_deck)
def allowed_rank(card_deck):
    allowed_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    for i in range(len(card_deck)):
        assert card_deck[i][0] in allowed_ranks


@then('deck contains all cards', card_deck)
def deck_length(card_deck):
    assert len(card_deck) == 52


@then('deck contains no duplications', card_deck)
def unique_card(card_deck):
    unique = []
    assert type(card_deck) == list
    assert len(card_deck) == 52
    for i in range(len(card_deck)):
        assert card_deck[i] not in unique
        unique.append(card_deck[i])

#@then('deck is different from previous deck', card_deck, previous_deck)
#def new_deck_previous_deck(card_deck, previous_deck):
#    assert card_deck != previous_deck





