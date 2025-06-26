from abc import ABC, abstractmethod

class Dog(ABC): # Abstract Base Class for Dog
    def __init__(self, name, age, owner_phone):
        self.__name = name
        self.__age = age
        self.__owner_phone = owner_phone

    def print_owner_phone(self):
        print(f"Owner's phone number: {self.__owner_phone}")

    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    @property
    def owner_phone(self):
        return self.__owner_phone
    
    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age

    @owner_phone.setter
    def owner_phone(self, phone):
        self.__owner_phone = phone

    @abstractmethod
    def makes_sound(self): # this is an abstract method, # subclasses must implement it
        pass
    
    @abstractmethod
    def perform_trick(self):
        print(f"{self.name} performs a trick! 🐾")


#dog = Dog("Buddy", 5, '123-456-7890')
#print(dog.name)
#dog.makes_sound()
#print(dog.name)
#dog.name = "Max"
#print(dog.name)

# Abstract class example
class Schnauzer(Dog):
    def makes_sound(self):
        print("Woof! Woof!")

    def perform_trick(self):
        print(f"{self.name} rolls over! 🐶")

class Buddy(Dog):
    def makes_sound(self):
        print("Bark! Bark!")

    def perform_trick(self):
        print(f"{self.name} plays dead! 🐕")


my_dog = Schnauzer('Perla', 15, '123-456-7890')
my_dog.makes_sound()