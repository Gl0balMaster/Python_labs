months = [31,28,31,30,31,30,31,31,30,31,30,31]
x=input("введите дату рождения в ф0рмате дд.мм.гг ")
x = x.split('.')
days = 0
for i in range(0,int(x[1]) - 1):
    days+=months[i]
days+=int(x[0])

if(days >= 20 and days <= 49):
    print("водолей")
elif(days >= 50 and days <= 79):
    print("рыбы")
elif(days >= 80 and days <= 109):
    print("овен")
elif(days >= 110 and days <= 140):
    print("телец")
elif(days >= 141 and days <= 171):
    print("близнецы")
elif(days >= 172 and days <= 203):
    print("рак")
elif(days >= 204 and days <= 234):
    print("лев")
elif(days >= 235 and days <= 265):
    print("дева")
elif(days >= 266 and days <= 295):
    print("весы")
elif(days >= 296 and days <= 325):
    print("скорпион")
elif(days >= 326 and days <= 355):
    print("стрелец")
elif((days >= 356 and days <= 365) or (days >= 0 and days <= 19)):
    print("козерог")