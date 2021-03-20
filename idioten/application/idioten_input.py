"""
Module for handling game input.
"""


INPUTS = {"keyboard": '', "status": 'unknown'}


def kb_input(valid_input):
    """
    Method for handling game input through keyboard.
    Determines if input is vald, where "valid" input is stated in VALID_INPUT.
    """
    INPUTS["keyboard"] = input('Waiting for input\n')
    if INPUTS["keyboard"] in valid_input:
        INPUTS["status"] = 'OK'
    else:
        INPUTS["status"] = 'NOK'
    #print(INPUTS)
    return INPUTS


def get_input(valid_input):
    """ Returns only valid input. """
    ok_input = {}
    ok_input["status"] = 'NOK'
    while ok_input["status"] == 'NOK':
        ok_input = kb_input(valid_input)
        if ok_input["status"] == 'NOK':
            print('Input a valid value.')
        else:
            return ok_input["keyboard"]
