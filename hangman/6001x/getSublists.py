def getSublists(L, n):
    subLists = []
    temp = []

    for start in range(len(L)-(n-1)):
        temp = L[start:n]
        n += 1
        subLists.append(temp)
    
    return subLists



##L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
L = [1, 1, 1, 1, 4]
n = 2
print getSublists(L, n)

