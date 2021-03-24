"""
Module testing the drawing of cards from the deck.
"""

from pytest_bdd import scenario, given, when, then
from idioten.application.idioten_new_cards import new_cards, deal_cards


@scenario(
    "features/idioten_new_cards.feature",
    "Cards drawn from the deck no longer exists in the deck"
)
def test_cards_removed_from_deck():
    """ Tests that drawn cards are no longer present in the deck. """


@scenario("features/idioten_new_cards.feature", "Exactly four cards are drawn from the deck")
def test_amount_in_deck():
    """ Tests that exactly four cards are drawn from the deck. """


@scenario("features/idioten_new_cards.feature", "Exactly four cards are to be dealt")
def test_amount_dealt():
    """ Tests that exactly four cards are dealt each round. """


@scenario("features/idioten_new_cards.feature", "Cards are drawn in a specific order")
def test_drawn_order():
    """ Tests that cards from the deck is drawn in the correct order. """


@scenario(
    'features/idioten_new_cards.feature',
    'Cards are dealt to the correct row, even if columns are uneven',
    example_converters=dict(board_start=str, board_end=str)
)
def test_dealing_row():
    """ Testing that cards are dealt to the correct row in each column. """


@given("an existing deck")
def given_deck(boards_fixture):
    """ Deck for testing present, and in specific order. """
    assert len(boards_fixture["deck"]) == 52
    assert boards_fixture["deck"][0] == '9C'
    assert boards_fixture["deck"][1] == '4D'
    assert boards_fixture["deck"][2] == 'AH'
    assert boards_fixture["deck"][3] == '8D'
    assert boards_fixture["deck"][4] == 'JS'


@given('a <start_board>')
def given_start_board(boards_fixture, start_board):
    """ Provides different boards for dealing cards to. """
    print(boards_fixture[start_board])
    boards_fixture["board"] = boards_fixture[start_board].copy()


@when("cards are drawn from the deck")
def draw_cards(boards_fixture):
    """ Drawing cards from the deck. """
    new_cards(boards_fixture)


@when('cards are dealt to the board')
def deal_cards_to_board(boards_fixture):
    """ Deal cards to boards. """
    deal_cards(boards_fixture)


@then("cards can no longer be found in the deck")
def cards_not_in_deck(boards_fixture):
    """ Method to assert cards has been drawn from the deck. """
    for i in range(len(boards_fixture["new_round"])):
        assert boards_fixture["new_round"][i] not in boards_fixture["deck"]


@then("deck size is decreased by four")
def deck_size_reduced(boards_fixture):
    """ Testing that correct number of cards are drawn from the deck. """
    assert len(boards_fixture["deck"]) == 48
    # TODO: Modify to take relative number instead of absolute.


@then("cards to be dealt are four")
def new_round_size(boards_fixture):
    """ Testing that the cards to be dealt are exactly four. """
    assert len(boards_fixture["new_round"]) == 4


@then("the first four cards in the deck are drawn")
def draw_order(boards_fixture):
    """ Verify cards are drawn in the correct order. """
    assert boards_fixture["new_round"][0] == '9C'
    assert boards_fixture["new_round"][1] == '4D'
    assert boards_fixture["new_round"][2] == 'AH'
    assert boards_fixture["new_round"][3] == '8D'
    assert boards_fixture["deck"][0] == 'JS'


@then('board looks like <end_board>')
def board_is_according_to(boards_fixture, end_board):
    """ Verify cards are dealt to the correct row in each column. """
    assert boards_fixture["board"] == boards_fixture[end_board]

# TODO: Add more test cases.
