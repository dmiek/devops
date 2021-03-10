

board = []
rond = []
rad01 = []
deck = ["1","2","3","4","5","6","7","8","9","10","11","12","x"]
print(*rond)
#print(*deck)


def remove_card(g, board):

    row = board[-1]
    print(*row)
    if g == "a":
        del rad01[0]
    elif g == "s":
        del rad01[1]
    elif g == "d":
        del rad01[2]
    elif g == "f":
        del rad01[3]
    else:
        print("Not a valid position to remove")
    return



