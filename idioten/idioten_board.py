import random
import sys


# FUNCTIONS:

def createDeck():
    print("creating deck")
    cardfaces = []
    suits = ["C", "D", "H", "S"]
    royals = ["A", "T", "J", "Q", "K"]
    deck = []

    for i in range(2, 10):
        cardfaces.append(str(i))

    for j in range(len(royals)):
        cardfaces.append(royals[j])

    for k in range(len(suits)):
        for l in range(len(cardfaces)):
            card = (cardfaces[l] + suits[k])
            deck.append(card)
    random.shuffle(deck)
    print("deck created")
    return deck


def newGame():
    print("initiating new game")
    board = [emptyRow()]
    deck = createDeck()
    board = dealCards(board, deck)

    # TEST
    if len(board) != 1:
        print("new board not of correct size")
        sys.exit("exiting")
    print("*** NEW GAME INITIATED ***")
    return board


def addCards(deck):
    print("adding cards from deck to new round")
    rond = []
    for i in range(4):
        rond.append(deck[0])
        deck.pop(0)
    print("cards added to round")
    return rond


def dealCards(board, deck):
    print("attempting to deal cards to board")
    if len(deck) < 1:
        print("deck empty; try to finish game")
        return board
    print("still cards left in deck")
    rond = addCards(deck)
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
        board.append(emptyRow())
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


def removeCard(board, r):
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


def helpMenu(board):
    print("*** HELP MENU ***")
    print("d = deal cards")
    print("e = end game")
    print("m = move card to empty spot")
    print("n = new game")
    print("t = test mode")
    print("1-4 = remove card in column")
    print("*** END HELP MENU ***")
    return board


def playGame(board):
    cleanUpBoard(board)
    displayBoard(board)
    print("select action:")
    r = input()
    if r == "d":
        board = dealCards(board, deck)
        return board
    elif r == "1" or r == "2" or r == "3" or r == "4":
        board = removeCard(board, r)
        return board
    elif r == "e" or r == "exit":
        sys.exit("ending game, thanks for playing!")
    elif r == "e" or r == "exit":
        finishGame()
    elif r == "m":
        board = moveCard(board)
        return board
    elif r == "n":
        board = newGame()
        return board
    elif r == "help":
        helpMenu(board)
        return board
    else:
        print("input not mapped to action")
        print("type 'help' to display available commands")
        return board


def displayBoard(board):
    print("displaying current board")
    for i in range(len(board)):
        print(*board[i])


def emptyRow():
    row = ["- ", "- ", "- ", "- "]
    return row


def moveCard(board):
    print("attempting to move card to empty spot")
    # Args: board, m = which card to move (1-4), r = to which position (1-4).
    m = (int(input("select a card to move: ")) - 1)
    r = (int(input("select a position to move to: ")) - 1)
    if okToMove(board, r) == False:     # Verify position of first row empty.
        print("not ok to move")
        return board
    p = -1                              # Look at last row of board
    row = board[p]
    while row[m] == "- ":               # While element empty,
        p = p - 1                       # look in the previous row.
        row = board[p]
    element = row[m]                    # When element not emtpy, copy
    row[m] = "- "                       # and replace with empty element.
    board[p] = row                      # Replace row in board with emptied row.
    row = board[0]                      # Copy first row of board,
    row[r] = element                    # and replace empty position with element.
    return board


def cleanUpBoard(board):
    lastRow = board[-1]                     # Copy last row of board.
    check = []                              # Create check list.
    if len(board) > 1:                  # Given board is larger than 1 row.
        for i in range(len(lastRow)):   # When the last row consist of empty elements only.
            if lastRow[i] == "- ":          # Check if element in last row is empty.
                check.append("x")           # If true, add counter to check list.
        if len(check) == 4:             # Then the last row is removed.
            del board[-1]                   # Delete last row of board.
            return board
        else:
            return board
    else:
        print("board only one row")
        return board


def okToRemove(board):
    print("checking if remove request is ok or not")


def okToMove(board, r):
    row = board[0]
    if row[r] == "- ":
        return True
    else:
        return False


def countCardsDealt():
    print("count how many cards has been dealt form the deck")


def finishGame():
    print("trying to evaluate victory")

def endGameEvaluationboard(board):
    x = 1
    while len(deck) < 1:
        board = playGame(board)


# SETUP:
print("***")
print("*** SETUPING UP GAME ***")
board = [emptyRow()]
print("empty board created")
rond = emptyRow()
print("round emptied")
deck = createDeck()
print("*** SETUP FINISHED ***")

# PLAY:

print("***")
print("*** GAME INITIATED ***")
newGame()
displayBoard(board)
print("***")

while len(deck) > 0:
    print("playing game")
    board = playGame(board)
    print("***")

print("*** DECK EMPTY ***")

endGameEvaluationboard(board)
