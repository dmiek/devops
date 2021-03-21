"""
Module for handling game input.
"""


def kb_input(game_comps):
    """
    Method for handling game input through keyboard.
    Determines if input is vald, where "valid" input is stated in VALID_INPUT.
    """
    game_comps["player_input"] = input('Waiting for input\n')
    if game_comps["player_input"] in game_comps["valid_input"]:
        game_comps["input_status"] = 'OK'
    else:
        game_comps["input_status"] = 'NOK'
    return game_comps


def get_input(game_comps):
    """ Returns only valid input. """
    game_comps["player_input"] = ''
    game_comps["input_status"] = 'NOK'
    while game_comps["input_status"] == 'NOK':
        game_comps = kb_input(game_comps)
        if game_comps["input_status"] == 'NOK':
            print('Input a valid value.')
        else:
            return game_comps
