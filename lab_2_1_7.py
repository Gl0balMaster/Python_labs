x = input("Введите строку ")

counter = 1
comprStr = ""
if(len(x) == 1):
    print(x)
else:
    for i in range(0,len(x) - 1):
        if(x[i] == x[i+1]):
            counter+=1
        else:
            comprStr+=x[i]
            comprStr+=str(counter)
            counter = 1

print(comprStr)