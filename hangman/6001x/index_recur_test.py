aStr = 'dwtdwadwat'

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

print lenRecur(aStr)
