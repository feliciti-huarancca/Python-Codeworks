
class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def print_details(self):
        print(f"Hi, I am {self.name}, I am {self.age} years old, and my color is {self.color}")

dog = Dog("Buddy", 5, "brown")
#dog.print_details()

perla = Dog("Perla", 15, "white")
#perla.print_details()

#Building a game -- Parent Class and Child Class

class Character:
    def __init__(self, name, health, attack_power, gold, gender = None):
        self.name = name
        self.health = health
        self.gender = gender
        self.gold = gold
        self.attack_power = attack_power

    def print_details(self):
        print(f'****** {self.name} ******')
        print(f'Health: {self.health}')
        print(f'Gold: {self.gold}')
        if self.gender:  print(f'Gender: {self.gender}')
        print(f'Attack Power: {self.attack_power}')
        print('***********************\n')

    def attack(self, enemy: 'Character'):
        print(f'{self.name} attacks ⚔️  to {enemy.name}!')
        damage = self.attack_power
        enemy.health -= damage
        print(f'Damage: {damage} 💥 | Enemy health: {enemy.health} 🔋')

    def is_alive(self):
        return self.health > 0

slate = Character('Slate', 100, 'male', 20)
kim = Character('Kim', 80, 'female', 26)
#slate.print()
#kim.print()

# Monster Class Inheritance
class Monster(Character):
    def __init__(self):
        name = 'Goblin'
        health = 40
        attack_power = 12
        gold = 5
        super().__init__(name, health, attack_power, gold)

def dungeon_room(adventurer: Character):
    print(f'You enter a dark room in the dungeon!! 🕷️🕸️🕷️')
    adventurer.print_details()
    monster = Monster()
    print('A wild monster appears! 🐉')
    monster.print_details()
    adventurer.attack(monster)
    monster.print_details()

adventurer = Character('Slate', 100, 30, 'male')
dungeon_room(adventurer)

def battle(adventurer: Character, monster: Monster):
    while adventurer.is_alive() > 0 and monster.is_alive() > 0:
        adventurer.attack(monster)
        monster.attack(adventurer)

        choice = input('Keep fighting 1 or run away 2? ')

        if choice == '2':
            print(f'{adventurer.name} runs away! 🏃‍♂️')
            break
    if not monster.is_alive():
        adventurer.gold += monster.gold

    adventurer.print_details()

adventurer = Character('Slate', 100, 30, 6, 'male')
monster = Monster()
#battle(adventurer, monster)

def play_game():
    print('Welcome to the Dungeon Adventure Game! 🏰')
    name = input('Enter your character name: ')
    gender = input('Enter your character gender: ')
    adventurer = Character(name, 100, 80, 7, gender)

    dungeon_room(adventurer)

    while adventurer.is_alive():
        choice = input('Do you want to continue exploring the dungeon? (yes/no) ')
        if choice.lower() == 'yes':
            dungeon_room(adventurer)
        else:
            print('Good bye quitter!! 🤨')
            break
        
    if adventurer.is_alive():
        print(f'You flee the dungeon with {adventurer.gold} gold! 💰')

play_game()