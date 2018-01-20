'''
# Loops
for i in [2,4,8,10]:
    print("i = ",i)

# Using range
# range(10) means from 0 to 9
for i in range(10):
    print("i = ",i)

# range (2,10) will start from 2 and goes up to 9
for i in range(2,10):
    print("i = ", i)

# Print the odd numbers from 0 to 20
for num1 in range(1, 20):
    if (num1 % 2) != 0:
        print(num1)

# Request a user to input a number and convert it to float and print it rounded to 2 decimals
myfloat = input("Enter a number: ")
myfloat = float(myfloat)
print ("The number in float: {:.2f}".format(myfloat))

# Request user to enter their investment and interest rate
# Each year their investment will be increased by the investment + investment * interest rate
# Print the earnings after 10 years
investment = input ("Your investment?: ")
interestrate = input ("Interest rate?: ")
investment = float(investment)
interestrate = float(interestrate)
for years in range(1,11):
    investment = investment + (investment * (interestrate/100))
print ("The earnings are: {:.2f}".format(investment))

# Deek's solution

# Ask for the money and the interest rate
money = float(input("How much to invest? "))
interestrate = float(input("Interest rate?: "))
# Convert the value to float anf round it to 2 decimals
interestrate = interestrate * .01
# Cycle through 10 years usin for loop and range 0 to 9
for years in range(10):
    money = money + (money * interestrate)
# Output the results
print("Investment after 10 years: {:.2f}".format(money))

# Floating number are not precise: Only first 10 digits are reliable
num = 0.1 + 0.1 + 0.1 - 0.3
print(num)

# import random module
import random
# Generat a random number between 1 and 51 integer
rand_num = random.randrange(1, 51)
# Iterate until the we're at the random number
i = 1
while i != rand_num:
    i += 1
# Print when we found the random number
print("The random number is: ",rand_num)

# Break and continue
# Print all odd numbers until 20, stop id number is 15

i = 1
while i <= 20:
    if i%2 == 0:
        i+=1
        continue # This will jump back to the loop beginning and will ignore everything further
    if i == 15:
        break # This will jump out from the loop
    print("The odd number: ",i) # This will be true if the number is not odd and not 15
    i += 1
'''

###############################
#       Pine tree printing    #
###############################
# Ask for the tree height
tall = int(input("Tree height: "))
stump = tall - 1 # save the position of the stump
spaces = tall - 1 # The spaces are always actual height -1, at starting setting to requested height - 1
branches = 1 # branches are 1, 3, 5, 7, etc. Startin with 1
while tall != 0: # Cycle until tall is 0
    tall -= 1 # decrese tall
    for i in range(spaces): # printing spaces
        print(' ',end="") # print without new line
    for i in range(branches): # printing hashes
        print('#',end="") # print without new line
    spaces -= 1 
    branches +=2
    print() # new line at the end of the level
for i in range(stump): # print the stump
    print(" ",end="")
print("#")

