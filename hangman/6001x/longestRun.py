def longestRun(L):
    longest = 0
    longe = 1
    langd = len(L)
    L.append(-1)

    
    
    for k in range(len(L)):
        
        if (k+1) <= langd:
            if L[k+1] >= L[k]:
                longe += 1
            else:
                if longe > longest:
                    longest = longe
                longe = 1
        else:
            
            return longest

    return longest

##L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2, 1, 3, 2,1,2,3,4,5,6,7,7,7,8]
##L = [0]
##L = [1,1,1,1,1]
##L = [1, 2, 3, -1, -2, -3, -4, -5, -6]
L = [1, 0, 0, 0, 4, 5, 1, 2, 9, 4, -1, 0]
print longestRun(L)
