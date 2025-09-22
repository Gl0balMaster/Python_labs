bool  = True
x = input("введите число: ")
for i in range(0,len(x)):
    if(x[i] != x[len(x) - i - 1]):
       bool = False

if(bool == 1):
    print("Палиндром")
else:
    print("не палиндром")