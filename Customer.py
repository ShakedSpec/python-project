import Person


class Customer(Person.Person):
    def __init__(self, firstname, lastname, Id, age, phoneNumber, married, 
                  balance, bankNumber):
        super().__init__(firstname, lastname, Id, age, phoneNumber, married)
        self.account_number = bankNumber
        self.positive_Balance = False
        self.balance=balance


    def get_bank_account_number(self):
        return self.account_number
    def get_balance(self):
        return self.balance

    

 