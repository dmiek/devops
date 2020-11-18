"""
Module to control how cards are drawn from the deck.
"""


def new_cards(board):
    """ Method to control how cards are drawn from the deck. """
    print("adding cards from deck to new round")
    board["new_round"] = []
    for _ in range(4):
        board["new_round"].append(board["deck"][0])
        board["deck"].pop(0)
    return board
