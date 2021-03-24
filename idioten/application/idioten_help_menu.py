"""
Module provides guidance to the player depending on the current state of the game.
"""


def help_menu(game_comps):
    """ Provides guidance to the player. """
    menu_output = ('\n*** HELP MENU ***\n')
    possible_input = {
        'd':    'd = deal cards',
        'e':    'e = end game',
        'm':    'm = move card to empty spot',
        'n':    'n = new game',
        '1':    '1-4 = remove card in column\n',
    }
    for i in game_comps["valid_input"]:
        if i in game_comps["valid_input"]:
            menu_output += possible_input[i] + '\n'

    menu_output += '*** END HELP MENU ***\n'
    game_comps["menu_output"] = menu_output
    return game_comps
