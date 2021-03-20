"""
Idioten card game.
"""

import sys

from idioten_setup import game_setup
from idioten_input import get_input

GAME_COMPONENTS = {}
GAME_RUNNING = 0


def game_just_started():
    valid_input = ['e', 'n', 'help']
    while GAME_RUNNING == 0:
        print(
            '*** GAME STARTED ***\n'
            '*** What do you want to do? ***\n'
            '*** Press "N" to start a new game. ***\n'
            '*** Press "E" to exit. ***\n'
            '*** Type "help" to display HELP menu. ***'
        )
        player_input = get_input(valid_input)
        determine_input(player_input)


def determine_input(g_input):
    """ Module for determining what actions is requested. """
    if g_input == 'e':
        sys.exit('*** Exiting game, thanks for playing! ***')
    elif g_input == 'help':
        help_menu()
        return
    elif g_input == 'n':
        start_new_game(GAME_COMPONENTS)
    else:
        print('*** Do not know what to do. ***')


def start_new_game(GAME_COMPONENTS):
    """ Sets up a new game. """
    GAME_COMPONENTS = game_setup(GAME_COMPONENTS)
    return GAME_COMPONENTS


def help_menu():
    print(
        "*** HELP MENU ***\n",
        "d = deal cards\n",
        "e = end game\n",
        "m = move card to empty spot\n",
        "n = new game\n",
        "t = test mode\n",
        "1-4 = remove card in column\n",
        "*** END HELP MENU ***"
    )
    return


game_just_started()
game_input = valid_input()
determine_input(game_input)