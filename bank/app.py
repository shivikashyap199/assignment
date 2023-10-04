from banking.bank import Bank
from banking.atm import ATM


def get_bank():
    bank=Bank('ICICI',12)
    #add dummy account to the bank
    bank.open_account('Sanjay','p@ss',500000)
    bank.open_account('Prabhat','p@ss',500000)
    bank.open_account('Fagun','p@ss',500000)
    return bank


def main():
    bank=get_bank()
    atm=ATM(bank)

    atm.start()
    print('ATM shutdown')

if __name__=='__main__':
    main()