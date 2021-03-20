import sys
from idioten.idioten_deck import create_deck
from application.idioten_input import kb_input
from idioten.idioten_empty_row import empty_row
from idioten.application.idioten_new_cards import new_cards


# FUNCTIONS:

def new_game():
    print("initiating new game")
    board = [empty_row()]
    deck = create_deck()
    board = dealCards(board, deck)


def dealCards(board, deck):
    print("attempting to deal cards to board")
    if len(deck) < 1:
        print("deck empty; try to finish game")
        return board
    print("still cards left in deck")
    rond = new_cards(deck)
    print("cards to be added this round", *rond)
    lastRow = board[-1]
    check = []
    for i in range(4):          # Check number of empty elements in last row
        if lastRow[i] == "- ":
            check.append("x")   # Add x to check list
    print("number of empty elements in last row of current board: ", len(check))
    if len(check) == 4:                 # All elements in last row empty
        print("board consist of a single empty row")
        board.append(rond)
        del board[0]
    elif len(check) == 0:               # All elements in last row NOT empty
        print("last row is fully populated with cards; adding new round straight up")
        board.append(rond)
        displayBoard(board)
    else:                               # Some elements in last row empty
        print("adding cards to the current asymmetric last row")
        board.append(empty_row())
        print("adding empty row to current board")
        displayBoard(board)
        for i in range(4):
            row = board[0]              # Check if first row is empty
            if row[i] == "- ":          # If firstRow[i] is empty, then add card
                row[i] = rond[0]        # Add new card to row[i]
                board[0] = row          # Replace first row of board with new row
            else:                       # If first row is not, empty, continue with investigation
                p = -1
                row = board[p]          # Check last row
                while row[i] == "- ":   # While checked row[i] is empty,
                    p = p - 1           # check the previous row
                    row = board[p]      #
                p = p + 1               # Go back one row to an empty element
                row = board[p]          # Copy that row
                row[i] = rond[0]        # Replace element[i] in row with next card in deck
                board[p] = row          # Update current row in board with new card
            del rond[0]                 # Remove card just added to board from deck
    print("cards dealt to board")
    return board





# def playGame(board):
#     cleanUpBoard(board)
#     displayBoard(board)
#     # if game_active == 0:
#     #     print('start new game by intering "n"')
#     # else:
#     #     print("select action:")
#     r = kb_input()
#     if r == "d":
#         board = dealCards(board, deck)
#         return board
#     elif r == "1" or r == "2" or r == "3" or r == "4":
#         board = removeCard(board, r)
#         return board
#     elif r == "e" or r == "exit":
#         sys.exit("ending game, thanks for playing!")
#
#     # elif r == "e" or r == "exit":
#     #     finishGame()
#     elif r == "m":
#         board = move_card(board)
#         return board
#     elif r == "n":
#         board = new_game()
#         return board
#     elif r == "help":
#         helpMenu(board)
#         return board
#     else:
#         print("input not mapped to action")
#         print("type 'help' to display available commands")
#         return board


def displayBoard(board):
    print("displaying current board")
    for i in range(len(board)):
        print(*board[i])


def countCardsDealt():
    print("count how many cards has been dealt form the deck")


def finishGame():
    print("trying to evaluate victory")

# def endGameEvaluationboard(board):
#     x = 1
#     while len(deck) < 1:
#         board = playGame(board)
#     game_active = False

