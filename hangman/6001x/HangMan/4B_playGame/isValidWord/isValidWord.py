wordList = ['apa', 'apple', 'appar', 'appri', 'apaa']
word = 'apple'
hand = {'a':2, 'p':2, 'l':1, 'u':0, 'e':1, 'r':1}

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    validHand = hand.copy()
    if word == '':
        return False
    elif word in wordList:
        for letter in word:
        
            if validHand.get(letter, 0) == 0:
                return False
            else:
                validHand[letter] -= 1
        return True
    else:
        return False







print isValidWord(word, hand, wordList)
