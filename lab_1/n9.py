x=input("введите ip адрес: ")
bool = True
if(len(x) != 15):
    print("Не правильная длинна")
else:
    x=x.split('.')
    if(len(x) != 4):
        bool = False
    if(not x[0].isdigit() or not (0<int(x[0]) and int(x[0])<=255)):
        bool = False
    if(not x[1].isdigit() or not (0<int(x[1]) and int(x[1])<=255)):
        bool = False
    if(not x[2].isdigit() or not (0<int(x[2]) and int(x[2])<=255)):
        bool = False
    if(not x[3].isdigit() or not (0<int(x[3]) and int(x[3])<=255)):
        bool = False

if(bool == 1 and len(x) == 4):
    print("коректный ip")
else:
    print("не коректный ip")