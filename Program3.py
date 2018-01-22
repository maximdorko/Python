'''
while True:
    try:
        number = int(input("Please enter a number: "))
        break # it will get out from the loop if input succeeds
    except ValueError: # In case of value error (e.g.: letter entered)
        print("You didn't enter a number!")
    except: # In case of any error, nit ValueError
        print("Unknown error happened")
print(number)

# Guess game, requests input of a number and if it's not correct, repeat it, if correct
# write, you guessed it
import random
randomNumber = random.randrange(1,10)
while True:
    try:
        guessNumber = int(input("Guess the number: "))
        if guessNumber == randomNumber:
            print("You guessed it. It was: {}".format(randomNumber))
            break
    except:
        print("Wrong")
        continue

import math

print("ceil(4.4) =", math.ceil(4.4)) # round up 4.4 to 5
print("floor(4.4) = ", math.floor(4.4)) # round down to 4
print("fabs(-4.4) = ", math.fabs(-4.4)) # absolute value
print("factroial(4) = ", math.factorial(4)) # factorial
print("fmod(5,4) =", math.fmod(5,4)) # Returns remainder of division (5/4)
print("trunc(4.2) =", math.trunc(4.2)) # Receives a float and truncate to integer
print("pow(2,3) = ", math.pow(2,3)) # 2^3
print("math.e = ", math.e)
print("math.pi = ", math.pi) # Return pi
print("exp(4) = ", math.exp(4)) # Return e^x


from decimal import Decimal as D # Import the Decimal function from decimal module and call it "D" as alias
# Precise float operations
sum = D(0)
sum += D("0.1")
sum += D("0.1")
sum += D("0.1")
sum -= D("0.3")
print(sum)

print(type(3)) # type gives back the type of a variable
print(type(3.4))
print(type("Maxim"))

sampleString = "This is a very important string"
print(sampleString[0]) # String characters can be refereced with the index
print(sampleString[-1]) # -1 as index will give back the last character
print("Length: ", len(sampleString)) # Gives back the length of the string
print(sampleString[0:4]) # Returns the characters from 0 to 3
print(sampleString[5:]) # Gives back the string from 5th character to the end of the string
print("Maxim's " + sampleString) # Concatenate strings
print("Five times" * 5) # Multipy a string 5 times
numberString = str(4) # Converts a number to string
print(numberString)

for char in sampleString: # Cycles through each character of the string
    print(char)

for doubleChar in range(0, len(sampleString)-1,2): # gets every second char and prints in pairs
    print(sampleString[doubleChar] + sampleString[doubleChar + 1])

# Unicode of a char is:
# A - Z : 65 - 90
# a - z : 97 - 122

print("A = ", ord("A")) # Returns the unicode of a character
print("65 = ", chr(65)) # Returns the character represented by the unicode
'''
# Enter a string in upper case e.g.: AAAA
# return a message by converting each character in unicode. e.g.: 65656565
# Print the original message by converting back to Characters the secret message AAAA
messageString = input("Enter the message in all UPPER case: ")
secretMessage = ""
convertedSecret = ""
for i in messageString: 
    if i == " ":
        secretMessage = secretMessage + "09" # If the char is space, we need it's unicode 32, substracted will be 9 s covert it to 09
    else:
        secretMessage += str(ord(i)-23) #Substract 23 from the code to handle lower char 3 digit unicode 
print("The secret message is: ", secretMessage)
for i in range(0,len(secretMessage)-1,2):
    convertedSecret += chr(int(secretMessage[i] + secretMessage[i+1])+23) # Add 23 to get back the original unicode
print(convertedSecret)








