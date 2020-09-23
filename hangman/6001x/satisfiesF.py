def f(s):
    return 'a' in s or 'b' in s

L = ['a', 'b', 'a', 'a', 8, 'c', 'a', 'd', {}, [], (), 'a']

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    s = []
    for k in range(len(L)):
        if type(L[k]) != str:
            L[k] = 'int'
        if f(L[k]) == False:
            s.append(k)
    s.reverse()
    for bit in range(len(s)):
        L.pop(int(s[bit])) 

    return len(L)
      
print satisfiesF(L)
print L

## run_satisfiesF(L, satisfiesF)
