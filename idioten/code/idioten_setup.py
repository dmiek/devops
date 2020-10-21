"""
Module for setting up a new game.
"""
from code.idioten_board import emptyRow
from code.idioten_deck import create_deck

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
