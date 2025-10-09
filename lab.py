import random

MAX_ID = 100000
cur_coef = {"usd": 2, "euro": 3, "byn": 1}  # коэфициенты обмена по сравнению к byn


class BankError(Exception):
    """Базовое исключение для банковских операций"""
    pass


class ClientNotFoundError(BankError):
    """Клиент не найден"""
    pass


class AccountNotFoundError(BankError):
    """Счет не найден"""
    pass


class InsufficientFundsError(BankError):
    """Недостаточно средств"""
    pass


class InvalidAmountError(BankError):
    """Неверная сумма"""
    pass


class CurrencyNotSupportedError(BankError):
    """Валюта не поддерживается"""
    pass


class BankFullError(BankError):
    """Банк переполнен"""
    pass


def func_log(client_id):
    def func_log_inside(func):
        def wrapper(*args, **kwargs):
            try:
                with open("Клиент_" + str(client_id) + ".txt", "a", encoding='utf-8') as file:
                    if func.__name__ == "add_cur":
                        file.write(f"На счет {args[0]} добавлено: {args[1]} {args[0]}\n")
                    elif func.__name__ == "min_cur":
                        file.write(f"Со счета {args[0]} снято: {args[1]} {args[0]}\n")
                    elif func.__name__ == "transfer":
                        file.write(f"Перевод: {args[2]} {args[0]} -> {args[1]}\n")
                    elif func.__name__ == "open_bank_num":
                        file.write(f"Открыт счет {args[1]}\n")
                    elif func.__name__ == "delete_account":
                        file.write(f"Закрыт счет {args[1]}\n")

                result = func(*args, **kwargs)
                return result
            except Exception as e:
                print(f"Ошибка логирования: {e}")
                return func(*args, **kwargs)

        return wrapper

    return func_log_inside


class BankNum:
    def __init__(self, currency):
        try:
            if currency not in cur_coef:
                raise CurrencyNotSupportedError(f"Валюта {currency} не поддерживается")
            self.curr = currency
            self.value = 0
        except CurrencyNotSupportedError as e:
            print(f"Ошибка создания счета: {e}")
            raise

    def show(self):
        try:
            print("Curr: " + self.curr + ", value: " + str(self.value) + "\n")
        except Exception as e:
            print(f"Ошибка при показе счета: {e}")


class Client:
    def __init__(self, name, uid):
        try:
            if not name or len(name.strip()) == 0:
                raise ValueError("Имя не может быть пустым")
            if uid <= 0:
                raise ValueError("ID должен быть положительным")

            self.bank_nums = dict()
            self.name = name
            self.uid = uid
        except ValueError as e:
            print(f"Ошибка создания клиента: {e}")
            raise

    def have_num_w_cur(self, cur):
        try:
            return cur in self.bank_nums
        except Exception as e:
            print(f"Ошибка проверки счета: {e}")
            return False

    def show_num(self, cur):
        def _show_num(cur):
            try:
                if not self.have_num_w_cur(cur):
                    raise AccountNotFoundError(f"Счет {cur} не существует")
                self.bank_nums[cur].show()
            except AccountNotFoundError as e:
                print(f"Ошибка: {e}")
            except Exception as e:
                print(f"Ошибка при показе счета: {e}")

        return _show_num(cur)

    def show_nums(self):
        def _show_nums():
            try:
                if not self.bank_nums:
                    print("Нет открытых счетов\n")
                    return

                for cur, account in self.bank_nums.items():
                    print(f"{cur}:  {account.value}\n")
            except Exception as e:
                print(f"Ошибка при показе счетов: {e}")

        return _show_nums()

    def add_cur(self, cur, amount, client_id):
        @func_log(client_id)
        def _add_cur(cur, amount):
            try:
                if amount <= 0:
                    raise InvalidAmountError("Сумма должна быть положительной")
                if not self.have_num_w_cur(cur):
                    raise AccountNotFoundError(f"Счет {cur} не существует")

                self.bank_nums[cur].value += amount
                print(f"Счет {cur} пополнен на {amount}\n")
            except InvalidAmountError as e:
                print(f"Ошибка: {e}")
            except AccountNotFoundError as e:
                print(f"Ошибка: {e}")
            except Exception as e:
                print(f"Ошибка при пополнении счета: {e}")

        return _add_cur(cur, amount)

    def empty(self):
        try:
            return len(self.bank_nums) == 0
        except Exception as e:
            print(f"Ошибка проверки счетов: {e}")
            return True

    def trans_empty(self):
        try:
            return len(self.bank_nums) <= 1
        except Exception as e:
            print(f"Ошибка проверки счетов: {e}")
            return True

    def cur_exist(self, cur):
        try:
            return cur in self.bank_nums
        except Exception as e:
            print(f"Ошибка проверки валюты: {e}")
            return False

    def min_cur(self, cur, amount, client_id):
        @func_log(client_id)
        def _min_cur(cur, amount):
            try:
                if amount <= 0:
                    raise InvalidAmountError("Сумма должна быть положительной")
                if not self.have_num_w_cur(cur):
                    raise AccountNotFoundError(f"Счет {cur} не существует")
                if self.bank_nums[cur].value < amount:
                    raise InsufficientFundsError(f"Недостаточно средств на счете {cur}")

                self.bank_nums[cur].value -= amount
                print(f"Со счета {cur} снято {amount}\n")
                return True

            except (InvalidAmountError, AccountNotFoundError, InsufficientFundsError) as e:
                print(f"Ошибка: {e}")
                return False
            except Exception as e:
                print(f"Ошибка при снятии средств: {e}")
                return False

        return _min_cur(cur, amount)

    def transfer(self, cur1, cur2, amount, client_id):
        @func_log(client_id)
        def _transfer(cur1, cur2, amount):
            try:
                if amount <= 0:
                    raise InvalidAmountError("Сумма должна быть положительной")
                if not self.have_num_w_cur(cur1):
                    raise AccountNotFoundError(f"Счет {cur1} не существует")
                if not self.have_num_w_cur(cur2):
                    raise AccountNotFoundError(f"Счет {cur2} не существует")
                if self.bank_nums[cur1].value < amount:
                    raise InsufficientFundsError(f"Недостаточно средств на счете {cur1}")

                self.bank_nums[cur2].value += amount * cur_coef[cur1] / cur_coef[cur2]
                self.bank_nums[cur1].value -= amount
                print(f"Перевод выполнен: {amount} {cur1} -> {cur2}\n")
                return True

            except (InvalidAmountError, AccountNotFoundError, InsufficientFundsError) as e:
                print(f"Ошибка перевода: {e}")
                return False
            except Exception as e:
                print(f"Неожиданная ошибка при переводе: {e}")
                return False

        return _transfer(cur1, cur2, amount)


class Bank:
    clients = dict()
    cur_client = Client("1", 1)

    def __init__(self):
        pass

    def create_client(self, name, uid):
        def _create(name, uid):
            try:
                if not name or len(name.strip()) == 0:
                    raise ValueError("Имя клиента не может быть пустым")
                if uid <= 0:
                    raise ValueError("ID клиента должен быть положительным числом")
                if uid in self.clients:
                    raise ValueError(f"Клиент с ID {uid} уже существует")

                client = Client(name, uid)
                self.clients[uid] = client
                self.cur_client = client
                return client
            except ValueError as e:
                print(f"Ошибка создания клиента: {e}")
                raise
            except Exception as e:
                print(f"Неожиданная ошибка при создании клиента: {e}")
                raise BankError(f"Ошибка создания клиента: {e}")

        return _create(name, uid)

    def open_bank_num(self, client, curr):
        def _open_bank_num(client, curr):
            try:
                if client is None:
                    raise ClientNotFoundError("Клиент не найден")
                if curr not in cur_coef:
                    raise CurrencyNotSupportedError(f"Валюта {curr} не поддерживается")

                if client.have_num_w_cur(curr):
                    print(f"счет с {curr} уже существует\n")
                else:
                    num = BankNum(curr)
                    client.bank_nums[curr] = num
                    print(f"Счет {curr} успешно создан\n")
            except ClientNotFoundError as e:
                print(f"Ошибка: {e}")
            except CurrencyNotSupportedError as e:
                print(f"Ошибка: {e}")
            except Exception as e:
                print(f"Неожиданная ошибка при создании счета: {e}")

        return _open_bank_num(client, curr)

    def delete_account(self, client, currency, client_id):
        @func_log(client_id)
        def _delete_account(currency):
            try:
                if currency not in client.bank_nums:
                    raise AccountNotFoundError(f"Счет с валютой {currency} не найден")

                del client.bank_nums[currency]
                print(f"Счет {currency} успешно удалён\n")
                return True

            except AccountNotFoundError as e:
                print(f"Ошибка: {e}")
                return False
            except Exception as e:
                print(f"Неожиданная ошибка при удалении счета: {e}")
                return False

        return _delete_account(currency)

    def show_client_info(self, client):
        def _show_client_info(client):
            try:
                if client is None:
                    raise ClientNotFoundError("Клиент не найден")
                print(f"uid: {client.uid} ФИО: {client.name}\n")
            except ClientNotFoundError as e:
                print(f"Ошибка: {e}")
            except Exception as e:
                print(f"Ошибка при показе информации: {e}")

        return _show_client_info(client)

    def delete_client(self, client_id):
        def _delete_client(client_id):
            try:
                if client_id not in self.clients:
                    raise ClientNotFoundError(f"Клиент с ID {client_id} не найден")

                self.clients.pop(client_id)
                print(f"Клиент {client_id} удален\n")
            except ClientNotFoundError as e:
                print(f"Ошибка: {e}")
            except Exception as e:
                print(f"Ошибка при удалении клиента: {e}")

        return _delete_client(client_id)


def start_screen(bool_free_id, bank):
    uid = 0
    choice = int(input("1. Зарегистрировать новый аккаунт\n"
                       "2. Войти в аккаунт\n"
                       "3. Выйти\n"))
    if choice == 1:
        temp = input("Введите ваше ФИО\n")
        name = temp

        while not bool_free_id:
            if len(bank.clients) < MAX_ID:
                uid = random.randint(1, MAX_ID)
                if bank.clients.get(uid) is None:
                    bool_free_id = True
            else:
                print("В банке переполнение клиентов\n")
                bool_free_id = False

        print(f"Ваш уникальный uid: {uid}\n")
        client = bank.create_client(name, uid)
        client.add_cur = func_log(client.uid)(client.add_cur)
        client.min_cur = func_log(client.uid)(client.min_cur)
        client.transfer = func_log(client.uid)(client.transfer)
        input("Нажмите Enter для продолжения...\n")
        return client

    elif choice == 2:
        uid = int(input("Введите ваш уникальный uid: \n"))
        client = bank.clients.get(uid)
        if client is None:
            print("Клиент с таким ID не найден\n")
            return None
        else:
            print(f"Добро пожаловать, {client.name}!\n")
            input("Нажмите Enter для продолжения...\n")
            return client

    elif choice == 3:
        exit(1)
    else:
        print("Неверный ввод\n")
        return None


def main():
    bool_free_id = False
    bool_full_exit = False
    bank = Bank()

    while not bool_full_exit:
        cur_client = start_screen(bool_free_id, bank)
        bool_exit = False
        while not bool_exit:
            choice = int(input("1. Создать счет\n"
                               "2. Удалить счет\n"
                               "3. Пополнить счет\n"
                               "4. Снять со счета\n"
                               "5. Перевод между вашими счетами\n"
                               "6. Ваша информация\n"
                               "7. Вывод всех средств на экран в валюте\n"
                               "8. Выйти\n"))
            uid = cur_client.uid
            if choice == 1:
                cur = int(input("1.usd\n 2.euro\n 3.byn\n 4.выход\n"))
                func = func_log(cur_client.uid)(bank.open_bank_num)
                if cur == 1:
                    func(cur_client, "usd", cur_client.uid)
                elif cur == 2:
                    func(cur_client, "euro", cur_client.uid)
                elif cur == 3:
                    func(cur_client, "byn", cur_client.uid)
                elif cur == 4:
                    pass
                else:
                    print("Неверный ввод\n")

            elif choice == 2:
                cur_client.show_nums(uid)
                cur = input("Какой счет хотите удалить?\n")
                func = func_log(cur_client.uid)(bank.delete_account)
                if cur in cur_coef:
                    func(cur_client, cur, cur_client.uid)
                else:
                    print("Неверная валюта\n")

            elif choice == 3:
                if cur_client.empty():
                    print("нет счетов для пополнения\n")
                else:
                    cur_client.show_nums(cur_client.uid)
                    temp = input("какой счет хотите пополнить\n")
                    if temp in cur_coef:
                        if cur_client.bank_nums.get(temp) is None:
                            print(f"счета {temp} не существует\n")
                        else:
                            summ_to_add = int(input("введите сумму для пополнения\n"))
                            cur_client.add_cur(temp, summ_to_add, cur_client.uid)
                    else:
                        print("неправильный ввод\n")

            elif choice == 4:
                if cur_client.empty():
                    print("нет счетов для снятия\n")
                else:
                    cur_client.show_nums(uid)
                    temp = input("с какого счета хотите снять\n")
                    if temp in cur_coef:
                        if cur_client.bank_nums.get(temp) is None:
                            print(f"счета {temp} не существует\n")
                        else:
                            summ_to_add = int(input("введите сумму для снятия\n"))
                            cur_client.min_cur(temp, summ_to_add, uid)
                    else:
                        print("неправильный ввод\n")

            elif choice == 5:
                if cur_client.trans_empty():
                    print("нет счетов для переводов\n")
                else:
                    cur_client.show_nums(uid)
                    cur_1 = input("с какого счета хотите перевести\n")
                    if cur_client.bank_nums.get(cur_1) is None:
                        print(f"счета {cur_1} не существует")
                    else:
                        cur_2 = input("на какой счет хотите перевести\n")
                        if cur_client.bank_nums.get(cur_2) is None:
                            print(f"счета {cur_2} не существует")
                        else:
                            print(
                                f"текущий курс перевода с {cur_1} в {cur_2} равен {cur_coef[cur_1] / cur_coef[cur_2]}\n")
                            confirm = int(input("вы согласны с таким курсом?\n 1. Да\n 2. Нет\n"))
                            if confirm == 1:
                                amount = int(input("сколько перевести?\n"))
                                cur_client.transfer(cur_1, cur_2, amount, uid)
                            else:
                                pass

            elif choice == 6:
                bank.show_client_info(cur_client)
                if len(cur_client.bank_nums) == 0:
                    print("нет счетов для показа\n")
                else:
                    cur_client.show_nums(uid)
                    out_in_file = int(input("Надо ли вам сделать дополнительно выписку в файл?\n 1.Да\n 2. Нет\n"))
                    if out_in_file == 1:
                        try:
                            with open("Счет_клиента_" + str(cur_client.uid) + ".txt", "w", encoding='utf-8') as file:
                                file.write(f"Выписка по счетам клиента\n")
                                file.write(f"ID клиента: {cur_client.uid}\n")
                                file.write(f"ФИО: {cur_client.name}\n")
                                file.write("=" * 40 + "\n")
                                file.write("Счета и балансы:\n")
                                for currency, account in cur_client.bank_nums.items():
                                    file.write(f"{currency}: {account.value}\n")
                                file.write("=" * 40 + "\n")
                            print(f"Выписка сохранена в файле Счет_клиента_{cur_client.uid}.txt")
                        except Exception as e:
                            print(f"Ошибка при создании выписки: {e}")
                    elif out_in_file == 2:
                        pass
                    else:
                        print("Неверный ввод")

            elif choice == 7:
                if len(cur_client.bank_nums) == 0:
                    print("у вас нет счетов в банке\n")
                else:
                    cur_client.show_nums(uid)
                    cur = input("в какой валюте вывести на экран?\n")
                    if cur in cur_coef:
                        total = 0
                        for currency, account in cur_client.bank_nums.items():
                            total += account.value * (cur_coef[currency] / cur_coef[cur])
                        print(f"На всех счетах у вас в сумме {total} {cur}\n")
                    else:
                        print("банк не поддерживает такую валюту\n")

            elif choice == 8:
                bool_exit = True
            else:
                print("Неверный ввод\n")
            input("Нажмите Enter для продолжения...\n")


main()
