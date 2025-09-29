str = input("Введите строку из слов")
words =  str.split()
dict = dict()
unique  = 0
for word in words:
    word.lower()
    if(dict.get(word.lower()) != None):
        dict[word.lower()]+=1
    else:
        dict[word.lower()] = 1
for word in dict:
    unique +=1
print("строка в формате слово : значение",dict)
print("unique word amount: ", unique)