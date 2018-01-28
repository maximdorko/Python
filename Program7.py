'''
import os # Imports OS file module

with open("mydata.txt", mode = "w", encoding="utf-8") as myFile:
# Opens a file (with guarantees, it will be closed if the program hangs. "w" means overwrite anything in it. "a" means append).
# The file is open with UTF-8 encoding. The file can be accessed as "myFile"
    myFile.write("Some random text\nAnd some more random text\nAnd even more") # Writes in the file. Write is not adding CRLF at the end automatically

with open("mydata.txt", encoding="utf-8") as myFile: # Opens the file in read mode. If the mode is not defined, it's read mode
#    myFile.read() # Reads everything until a CRLF
#    myFile.readline() # Reads everything, including new lines
#    myFile.readlines() # Returns a list type with all the lines, including new lines
    print(myFile.read()) # Read the file into one string

print(myFile.closed) # Gives True if the file is closed
print(myFile.name) # Gives back the file name of the alias
print(myFile.mode) # Gives back the last used mode on the file

os.rename("mydata.txt", "mydata2.txt") # Renames the file
os.remove("mydata2.txt") # Deletes the file
os.mkdir("mydir") # Create a directory
os.chdir("mydir")


import os

os.chdir("mydir") # Change to the directory
print("My current directory is: ", os.getcwd()) # Prints the current directory
os.chdir("..") # Moves one directory up
print("My current directory is: ", os.getcwd()) # Prints the current directory
os.rmdir("mydir") # Removes a directory

import os
with open("mydata.txt", mode = "w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nAnd some more random text\nAnd even more")
with open("mydata.txt", encoding="utf-8") as myFile:
    lineNum = 1
    while True:
        line = myFile.readline() # Reads only one line into the variable
        if not line: # Means the line don't have any data
            break # Break out for loop if no data
        print("Line: ", lineNum, " : ", line, end = "") # Prints the line number and the value of the line
        lineNum += 1


# Read the file line by line
# Print the number of owrds in each line
# Print the average word length for each word
import os
with open("mydata.txt", mode = "w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nAnd some more random text\nAnd even more")
actualLine = []
lineNum = 1
wordsNum = 0
with open("mydata.txt", encoding="utf-8") as myFile:
    while True:
        actualLine = myFile.readline().split()
        if not actualLine:
            break
        wordsNum = len(actualLine)
        wordTotalLength = 0
        for i in range(wordsNum):
            wordTotalLength += len(actualLine[i])
        averageWordLength = wordTotalLength / wordsNum
        print( lineNum, " : ", "Number of Words: ", wordsNum, "|| Average word length: {:.2f}".format(averageWordLength))
        lineNum += 1
'''

# Tuples:
# Tuples is a list, but items can't be changed within the list
myTuple = (1, 2, 3, 4, 5) # Define a tuple
print("First value in the Tuple: ", myTuple[0]) # Prints the first item in the Tuple
print("First 3 values in the Tuple: ", myTuple[0:3]) # Prints the first 3 items in the Tuple
print("The Tuple's length = ", len(myTuple))
myTuple = myTuple + (13, 15, 21) # Items added to the Tuple
print("Items in the Tupple: ", myTuple)
print("5 in Tuple? ", 5 in myTuple) # Gives True is 5 is in the Tuple
for i in myTuple:
    print(i)
aList = [22, 554, 23] # Defines a list
aTuple = tuple(aList) # Converts a list into a tuple
aList = list(aTuple) # Coverts a tuple into a list
print("Min value in the Tuple: ", min(myTuple)) # Gives the minimum value in the tuple
print("Max value in the Tuple: ", max(myTuple)) # Gives the maximum value in the tuple
