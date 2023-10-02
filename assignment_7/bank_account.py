class BankAccount:
    def __init__(self, account_holder, password, initial_balance):
        self.account_holder = account_holder
        self.password = password
        self.balance = initial_balance
        self.max_balance = initial_balance
        self.od_limit = 0
        self.od_fee = 0

    def deposit(self, amount):
        self.balance += amount
        if self.balance > self.max_balance:
            self.max_balance = self.balance

    def withdraw(self, amount):
        pass

    def credit_interest(self):
        pass


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, password, initial_balance):
        super().__init__(account_holder, password, initial_balance)
    def withdraw(self, amount):
        min_balance = 5000
        max_withdrawal = self.balance - min_balance
        if amount <= max_withdrawal:
            self.balance -= amount

    def credit_interest(self):
        self.balance+=(self.balance*5.5)/1200


class CurrentAccount(BankAccount):
    def __init__(self,account_holder, password, initial_balance):
        super().__init__(account_holder, password, initial_balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def credit_interest(self):
       print("no intrest")


class OverdraftAccount(BankAccount):
    def __init__(self, account_holder, password, initial_balance):
        super().__init__(account_holder, password, initial_balance)
        self.od_limit = 0.1 * self.max_balance
        self.od_fee = 0

    def withdraw(self, amount):
        max_withdrawal = self.balance + self.od_limit
        if amount <= max_withdrawal:
            self.balance -= amount
            if self.balance < 0:
                self.od_fee += 0.01 * abs(self.balance)

    def credit_interest(self):
        self.balance+=(self.balance*5.5)/1200


class Bank:
    def __init__(self):
        self.accounts = []

    def open_account(self, account_holder, password, initial_balance, account_type):
        account = account_type(account_holder, password, initial_balance)
        self.accounts.append(account)
        return account

    def transfer(self, sender_account, amount, password, receiver_account):
        if sender_account.password == password:
            sender_account.withdraw(amount)
            receiver_account.deposit(amount)
        else:
            print("Password incorrect. Transfer failed.")


class ATM(Bank):
    def __init__(self, bank):
        self.bank = bank

    def enter_pin(self):
        self.pin= input("enter the atm password")
        if self.pin==self.bank.password:
            self.menu()
        else:
            print("Wrong password")    

    def menu(self):
        print("Enter 1 to deposit")
        print("Enter 2 to withdraw")

        option= int(input("enter you choice"))

        if option==1:
            deposit_amount= int(input("enter amount to deposit"))
            self.bank.deposit(deposit_amount)

        elif option==2:
            withdraw_amount= int(input("enter amount to withdraw"))
            self.bank.withdraw(withdraw_amount)



# Example usage:
icici = Bank()

a1 = icici.open_account('Vivek', 'p@ss', 50000, SavingsAccount)
a2 = icici.open_account('Sanjay', 'p@ss', 50000, OverdraftAccount)

icici.transfer(a1, 10000, 'p@ss', a2)

atm1= ATM(a1)
atm1.enter_pin()
atm1.transfer(a1, 10000, 'p@ss', a2)


print(a1.balance)
print(a2.balance)