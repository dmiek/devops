"""
Module for setting up a new game.
"""
from DevOps.idioten.idioten_board import emptyRow
from DevOps.idioten.idioten_deck import create_deck

deck = []
board = []

def game_setup():
    """ Setting up new game from scratch. """
    print("***")
    print("*** SETUPING UP GAME ***")
    board = [emptyRow()]
    print("empty board created")
    rond = emptyRow()
    print("round emptied")
    deck = create_deck()
    print("*** SETUP FINISHED ***")
    return deck, board
