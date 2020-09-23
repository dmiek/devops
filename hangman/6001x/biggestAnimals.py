animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    amountOf = 0
    key = ''
    for i in aDict:
        if len(aDict[i]) > amountOf:
            key = "'"+i+"'"
        else:
            return None
    return key
    
print biggest(animals)



