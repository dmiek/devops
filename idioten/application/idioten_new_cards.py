"""
Module to control how cards are drawn from the deck and dealt to the board.
"""


def new_cards(game_comps):
    """ Method to control how cards are drawn from the deck. """
    print("adding cards from deck to new round")
    game_comps["new_round"] = []
    for _ in range(4):
        game_comps["new_round"].append(game_comps["deck"][0])
        game_comps["deck"].pop(0)
    return game_comps

def deal_cards(game_comps):
    """ Deal cards to the board from the deck. """
    game_comps = new_cards(game_comps)
    for i in range(len(game_comps["board"][0])):
        if game_comps["board"][-1][i] == '- ':
            game_comps["board"][-1][i] = game_comps["new_round"][i]
            game_comps["new_round"][i] = '- '
    game_comps["board"].append(game_comps["new_round"])
    game_comps["new_round"] = []
