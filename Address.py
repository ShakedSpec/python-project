class Address(object):
    def __init__(self, cityName, streetName, numHouse):
        self.cityName = cityName
        self.streetName = streetName
        self.numHouse = numHouse

    def changeAddress(self, newCityName, newStreetName, newHouseNum):
        self.cityName = newCityName
        self.streetName = newStreetName
        self.numHouse = newHouseNum

    def show(self):
        print("\nAddress: City Name: " + self.cityName + "\nStreet Name: " + self.streetName + " " + str(self.numHouse))

