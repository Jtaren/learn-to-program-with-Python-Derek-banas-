"""
for i in [2, 4, 6, 8, 10]:
    print("i = ", i)

for j in range(10):
    print("j = ", j)

for x in range(2, 10):
    print("x = ", x)
"""

"""
i = 2
print((i % 2) == 0)
# Use for loop through the list from 1 to 21
for y in range(2, 21):
# Use modulus to check that the result is NOT EQUAL to 0.
    if ((y % 2) != 0):
# Print the odds
        print("y = ", y)
"""

"""
your_float = input("Enter a float: ")

your_float = float(your_float)

print("Round to 2 decimals : {:.2f}".format(your_float))
"""

"""
# Have the user enter their investment amount and expected interest
# Each year their investment will increase by their investment + their investment * interest rate is
# Print out the earnings after a 10 year period

# Ask for the money invested + the interest rate
money = input("How much to invest : ")
interest_rate = input("Interest Rate : ")
# Convert the value to a float
money = float(money)
# Convert value to a float and round the percentage rate by 2 digits
interest_rate = float(interest_rate) * .01
# Cycle through 10 years using a for loop and range from 0 to 9
for i in range(10):
    money = money + (money * interest_rate)
# Output the results
print("Investment after 10 years : {:.2f}".format(money))
"""


"""
import random

rand_number = random.randrange(1, 51)
i = 1

while (i != rand_number):
    i += 1
print("The random value is : ", rand_number)
"""


"""
i = 1

while i <= 20:
    if (i % 2) == 0:
        i += 1
        continue

    if i == 15:
        break

    print("Odd : ", i)
    i += 1
"""


"""
# Use 1 while loop and 3 for loops
# 4 spaces : 1 hash
# 3 spaces : 3 hashes
# 2 spaces : 5 hashes
# 1 space : 7 hashes
# 0 spaces : 9 hashes

# need to do:
# 1. Decrement spaces by 1 each time through the loop
# 2. Increment the hashes by 2 each time through the loop
# 3. Save spaces to the stump by calculating three height - 1
# 4. Decrement from tree height until it equals 0
# 5. Print spaces and then hashes for each row
# 6. print stump spaces and then 1 hash

# Get the number of rows for the tree
tree_height = input("How tail is the tree : ")
# Convert into an integer
tree_height = int(tree_height)
# Get the starting spaces for the top of the tree
spaces = tree_height - 1
# There is one hash to start that will be incremented
hashes = 1
# Save stump spaces til later
stump_spaces = tree_height - 1
# make sure the right number of rows are printed
while tree_height != 0:
# Print the spaces
    for i in range(spaces):
        print(' ', end="")
# print the hashes
    for i in range(hashes):
        print('*', end="")
# Newline after each row is printed
    print()
# That spaces is decremented by 1 each time
    spaces -= 1
# That hashes is incremented by 2 each time
    hashes += 2
# Becrement tree height each time to jump out of the loop
    tree_height -= 1
# Print the spaces before the stump and then the hash
for i in range(stump_spaces):
    print(' ', end="")
print('#')
"""

for i in range(20):
    if(i % 2) == 0:
        print(i)