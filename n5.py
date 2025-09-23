bool = False
x = input("Введите число чтобы узнать, является ли оно магическим: ")
num_sum = 0
if(int(x) % 7 == 0):
    print("magic")
else:
    bool = True
    num_sum = sum(list(map(int, list(x))))
if bool == True:
    print(num_sum)