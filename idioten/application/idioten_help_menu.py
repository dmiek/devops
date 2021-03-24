"""
Module provides guidance to the player.
"""


def help_menu(game_comps):
    """ Provides guidance to the player. """
    # TODO Make menu dynamic depending on "valid input".
    menu_output = []
    possible_input = {
        'd': 'd = deal cards',
        'e': 'e = end game',
        'm': 'm = move card to empty spot',
        'n': 'n = new game',
    }
    #valid_input = game_comps["valid_input"].copy()
    for i in game_comps["valid_input"]:
        print('valid input', game_comps["valid_input"])
        if i in game_comps["valid_input"]:
            menu_output.append(possible_input[i])
            print('test', menu_output)


#    menu = (
#            "\n*** HELP MENU ***\n",
#            "d = deal cards\n",
#            "e = end game\n",
#            "m = move card to empty spot\n",
#            "n = new game\n",
#            "t = test mode\n",
#            "1-4 = remove card in column\n",
#            "*** END HELP MENU ***\n"
#        )
#    print(*menu)
    print('menu output', menu_output)
    game_comps["menu_output"] = menu_output
    return game_comps

#game_comps = {}
#help_menu(game_comps)