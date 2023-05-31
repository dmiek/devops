"""
Module for testing the deck generator.
"""


from pytest_bdd import scenario, given, when, then
from idioten.application.idioten_deck import create_deck


@scenario("features/idioten_deck.feature", "Deck is of the correct type")
def test_correct_type():
    """ Scenario for testing deck type. """


@scenario("features/idioten_deck.feature", "Deck only contains allowed colours")
def test_allowed_colours():
    """ Scenario for testing colours. """


@scenario("features/idioten_deck.feature", "Deck only contains allowed ranks")
def test_allowed_ranks():
    """ Scenario for testing ranks. """


@scenario("features/idioten_deck.feature", "Deck contains correct number of cards")
def test_correct_number_of_cards():
    """ Scenario for testing card dek size. """


@scenario("features/idioten_deck.feature", "Deck is different from previous deck")
def test_new_deck_different():
    """ Scenario for testing deck shuffling. """


@scenario("features/idioten_deck.feature", 'Deck contains no duplications')
def test_no_duplications():
    """ Scenario for testing for duplications. """


@given("an existing deck")
def existing_deck(decks_fixture):
    """ Asserting existing deck is of correct size and type. """
    assert len(decks_fixture["current"]) == 52
    assert isinstance(decks_fixture["current"], list)


@when('deck is shuffled')
def build_deck(decks_fixture):
    """ Shuffling deck. """
    decks_fixture["new"] = create_deck()
    assert len(decks_fixture["new"]) == 52
    assert isinstance(decks_fixture["new"], list)


@then('deck components are of correct type (list)')
def deck_type(decks_fixture):
    """ Testing deck is of correct type. """
    assert isinstance(decks_fixture["new"], list)


@then('deck contains only allowed colours')
def allowed_colour(decks_fixture):
    """ Testing deck contains correct colours. """
    allowed_colours = ["D", "S", "C", "H"]
    for i in range(len(decks_fixture["new"])):
        assert decks_fixture["new"][i][1] in allowed_colours


@then('deck contains only allowed ranks')
def allowed_rank(decks_fixture):
    """ Testing deck contains correct ranks. """
    allowed_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    for i in range(len(decks_fixture["new"])):
        assert decks_fixture["new"][i][0] in allowed_ranks


@then('deck contains all cards')
def deck_length(decks_fixture):
    """ Testing deck is of the correct size. """
    assert len(decks_fixture["new"]) == 52


@then('deck contains no duplications')
def unique_card(decks_fixture):
    """ Testing deck contains no duplications. """
    unique = []
    for i in range(len(decks_fixture["new"])):
        assert decks_fixture["new"][i] not in unique
        unique.append(decks_fixture["new"][i])


@then('new deck is different from previous deck')
def new_deck_previous_deck(decks_fixture):
    """ Testing deck shuffling. """
    assert decks_fixture["new"] != decks_fixture["current"]
