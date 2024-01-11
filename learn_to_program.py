"""
# Ask the user to input their name and assign it to a variable named name.
name = input('What is your name')
# Print out hello followed by the name they entered
print('Hello', name)
"""

"""
# Ask the user to input 2 values and store them in variables num1, num2.
num1, num2 = input('Enter 2 numbers: ' ).split()
# Convert the strings into regular number integer.
num1 = int(num1)
num2 = int(num2)
# Add the values entered and store in sum
sum = num1 + num2
# Subtract values and store in difference
difference = num1 - num2
# Multiply the value and store in product
product = num1 * num2
# Divide the value and store in quotient
quotient = num1 / num2
# Use modulus on the value to find the remainder
remainder = num1 % num2
# Print the results
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
"""

"""
# problem: receive miles and convert to kilometers
# Kilometers = miles * 1.60934
# Enter miles 5
# 5 miles equals 8.04 kilometers

# Ask the user to input miles and assign it to the miles variable
miles = input('Enter miles ')
# Convert from string to integer
miles = int(miles)
# Perform calculation by multiplying 1.60934 times miles
kilometers = miles * 1.60934
# print results using format()
print("{} miles equals {} kilometers".format(miles, kilometers))
"""

"""
# Enter calculation: 5 * 6
# 5 * 6 = 30

# Store the user input into integers
num1, operator, num2 = input('Enter calculation ').split()
# convert the strings into integers
num1 = int(num1)
num2 = int(num2)
# if + then we need to provide output based on addition
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1*num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1/num2))
elif operator == "*":
    print("{} - {} = {}".format(num1, num2, num1-num2))
else:
    print("use either + - * or / next time")
# print the result
"""

# we'll provide different output based on age
# 1 - 18  --> important
# 21, 50, --> important
# All others --> Not important

"""
# Receive age and store in age
age = eval(input('Enter age: '))
# If age is both greater than or equal to 1 and less than or equal to 18 important
if (age >= 1) and (age <= 50):
    print("Important Birthday")
# if age is either 21 or 50 important
elif (age == 21) or (age == 50):
    print("important Birthday")
# we check if age is less than 65 and then convert true to false and vice versa
elif not(age < 65):
    print("important Birthday")
# Else not important
else:
    print("Sorry, Not Important")
"""

# if age is 5 go to kindergarten.
# Ages 6 through 17 goes to grades 1 through 12.
# If age is greater then 17 say go to college.
# try to complete with 10 or less times.

# Ask for the age
age = eval(input("Enter age: "))
# handle if age < 5
if age < 5:
    print("Too Young for school")
# Specialoutput just for age 5.
elif age == 5:
    print("Go to kindergarten")

# since a number is the result for ages 6 - 17 we can check them all with 1 condition
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("go to {} grade".format(grade))
# handle everyone else
else:
    print("Go to College")