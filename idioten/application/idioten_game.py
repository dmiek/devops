"""
Idioten card game.
"""

import sys

from idioten_setup import game_setup
from idioten_input import get_input

game_components = {}
game_running = 0


def game_just_started():
    valid_input = ['e', 'n']
    print(
        '*** GAME STARTED ***\n'
        '*** What do you want to do? ***\n'
        '*** Press "N" to start a new game. ***\n'
        '*** Press "E" to exit. ***\n'
        '*** Type "help" to display HELP menu. ***'
    )
    player_input = get_input(valid_input)



def determine_input(g_input):
    """ Module for determining what actions is requested. """
    if g_input == 'e':
        sys.exit('*** Exiting game, thanks for playing! ***')
    elif g_input == 'help':
        help_menu()
        return
    else:
        print('*** Do not know what to do. ***')


def start_new_game(game_components):
    """ Sets up a new game. """
    game_components = game_setup(game_components)
    return game_components


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