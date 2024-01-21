"""
class Sum:
    @staticmethod
    def getSum(*args):

        sum  = 0

        for i in args:
            sum += i

        return sum
    
def main():
    print("Sum : ", Sum.getSum(1, 2, 3, 4, 5))

main()
"""

"""
class Dog:

    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name

        Dog.num_of_dogs += 1

    @staticmethod
    def getNumOfDogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))

def main():

    spot = Dog("Spot")

    doug = Dog("Doug")

    spot.getNumOfDogs()

    doug.getNumOfDogs()

main()
"""

"""
# import sum
from sum import getSum
# from sum import *

# print("Sum :", sum.getSum(1, 2, 3, 4, 5))
print("Sum :", getSum(1, 2, 3, 4, 5))
"""

"""
try:
    aList = [1, 2, 3]

    print(aList[3])

# except(IndexError, NameError)

except IndexError:
    print("Sorry that index doesn't exist")

except:
    print("An unknown error occured")
"""


"""
class DogNameError(Exception):
    
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    dogName = input("What is your dogs name : ")

    if any(char.isdigit() for char in dogName):
        raise DogNameError
        
except DogNameError:
    print("Your dogs name can't contain a number")
"""


"""
num1, num2 = input("Enter 2 values to divide : ").split()

try:
    quotient = int(num1) / int(num2)

    print("{} / {} = {}".format(num1, num2, quotient))

except ZeroDivisionError:
    print("You didn't divide by zero")

else:
    print("You didn't raise an exception")

finally:
    print("I execute no matter what")
"""

# Create a file named mydata.txt
# Use what you learned in part 8 to find out how to open a file without with (open in try)
# Catch FileNotFoundError
# In else print contents
# In finally
# Open nonexistent file mydata3.txt

try:
    myFile = open("mydata2.txt", encoding="utf-8")

except FileNotFoundError as ex:
    print("That file was not found")

    print(ex.args)

else:
    print("File :", myFile.read())
    myFile.close()

finally:
    print("Finished Working with File")