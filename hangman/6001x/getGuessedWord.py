secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']


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


print getGuessedWord(secretWord, lettersGuessed)
