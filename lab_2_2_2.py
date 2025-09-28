def merge_dicts(dict_1, dict_2):
    for item in dict_2:
        if (dict_1.get(item) != None):
            if (type(dict_1[item]) == type(dict_2[item])):
                if(type(dict_1.get(item)) == int):
                    dict_1[item] = dict_2[item]
                
                else:
                    merge_dicts(dict_1[item],dict_2[item])
        
            else:
                temp_dict = list()
                temp_dict.append(dict_1[item])
                temp_dict.append(dict_2[item])
                dict_1[item] = temp_dict
        
        else:
            dict_1[item] = dict_2[item]