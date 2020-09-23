VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 4

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

word = 'weed'

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


print getWordScore(word, HAND_SIZE)
