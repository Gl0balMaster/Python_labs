bool = False
x = int(input())
sum = 0
if(x%7 == 0):
    print("magic")
else:
    bool = True
    while(x !=0):
        sum+= x %10;
        x//=10
if bool == True:
    print(sum)