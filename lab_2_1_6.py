x = input("Введите список через одинарный пробел ")
arr = dict()
words = x.split()


for word in words:
    if arr.get(word) == None:
        arr[word] = 1
    else:
        arr[word]+=1

for word in arr:
    print(word)