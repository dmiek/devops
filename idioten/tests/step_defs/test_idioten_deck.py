"""
Module for testing the deck generator.
"""


from idioten_deck import create_deck
from pytest_bdd import scenario, given, when, then


@scenario("../features/idioten_deck.feature", "Deck is of the correct type")
def test_correct_type():
    """ Scenario for testing deck type. """


@scenario("../features/idioten_deck.feature", "Deck only contains allowed colours")
def test_allowed_colours():
    """ Scenario for testing colours. """


@scenario("../features/idioten_deck.feature", "Deck only contains allowed ranks")
def test_allowed_ranks():
    """ Scenario for testing ranks. """


@scenario("../features/idioten_deck.feature", "Deck contains correct number of cards")
def test_correct_number_of_cards():
    """ Scenario for testing card deck size. """


@scenario("../features/idioten_deck.feature", "Deck is different from previous deck")
def test_new_deck_different():
    """ Scenario for testing deck shuffling. """


@scenario("../features/idioten_deck.feature", 'Deck contains no duplications')
def test_no_duplications():
    """ Scenario for testing for duplications. """


@given("existing deck")
def existing_deck(decks):
    """ Asserting existing deck is of correct size and type. """
    assert len(decks["current"]) == 52
    assert isinstance(decks["current"], list)


@when('deck shuffled')
def build_deck(decks):
    """ Shuffling deck. """
    decks["new"] = create_deck()
    assert len(decks["new"]) == 52
    assert isinstance(decks["new"], list)


@then('deck is of correct type')
def deck_type(decks):
    """ Testing deck is of correct type. """
    assert isinstance(decks["new"], list)


@then('deck contains only allowed colours')
def allowed_colour(decks):
    """ Testing deck contains correct colours. """
    allowed_colours = ["D", "S", "C", "H"]
    for i in range(len(decks["new"])):
        assert decks["new"][i][1] in allowed_colours


@then('deck contains only allowed ranks')
def allowed_rank(decks):
    """ Testing deck contains correct ranks. """
    allowed_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    for i in range(len(decks["new"])):
        assert decks["new"][i][0] in allowed_ranks


@then('deck contains all cards')
def deck_length(decks):
    """ Testing deck is of the correct size. """
    assert len(decks["new"]) == 52


@then('deck is different from previous deck')
def new_deck_previous_deck(decks):
    """ Testing deck shuffling. """

    assert decks["new"] != decks["current"]


@then('deck contains no duplications')
def unique_card(decks):
    """ Testing deck contains no duplications. """
    unique = []
    for i in range(len(decks["new"])):
        assert decks["new"][i] not in unique
        unique.append(decks["new"][i])
