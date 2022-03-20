
# Main class
from Customer import Customer
import ctypes

class BankSystem:

    def __init__(self):   
        self.customers = {}
        self.employees = {}

    def addEmployee(self, employee):
        self.employees.append(employee)

    def addCustomer(self, customer):
        self.customers[customer.account_number]=customer
    def get_customer_by_account_number(self, bankNumber):
           return self.customers[bankNumber]
       

      

