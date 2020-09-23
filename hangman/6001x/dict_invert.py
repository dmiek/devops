

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    reverse_dict = {}
    for key, value in d.iteritems():
        if not isinstance(value, (list)):
            value = [value]
        for val in value:
            reverse_dict[val] = reverse_dict.get(val, [])
            reverse_dict[val].append(key)

    for keys,values in reverse_dict.items():
        temp = values
        temp1 = temp.sort()
        reverse_dict[keys] = temp

    return reverse_dict


print dict_invert(d = {1:10, 2:20, 3:30, 4:30})
