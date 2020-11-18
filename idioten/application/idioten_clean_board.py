"""
Module for cleaning up  empty rows in boards.
"""


def clean_board(board, board_name):
    """ Method for cleaning up empty rows from the board, to keep it neat and tidy. """
    if len(board[board_name]) <= 1:
        print('board cannot be cleaned, too small')
        return board

    last_row = -1
    board_cleaned = False
    while board_cleaned is not True:
        for i in range(len(board[board_name][last_row])):
            if board[board_name][last_row][i] != '- ':
                board_cleaned = True
                print('row not empty, cannot remove')
                return board
        del board[board_name][last_row]
        if len(board[board_name]) <= 1:
            return board
