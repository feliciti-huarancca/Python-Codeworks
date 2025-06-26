from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, price_per_day):
        self.__make = make
        self.__price_per_day = price_per_day

    @property
    def make(self):
        return self.__make
    
    @property
    def price_per_day(self):
        return self.__price_per_day
    
    @make.setter
    def make(self, value):
        if isinstance(value, str):
            self.__make = value
        else:
            print("Make must be a string")
        
    @price_per_day.setter
    def price_per_day(self, value):
        if isinstance(value, int):
          self.__price_per_day = value
        else:
          print("Make must be a int")

    @abstractmethod
    def show_details(self):
        pass

    def rent(self, days):
        if days > 0:
            print(f'The rent will cost: {days * self.price_per_day}')
        else: 
            print('Please provide a valid number of days')
    
class Car(Vehicle):
    def __init__(self, make, price_per_day, doors):
        self.doors = doors
        super().__init__(make, price_per_day)
    
    def show_details(self):
        print('Car Details')
        print(f'🚗 Make by: {self.make}')
        print(f'💰 Price per day: {self.price_per_day}')
        print(f'🚗 Doors: {self.doors}')

class Bike(Vehicle):
    def __init__(self, make, price_per_day):
        super().__init__(make, price_per_day)

    def show_details(self):
        print('Bike Details')
        print(f'🚗 Make by: {self.make}')
        print(f'💰 Price per day: {self.price_per_day}') 


carro = Car(1980, 20000, 4)
carro.show_details()
print(carro.price_per_day)
carro.price_per_day = 100
carro.show_details()
carro.rent(4)