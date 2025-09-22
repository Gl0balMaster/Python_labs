chars = ['a', 'e', 'i', 'o', 'u']
x= input("введите строку ")
for char in chars:
    x = x.replace(char,'')
print(x)