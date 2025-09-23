check = True
x = input("Введите пароль длинной больше 16 символов и без спец символов: ")
if(len(x) <16):
    print("слишком короткий пароль")
    check = False
else:
    if(x.isidentifier() == False):
        print("есть спец символы")
        check = False

if(check == True):
    print("пароль подходит")