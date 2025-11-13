import random
x = random.randint(1,100)
y = 0
while y!=x:
    y = int(input("введите число "))
    if(y<x):
        print("меньше загаданного")
    elif(y>x):
        print("больше загаданного")
    else:
        print("вы угадали")
        break
