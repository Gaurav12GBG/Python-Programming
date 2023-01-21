"""
Problem Statement : To accept a number from user and print digits of a number in a reverse order.
"""

Number = int(input("Enter the integer Number :"))
Reverse_number = 0
while Number > 0:
    Remainder = Number % 10
    Reverse_number = (Reverse_number*10) + Remainder
    Number = Number//10
print("The Reverse number of entered number is ", Reverse_number)

"""
Output :
        Enter the integer Number :789
        The Reverse number of entered number is  987
"""
