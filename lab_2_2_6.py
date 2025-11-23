def unique_elements(items):
    unique = dict()
    for item in items:
        if type(item) == int:
            unique[item] = 1
        else:
            temp = unique_elements(item)
            for elem in temp:
                unique[elem] = 1
    return list(unique.keys())