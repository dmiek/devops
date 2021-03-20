"""
Idioten card game.
"""


from idioten_setup import game_setup
from idioten_input import kb_input

game_components = {}

print('*** GAME STARTED ***')
print('*** What do you want to do? ***')
print('*** Press "N" to start a new game. ***')
print('*** Type "help" to display HELP menu. ***')
game_input = kb_input()
print(game_input)





def determine_input(game_input):
    """ Module for determining what actions is requested. """


def start_new_game(game_components):
    """ Sets up a new game. """
    game_components = game_setup(game_components)
    return game_components


def helpMenu():
    print("*** HELP MENU ***")
    print("d = deal cards")
    print("e = end game")
    print("m = move card to empty spot")
    print("n = new game")
    print("t = test mode")
    print("1-4 = remove card in column")
    print("*** END HELP MENU ***")
