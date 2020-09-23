aTup = ('I', 'am', 'a', 'test', 'tuple')

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    tuplee = ()
    for i in range(len(aTup)):
        if i%2 == 0:
            tuplee = tuplee+(aTup[i],)
            print tuplee
    return tuplee


print oddTuples(aTup)
