class Person():
    def __init__(self, firstname, lastname, Id, age, phoneNumber, married):
        self.firstName = firstname
        self.lastName = lastname
        self.Id = Id
        self.age = age
        self.phoneNumber = phoneNumber
        self.married = married
        

    def marry(self, new_lastname, partnerName):
        if new_lastname != self.lastName:
            self.lastName = new_lastname
        self.partner = partnerName
        self.married = True

    def divorce(self):
        self.married = False

    def show(self):
        print("\nPerson name: " + self.firstName + " " + self.lastName + "\nId:  " + str(self.Id) + "\nage: " + str(self.age)
              + "\nPhone-number: " + str(self.phoneNumber) + " Married:\n" + self.married)