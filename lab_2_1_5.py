x = input()
y = input()

let1 = dict()
let2 = dict()

for num in x.split():
    if let1.get(num) is None:
        let1[num] = 1
    else:
        let1[num]+=1

for num in y.split():
    if let2.get(num) is None:
        let2[num] = 1
    else:
        let2[num]+=1

checker = True

for key, value in let1.items():
    if let2.get(key) is None or let2.get(key) != value:
        checker = False
        break

for key, value in let2.items():
    if let1.get(key) is None or let1.get(key) != value:
        checker = False
        break

if not checker:
    print("не аннограмма")
else:
    print("аннограмма")