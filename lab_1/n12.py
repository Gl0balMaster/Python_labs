minutes_def = 60
sms_def = 30
internet_def = 1024
base = 24.99

minutes = int(input("введите кол-во израсходованных минут "))
sms = int(input("введите кол-во израсходованных смс "))
internet = int(input("введите кол-во израсходованных мегабайт "))
minutes = 0 if minutes<minutes_def else (minutes-minutes_def)*0.89
sms = 0 if sms<sms_def else (sms - sms_def)*0.59
internet = 0 if internet<internet_def else (internet-internet_def)*0.79
price = base + minutes+sms+internet
print("базовая цена ", base, "дополнительно за смс", sms, "дополнительно за минуты ", minutes, "дополнительно за интернет", internet, "финальная цена", price)