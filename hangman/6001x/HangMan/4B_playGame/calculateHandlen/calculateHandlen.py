def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    lenn = 0
    for key in hand.keys():
        if hand.get(key, 0) >= 1:
            lenn += hand[key]
    return lenn

        
hand = {'a':2, 'p':2, 'l':1, 'u':0, 'e':1, 'r':1}

print calculateHandlen(hand)
