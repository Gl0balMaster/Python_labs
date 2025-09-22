check = True
x = input()
if(len(x) <16):
    print("too small")
    check = False
else:
    for char in x:
        if(not char.isalpha() and not char.isdigit()):
            print("have special")
            check = False
            break
        
if(check == True):
    print("all good")