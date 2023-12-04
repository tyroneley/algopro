class MainClass:
    def __init__(self, foodName, foodAmount):
        self.__foodName = foodName
        self.__foodAmount = foodAmount
        self.__standardPrice = self.__storeFood()
        self.__calculatedPrice = self.calculatePriceTV()
        return self

    def __storeFood(self):
        if self.__foodName == "Dry Cured Iberian Ham":
            self.__standardPrice = 177.80
        elif self.__foodName == "Wagyu Steak":
            self.__standardPrice = 450.00
        elif self.__foodName == "Matsutake Mushrooms":
            self.__standardPrice = 272.00
        elif self.__foodName == "Kopi Luwak Coffee":
            self.__standardPrice = 306.50
        elif self.__foodName == "Moose Cheese":
            self.__standardPrice = 487.20
        elif self.__foodName == "White Truffles":   
            self.__standardPrice = 3600.00
        elif self.__foodName == "Blue Fin Tuna":
            self.__standardPrice = 3603.00
        elif self.__foodName == "Le Bonnotte Potatoes":
            self.__standardPrice = 270.81
        
    def calculatePriceTV(self):
        print(self.__standardPrice)
        self.__calculatedPrice = self.__foodAmount * self.__standardPrice
    
    def __str__(self):
        return f"{self.__foodName}, {self.__foodAmount}, {self.__standardPrice}, {self.__calculatedPrice}"
