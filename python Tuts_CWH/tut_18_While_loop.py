
# while loop:

# i = 0
#
# while i < 45:
#     print(i, end=" ")
#     i = i + 1

# Write a program to calculate the average of five numbers by taking it from users.
#
# add = 0
# i = 0
#
# while i < 5:
#     nums = int(input("Enter the numbers :"))
#     add = add + nums
#     i = i + 1
# print("The average of five numbers is :", add/5)


#  Display fibonacci series up to 10 terms.

terms = 30
#first two numbers
num1, num2 = 0, 1
count = 0

print("Fibonacci sequence:")
while count < terms:
    print(num1, end=" ")
    temp = num1 + num2
#     updated values
    num1 = num2
    num2 = temp
    count = count + 1

# Write a loop to find factorial of any number.

# print("Welcome in my calculator to find factorial of a number.")
# num = int(input("Enter the number"))
# factorial = 1
# if num < 0:
#     print("Factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1, num + 1):
#         factorial = factorial * i
#     print("The factorial of", num, "is", factorial)

