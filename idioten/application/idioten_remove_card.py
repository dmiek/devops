"""
Function controlling how cards are removed from the board.
"""


def remove_card(board, r):
    print("attempting to remove card")
    row = board[0]
    p = -1
    h = (int(r) - 1)
    if row[h] == "- ":
        print("column empty, cannot remove card")
        return board
    row = board[p]
    while row[h] == "- ":
        p = p - 1
        row = board[p]
    if row[h] != "- ":
        row[h] = "- "
    # replace row in board
    board[p] = row
    print("removed card in column")
    return board
