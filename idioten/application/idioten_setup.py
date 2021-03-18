"""
Module for setting up a new game.
"""
from idioten.application.idioten_empty_row import empty_row
from idioten.application.idioten_deck import create_deck

deck = []
board = []
rond = []

def game_setup():
    """ Setting up new game from scratch. """
    print("***")
    print("*** SETTING UP GAME ***")
    board = [empty_row()]
    print("empty board created")
    #rond = empty_row()
    #print("round emptied")
    #deck = create_deck()
    print("*** SETUP FINISHED ***")
    #return deck, board, rond
    return board