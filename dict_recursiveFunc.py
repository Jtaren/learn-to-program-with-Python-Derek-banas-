"""
ArenDict = {"fName" : "Aren", "lName" : "Solomon", "address" : "No.22 Sandaji st"}
print("My name : ", ArenDict["fName"])
ArenDict["address"] = ["No.2 Revenue House"]
ArenDict["city"] = "Lafia"
print("Is there a city :", "city" in ArenDict)
print(ArenDict)
print(ArenDict.values())
print(ArenDict.keys())

for k, v in ArenDict.items():
    print(k, v)

print(ArenDict.get("mName", "Not Here"))

del ArenDict["lName"]
print(ArenDict)

for i in ArenDict:
    print(i)
ArenDict.clear()
employees = []
fName, lName = input("Enter Employee Name : ").split()
employees.append({'fName': fName, 'lName' : lName})
print(employees)
"""

"""# Enter Customer (Yes/No) : y
# Enter Customer Name : Derek banas
# Enter Customer (Yes/No) : y
# Enter Customer Name : Sally Smith
# Enter Customer (Yes/No) : n

# Create an list
Customers = []
# Create a loop
while True:
    # Get input and make it work for y or n
    createEntry = input("Enter Customer (Yes/No) : ")
    createEntry = createEntry[0].lower()
    # Check to leave loop
    if createEntry == 'n':
        break
    # Get customer data
    else:
        fName, lName = input("Enter Customer Name : ").split()
        # Add customer data to list
        Customers.append({'fName' : fName, 'lName' : lName})

# Print customer data
for Cust in Customers:
    print(Cust['fName'], Cust['lName'])
"""

"""
# 3! = 3 * 2 * 1
def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num -1)
        return result
print("4! = ", factorial(4))

# 1st : result = 4 * factorial(3) : 4 * 6
# 2nd : result = 3 * factorial(2) : 3 * 2
# 3rd : result = 2 * factorial(1) : 2 * 1
"""

# 1, 1, 2, 3, 5, 8, 13

# Fn = Fn - 1 + Fn - 2
# where F0 = 0 and F1 = 1

# print(fib(3))
# 1st : result = fib(2) + fib(1) : 2 + 1 = 3
# 2nd : result = (fib(1) + (fib(0)) + fib(0)) : 1 + 0 = 1

"""
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib(n - 1) + fib(n - 2)
        return result
print(fib(3))
print(fib(4))
print(fib(5))
"""
