def merge_sorted_list(list_a, list_b):
    result = list()
    iter_1 = 0
    iter_2 = 0
    while iter_1 < len(list_a) and iter_2 < len(list_b):
        if list_a[iter_1] < list_b[iter_2]:
            result.append(list_a[iter_1])
            iter_1 += 1
        else:
            result.append(list_b[iter_2])
            iter_2 += 1

    while iter_1 < len(list_a):
        result.append(list_a[iter_1])
        iter_1 += 1

    while iter_2 < len(list_b):
        result.append(list_b[iter_2])
        iter_2 += 1

    return result