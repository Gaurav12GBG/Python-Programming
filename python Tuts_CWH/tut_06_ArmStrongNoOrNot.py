
"""
Problem Statement : To check whether input number is Armstrong number or not . An Armstrong number is an integer with three digits such that the sum of the cubes of its digits is equal to the number itself. Ex. 371
"""

# Taking input from the user
Number = int(input("Enter the number :"))

# Initialization sum
sum = 0

# Find the sum of the cube of each digit
temp = Number
while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** 3)
    temp = temp // 10

# Displaying the result
if Number == sum:
    print(f"{Number} is an Armstrong Number")
else:
    print(f"{Number} is not an Armstrong Number")

"""
Output :

Enter the number :371
371 is an Armstrong Number
"""
