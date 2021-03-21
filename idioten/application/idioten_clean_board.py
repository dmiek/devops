"""
Module for cleaning up  empty rows in boards.
"""


def clean_board(game_comps, board):
    """ Method for cleaning up empty rows from the board, to keep it neat and tidy. """
    if len(game_comps[board]) <= 1:
        print('board cannot be cleaned, too small')
        return game_comps

    last_row = -1
    board_cleaned = False
    while board_cleaned is not True:
        for i in range(len(game_comps[board][last_row])):
            if game_comps[board][last_row][i] != '- ':
                print('row not empty, cannot remove')
                return game_comps
        del game_comps[board][last_row]
        if len(game_comps[board]) <= 1:
            return game_comps
