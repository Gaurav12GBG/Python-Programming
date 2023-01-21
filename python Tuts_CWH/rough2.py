"""
Problem Statement : To accept N numbers from user. Compute and display maximum in list , minimum in list , sum
                    and average of numbers.
"""

# lst = []
# How_many_numbers = int(input("Enter how many number you want to insert in a list :"))
# print("Please insert the number in a list :")
# for i in range(0, How_many_numbers):
#     Numbers = int(input())
#     lst.append(Numbers)
# print("The numbers entered by user in a list is :", lst)
#
# def Choose_Operation():
#     operation = (input("Please select the operation that you want to perform : \n  1. Minimum() \n  2. Maximum() \n  3. Sum() \n  4. average() \nPlease Enter Your Choise :"))
#
#     if operation == '1':
#         Find_Minimum()
#     elif operation == '2':
#         Find_Maximum()
#     elif operation == '3':
#         Find_Sum()
#     elif operation == '4':
#         Find_Average()
#     else:
#         print("\nError! Please enter a valid input")
#         again()
#
# def Find_Maximum():
#     maximum_number = max(lst)
#     print("The minimum number from the list =", maximum_number)
#
# def Find_Minimum():
#     minimum_number = min(lst)
#     print("The minimum number from the list =", minimum_number)
#
# def Find_Sum():
#     Total = 0
#     for element in lst:
#        Total = Total + element
#
#     print("The sum of numbers from the list =", Total)
#
# def Find_Average():
#     Total = 0
#     for element in lst:
#         Total = Total + element
#
#     Average = Total/len(lst)
#     print("The Average of numbers from the list =", Average)
#
# def again():
#         cal_again = input("Do you want to calculate again ? \nPlease type y for YES and n for NO :")
#
#         if cal_again == "y":
#             print("\nHii, Again !!!")
#             Choose_Operation()
#
#
#         elif cal_again == "n":
#             print("See you later !!!")
#
#         else:
#             again()
#
# Choose_Operation()
# Empty list
lst = []

# Input For Choosing how many number user wants
How_many_numbers = int(input("Enter how many number you want to insert in a list :"))

# Numbers input from user
print("Please insert the number in a list :")

# Appending in a list using for loop and append function
for i in range(0, How_many_numbers):
      Numbers = int(input())
      lst.append(Numbers)
print("The numbers entered by user in a list is :", lst)

# For Maximum Calculation
maximum_number = max(lst)
print("The minimum number from the list =", maximum_number)

# For Minimum Calculation
minimum_number = min(lst)
print("The minimum number from the list =", minimum_number)

# For Sum Calculation
Total = 0
for element in lst:
  Total = Total + element
print("The sum of numbers from the list =", Total)

# For Average Calculation
Total = 0
for element in lst:
  Total = Total + element
Average = Total/len(lst)
print("The Average of numbers from the list =", Average)

"""
Output : Enter how many number you want to insert in a list :2
         Please insert the number in a list :
         12
         10
         The numbers entered by user in a list is : [12, 10]
         The minimum number from the list = 12
         The minimum number from the list = 10
         The sum of numbers from the list = 22
         The Average of numbers from the list = 11.0
"""