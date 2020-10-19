"""
Module for testing the deck generator.
"""


import pytest
from pytest_bdd import scenario, given, when, then
from idioten_deck import create_deck



@pytest.fixture
def decks():
    """ Fixture for card deck. """
    decks = {"current": create_deck(), "new": create_deck()}
    assert len(decks["current"]) == 52
    return decks


@scenario("idioten_deck.feature", "Deck is of the correct type")
def test_correct_type():
    """ Scenario for testing deck type. """
    pass


@scenario("idioten_deck.feature", "Deck only contains allowed colours")
def test_allowed_colours():
    """ Scenario for testing colours. """
    pass


@scenario("idioten_deck.feature", "Deck only contains allowed ranks")
def test_allowed_ranks():
    """ Scenario for testing ranks. """
    pass


@scenario("idioten_deck.feature", "Deck contains correct number of cards")
def test_correct_number_of_cards():
    """ Scenario for testing card deck size. """
    pass


@scenario("idioten_deck.feature", "Deck is different from previous deck")
def test_new_deck_different():
    """ Scenario for testing deck shuffling. """
    pass


@scenario("idioten_deck.feature", 'Deck contains no duplications')
def test_no_duplications():
    """ Scenario for testing for duplications. """
    pass


@given("existing deck")
def existing_deck(decks):
    """ Asserting existing deck is of correct size and type. """
    assert len(decks["current"]) == 52
    assert type(decks["current"]) == list


@when('deck shuffled')
def build_deck(decks):
    """ Shuffling deck. """
    assert len(decks["new"]) == 52
    assert type(decks["new"]) == list



@then('deck is of correct type')
def deck_type(decks):
    """ Testing deck is of correct type. """
    assert type(decks["new"]) == list


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
