def merge_dicts(dict_1, dict_2):
    for item in dict_2:
        if item in dict_1:
            if type(dict_1[item]) == type(dict_2[item]):
                if type(dict_1.get(item)) == int:
                    dict_1[item] = dict_2[item]
                elif isinstance(dict_1[item], dict):
                    merge_dicts(dict_1[item], dict_2[item])
                else:
                    dict_1[item] = dict_2[item]
            else:
                temp_list = list()
                temp_list.append(dict_1[item])
                temp_list.append(dict_2[item])
                dict_1[item] = temp_list
        else:
            dict_1[item] = dict_2[item]
    return dict_1