"""
Module for keeping fixtures.
"""


import pytest
from idioten.application.idioten_deck import create_deck
from idioten.application.idioten_empty_row import empty_row


@pytest.fixture
def game_fixture():
    """ Fixture for holding game components. """
    components = {
        "deck": [],
        "board": []
    }
    return components


@pytest.fixture
def boards_fixture():
    """ Dict holding all boards. """
    boards = {
        "deck": ['9C', '4D', 'AH', '8D', 'JS', '3D', 'JC', '8S', 'KC', '2D', '2C', '2S', '5H',
                 '3H', 'TC', '6H', 'QC', '6C', '6D', '5S', 'QD', 'JH', '7D', '8C', '3C', 'TS',
                 'QS', '4C', '9H', '4H', 'KS', 'TD', 'QH', 'KH', '9D', '5C', '5D', 'AS', '7H',
                 'AC', '7S', '3S', 'KD', '7C', 'AD', '4S', '8H', 'TH', 'JD', '2H', '9S', '6S'],

        "single_even_pre": [
            ['5C', 'TD', 'KC', 'QS'],
        ],
        "single_even_post": [
            ['5C', 'TD', 'KC', 'QS'],
            ['9C', '4D', 'AH', '8D']
        ],
        "single_uneven_1_pre":  [
            ['- ', 'TD', 'KC', '- ']
        ],
        "single_uneven_1_post": [
            ['9C', 'TD', 'KC', '8D'],
            ['- ', '4D', 'AH', '- ']
        ],
        "single_uneven_2_pre": [
            ['5C', '- ', '- ', 'QS']
        ],
        "single_uneven_2_post": [
            ['5C', '4D', 'AH', 'QS'],
            ['9C', '- ', '- ', '8D']
        ],
        "empty_board_single": [
            empty_row()
        ],
        "empty_board_double": [
            empty_row(),
            empty_row()
        ],
        "void": [

        ],
        "void2": [
            []
        ],
        "populated_single_OK_pre": [
            ['TD', '2C', '3S', 'KD']
        ],
        "populated_single_OK_post": [
            ['- ', '2C', '3S', 'KD']
        ],
        "populated_single_NOK": [
            ['TH', '2C', '3S', 'KD']
        ],
        "populated_double_OK_pre": [
            ['5C', '4H', 'KC', 'QS'],
            ['TD', '2C', '3S', 'KD']
        ],
        "populated_double_OK_post": [
            ['5C', '4H', 'KC', 'QS'],
            ['- ', '2C', '3S', 'KD']
        ],
        "populated_double_NOK": [
            ['5C', '4H', 'KC', 'QS'],
            ['TH', '2C', '3S', 'KD']
        ],
        "populated_triple_OK_pre": [
            ['5C', '4H', 'KC', 'QS'],
            ['TD', '2C', '3S', 'KD'],
            ['- ', '6C', '7D', 'QH']
        ],
        "populated_triple_OK_post": [
            ['5C', '4H', 'KC', 'QS'],
            ['- ', '2C', '3S', 'KD'],
            ['- ', '6C', '7D', 'QH']
        ],
        "populated_triple_NOK": [
            ['5C', '4H', 'KC', 'QS'],
            ['TD', '2C', '3S', 'KD'],
            ['- ', '6C', '7D', 'QH']
        ],
        "move_single_pop_NOK": [
            ['5C', '4H', 'KC', 'QS']
        ],
        "move_double_pop_NOK": [
            ['5C', '4H', 'KC', 'QS'],
            ['TH', '2C', '3S', 'KD']
        ],
        "move_triple_pop_NOK": [
            ['5C', '4H', 'KC', 'QS'],
            ['TD', '2C', '3S', 'KD'],
            ['- ', '6C', '7D', 'QH']
        ],
        "move_single_pop_OK_pre": [
            ['- ', '2C', '3S', 'KD']
        ],
        "move_single_pop_OK_post2": [
            ['2C', '- ', '3S', 'KD']
        ],
        "move_single_pop_OK_post3": [
            ['3S', '2C', '- ', 'KD']
        ],
        "move_single_pop_OK_post4": [
            ['KD', '2C', '3S', '- ']
        ],
        "move_double_pop_OK_pre": [
            ['5C', '4H', 'KC', '- '],
            ['TH', '2C', '3S', '- ']
        ],
        "move_double_pop_OK_post1": [
            ['5C', '4H', 'KC', 'TH'],
            ['- ', '2C', '3S', '- ']
        ],
        "move_double_pop_OK_post2": [
            ['5C', '4H', 'KC', '2C'],
            ['TH', '- ', '3S', '- ']
        ],
        "move_double_pop_OK_post3": [
            ['5C', '4H', 'KC', '3S'],
            ['TH', '2C', '- ', '- ']
        ],
        "move_triple_pop_OK_pre": [
            ['5C', '- ', 'KC', 'QS'],
            ['TD', '- ', '3S', 'KD'],
            ['2C', '- ', '7D', 'QH']
        ],
        "move_triple_pop_OK_post1": [
            ['5C', '2C', 'KC', 'QS'],
            ['TD', '- ', '3S', 'KD'],
            ['- ', '- ', '7D', 'QH']
        ],
        "move_triple_pop_OK_post3": [
            ['5C', '7D', 'KC', 'QS'],
            ['TD', '- ', '3S', 'KD'],
            ['2C', '- ', '- ', 'QH']
        ],
        "move_triple_pop_OK_post4": [
            ['5C', 'QH', 'KC', 'QS'],
            ['TD', '- ', '3S', 'KD'],
            ['2C', '- ', '7D', '- ']
        ],
        "move_quad_asym_OK_pre": [
            ['- ', 'TD', 'KC', 'QS'],
            ['- ', '2C', '3S', 'KD'],
            ['- ', '- ', '7D', 'QH'],
            ['- ', '- ', '- ', '5C']
        ],
        "move_quad_asym_OK_post2": [
            ['2C', 'TD', 'KC', 'QS'],
            ['- ', '- ', '3S', 'KD'],
            ['- ', '- ', '7D', 'QH'],
            ['- ', '- ', '- ', '5C']
        ],
        "move_quad_asym_OK_post3": [
            ['7D', 'TD', 'KC', 'QS'],
            ['- ', '2C', '3S', 'KD'],
            ['- ', '- ', '- ', 'QH'],
            ['- ', '- ', '- ', '5C']
        ],
        "move_quad_asym_OK_post4": [
            ['5C', 'TD', 'KC', 'QS'],
            ['- ', '2C', '3S', 'KD'],
            ['- ', '- ', '7D', 'QH'],
            ['- ', '- ', '- ', '- ']
        ],
        "move_quad_asym_NOK1": [
            ['2C', 'TD', 'KC', 'QS'],
            ['- ', '- ', '3S', 'KD'],
            ['- ', '- ', '7D', 'QH'],
            ['- ', '- ', '- ', '5C']
        ],
        "move_quad_asym_NOK2": [
            ['2C', 'TD', 'KC', 'QS'],
            ['- ', 'AD', '3S', 'KD'],
            ['- ', '- ', '7D', 'QH'],
            ['- ', '- ', '- ', '5C']
        ],
        "clean_double_OK_pre": [
            ['- ', '- ', '7D', 'QH'],
            ['- ', '- ', '- ', '- ']
        ],
        "clean_double_OK_post": [
            ['- ', '- ', '7D', 'QH']
        ],
        "clean_triple_OK_pre": [
            ['- ', '2C', '3S', 'KD'],
            ['- ', '- ', '7D', 'QH'],
            ['- ', '- ', '- ', '- ']
        ],
        "clean_triple_OK_post": [
            ['- ', '2C', '3S', 'KD'],
            ['- ', '- ', '7D', 'QH']
        ],
        "clean_quad_OK_pre": [
            ['5C', 'TD', 'KC', 'QS'],
            ['- ', '2C', '3S', 'KD'],
            ['- ', '- ', '7D', '- '],
            ['- ', '- ', '- ', '- ']
        ],
        "clean_quad_OK_post": [
            ['5C', 'TD', 'KC', 'QS'],
            ['- ', '2C', '3S', 'KD'],
            ['- ', '- ', '7D', '- ']
        ],
        "clean_superdirty_OK_pre": [
            ['5C', 'TD', 'KC', 'QS'],
            ['- ', '2C', '3S', 'KD'],
            ['- ', '- ', '7D', '- '],
            ['- ', '- ', '- ', '- '],
            ['- ', '- ', '- ', '- '],
            ['- ', '- ', '- ', '- '],
            ['- ', '- ', '- ', '- '],
            ['- ', '- ', '- ', '- '],
            ['- ', '- ', '- ', '- ']
        ],
        "scramble_1": 'dwadwadwadwadwa',
        "scramble_2": 32131231.2321312,
        "scramble_3": 32132132321312,
        "scramble_4": True,
        "scramble_5": False,
        "scramble_6": 0x10,
        "scramble_7": 321321312 + 1,
        "scramble_8": 4.2e-4,
        "scramble_9": 1.79e308,
        "scramble_10": '2'
    }
    return boards


@pytest.fixture
def rows_fixture():
    """ Method containing rows for testing. """
    rows = {
        "void":                 [],
        "empty_row":            ['- ', '- ', '- ', '- '],
        "populated_OK_1":       ['TD', '3C', '2H', 'KD'],
        "populated_clubs":      ['TC', '3C', '5C', '2C'],
        "populated_NOK_1":      ['TS', '3C', '2H', 'KD'],
        "populated_NOK_4":      ['TD', '3C', '2H', 'KD'],
        "position_empty_2":     ['TD', '- ', '2H', 'KD'],
        "royals":               ['JS', 'QS', 'KS', 'AS']
    }
    return rows


@pytest.fixture
def decks_fixture():
    """ Fixture for card deck. """
    cards = {
        "current":      create_deck(),
        "full_deck":    create_deck(),
        "deck_empty":   [],
        "1_card":       ['2D'],
        "2_cards":      ['2D', '3H'],
        "3_cards":      ['2D', '3H', 'AC'],
        "4_cards":      ['2D', '3H', 'AC', 'KS'],
        "5_cards":      ['2D', '3H', 'AC', 'KS', '5D']
    }
    return cards


@pytest.fixture
def input_fixture():
    """ Fixture for creating input object. """
    inputs = {"keyboard": '', "status": 'unknown'}
    assert len(inputs) == 2
    assert len(inputs["keyboard"]) == 0
    assert inputs["status"] == 'unknown'
    return inputs


@pytest.fixture()
def empty_row_fixture():
    """ Empty row. """
    bench_board = ['- ', '- ', '- ', '- ']
    return bench_board


@pytest.fixture()
def menu_fixture():
    """ Fixture for providing test data for menu module. """
    menu = {
        "deal_cards":   ["deal cards"],
        "end_game":     ["end game", "help menu", "end help menu"],
        "move_card":    ["move card to"],
        "new_game":     ["new game", "help menu", "end help menu"],
        "end_new":      ["end game", "new game", "help menu", "end help menu"],
        "deal_end_new": ["deal cards", "end game", "new game"],
        "x":            ["x"],
        "positions":    ["remove card in column"],

        "d":    ['d'],
        "e":    ['e'],
        "m":    ['m'],
        "n":    ['n'],
        "en":   ['e', 'n'],
        "den":  ['d', 'e', 'n'],
        "1":    ['1'],
        "2":    ['2'],
        "3":    ['3'],
        "4":    ['4'],
        "5":    ['5']
    }
    return menu
