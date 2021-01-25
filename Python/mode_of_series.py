def mode_dict(lst):
    unique_values = {i: 0 for i in list(set(lst))}
    for i in lst:
        if i in unique_values.keys():
            unique_values[i] += 1
    return unique_values

def mode(lst):
    unique_values = {i: 0 for i in list(set(lst))}
    for i in lst:
        if i in unique_values.keys():
            unique_values[i] += 1
    maks = max(unique_values.values())
    return [i for i in list(unique_values) if unique_values[i] == maks]
