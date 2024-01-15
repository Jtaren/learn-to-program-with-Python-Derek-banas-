"""
rand_string = "   this is an important string   "

print("rand_string = ", rand_string.lstrip())
print("rand_string = ", rand_string.rstrip())
print("rand_string = ", rand_string.strip())
print(rand_string.upper())
print(rand_string.lower())

print(rand_string.split())
for i in rand_string.split():
    print(i)

print("How many is : ", rand_string.count("is"))
print("Where is string : ", rand_string.find("string"))
print(rand_string.replace("an ", "a kind of "))

a_list = ["bunch", "of", "random", "words"]
print(" ".join(a_list))
"""

"""
# Ask for s string
orig_string = input("Convert to Acronym : ")
# Convert the string to uppercase 
orig_string = orig_string.upper()
# Convert the string into a list
list_of_words = orig_string.split()
# Cycle through the list
for word in list_of_words:
# Get the 1st letter of the word and eliminate the newline
    print(word[0], end="")
# Add a newline
print()
"""


"""
letter_z = "z"
num_3 = "3.14"
a_space = " "

# print("Is z a letter or number : ", letter_z.isalnum())
# print("Is z a letter : ", letter_z.isalpha())
# print("Is z a number : ", num_3.isdigit())
# print("Is z a lowercase : ", letter_z.islower())
# print("Is z a uppercase : ", letter_z.isupper())
# print("Is space a space : ", a_space.isalpha())

def isFloat(num_3):
    try:
        float(num_3)
        return True
    except ValueError:
        return False
print("is Pi a float : ", isFloat(num_3))
"""

# A - Z 65 - 90
# a - z 97 - 122
#ord(your_letter)
#chr(your_code)

# Hints
# Use isupper() to decide which unicodes to work with
# Add the key (number of characters to shift) and if the key is bigger or smaller than the unicode for
# A, Z, a, z increase or decrease by 26

# Receive the message to encrypt and the number of character to shift
message = input("Enter your message : ")
key = int(input("How many characters should we shift (1 - 26 )"))
# Prepare the secret_message
secret_message = ""
# Cycle through each character in the messsage
for char in message:
    # If itn't a letter then keep it as it is
    if char.isalpha():
    # Get the character code and the shift amount
        char_code = ord(char)
        char_code += key
    # If uppercase then compare to uppercase unicodes
        if char.isupper():
        # If bigger then Z subtract 26  
            if char_code > ord('Z'):
                char_code -= 26
        # If smaller then A add 26
            if char_code > ord('A'):
                char_code += 26
    # Do the same for lower charaters
        else:
            if  char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26
    # Convert from code to letter and add to message
        secret_message += chr(char_code)
# If not a letter leave character as is
    else:
        secret_message += char
print("Encrypt : ", secret_message)
# To decrypt the only thing that changes is the sign of the key

# To decrypt the only thing that changes is the sign of the key

key = -key
orig_message = ""

for char in message:
    # If itn't a letter then keep it as it is
    if char.isalpha():
    # Get the character code and the shift amount
        char_code = ord(char)
        char_code += key
    # If uppercase then compare to uppercase unicodes
        if char.isupper():
        # If bigger then Z subtract 26  
            if char_code > ord('Z'):
                char_code -= 26
        # If smaller then A add 26
            if char_code > ord('A'):
                char_code += 26
    # Do the same for lower charaters
        else:
            if  char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26
    # Convert from code to letter and add to message
        orig_message += chr(char_code)
# If not a letter leave character as is
    else:
        orig_message += char
print("Encrypt : ", orig_message)

