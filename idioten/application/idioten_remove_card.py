"""
Function controlling how cards are removed from the board.
"""


from idioten.application.idioten_ok_to_remove import ok_to_remove


def remove_card(boards, k_b):
    """ Logic to remove cards from board. """

    board = boards          # extract playing board
    pos = (int(k_b) - 1)      # modify input to coding logic
    p = -1                  # used to ascend one level in board
    print('attempting to remove card')

    # check length of board
    if len(board) == 1:
        row = board[0]      # check first row
        if row[pos] == '- ':
            print('column empty, cannot remove card')
            return board
        # If column not empty, check if OK to remove
        else:
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
            else:
                # do not remove card from position
                print('card NOK to remove')
                return board


    # if board is larger than one row
    else:
        row = board[p]          # continue to last row of board

        # if column is empty, ascend one row until non-empty row is found
        while row[pos] == '- ':
            p = p - 1
            row = board[p]
            print('ascended one level')

        # when row is no longer empty
        print('row no longer empty')
        if row[pos] != '- ':      # assert row no longer empty
            # assess if OK to remove
            remove_ok_status = ok_to_remove(row, pos)
            if remove_ok_status == 1:
                row[pos] = '- '
                print('removed card in column')
            else:
                print('card NOK to remove')

        # replace row in board with current row
        board[p] = row
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
