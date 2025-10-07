x = int(input("Введите сумму для размена купюрами по 100, 50, 10, 5, 2, 1: "))
hundreds = int(x/100)
x-=hundreds*100
fifties = int(x / 50)
x-=fifties* 50
tens=int(x/10)
x-=tens*10
fives=int(x/5)
x-=fives*5
two = int(x/2)
x-=2*two
ones = int(x/1)
x-=ones
print(f"100: {hundreds}, 50: {fifties}, 10: {tens}, 5: {fives}, 2: {two}, 1: {ones}")