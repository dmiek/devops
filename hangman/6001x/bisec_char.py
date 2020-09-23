## Sort characters
aStr = 'aaaabbcdeeeffghhjjjjjklllmnoppqqrsttuvvxxyyz'
char = 'i'



def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''

    def lenRecur(aStr):
        '''
        aStr: a string

        returns: int, the length of aStr
        '''
        langd = 0
        if aStr == '':
            return langd
        else:
            langd += 1
            return langd + lenRecur(aStr[1:])

    if aStr == '':
        return False
    start = aStr[0]
    stop = lenRecur(aStr)
    tryy = aStr[stop/2]

    if tryy == char:
        return True
    elif stop == 1:
        return False
    else:
        if tryy > char:
            aStr = aStr[:stop/2]
            return isIn(char, aStr)
        else:
            aStr = aStr[stop/2+1:]
            return isIn(char, aStr)
        


print isIn(char,aStr)







