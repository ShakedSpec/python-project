import Person


class Employee(Person):
    def __init__(self, firstname, lastname, Id, age, phoneNumber, married, partner, serialNumber, salary,
                 experience_In_Years, bonus):
        super().__init__(firstname, lastname, Id, age, phoneNumber, married, partner)
        self.serialNumber = serialNumber
        self.salary = salary
        self.experience_In_Years = experience_In_Years
        self.bonus = 0

    def set_bonus(self, amount):
        if amount > 0:
            self.bonus += amount

    def show(self):
        print("\nEmployee name: " + self.firstName + " " + self.lastName + "\nage: " + str(self.age)
              + "\nsalary for an hour: " + str(self.salary) + " shekels\n")

    def calculate_salary(self, hours):
        amount = (hours * (self.salary + 0.5 * self.experience_In_Years)) + self.bonus
        print("\nThe salary of " + self.firstName + " " + self.lastName + " is " + str(amount) + " shekels")
        return amount
