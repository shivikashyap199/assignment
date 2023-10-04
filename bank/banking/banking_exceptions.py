

class BankingException(Exception):
    def __init__(self, account_number, message=None):
        if not message:
            message= type(self).__name__ 
        super().__init__(message)
        self._account_number = account_number

class InvalidAccountNumberException(BankingException):
    pass

class InvalidCredentialsException(BankingException):
    pass

class InsufficentBalanceException(BankingException):
    def __init__(self,account_number, deficit=0, message='Insuffcient Balance'):
        super().__init__(account_number, message)
        self._deficit=deficit
        
    def get_deficit_amount(self): return self._deficit

class InvalidDenominationException(BankingException):
    pass


