"""
Module for handling game input.
"""
import sys

VALID_INPUT = ('d', '1', '2', '3', '4', 'n', 'e')
INPUTS = {"keyboard": '', "status": 'unknown'}


def kb_input():
    """
    Method for handling game input through keyboard.
    Will only accept values defined in VALID_INPUT.
    """
    INPUTS["keyboard"] = input('Waiting for input')
    if INPUTS["keyboard"] in VALID_INPUT:
        INPUTS["status"] = 'OK'
        print(INPUTS)
        return INPUTS
    else:
        INPUTS["status"] = 'NOK'
        print(INPUTS)
        return INPUTS


def nput(game_active):
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


# t = Input('test input', 'unknown')
# print(t.keyboard)
# print(t.status)

#kb_input()