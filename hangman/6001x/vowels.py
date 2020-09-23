s = 'azcbobobegghakl'
tot = 0
vow = tot

def Vowels(s):
    tot = 0
    tot += s.count('a')
    tot += s.count('e')
    tot += s.count('i')
    tot += s.count('o')
    tot += s.count('u')    
    return tot

vow = Vowels(s)

print 'Number of vowels: ' + str(vow)
