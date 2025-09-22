x=input("введите ip адрес: ")
if(len(x) != 15):
    print("Не правильная длинна")

bool = True
x=x.split('.')
for num in x:
    if(not num.isdigit() or not (0<int(num) and int(num)<=255)):
        bool = False
if(bool == 1 and len(x) == 4):
    print("коректный ip")
else:
    print("не коректный ip")