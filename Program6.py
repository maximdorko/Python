#Dictionaires
'''
maximDict = {"fName" : "Maxim", "lName" : "Dorko", "sAddress" : "Streets of Rage", 
            "sCity" : "London"} # creates a dictionaire with key and value
print("My name is: ", maximDict["fName"],maximDict["lName"]) # prints the dictionaire elemnets by referring to the key
maximDict["sAddress"] = "Streets of Pages" # Change the value of an item in the dictionaire
print(maximDict)
maximDict["sCountry"] = "UK" # Adds a new key and value to the dict
print("Is there a coutry? ", "sCountry" in maximDict) # Checks if there is key in the dict

print(maximDict.values()) # Prints the values in dict
print(maximDict.keys()) # Prints the keys in dict

for i, j in maximDict.items(): # Checks each key in the dict
    print(i, j)

print(maximDict.get("lName", "Not there")) # Checks for a key, if exists, will give back the value if not, will print "Not there"

del maximDict["sCountry"] # Delete a key from dict

for i in maximDict: # Cycles through dict keys
    print(i)

maximDict.clear() # Clears the dict

employeesList = []
fName, lName = input("Please enter the name of the employee: ").split()
employeesList.append({"fName": fName, "lName" : lName})
print(employeesList)


# Create a list of cutomers
# Enter Customer? (Yes/No)
# Enter Customer name: Maxim Dorko
yesAnswers = ["Yes", "y", "yes", "ok"]
customerList = []
while True:
    enterChoice = input("Enter customer? (Yes/No)")
    if enterChoice in yesAnswers:
        fName, lName = input("Enter Customer name: ").split()
        customerList.append({"fName" : fName, "lName" : lName})
    else:
        break
for customerName in customerList:
    print(customerName["fName"], customerName["lName"])
'''
# Recursive functions
# Caclulate factrial: 3! = 3 * 2 * 1
def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num -1)
        print(num)
        return result

number = int(input("Which number's factorial to calculate? "))
print("The result is: ", factorial(number))
'''
# Calculate Fibonachi
# 1, 1, 2, 3, 5, 8, 13
# Fn = Fn - 1 + Fn - 2
# Where F0 = 0 and F1 = 1
def fiboCalc(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fiboCalc(num - 1) + fiboCalc (num - 2)
        return result
print(fiboCalc(3))
for i in range(30):
    print(fiboCalc(i), end=", ")
print()
'''








