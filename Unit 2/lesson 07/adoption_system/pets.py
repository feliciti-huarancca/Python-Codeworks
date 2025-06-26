from abc import ABC, abstractmethod

class Pet(ABC):
  def __init__(self, name, breed, age, found_date = 0):
    self.name = name
    self.breed = breed
    self.age = age
    self.found_date = found_date

  @abstractmethod
  def behavior(self):
    pass

  def show_details(self):
    print(f'{self.name} the {self.breed}, Age: {self.age}, Time in Shelter {self.found_date}')

class Dog(Pet):
  def __init__(self, name, breed, age, found_date, is_smart):
    super.__init__(name, breed, age, found_date)
    self.is_smart = is_smart

  def behavior(self):
    if self.is_smart:
      return 'It is good with commands and loves to fetch'
    else:
      return 'Aggresive and barks at the mail man'

class Cat(Pet):
  def __init__(self, name, breed, age, found_date, is_trait):
    super.__init__(name, breed, age, found_date)
    self.is_trait = is_trait

  def behavior(self):
    if self.is_trait:
      return 'This cat has special traits 😸'
    return 'This cat is boring 🐈'

bruno =  Pet('Bruno', 'Aussie', 1, 2024)
bruno.show_details()