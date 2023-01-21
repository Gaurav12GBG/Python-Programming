
"""
1. Write a program that finds the greatest of three given number using function. Pass number as argument.
"""

num1 = int(input("Enter the 1st number\n"))
num2 = int(input("Enter the 2nd number\n"))
num3 = int(input("Enter the 3rd number\n"))

def greatest_num ():
    if num1 > num2:
        print("The greatest number is:", num1)
    elif num2 > num3:
        print("The greatest number is:", num2)
    elif num3 > num1:
        print("The greatest number is:", num3)
    elif num1 == num2 == num3:
        print("Your choosing same numbers, Please choose different numbers like ( 11, 42, 48 )")

greatest_num()

"""
Output : Enter the 1st number
         12
         Enter the 2nd number
         45
         Enter the 3rd number
         78
         The greatest number is: 78
"""


"""
2. Write a function is 'leap_year' which takes the year as its argument and checks whether the year is leap year or not 
   and then display appropriate message on screen.
"""
Year = int(input("Please enter the year\n"))

def leap_year():
    if Year % 4 == 0:
        print(Year, "is a leap year")
    else:
        print(Year, "is not a leap year")

leap_year()

"""
Output : Please enter the year
         2021
         2021 is not a leap year
"""



