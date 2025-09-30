class Bank:

    id = 0
    clients = dict()

    def __init__(self):
        pass

    def create_client(self,name):
        client = Client(name,self.id)
        self.clients[id] = client
        self.id+=1

    def open_bank_num(self,client, curr):
        if(client.have_num_w_cur(curr)):
            print(f"счет с {curr} уже существует" )
        else:
            num = Bank_num(curr)
            client.Bank_nums[curr] = num

    def show_client_info(self,client):
        print(f"id: {client.uid} ФИО: {client.name}")
    
    def  delete_client(self,client):
        self.clients.pop(id)

class Bank_num:

    curr = ""
    value = 0
    def __init__(self,currency):
        self.curr = currency

    # показать счет
    def Show(self):
        print("Curr: " + self.curr + ", value: " + str(self.value)+"\n")

class Client:

    uid = 0
    name = ""
    # словарь валюта : счет
    Bank_nums = dict()

    def __init__(self,name,id):
        self.Bank_nums = dict()
        self.name = name
        self.uid = id

    # проверка на наличиче такого счета
    def have_num_w_cur(self,cur):
        if(self.Bank_nums.get(cur) == None):
            return False
        else:
            return True

    # показать конкретный счет
    def show_num(self,cur):
        if(self.Bank_nums[cur] != None):
            self.Bank_nums[cur].Show()

    # показать имеющиеся счета
    def Show_nums(self):       
        print(list(self.Bank_nums.keys()))

    # пополнить счет cur на amount
    def add_cur(self, cur, amount):
        if self.have_num_w_cur(cur):
            self.Bank_nums[cur].value += amount
        else:
            print("Счет " + cur +" не существует")

    # снять со счета cur кол-во amount
    def min_cur(self, cur, amount):
        if self.have_num_w_cur(cur):
            if(self.Bank_nums[cur].value < amount):
                print("Недостаточно " + cur +"\n")
            else:
                self.Bank_nums[cur].value -= amount
        else:
            print("Счет "+cur +" не существует")

    # перевести со счета cur1 на cur2 кол-во amount
    def transfer(self,cur1,cur2, amount):
        if(self.have_num_w_cur(cur1) and self.have_num_w_cur(cur2)):
            if(self.Bank_nums[cur1].value < amount):
                print("Недостаточно "+cur1+"\n")
            else:
                self.add_cur(cur2,amount)
                self.min_cur(cur1,amount)
        elif(not self.have_num_w_cur(cur1)):
            print("Счет "+cur1 +" не существует")
        else:
            print("Счет "+cur2 +" не существует")

    

b = Bank()

name = "asd ddd fff"
b.create_client(name)
for key,value in b.clients.items():
    print(f"key {key} and value {value}")

# curr_client = b.clients.get(b.id - 1)
# print(curr_client)
# b.open_bank_num(curr_client,"usd")
# b.open_bank_num(curr_client,"euro")
# b.open_bank_num(curr_client,"usd")

# b.show_client_info(curr_client)

# b.delete_client(curr_client)

# print(len(b.clients()))