''' 
#Ask the user to input their name and assign it to a variable named 'name'
name = input('What is your name? ')

# Print the name entered
print('Hello',name)

# Ask the user to input 2 values and stre them in variables num1 and num2
num1, num2 = input ("Enter to numbers: ").split() 
# Convert the strings into regular numbers Integer
num1=int(num1)
num2=int(num2)
# Add the values enetered and store in a variable sum
sum = num1 + num2
# Subtract values and store in difference
difference = num1 - num2
# Multipy values and store in product
production = num1 * num2
# Divide values and store in quotient
quotient = num1 / num2
# Use modulus on the values to find their remainder
remainder = num1 % num2
# Print the results
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, production))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))

# Problem: Receive miles and convert to kilometers
# kilometers = miles * 1.60934
# Enter Miles 5
# 5 miles equals 8.04 kilometers

# Ask user to enter miles and assign it to miles variable
miles = input("Miles? ")
# Convert the string into integer
miles = int(miles)
# calculate kilometers by multipliing miles by 1.60934
kilometers = miles * 1.60934
# Disaplay a text showing the miles and the kilometers
print("{} miles equals to {} kilometers".format(miles, kilometers))


# Enter calculation: 5 + 6
# 5 + 6 = 11

# Ask user to input the calculation
num1, operation, num2 = input("Enter the calculation: ").split()
# Convert num1 and num2 to integer
num1 = int(num1)
num2 = int(num2)
# Calculate the result based on the operation and store it in the result 
if operation == "+":
    result = num1 + num2
elif operation == "*":
    result = num1 * num2
elif operation == "-":
    result = num1 - num2
elif operation == "/":
    result = num1 / num2
else:
    result = False
# Print out the calculation and the result
if result == False:
    print("Use + - * or /")
else:
    print("{} {} {} = {}".format(num1, operation, num2, result))

# We'll provide different output based on the age
# 1 - 18 -> Important
# 21, 50, < 65 -> Important
# All others -> Not important

# Receive and age and store in variable age
age = eval(input("Your age? "))

# and : if both conditions true return true
# or : if either conditions true return true
# not : Convert a true into a false and vica versa

# if age both greater and equal to 1 and less then or equal 18 Important
if (age >= 1 and age <= 18):
    print("Important")
# if age is 21, 50 Important
elif (age == 21 or age == 50):
    print("Important")
# We check if age is less then 65 and convert true to false and vica versa
elif not(age < 65):
    print("Important")
# Else Not important
else:
    print("Not important")

# If age is 5 Go to Kindergarden
# If ages 6 through 17 goes to grades 1 through 12
# If age is greather then 17 say go to college
# Try to complete with 10 or less lines

# Ask the user for age
age = eval(input("Your age? "))
# If age is 5, print go to kindergarden
if age == 5:
    print("Go to kindergarden")
# If ages is 6 through 17 print go to grade 1 through 12
elif (age >= 6 and age <= 17):
    print("Go to grade {}".format(age-5))
# If age is 17 or above, go to college
elif age > 17:
    print("Go to college")

# Print out Python version used
import sys
print(sys.version_info)

'''

