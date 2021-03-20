"""
Module for handling game input.
"""

VALID_INPUT = ('d', '1', '2', '3', '4', 'n', 'e', 'hello', 'help')
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

    INPUTS["status"] = 'NOK'
    print(INPUTS)
    return INPUTS
