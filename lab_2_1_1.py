input_string = input("Введите строку из слов")
words =  input_string.split()
dictionary = dict()
unique  = 0
for word in words:
    word = word.lower()
    if not dictionary.get(word.lower()) is None:
        dictionary[word.lower()]+=1
    else:
        dictionary[word.lower()] = 1
unique = len(dictionary)
print("строка в формате слово : значение",dictionary)
print("количество уникальных слов: ", unique)