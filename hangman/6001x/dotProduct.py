listA = [1, 2, 3]
listB = [4, 5, 6]

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    ans = 0
    for n in range(len(listA)):
        ans += listA[n]*listB[n]
    return ans




print dotProduct(listA, listB)
