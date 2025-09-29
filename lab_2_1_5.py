x = input()
y = input()

let1 = dict()
let2 = dict()

for num in x.split():
    if(let1.get(num) == None):
        let1[num] = 1
    else:
        let1[num]+=1

for num in x.split():
    if(let1.get(num) == None):
        let1[num] = 1
    else:
        let1[num]+=1

sorted(let1)
sorted(let2)

bool = True

for key, value in let1.items:
    if(let2.get(key) == None or let2.get(key) != value):
        bool = False
        break


if(bool == False):
    print("не аннограмма")
else:
    print("аннограмма")