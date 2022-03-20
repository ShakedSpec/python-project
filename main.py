from Address import Address
import Employee
import Person
import Customer

def main():

  daniel=Person.Person("shaked","spec",3333,30,"050","no",0,123)
  daniel.show()
  shaked=Customer.Customer("shaked","spector",308132281,34,"050","yes",4000,777)
  shaked.show()
  address1=Address("Netanya","Pinhas Lavon",29)
  address1.show
  shaked_bnumber=shaked.get_bank_account_number()

  print("shaked balance: {}".format(shaked.get_balance()))
  print("shaked's Bank number: {}".format(shaked_bnumber))
if __name__ == "__main__":
    main()