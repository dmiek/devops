from pytest_bdd import scenario, given, when, then, parsers
from idioten_deck import create_deck

deck = []
previous_deck = []
unique_card = []


@scenario("idioten_deck.feature", "Deck only contains allowed colours")
def test_allowed_colours():
    pass


@scenario("idioten_deck.feature", "Deck only contains allowed ranks")
def test_allowed_ranks():
    pass


@scenario("idioten_deck.feature", "Deck is of the correct type")
def test_correct_type():
    pass


# @scenario("idioten_deck.feature", "Deck contains correct number of cards")
# def test_correct_number_of_cards():
#     pass


@scenario("idioten_deck.feature", "Deck is different from previous deck")
def test_new_deck_different():
    pass


@pytest.fixture
def card_deck():
    deck = create_deck()
    return deck


@given("existing deck")
def existing_deck():
    previous_deck = create_deck()
    return previous_deck


@when(parsers.parse('{deck} shuffled'))
def deck_shuffled():
    deck = create_deck()
    assert type(deck) == list
    assert len(deck) == 52
    return deck


@then('deck contains only allowed colours')
def allowed_colour():
    # Check that deck only contains allowed colours.
    allowed_colours = ["D", "S", "C", "H"]
    for i in deck:
        assert i[1] in allowed_colours


@then('deck contains only allowed ranks')
def allowed_rank():
    allowed_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    for i in deck:
        assert i[0] in allowed_ranks


@then('deck is of correct type')
def deck_type():
    assert type(deck) == list
    assert len(deck) == 52


@then('deck contains all cards')
def deck_langd():
    assert len(deck) == 52


@then(parsers.parse('{deck} contains no duplications'))
def unique_card(deck):
    unique_card = []
    assert type(deck) == list
    assert len(deck) == 52
    for i in range(len(deck)):
        assert deck[i] not in unique_card
        unique_card.append(deck[i])


@then(parsers.parse('{deck} is different from {previous_deck}'))
def new_deck_previous_deck(deck, previous_deck):
    assert deck != previous_deck





