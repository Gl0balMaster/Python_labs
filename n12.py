# minutes,sms,internet,base
data = [60,30,1024,24.99]
min = int(input("введите кол-во израсходованных минут "))
sms = int(input("введите кол-во израсходованных смс "))
internet = int(input("введите кол-во израсходованных мегабайт "))
min = 0 if min<int(data[0]) else (min-int(data[0]))*0.89
sms = 0 if sms<int(data[1]) else (sms-int(data[1]))*0.59
internet = 0 if internet<int(data[2]) else (internet-int(data[2]))*0.79
price = data[3] + min+sms+internet
print("базовая цена ", data[3], "дополнительно за смс", sms, "дополнительно за минуты ", min, "дополнительно за интернет", internet, "финальная цена", price)