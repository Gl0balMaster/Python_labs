def flatten_list(items):
    for k in range(0,len(items)):
        if type(items[0]) == list:
            for i in range(0,len(items[0])):
                items.append(items[0][i])
        else:
            items.append(items[0])
        items.pop(0)
        
    for item in items:
        if type(item) != int:
            flatten_list(items)