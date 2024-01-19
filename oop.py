"""
# Real World Objects : Attributes & Capabilities
# Dog Attributes (Fields / Variables) : Height, Weight, Favorite Food
# Dog Capabilities (Methods / Function) : Run, Walk, Eat

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
    spot = Dog("spot", 66, 26)

    spot.bark()
    bowser = Dog()
    bowser.bark()

main()
"""

"""
class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("Retrieving the height")
        return self.__height

    @height.setter
    def height(self, value):

        if value.isdigit():
            self.__height = value
        else:
            print("Please only enter numbers for height")

    @property
    def width(self):
        print("Retrieving the height")
        return self.__width

    @width.setter
    def width(self, value):

        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for height")

    def getArea(self):
        return int(self.__width) * int(self.__height)

def main():
    aSquare = Square()

    height = input("Enter Height : ")
    width = input("Enter Width : ")

    aSquare.height = height
    aSquare.width = width

    print("Height : ", aSquare.height)
    print("Width :", aSquare.width)

    print("The Area is :", aSquare.getArea())

main()
"""


# Sam attacks Paul and deals 9 damage
# Paul is down to 10 health
# Paul attacks Sam and deals 7 damage
# Sam is down to 7 health
# Sam attacks Paul and deals 19 damages
# Paul is down to -9 heath
# Paul has Died and Sam is victorious
# Game Over

import random
import math

# Warriors & Battle Class
class Warrior:
    def __init__(self, name="Warrior", health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax
# Warriors will have names, health, and attack and block maximums

# They will have the capabilities to attack and block random amounts
    def attack(self):
        attkAmt = self.attkMax * (random.random() + .5)

        return attkAmt
    
    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)

        return blockAmt
# Attack random() 0.0 to 1.0 * mazAttack + .5

# Block will use random()

# battle class capabilities of looping until 1 warrior dies.
class Battle:
    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game over")
                break
            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game over")
                break
# Warriors will each get a turn to attack each other.

# Function gets 2 warriors

# 1 warrior attacks the other

#Attacks and blocks ne integers