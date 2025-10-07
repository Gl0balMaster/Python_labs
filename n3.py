check = True
x = input("Введите пароль длинной больше 16 символов и без спец символов: ")
if len(x) < 16 :
    print("слишком короткий пароль")
    check = False
elif x.isalpha():
    print("Пароль содержит только буквы")
    check = False
elif x.isdigit():
    print("пароль содержит только цифры")
    check = False
elif not x.isidentifier():
        print("есть спец символы")
        check = False

if check :
    print("пароль подходит")