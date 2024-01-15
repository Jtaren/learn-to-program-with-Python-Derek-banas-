import random
import math

# [0 : "string"] [1 : 1.234] [2 : 28] [3 : "c"]

"""
randList = ["string", 1.234, 28]
oneToTen = list(range(10))
randList = randList + oneToTen
print(randList[0])
print("list length :", len(randList))
first3 = randList[0:3]

for i in first3:
    print("{} : {}".format(first3.index(i), i))
print(first3[0] * 3)
print("string" in first3)
print("Index of string :", first3.index("string"))
print("How many strings :", first3.count("string"))
first3[0] = "New String"

for i in first3:
    print("{} : {}".format(first3.index(i), i))
first3.append("Another")
for i in first3:
    print("{} : {}".format(first3.index(i), i))
"""

"""numList = []
for i in range(5):
    numList.append(random.randrange(1,9))
for i in numList:
    print(i)
"""

"""
# Bubble Sort
# An outer loop decreases in size each time
# The goal is to have the largest number at the end of the list when the outer loop completes 1 cycle
# The inner loop starts comparing indexes at the beginning of the loop
# Check if list[index] > list[index + 1]
# if so swap the index values
# when the inner loop completes the largest number is at the end of the list
# Decrement the outer loop by 1

# i = len(numList)
numList = []

for i in range(5):
    numList.append(random.randrange(1,10))
i = len(numList) - 1
while i > 1:
    j = 0
    while j < i:
        print("\nIs {} > {}".format(numList[j], numList[j+1]))
        if numList[j] > numList[j + 1]:

            print("Switch")

            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp
        else:
            print("Don't Switch")
        j += 1
        for k in numList:
            print(k, end=", ")
        print()
    print("END OF ROUND")
    i -= 1
for k in numList:
    print(k, end=", ")
print()
"""

"""
numList = []
for i in range(5):
    numList.append(random.randrange(1,10))
numList.sort()
numList.reverse()
numList.insert(5,10)
numList.remove(10)
numList.pop(2)
for k in numList:
    print(k, end=",")
print()
"""

"""
evenList = [i*2 for i in range(10)]

for i in evenList:
    print(i)
"""

"""numList = [1,2,3,4,5]
listOfValues = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)] for m in numList]

for i in listOfValues:
    print(i)
print()

multiDList = [[0] * 10 for i in range(10)]
multiDList[0][1] = 10
print(multiDList[1][1])
"""

"""listTable = [[0] * 10 for i in range(10)]
for i in range(4):
    for j in range(4):
        listTable[i][j] = "{} : {}".format(i, j)
for i in range(4):
    for j in range(4):
        print(listTable[i][j], end=" || ")
    print()
"""

# Create the multidimensional list
multTable = [[0] * 10 for i in range(10)]
# Increment with outer for
for i in range(1, 10):
# Increment with inner for
    for j in range(1, 10):
# Assign the value to the ceil
        multTable[i][j] = i * j
# Output the data
for i in range(1, 10):
    for j in range(1, 10):
        print(multTable[i][j], end=", ")
    print()