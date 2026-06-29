# Note : __init__(self) is a constructor used to construct or make objects
# Note : '.' used in lines such as "self.name" is known as Attribute Access Operator

import random

class Player:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, target):
        damage = random.randint(5, 15)

        print(f"{self.name} attacks {target.name}!")
        print(f"Damage dealt: {damage}")

        target.take_damage(damage)


    def take_damage(self, damage):
        self.health -= damage

        if self.health < 0:
            self.health = 0

        print(f"{self.name}'s health: {self.health}\n")

        