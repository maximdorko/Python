'''

rand_string = "       this is an important string      "

print(rand_string.lstrip()) #Removes the spaces from the left
print(rand_string.rstrip()) #Removes the spaces from the right
print(rand_string.strip()) #Removes all spaces from the string beginning and end

print((rand_string.strip()).capitalize()) #Removes spaces from beg/end and capitalize the first letter (even if it's space)

print((rand_string.strip()).upper()) #Removes spaces from beg/end and convert to uppercase the whole string

print((rand_string.strip()).lower()) #Removes spaces from beg/end and convert the whole string to lowercase

theList = ["A", "lot", "of", "Words"] #define a list
print(" ".join(theList)) #join the elements of the list and using " " as separator

theListNew = rand_string.split() #split a string into a list
for i in theListNew: #cycle the lements of the list an adding the string into the "i" variable
    print(i)

print("How many 'is' in the string: ", rand_string.count("is")) #Count, how many times "is" in the string

print("Where 'is' in the string:", rand_string.find("is")) #Will give back the index of the "is" in the string. The first one occurence

print(rand_string.replace("an ", "a kind of ")) #Replaces "an" in the string with "a kind of"


# Create a Acronym generator
# Request user to enter a string. e.g.: Random Access Memory
# Convert the string into acronym, all uppercase letters. e.g.: RAM

userString = input("Please enter the string: ")
userWords = userString.split()
print(userString, "Acronym is: ", end="")
for i in userWords:
    print(i[0].upper(), end="")
print()


aLetterZ = "z"
aNumber3 = "3.14"
aSpace = " "

print("Is 'z' a letter or number? ", aLetterZ.isalnum()) # Checks if the string is all alphanumerical
print("Is 'z' a letter? ", aLetterZ.isalpha()) # Checks if the string is all letter
print("Is '3.14' a number? ", aNumber3.isdigit()) # Checks if the string is all number
print("Is 'z' a lowercase? ", aLetterZ.islower()) # Checks if the string is all lowercase
print("Is 'z' a uppercase? ", aLetterZ.isupper()) # Checks if the string is all uppercase
print("Is 'Space' a space? ", aSpace.isspace()) # Checks if the string is a space

def isfloat(str_val): # Define a function with one value
    try:
        float(str_val) # Check if it can be converted to float
        return True # Success, return True
    except ValueError: # If the conversion gives ValueError, return False
        return False

print("Is 3.14 a number? ", isfloat(aNumber3))
'''

# Request a sentence from the user
# Encrypt the string by shifting the characters unicode by +3
# If the character is not a letter, leave it alone
# A - Z : 65 - 90
# a - z : 97 - 122
# ord(yourletter) to get unicode
# chr(yourletter) to get letter from unicode


def encrypt_char(letter, letterShift):
    """Shift the string character Unicode by letterShift value"""
    letter_unicode = ord(letter) + letterShift
    if letter.isupper():
        if letter_unicode > 90:
            letter_unicode -= 26
        elif letter_unicode < 65:
            letter_unicode += 26
    else:
        if letter_unicode > 122:
            letter_unicode -= 26
        elif letter_unicode < 97:
            letter_unicode += 26
    return chr(letter_unicode)

userSentence = input("Please enter you sentence: ")
numberToShift = int(input("Number of shift: "))
secretString = ""
for i in userSentence:
    if i.isalpha():
        secretString += encrypt_char(i, numberToShift)
    else:
        secretString += i
print("Original String was: ", userSentence)
print("The encrypted string is: ", secretString)
decryptedString = ""
for i in secretString:
    if i.isalpha():
        decryptedString += encrypt_char(i, numberToShift*-1)
    else:
        decryptedString += i
print("Decrypted string is: ", decryptedString)
