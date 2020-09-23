s = 'azcbobobegghakl'
vow = 0

def Bob(s):
    tot = sum(s[i:].startswith("bob") for i in range(len(s)))
    print tot
    return tot

vow = Bob(s)

print 'Number of times bob occurs is: ' + str(vow)
