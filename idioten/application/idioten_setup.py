"""
Module for setting up a new game.
"""
from idioten.application.idioten_empty_row import empty_row
from idioten.application.idioten_deck import create_deck


def game_setup(game_comps):
    """ Setting up new game from scratch. """
    print("*** SETTING UP GAME ***")
    game_comps["board"] = [empty_row()]
    print("board cleared")
    game_comps["deck"] = create_deck()
    print("deck shuffled")
    print("*** SETUP FINISHED ***")
    return game_comps
