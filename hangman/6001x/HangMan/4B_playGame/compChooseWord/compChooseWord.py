import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
hand = {}
wordList = []


##getFrequencyDict(sequence)

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

wordList = loadWords()

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

hand = dealHand(HAND_SIZE)

def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                          # print an empty line


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
##                displayHand(hand)
        return True
    else:
        return False


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    updHand = hand.copy()
    for letter in word:
        updHand[letter] = updHand.get(letter, 0) - 1
    return updHand

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    lenn = 0
    for key in hand.keys():
        if hand.get(key, 0) >= 1:
            lenn += hand[key]
    return lenn

def getWordScore(word, n):
    points = 0
    if len(word) < 1:
        return 0
    for letter in word:
        points += SCRABBLE_LETTER_VALUES[letter]
    points *= len(word)
    if n == len(word):
        points += 50
    return points
    
def compChooseWord(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    
    
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    score = 0
    validHand = {}
    
    # Create a new variable to store the best word seen so far (initially None)  
    maxWord = None
    
    # For each word in the wordList
    for ord in wordList:
        validHand = hand.copy()

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(ord, validHand, wordList) == True:
        
##        for bstav in ord:
##            if validHand.get(bstav, 0) < 1:
##                break
##            else:
##                validHand[bstav] -= 1 
##            

                # Find out how much making that word is worth
                score = getWordScore(ord, n)

                # If the score for that word is higher than your best score
                if score > maxScore:
                    
                    # Update your best score, and best word accordingly
                    maxScore = score
                    maxWord = ord
                    validHand = {}
    return str(maxWord)

    

##    
##    # As long as there are still letters left in the hand:
##
##    while calculateHandlen(hand) > 0:
##        
##        # Display the hand
##        print 'Current hand: ',
##        displayHand(hand)
##            
##        # Ask user for input
##        word = raw_input('Enter word, or a "." to indicate that you are finished: ')
##            
##        # If the input is a single period:
##        if word == '.':
##            
##            # End the game (break out of the loop)
##            break
##                
##        # Otherwise (the input is not a single period):
##            
##        else:
##            # If the word is not valid:
##            if isValidWord(word, hand, wordList) == False:
##            
##                # Reject invalid word (print a message followed by a blank line)
##                print 'Invalid word, please try again: \n'
##                
##            # Otherwise (the word is valid):
##            else:
##                
##                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
##                totScore += getWordScore(word, n)
##                print '"' + str(word) + '" earned ' + str(getWordScore(word, n)) + ' points. Total: ' + str(totScore) + ' points \n'
##                
##                # Update the hand 
##                hand = updateHand(hand, word)
##
##        # Game is over (user entered a '.' or ran out of letters), so tell user the total score
##    if word == '.':
##        print 'Goodbye! Total score ' + str(totScore) + ' points.'
##    else:
##        print 'Run out of letters. Total score ' + str(totScore) + ' points.'
##
