"""
Module for testing the deck generator.
"""


import pytest
from pytest_bdd import scenario, given, when, then, parsers
from idioten_deck import create_deck


@pytest.fixture(scope="module")
def card_deck():
    """ Fixture for card deck. """
    deck = create_deck()
    assert len(deck) == 52


@pytest.fixture(scope="module")
def previous_deck():
    """ Fixture for previous deck. """
    previous_deck = create_deck()
    assert len(previous_deck) == 52



@scenario("idioten_deck.feature", "Deck is of the correct type")
def test_correct_type():
    """ Scenario for testing deck type. """
    pass                    #Calling for scenario


@scenario("idioten_deck.feature", "Deck only contains allowed colours")
def test_allowed_colours():
    """ Scenario for testing colours. """
    pass                    #Calling for scenario


@scenario("idioten_deck.feature", "Deck only contains allowed ranks")
def test_allowed_ranks():
    """ Scenario for testing ranks. """
    pass                    #Calling for scenario


@scenario("idioten_deck.feature", "Deck contains correct number of cards")
def test_correct_number_of_cards():
    """ Scenario for testing card deck size. """
    pass                    #Calling for scenario


@scenario("idioten_deck.feature", "Deck is different from previous deck")
def test_new_deck_different():
    """ Scenario for testing deck shuffling. """
    pass                    #Calling for scenario


@scenario("idioten_deck.feature", 'Deck contains no duplications')
def no_duplications():
    """ Scenario for testing for duplications. """
    pass                    #Calling for scenario


@given("existing deck")
def existing_deck(previous_deck):
    """ Asserting existing deck is of correct size and type. """
    assert len(previous_deck) == 52
    assert type(previous_deck) == list


@when('deck shuffled')
def build_deck():
    """ Shuffling deck. """
    card_deck = create_deck()
    assert type(card_deck) == list
    assert len(card_deck) == 52


@then('deck is of correct type')
def deck_type(card_deck):
    """ Testing deck is of correct type. """
    assert type(card_deck) == list


@then('deck contains only allowed colours')
def allowed_colour(card_deck):
    """ Testing deck contains correct colours. """
    allowed_colours = ["D", "S", "C", "H"]
    for i in range(len(card_deck)):
        assert card_deck[i][1] in allowed_colours


@then('deck contains only allowed ranks')
def allowed_rank(card_deck):
    """ Testing deck contains correct ranks. """
    allowed_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    for i in range(len(card_deck)):
        assert card_deck[i][0] in allowed_ranks


@then('deck contains all cards')
def deck_length(card_deck):
    """ Testing deck is of the correct size. """
    assert len(card_deck) == 52


@then('deck is different from previous deck')
def new_deck_previous_deck(card_deck, previous_deck):
    """ Testing deck shuffling. """
    assert len(card_deck) == 52
    assert len(previous_deck) == 52
    assert card_deck != previous_deck


@then('deck contains no duplications')
def unique_card(card_deck):
    """ Testing deck contains no duplications. """
    unique = []
    assert type(card_deck) == list
    assert len(card_deck) == 52
    for i in range(len(card_deck)):
        assert card_deck[i] not in unique
        unique.append(card_deck[i])
