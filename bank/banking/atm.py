
from utils.input import read_value
import banking.banking_exceptions as ex
from bank import Bank

class ATM(Bank): #ATM is NOT a type of BankAccount
    def __init__(self, bank):
        self._bank=bank
        self._keyboard=read_value
        
    def start(self):
        while True:
            print('ATM Menu')
            self._account_number= self._keyboard('Account Number?',int)
            self._password= self._keyboard('Password?')
            if self.authenticate(self._account_number, self._password) :
                self._user_menu()


    def _do_open_account(self):
        name=self._keyboard('name?')
        password=self._keyboard('password?')
        balance=self._keyboard('initial deposit?',int)
        type_of_account=self._keyboard('type?')
        account_number = self.open_account(name,password,balance,type_of_account)
        self._show_message(f'Your new account number is {account_number}')

    def _user_menu(self):
        
        while True:
            try:
                choice=self._keyboard('1.Deposit\t2.Withdraw\t3.Check Balance\t4. Transfer\t5. Close\t0.Exit\nChoose:',int)
                if choice==1:
                    self._do_deposit()
                elif choice==2:
                    self._do_withdraw()
                elif choice==3:
                    self._do_check_balance()
                elif choice==4:
                    self._do_transfer()
                elif choice==5:
                    self._do_close()
                elif     choice==0:
                    return
                else:
                    print('invalid choice. Retry')
            except ex.BankingException as e:
                print(f'ERROR with account {e._account_number}: {e}')
            print()
    

    def _do_close(self):
        if self._keyboard('To Close Account type "CLOSE ACCOUNT"?')=="CLOSE ACCOUNT":
            amount= self.close_account(self._account_number, self._password)
            self._show_message('account closed')
            self._dispense_cash(amount)
            

    def _do_deposit(self):
        amount = self._keyboard('Amount to Deposit? ',int)
        self.deposit(self._account_number, amount)
        self._show_message('Amount Deposited')
        
    def _do_withdraw(self):
        amount = self._keyboard('Amount to Withdraw? ',int)
        
        self.withdraw(self._account_number, amount,self._password)
        self._dispense_cash(amount)
        


    def _do_transfer(self):
        amount = self._keyboard('Amount to Transfer? ',int)
        to_account=self._keyboard('Transfer to ?', int)
        self.transfer(self._account_number, amount,self._password,to_account)
        self._show_message('Amount Transferred')
        


    def _do_check_balance(self):
        self._show_message(self.get_balance(self._account_number,self._password))



    def _dispense_cash(self, amount):
        print(f'Please take your cash {amount}')

    def _show_message(self,message):
        print(message)



