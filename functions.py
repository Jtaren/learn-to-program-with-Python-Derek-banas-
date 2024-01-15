"""
def add_numbers(num1, num2):
    return num1 + num2

print("5 + 4 =", add_numbers(5,4))
"""


"""
name = "dog"
def assign_name():
    name = "dog"
assign_name()
print(name)
"""

"""
def change_name(name):
    name = "mark"
name = "Tom"
change_name(name)
print(name)
"""

"""
def change_name(name):
    return "mark"
name = "Tom"
name = change_name(name)
print(name)
"""

"""gbl_name = "sally"

def change_name():
    global gbl_name
    gbl_name = "sammy"

change_name()

print(gbl_name)
"""

"""
def get_sum(num1, num2):
    sum = num1 + num2  # without return function is none
    return sum

print(get_sum(5,4))
"""

"""
# solve for x
# x + 4 = 9
# Do 4 + x = 9
# x will always be the 1st value received and you only will deal with addition
# Receive the string and split the string into variables
# Convert the strings into ints
# Convert the result into a string and join it to the string "X = "
# print()
def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()
    num1, num2 = int(num1), int(num2)
    return "x = " + str(num2 - num1)
print(solve_eq("x + 4 = 12"))
"""

"""
def multi_divide(num1, num2):
    return (num1 * num2), (num1 / num2)
mult, divide = multi_divide(5,4)
print("5 * 4 =", mult)
print("5 / 4 =", divide)
"""

"""
# A prime can only be divided by 1 and itself
# 5 is a prime, 1 and 5 = positive factor
# 6 is not a prime, 1, 2, 3, 6

# Input max prime
# use a for loop and check if modulus == 0 True

def isPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def getPrimes(max_number):
    list_of_primes = []

    for num1 in range(2, max_number):
        if isPrime(num1):
            list_of_primes.append(num1)
    return list_of_primes
max_num_to_check = int(input("Search for Primes up to : "))
list_of_primes = getPrimes(max_num_to_check)
for prime in list_of_primes:
    print(prime)
"""

"""
def sumAll(*args):
    sum = 0

    for i in args:
        sum += i

    return sum

print("Sum :", sumAll(1, 2, 3, 4, 5))
"""

"""
import math

def get_area(shape):
    shape = shape.lower()

    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please enter rectangle or circle")
def rectangle_area():
    length = float(input("Enter the length : "))
    width = float(input("Enter the width :"))

    area = length * width

    print("The area of the rectangle is", area)

def circle_area():
    radius = float(input("Enter the radius : "))
    area = math.pi * (math.pow(radius, 2))
    print("The area of the circle is {:.2f}".format(area))
"""




