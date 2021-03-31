"""
Idioten card game.
"""

import sys

from idioten_setup import game_setup
from idioten_input import get_input
from idioten_new_cards import deal_cards
from idioten_clean_board import clean_board
from idioten_help_menu import help_menu


GAME_COMPS = {"game_running": 0}


def start_game(game_comps):
    """ First layer of gameplay. """
    game_comps["valid_input"] = ['e', 'n', 'help']
    while game_comps["game_running"] == 0:
        print(game_comps)
        print(
            '*** GAME STARTED ***\n'
            '*** What do you want to do? ***\n'
            '*** Press "N" to start a new game. ***\n'
            '*** Press "E" to exit. ***\n'
            '*** Type "help" to display HELP menu. ***\n'
        )
        determine_action(game_comps)


def determine_action(game_comps):
    """ Module for determining what actions is requested. """
    game_comps = get_input(game_comps)
    if game_comps["player_input"] == 'd':
        game_comps = deal_cards(game_comps)
        return game_comps
    elif game_comps["player_input"] == 'e':
        sys.exit('*** Exiting game, thanks for playing! ***')
    elif game_comps["player_input"] == 'help':
        help_menu(game_comps)
        return
    elif game_comps["player_input"] == 'n':
        new_game(game_comps)
    # TODO: Add functionality for "removing card".
    else:
        print('*** Do not know what to do. ***')


def new_game(game_comps):
    """ Sets up a new game. """
    game_setup(game_comps)
    game_comps["game_running"] = 1
    game_comps["valid_input"] = ['1', '2', '3', '4', 'd', 'e', 'help', 'm', 'n']
    while game_comps["game_running"] == 1:
        display_board(game_comps)
        determine_action(game_comps)
        clean_board(game_comps)


def display_board(game_comps):
    print("displaying current board")
    for i in range(len(game_comps["board"])):
        print(*game_comps["board"][i])


start_game(GAME_COMPS)
