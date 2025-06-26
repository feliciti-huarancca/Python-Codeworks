
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def display_status(self):
        print(f'\n******** {self.name} ********')
        print(f"health: {self.health}")
        print(f'attack power: {self.attack_power}')
        print('**************************')

    def attack(self, enemy: 'Character'):
        print(f"\n{self.name} attacks 🤺 ")
        damage = self.attack_power
        enemy.health -= damage
        print(f" Damage: {damage} 💢 | {enemy.name} health: {enemy.health}")

    def is_alive(self):
        return self.health > 0
    
class Monster(Character):
    def __init__(self, health, attack_power):
        name = 'Goblin'
        super().__init__(name, health, attack_power)

    def taunt(self):
        print(f"\n{self.name} growls menacingly! 🐲")


def battle(hero: Character, monster: Monster):
    print("The battle begins!")

    while hero.is_alive() and monster.is_alive():
        hero.display_status()
        monster.display_status()

        hero.attack(monster)
        monster.taunt()

        if not monster.is_alive():
            print(f"\n{monster.name} has been defeated! 🎉")
            break

        monster.attack(hero)
        if not hero.is_alive():
            print(f"\n{hero.name} has been defeated! Game Over! 💀")
            break

        action = input("\n Keep [1]fighting, [2]run:  ")
        if action == "2":
            break

# Creating Objects
superman = Character('Superman', 100, 20)
monster1 = Monster(80, 30)

battle(superman, monster1)