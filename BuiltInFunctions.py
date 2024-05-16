# BuiltInFunctions.py
# Programmer: Adelita Martinez 
# Date: 16 May 2024
# Purpose: Demonstrate built in python functions

# # Get a number from user and display absolute 
# num = float(input('Please enter a number: '))
# # abs() returns the absolute value of a number
# absolute = abs(num)
# print('The absolute value is',absolute)

# # Find the minimum of two numbers
# num1 = float(input('Please enter first number: '))
# num2 = float(input('Please enter second number: '))
# # min() returns the largest item
# minimum_value = min(num1,num2)
# print('The lowest of those two numbers is', minimum_value)

# #Round a number
# new_num = float(input('Please enter a decimal number: '))
# # round() is used to round numbers
# rounded = round(new_num)
# print('The rounded value is', rounded)

# Raise a number to a power 
decimal_number = float(input('Please enter a decimal number: '))
exponenet = float(input("Please enter a value to raise number to: "))
# pow() Returns the value of x to the power of y
raised_value = pow(decimal_number, exponenet)
print('The value is', raised_value)
