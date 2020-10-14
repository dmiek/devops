"""
Module for handling game input.
"""
import sys

INPUT = ()
VALID_INPUT = ('d', '1', '2', '3', '4', 'n', 'e')
GAME_ACTIVE = 1


def kb_input(game_active):
    """
    Keyboard input.
    """
    if game_active == 0:
        print("Game over. Start a new game.")
    else:
        print("Select action: \n1-4 = Remove card in column \nd = Deal cards\nn = New game")

    inp = input()
    print(inp)


    if inp != 'n':
        if game_active == 0:
            print('Game not running')
        else:
            print("Dealing new game")

    elif inp == "d":
        print("Dealing cards")
    elif inp in ('1', '2', '3', '4'):
        print("Removing card in column " + inp)

    elif inp == 'e':
        sys.exit('Player exiting program.')
    else:
        print("Input not mapped to action")
    return inp


#while INPUT != 'e':
#    INPUT = kb_input(GAME_ACTIVE)
