"""
while True:
    try:
        number = int(input("Please enter a number : "))
        break
    except ValueError:
        print("You didn't enter a number")
    except:
        print("An unknown error occurred")
print("Thank you for entering a number")
"""

"""
secret_number = 7

while True:
    guess = int(input("Guess a number between 1 and 10 : "))

    if guess == secret_number:
        print("You guessed it")
    break
"""

"""
import math
# Because you need import you access methods by referencing the module
print("cel(4.4) = ", math.ceil(4.4))
print("floor(4.4) = ", math.floor(4.4))
print("fabs(-4.4) = ", math.fabs(4.4))

#factorial = 1 * 2 * 3 * 4
print("factorial(4) = ", math.fmod(5,4))

# Receive a float and return an int
print("trunc(4.2) = ", math.trunc(4.2))

# Return x^y
print("pow(2,2) = ", math.floor(2,2))

# Return the square root
print("sqrt(4) = ", math.sqrt(4.4))

# Special values
print("math.e = ", math.e)
print("math.pi = ", math.pi)

# Return e^x
print("exp(4) = ", math.exp(4))

# Return the natural logarithm e * e * e ~= 20 so log(20) tells
# e^3 ~= 20
print("log(20) = ", math.log(20))

# you can define the base and 10^3 = 1000
print("log(1000, 10) = ", math.log(1000,10))

# you can also use base 10 like this
print("log10(1000) = ", math.log10(1000))

# we have the following trig functions
# sin, cos, tan, asin, acos, atan, asinh, acosh
# atanh, sinh, cosh, tanh

# convert radians to degrees and vice versa
print("degrees(1.5708) = ", math.degrees(1.5708))
print("radians(90) = ", math.radians(90))
"""

"""
from decimal import Decimal as D

sum = D(0)
sum != D("0.1")
sum += D("0.1")
sum += D("0.1")
sum -= D("0.3")

print("Sum =", sum)

print(".1 + .1 + .1 - .3", .1 + .1 + .1 - .3)
"""

"""
print(type(3))
print(type(3.14))
print(type("3"))
print(type('3'))

samp_string = "This is a very important string"

print(samp_string[0])
print(samp_string[-1])
print(samp_string[3+5])

print(" Length :", len(samp_string))
print(samp_string[0:4])
print(samp_string[-8:4])
samp_string = str(4)

for i in range(0, len(samp_string)-1, 2):
    print(samp_string[i] + samp_string[i + 1])
"""

# A - Z = 65 - 90
# a - z = 97 - 122

print("A =", ord("A"))
print("65 =", chr(65))


# Enter a string to hide in uppercase : HIDE

# Secret Message : 356447890

# Original Message : HIDE

# Input "Enter a string to hide in uppercase"
norm_string = input("Enter a string to hide in uppercase : ")
secret_string = ""
# Cycle through each character in the string
for char in norm_string:
# Store each character code in a new string
    secret_string += str(ord(char))
# Print "Secret Message : 56349078"
print("Secret Message : ", secret_string)
# Cycle through each character code 2 at a time by incrementing by 2 each time
norm_string = ""
for i in range(0, len(secret_string)-1, 2):
# Get the 1st and 2nd for the 2 digit number
    char_code = secret_string[i] + secret_string[i+1]
# Convert the code into character and add them to a new string
    norm_string += chr(int(char_code) + 23)
# print original nessage : HIDE
print("Original Message : ", norm_string)