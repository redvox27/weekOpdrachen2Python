def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())

    return res

def capitalize_all_with_comprehension(array):

    array = [char.capitalize() for char in array]
    return array

arr = ["A", "b", "C", "d"]

print(capitalize_all_with_comprehension(arr))

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)

    return res

def only_upper_with_comprehension(array):
    array = [char for char in array if char.isupper()]
    return array

print(only_upper_with_comprehension(arr))