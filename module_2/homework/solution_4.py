def sort_objects(list, key):
    list.sort(key=lambda x: x[key])
    return list

list_dict = [{'a': 35, 'b': 108, 'c': 47}, {'a': 94, 'b': 1037, 'c': 40385}, {'a': 368, 'b': 56, 'c': 54}]

print(sort_objects(list_dict, 'b'))