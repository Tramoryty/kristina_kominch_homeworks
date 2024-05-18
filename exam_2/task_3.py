# 3) Создайте систему управления банковскими счетами, которая позволяет создавать,
# управлять и выполнять операции с банковскими счетами различных клиентов.
# 1.	Реализуйте класс Client, представляющий клиента банка. Класс должен иметь
# атрибуты name (имя клиента) и id (уникальный идентификатор клиента).
# 2.	Реализуйте класс BankAccount, представляющий банковский счет. Класс должен
# иметь атрибуты account_number (номер счета), balance (баланс счета) и client (объект
# типа Client, которому принадлежит счет). Класс также должен иметь методы deposit(amount)
# и withdraw(amount), которые позволяют пополнить или снять деньги со счета.
# 3.	Реализуйте класс Bank, представляющий банк. Класс должен иметь атрибут accounts,
# который является словарем, где ключами являются номера счетов, а значениями -
# объекты типа BankAccount. Класс также должен иметь методы create_account(client, initial_balance)
# для создания нового счета и get_account(account_number) для получения счета по его номеру.
# 4.	Добавьте в класс Bank методы для выполнения переводов между счетами
# (transfer(sender_account, receiver_account, amount)), а также для получения
# общего баланса клиента (get_total_balance(client)), который включает сумму денег на всех его счетах.
# 5.	Реализуйте обработку ошибок, например, недостаточно средств на счете при
# снятии денег или отсутствие счета при переводе.

class Client:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class BankAccount:
    def __init__(self, account_number, client, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        self.client = client

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Пополнение счета {self.account_number}: {amount}.\n'
                  f'Новый баланс: {self.balance}.')
        else:
            print('Сумма для пополнения баланса должна быть положительной.')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Недостаточно средств на счете.')
        elif amount <= 0:
            print('Сумма снятия должна быть положительной.')
        else:
            self.balance -= amount
            print(f'Снятие средств со счета {self.account_number}: {amount}.\n'
                  f'Новый баланс: {self.balance}.')


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, client, initial_balance):
        import random
        account_number = random.randrange(10**23, 10**24)
        new_account = BankAccount(account_number, client, initial_balance)
        self.accounts[account_number] = new_account
        print(f'Создан новый номер счета: {account_number}.\n'
              f'Клиент: {client.name}.\n'
              f'Начальный баланс: {initial_balance}.\n')
        return new_account

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            for account in self.accounts.values():
                if account.client.id == account_number:
                    return account
            print('Счет с таким номером или ID не найден.')
            return None

    def transfer(self, sender_account_number, receiver_account_number, amount):
        sender_account = self.get_account(sender_account_number)
        receiver_account = self.get_account(receiver_account_number)
        if sender_account and receiver_account:
            if sender_account.balance >= amount:
                sender_account.withdraw(amount)
                receiver_account.deposit(amount)
                print(f'Перевод {amount} со счета {sender_account_number} '
                      f'на счет {receiver_account_number} выполнен успешно.')
            else:
                print('Недостаточно средств на счете отправителя.')
        else:
            print('Ошибка при выполнении перевода.')

    def get_total_balance(self, client):
        total_balance = sum(account.balance for account in self.accounts.values() if account.client == client)
        print(f'Общий баланс для клиента {client.name}: {total_balance}.')
        return total_balance


client1 = Client('Первый Клиент', 1)
client2 = Client('Второй Клиент', 2)

bank = Bank()

account1 = bank.create_account(client1, 1000)
account2 = bank.create_account(client2, 500)

account1.deposit(500)
account1.withdraw(200)
account2.deposit(300)
account2.withdraw(1000)

bank.transfer(account1.account_number, account2.account_number, 300)
bank.transfer(account2.account_number, account1.account_number, 1000)

bank.get_total_balance(client1)
bank.get_total_balance(client2)

print(f'Найденный счет для клиента с ID 1: {bank.get_account(1).account_number}')
print(f'Найденный счет для клиента с ID 2: {bank.get_account(2).account_number}')
