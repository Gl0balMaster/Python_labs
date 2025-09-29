x = input("Введите числа через пробел: ")
nums = x.split(' ')
numstyped = []
for num in nums:
    if(num.count('.') == 1):
        numstyped.append(float(num))
    else:
        numstyped.append(int(num))



dict = dict()
unique = 0
repeat  =  []
div2 = []
ndiv2 = []
neg = []
fl = []
div5 = 0
maximum = max(nums)
minimum = min(nums)
for num in nums:
    if(dict.get(num) != None):
        dict[num]+=1
    else:
        dict[num] = 1

for num in numstyped:
    if(type(num) == int):

        if(num % 2 == 1):
            ndiv2.append(num)
        elif(num % 2 == 0):
            div2.append(num)
    if(num < 0 ):
        neg.append(num)
    if(type(num) == float):
        fl.append(num)
    if(num % 5 == 0):
        div5 += num

for num in dict:
    unique+=1

print(unique)
print(repeat)
print(div2)
print(ndiv2)
print(neg)
print(fl)
print(div5)
print(maximum)
print(minimum)

