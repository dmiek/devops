# -*- coding: utf-8 -*-
#Nummergissaren v0.1
print 'Tänk på ett nummer mellan 0 och 100!'

start = 0
slut = 100
led = 0
gissa = 0

while str(led) != 'c':
    gissa = (slut - start) / 2 + start
    print 'Är numret ' + str(gissa) + '?'
    led = raw_input('Ange om gissningen är (l)ägre, (h)ögre eller (c)orrekt:')
    if led == 'h':
        start = gissa
    elif led == 'l':
        slut = gissa
    elif led == 'c':
        break
    else:
        print 'Använd c, l eller h.'
print 'Numret är ' + str(gissa) + '!'



















