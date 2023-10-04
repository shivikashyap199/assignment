from banking.accounts.bank_account import BankAccount
from banking.accounts.bank_account import SavingsAccount,OverdraftAccount,CurrentAccount
import banking.banking_exceptions as ex

class Bank:
    def __init__(self, name,interest_rate):
        self. _name=name
        self.interest_rate=interest_rate
        self._last_id=0
        self._accounts=[]

    def open_account(self, name, password, balance,account_type):
        self._last_id+=1
        account = account_type(self._last_id, name, password, balance)
        self._accounts.append(account)
        return account

    def close_account(self, account_number, password):
        account=self._get_account(account_number)
        
        account.authenticate(password)
        
        if account._balance<0:
            raise ex.InsufficentBalanceException(account_number, - account._balance)
        
        self._accounts.remove(account)
        return account._balance
    
    def _get_account(self, account_number):
        for account in self._accounts:
            if account._account_number==account_number:
                return account
        raise ex.InvalidAccountNumberException(account_number,f'Invalid Account {account_number}')

    def deposit(self, amount):
        self._validate_amount(amount)
        self._balance+=amount

    def authenticate(self, account_num, password):
        account = self.get_account(account_num)
        if account:
            return account._password == password
        raise ex.IncorrectPassword
        
    def transfer(self, source_account, amount, password, target_account):
        source=self._get_account(source_account)
        target=self._get_account(target_account)
        
        source.withdraw(amount,password)
        target.deposit(amount)

    def get_balance(self, account_number, password):
        account=self._get_account(account_number)
        if account is not None and account.authenticate(password):
            return account._balance
        else:
            return None

    def get_account_list(self):
        str=''
        for account in self._accounts:
            str+=f'{account}\n'

        return str

