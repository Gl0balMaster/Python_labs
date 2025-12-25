x = input("введите первый набор чисел")
y = input("введите второй набор чисел")

xs = x.split()
xy = y.split()
numx = {float(num) for num in xs}
numsx = frozenset(numx)
numy = {float(num) for num in xy}
numsy = frozenset(numy)

cross = numsx.intersection(numsy)
print(cross)
xwoy = numsx.difference(numsy)
print(xwoy)
ywox = numsy.difference(numsx)
print(ywox)
sumxy = numsx.union(numsy)
wocross = sumxy.difference(cross)
print(wocross)