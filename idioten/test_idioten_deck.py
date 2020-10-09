import pytest
from pytest_bdd import scenario, given, when, then

from idioten_board import new_game
from idioten_board import game_active
from idioten_deck import create_deck

game_active = False

@scenario('Create a proper deck for the game')
def test_create_deck():
    pass

@given('no active round')
def no_active_round():
    assert.game_active = False

@when('new deck is generated')
def new_round_started():
    create_deck()


@then('deck contains only allowed colours')
def test_create_deck_allowed_colour(self):
        # Check that deck only contains allowed colours.
        deck = create_deck()
        allowed_colour = ["D","S","C","H"]
        for i in deck:
            self.assertIn(i[1], allowed_colour)

@then('Deck contains only allowed ranks')
def test_create_deck_allowed_ranks(self):
        # Check that deck contains only allowed ranks.
        deck = create_deck()
        allowed_ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
        for i in deck:
            self.assertIn(i[0], allowed_ranks)