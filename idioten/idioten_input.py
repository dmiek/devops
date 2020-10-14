"""
Module for handling game input.
"""
import sys

INPUT = ()
VALID_INPUT = ('d', '1', '2', '3', '4', 'n', 'e')
GAME_ACTIVE = 1


def kb_input(game_active):
    """Keyboard input."""
    if game_active == 0:
        sys.exit('Exiting program; no game active.')

    print("Select Action: \n1-4 = Remove Card in Column \nd = Deal Cards\nn = New Game ")
    inp = input()
    print(inp)

    if inp == "d":
        print("Dealing Cards")
    elif inp in ('1', '2', '3', '4'):
        print("Removing Card in Column " + inp)
    elif inp == "n":
        print("Dealing New Game")
    elif inp == 'e':
        print('Player exiting program')
    else:
        print("Input Not Mapped to Action")
    return inp


while INPUT != 'e':
    INPUT = kb_input(GAME_ACTIVE)
