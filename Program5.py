import random
import math
'''
randomList = ["string", 1.234, 28] # Create a list with the elements
oneToTen = list(range(10)) # Generates a list 0 to 9

randomList = randomList + oneToTen # Concatenate the two lists into one

print(randomList[0]) # Prints the first item of the list

print("List length: ", len(randomList)) # prints out the number of elements in the list

for i in randomList:
    print(i)

first3 = randomList[0:3] # Creates a list with the forst 3 items of the list

for i in first3:
    print('{} : {}'.format(first3.index(i), i)) # list.index gives back the index of the item. Prints out the list elements first with their index and then the element

print(first3[0] * 4) # Prints the first item 4 times

print("string" in first3) # True if "string" is in the list

print("Index of 'string' in the list: ", first3.index("string")) # Gives back the index of "string" in the list

print("How many times 'sring' is in the list", first3.count("string")) # Counts, how many times, "string" is in the list

first3[0] = "New String" # Changes the value of 0 item in the list
print(first3[0])

first3.append("One more item") # Adds an item to the end of the list

for i in first3:
    print('{} : {}'.format(first3.index(i), i))

randNumber = random.randrange(1, 9)
print("The Number is: ", int(randNumber))


# Create a list with 5 elemnts, with random elements from 1 to 9

randomList = [] # Create the list type
for i in range(5): # i is with in 1 to 5
    randomList.append(random.randrange(1, 10)) # Adds an element to the list with the value random from 1 to 9 
for i in randomList:
    print(i)


# Bubble sort experiment

randomList = [] # Create the list type
for i in range(5): # i is with in 1 to 5
    randomList.append(random.randrange(1, 10)) # Adds an element to the list with the value random from 1 to 9 
i = len(randomList) - 1 # From the number of elements, create an index varaible 
while i > 0: # Outer loop is running until the number of elements
    j = 0
    while j < i: # Inner loop running until the number of elements

        print("\nIs {} > {}".format(randomList[j], randomList[j + 1])) # print the current and the next element \n is new line

        if randomList[j] > randomList[j + 1]:
            print("Switching") # printing if changing elements
            temp = randomList[j + 1] # store one element in temp variable
            randomList[j+1]=randomList[j] # moves the element to the previous
            randomList[j] = temp # stores the previous in place of next
        else:
            print("No switch") # prints if there is no need to change
        j += 1

        for k in randomList:
            print(k, end = ", ") # prints the values of the list in this loop
        print()
    print("End of round, ", i) # prints the end of outer loop with the loop number
    i -= 1
for k in randomList:
    print(k, end=", ")
print()
'''
import random
import math

def randomListGenerator(elementsNumber):
    randomList = []
    for i in range(elementsNumber):
        randomList.append(random.randrange(1, 10))
    return randomList

def printList(listToPrint):
    for i in listToPrint:
        print(i, end = ", ")
        print()
    return
'''
numbers = randomListGenerator(5)
printList(numbers)

numbers.sort() # Sorts the list ascending
printList(numbers)
numbers.reverse() # Sorts the list descending
printList(numbers)
numbers.insert(5, 10) # inserts to the 5 index number 10
printList(numbers)
numbers.remove(10) # removes from the list the value 10
printList(numbers)
numbers.pop(2) # removes the item on index 2
printList(numbers)

evenList = [i*2 for i in range(10)] # Creates a list of 10 elements, from 1 to 10, doubling all element
printList (evenList)

numList = [1, 2, 3, 4, 5]
listOfValues = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)]
                for m in numList] # For each element in the list executes raise to the power to 2nd, 3rd and 4th
printList(listOfValues)

multiDList = [[0] * 10 for i in range(10)]
multiDList[0][1] = 5
printList(multiDList)

listTable = [[0] * 5 for i in range(5)]
for i in range(5):
    for j in range(5):
        listTable[i][j] = "{} : {}".format(i, j)
    
printList(listTable)
'''

# Create a multiplication table from 1 to 9

multiTable = [[0] * 9 for i in range(9)]
for i in range(9):
    for j in range(9):
        multiTable[i][j] = (i+1) * (j+1)
printList(multiTable)










