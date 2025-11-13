x = int(input("Введите число чтобы узнать, является ли оно магическим: "))
num_sum = 0
if not x % 7:
    print("Magic")
else:
    while x != 0:
        num_sum += x % 10
        x//=10
    print(num_sum)