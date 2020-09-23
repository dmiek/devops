# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    s = True
    if len(lettersGuessed) <= 0:
        s = False
        return s

    for letter in lettersGuessed:
        if letter not in avLetters:
            s = False
            return s

    
    for letter in secretWord:
        if letter not in lettersGuessed:
            s = False
            return s
            
    return s


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    s = True
    gues = []
    avLetters = 'abcdefghijklmnopqrstuvwxyz'

    for letter in lettersGuessed:
        if letter not in avLetters:
            s = False
            return s
    for letter in secretWord:
        gues.append('_')

    if len(lettersGuessed) <= 0:
        g = ' '.join(gues)
        return g

    for letter in secretWord:
        if letter in lettersGuessed:
            for n in range(len(secretWord)):
                if secretWord[n] == letter:
                    gues[n] = letter
                
    g = str(' '.join(gues))
    return g


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    avLetters = 'abcdefghijklmnopqrstuvwxyz'
    availLetters = list(avLetters)
    for letter in lettersGuessed:
        n = availLetters.index(letter)
        availLetters.pop(n)           
    return ''.join(availLetters)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    x = None
    nGuesses = 8
    lettersGuessed = []
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    print '--------------------------'
    
    while nGuesses > 0:
        print 'You have ' + str(nGuesses) + ' guesses left.'
        print 'Available letters: ' + getAvailableLetters(lettersGuessed)
        a = str(raw_input('Please guess a letter: '))
        a = a.lower()

        if a not in getAvailableLetters(lettersGuessed):
            if a in lettersGuessed:    
                print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
                if a not in lettersGuessed:
                    lettersGuessed.append(str(a)) 
                
        else:
            lettersGuessed.append(str(a)) 
            if a not in secretWord:
                print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)
                nGuesses -= 1
                

            else:
                if a not in lettersGuessed:
                    lettersGuessed.append(str(a))
                print 'Good guess: ' + getGuessedWord(secretWord, lettersGuessed)
            
          
        print '--------------------------'
        if '_' not in getGuessedWord(secretWord, lettersGuessed):
            print 'Congratulations, you won!'
            return x

        

    print 'Sorry, you ran out of guesses. The word was ' + str(secretWord) + '.'
    return x

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
