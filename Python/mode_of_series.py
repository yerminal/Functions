def mode_dict(lst): # It returns a dict that contains frequencies of the input.
    """
    >>> mode_dict([3,3,4,4,5,5,6])
    {3: 2, 4: 2, 5: 2, 6: 1}
    >>> mode_dict(["x","y","x"])
    {'x': 2, 'y': 1}
    """
    unique_values = {i: 0 for i in list(set(lst))}
    for i in lst:
        if i in unique_values.keys():
            unique_values[i] += 1
    return unique_values

def mode(lst): # It returns all modes of the input.
    """
    >>> mode(["x","y","x"])
    ['x']
    >>> mode(["x","y","x","y","z"])
    ['x', 'y']
    >>> mode([3,3,4,4,5,5,6])
    [3, 4, 5] 
    """
    unique_values = {i: 0 for i in list(set(lst))}
    for i in lst:
        if i in unique_values.keys():
            unique_values[i] += 1
    maks = max(unique_values.values())
    return [i for i in list(unique_values) if unique_values[i] == maks]
