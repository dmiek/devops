lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']


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

print getAvailableLetters(lettersGuessed)
