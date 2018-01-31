# Battle of Warriors
# A class for warriors with the attributes: Name, Health, Attack, Block
# Method for attack points
# Method for block points
# Class metod for Battle
import random
class Warriors:
    result = 0
    def __init__(self, name, health, attack, block):
        self.name = name
        self.health = health
        self.attack = attack
        self.block = block
    def attack_points(self):
        return self.attack * random.random()
    def block_points(self):
        return self.block * random.random()
    def print_health(self):
        print(self.health)
    @classmethod
    def battle(cls, warrior1, warrior2):
        cls.result = int(warrior1.attack_points() - warrior2.block_points())
        if cls.result <= 0:
            print("{} attacks {} and misses".format(warrior1.name, warrior2.name))
        else:
            print("{} attacks {} and deals {} damage".format(warrior1.name, warrior2.name, cls.result))
            warrior2.health -= cls.result
        print("{}'s health {}".format(warrior2.name, warrior2.health))
        return

warrior_1 = Warriors(input("Warrior name: "), 
                     int(input("Health: ")), 
                     int(input("Attack: ")),
                     int(input("Block: ")))
warrior_2 = Warriors(input("Warrior name: "), 
                     int(input("Health: ")), 
                     int(input("Attack: ")),
                     int(input("Block: ")))
attacking_warrior = 1
print("The match starts")
while True:
    if attacking_warrior == 1:
        Warriors.battle(warrior_1, warrior_2)
        if warrior_2.health <= 0:
            print("{} died, {} is the winner".format(warrior_2.name, warrior_1.name))
            break
    if attacking_warrior == 2:
        Warriors.battle(warrior_2, warrior_1)
        if warrior_1.health <= 0:
            print("{} died, {} is the winner".format(warrior_1.name, warrior_2.name))
            break
    if attacking_warrior == 1:
        attacking_warrior = 2
    else:
        attacking_warrior = 1
