# Real world objects : Attributes & Capabilities
# Dog attributes (Fields / Variables): Heiht, Weight, Favorite Food
# Dog capabilities (Methods / Functions): Run, Eat, Barks
'''
class Dog:
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight
    def run(self):
        print("{} the dog runs".format(self.name))
    def eat(self):
        print("{} the dog eats".format(self.name))
    def bark(self):
        print("{} the dog barks".format(self.name))
def main():
    spot = Dog("Spot", 23, 45)
    spot.bark()
    bowser = Dog()
    bowser.name = "Bowser"
    bowser.weight = 45
    bowser.height = 23
    bowser.run()
    print(bowser.name)
main()

class Sqaure:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width
    @property # Getter
    def height(self):
        print("Retriving the Height")
        return self.__height
    @height.setter # Setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please only enter numbers for height")
    @property
    def width(self):
        print("Retriving the Width")
        return self.__width
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for width")
    def getArea(self):
        return int(self.__width) * int(self.__height)
def main():
    aSquare = Sqaure()
    height = input("Enter the Height: ")
    width = input("Enter the Width: ")
    aSquare.height = height
    aSquare.width = width
    print("Height: ", aSquare.height)
    print("Width: ", aSquare.width)
    print("The Area is: ", aSquare.getArea())
main()
'''
# Fighting game
import random
class Warrior:
    def __init__(self, name="", life=0):
        self.name = name
        self.life = life
    def attack(self):
        attack_damage = random.randrange(1, 20)
        return attack_damage
    def defend(self):
        defend_points = random.randrange(1, 20)
        return defend_points
def main():
    Fighter1 = Warrior()
    Fighter2 = Warrior()
    Fighter1.name = input("First fighter's name: ")
    Fighter2.name = input("Second fighter's name: ")
    Fighter1.life = random.randrange(50, 100)
    Fighter2.life = random.randrange(50, 100)
    attacking_warrior = 1
    print(Fighter1.name, " life: ", Fighter1.life)
    print(Fighter2.name, "life: ", Fighter2.life)
    while True:
        if attacking_warrior == 1:
            damage_points = Fighter1.attack() - Fighter2.defend()
            if damage_points < 0:
                damage_points = 0
            Fighter2.life -= damage_points
            print(Fighter1.name, "attacks", Fighter2.name, "and deals", damage_points, "damage")
            print(Fighter2.name, "is down to ", Fighter2.life, "health")
            attacking_warrior = 2
        else:
            damage_points = Fighter2.attack() - Fighter1.defend()
            if damage_points <= 0:
                damage_points = 0
            Fighter1.life -= damage_points
            print(Fighter2.name, "attacks", Fighter1.name, "and deals", damage_points, "damage")
            print(Fighter1.name, "is down to ", Fighter1.life, "health")
            attacking_warrior = 1
        print(Fighter1.name, " life: ", Fighter1.life)
        print(Fighter2.name, "life: ", Fighter2.life)
        if Fighter1.life <= 0:
            print(Fighter1.name, "has died.", Fighter2.name, "is the winner!")
            break
        elif Fighter2.life <= 0:
            print(Fighter2.name, "has died.", Fighter1.name, "is the winner!")
            break
        #input("For next round, please hit ENTER")
main()
'''
# Create a Warrior and a Battle class
# Warriors will have names, life, attack and block maximums
# They will have the capabilities to attack and block random amounts
# Attack random() 0.0 to 1.0 * maxAttack + 0.5
# Block random() 0.0 to 1.0 * maxBlock + 0.5
# Battle Class capabilitiy of looping until 1 warrior dies
# Warriors will each get a turn to attack each other
# Function gets 2 warriors
# 1 warrior attacks the other
# Attacks and Block be integers
'''
