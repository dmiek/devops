aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    flaten = []
    for n in range(len(aList)):
        if type(aList[n]) == list:
            for j in range(len(aList[n])):
                flaten.append(aList[n][j])
        else:
            flaten.append(aList[n])

    for i in range(len(flaten)):
        if type(flaten[i]) == list:
            flaten = flatten(flaten)
    return flaten

print flatten([[1, [2, 3]], [[4, 5, 6], [7, [8, 9]]], [[3, 2, 1], [2, 1], [1, [0]]]])
