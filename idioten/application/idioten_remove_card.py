"""
Function controlling how cards are removed from the board.
"""


from idioten.application.idioten_ok_to_remove import ok_to_remove
from idioten.application.idioten_input_modifier import input_modifier


def remove_card(boards, k_b):
    """ Logic to remove cards from board. """

    board = boards                      # extract playing board
    print(board)
    pos = input_modifier(k_b)           # modify input to coding logic
    last_row = -1                       # used to ascend one level in board
    print('attempting to remove card')
    if len(board) < 1:
        print('game not setup')
        return board

    # check if column is already empty
    row = board[0]  # check first row
    if row[pos] == '- ':
        print('column empty, cannot remove card')
        return board

    # check length of board
    if len(board) == 1:
        # If column not empty, check if OK to remove
        print('assessing if OK to remove')
        print(row)
        wor = []
        wor.extend(row)
        remove_ok_status = ok_to_remove(wor, pos)
        print(row)
        if remove_ok_status == 1:
            # remove card from postion
            print('removing card from position' + str(pos))
            row[pos] = '- '
            print(row)
            board[0] = row
            return board
        # do not remove card from position
        print('card NOK to remove')
        return board

    # if board is 2 rows or larger, continue to last row of board
    print('assessing if OK to remove')
    row = board[last_row]  #
    print(row)

    # evaluate if position in last row is populated
    # if row is empty, ascend one row until non-empty row is found
    while row[pos] == '- ':
        last_row = last_row - 1
        row = board[last_row]
        print('ascended one level')
    # when row is no longer empty
    print('row no longer empty')
    if row[pos] != '- ':      # assert row no longer empty
        print('assess if OK to remove')
        wor = []
        wor.extend(row)
        remove_ok_status = ok_to_remove(wor, pos)
        if remove_ok_status == 1:
            row[pos] = '- '
            board[last_row] = row
            print('removed card in column')
            return board

        print('card NOK to remove')
        return board

#
# boards = [
#     ['TD', '2C', '3S', 'KD']
# ]

#boards = [
# ['- ', '- ', '- ', '- ']
# ]

# boards = {"play": [
#     ['TD', '2C', '3S', 'KD'],
#     ['- ', '- ', '- ', '- ']
# ]
# }
# r = 1
# board2 = remove_card(boards, 1)
# print(board2)
