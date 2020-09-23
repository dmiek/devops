aString = 'dwdwa'

def isPalindrome(aString):

    def toChars(aString):
        aString = aString.lower()
        ans = ''
        for c in aString:
            if c in 'abcdefghijklmnopqrstuvxyz':
                ans = ans + c
        return ans

    def isPal(aString):
        if len(aString) <= 1:
            return True
        else:
            return  aString[0] == aString[-1] and isPal(aString[1:-1])

    return isPal(toChars(aString))
