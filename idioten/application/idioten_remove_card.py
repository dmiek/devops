"""
Function controlling how cards are removed from the board.
"""


from idioten.application.idioten_ok_to_remove import ok_to_remove
from idioten.application.idioten_input_modifier import input_modifier


def remove_card(game_comps):
    """ Logic to remove cards from board. """
    print(game_comps["board"])
    pos = input_modifier(game_comps["player_input"])            # modify input to coding logic
    last_row = -1                                               # used to ascend one level in board
    print('attempting to remove card')
    if len(game_comps["board"]) < 1:
        print('game not setup')
        return game_comps

    # check if column is already empty
    row = game_comps["board"][0].copy()                                # check first row of board
    if row[pos] == '- ':
        print('column empty, cannot remove card')
        return game_comps

    # check length of board
    if len(game_comps["board"]) == 1:
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
            game_comps["board"][0] = row
            return game_comps
        # do not remove card from position
        print('card NOK to remove')
        return game_comps

    # if board is 2 rows or larger, continue to last row of board
    print('assessing if OK to remove')
    row = game_comps["board"][last_row].copy()
    print(row)

    # evaluate if position in last row is populated
    # if row is empty, ascend one row until non-empty row is found
    while row[pos] == '- ':
        last_row = last_row - 1
        row = game_comps["board"][last_row].copy()
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
            game_comps["board"][last_row] = row
            print('removed card in column')
            return game_comps

        print('card NOK to remove')
        return game_comps
