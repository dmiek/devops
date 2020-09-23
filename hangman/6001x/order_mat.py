order = 'jaja'

def item_order(order):
    sal = order.count('salad')
    ham = order.count('hamburger')
    wat = order.count('wat')
    tot = str('salad:'+str(sal)+' hamburger:'+str(ham)+' water:'+str(wat))
    return tot

tot = item_order(order)
print tot
