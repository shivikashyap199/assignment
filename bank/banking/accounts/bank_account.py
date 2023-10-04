import banking.banking_exceptions as ex

class BankAccount: #BankAccount is NOT a type of Bank
    def __init__(self, accountNumber, name, password, balance):
        self._account_number=accountNumber
        self._name=name
        self._password=password
        self._balance=balance

    def authenticate(self, password):
        if password!=self._password:
            raise ex.InvalidCredentialsException(self._account_number, 'Invalid Credentials')
        

    def change_password(self, oldPassword, newPassword):
        self.authenticate(oldPassword)
        #if we reach here, that means authenticatio is success
        self._password=newPassword
       
    def _validate_amount(self, amount):
        if amount<0:
            raise ex.InvalidDenominationException(self._account_number,'Amount Must be Positive')

    def deposit(self, amount):
        self._validate_amount(amount)
        self._balance+=amount
    def __str__(self):
        return f'BankAccont[AccountNumber={self._account_number},Name={self._name},Balance={self._balance}]'
    
class SavingsAccount(BankAccount):
    def __init__(self, account_nummber, name, password, initial_balance):
        super().__init__(account_nummber, name, password, initial_balance)
    def withdraw(self, amount, password):
        self._validate_amount(amount)
        self.authenticate(password)
        if self._balance <0 :
            raise ex.InsufficentBalanceException(self._account_number, amount-self._balance)
        min_balance = 5000
        max_withdrawal = self._balance - min_balance
        if amount <= max_withdrawal:
            self._balance -= amount

    def credit_interest(self):
        self._balance+=(self._balance*5.5)/1200


class CurrentAccount(BankAccount):
    def __init__(self,account_nummber, name, password, initial_balance):
        super().__init__(account_nummber, name, password, initial_balance)

    def withdraw(self, amount, password):
        self._validate_amount(amount)
        self.authenticate(password)
        if self._balance <0 :
            raise ex.InsufficentBalanceException(self._account_number, amount-self._balance)
        if amount <= self._balance:
            self._balance -= amount

    def credit_interest(self):
       print("no intrest")


class OverdraftAccount(BankAccount):
    def __init__(self,account_nummber, name, password, initial_balance):
        super().__init__(account_nummber, name, password, initial_balance)
        self.od_limit = 0.1 * self._balance
        self.od_fee = 0

    def withdraw(self, amount, password):
        self._validate_amount(amount)
        self.authenticate(password)
        if self._balance <0 :
            raise ex.InsufficentBalanceException(self._account_number, amount-self._balance)
        max_withdrawal = self._balance + self.od_limit
        if amount <= max_withdrawal:
            self._balance -= amount
            if self._balance < 0:
                self.od_fee += 0.01 * abs(self._balance)

    def credit_interest(self):
        self._balance+=(self._balance*5.5)/1200
