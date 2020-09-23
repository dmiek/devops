d1 = {4:70, 1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60, 5:80, 6:90}

def f(a,b):
    return a + b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    a = {}
    b = {}
    aTup = ()
    k1 = d1.keys()
    k2 = d2.keys()


    for k in d1:
        if k in d2:
            a[k] = f(d1[k], d2[k])
        else:
            b[k] = d1[k]
    for k in d2:
        if k in d1:
            a[k] = f(d1[k], d2[k])
        else:
            b[k] = d2[k]

    aTup = (a,b)
    return aTup

print dict_interdiff(d1,d2)
