x = input("Введите числа через пробел: ")
nums = x.split()
numstyped = []
for num in nums:
    if num.count('.') == 1:
        numstyped.append(float(num))
    else:
        numstyped.append(int(num))

dict_count = dict()
unique = []
repeat = []
div2 = []
ndiv2 = []
neg = []
fl = []
div5 = 0

maximum = max(numstyped)
minimum = min(numstyped)

for num in numstyped:
    num_str = str(num)
    if dict_count.get(num_str) is not None:
        dict_count[num_str] += 1
    else:
        dict_count[num_str] = 1

    if type(num) == int:
        if num % 2 == 0:
            div2.append(num)
        else:
            ndiv2.append(num)

    if num < 0:
        neg.append(num)

    if type(num) == float:
        fl.append(num)

    if num % 5 == 0:
        div5 += num

for num_str, count in dict_count.items():
    num_value = float(num_str) if '.' in num_str else int(num_str)
    if count == 1:
        unique.append(num_value)
    else:
        if num_value not in repeat:
            repeat.append(num_value)

print("Уникальные числа:", unique)
print("Повторяющиеся числа:", repeat)
print("Четные числа:", div2)
print("Нечетные числа:", ndiv2)
print("Отрицательные числа:", neg)
print("Числа с плавающей точкой:", fl)
print("Сумма чисел кратных 5:", div5)
print("Максимальное число:", maximum)
print("Минимальное число:", minimum)