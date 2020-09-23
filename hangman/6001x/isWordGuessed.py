secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's', 'p', 'a']
avLetters = 'abcdefghijklmnopqrstuvwxyz'

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

print isWordGuessed(secretWord, lettersGuessed)
