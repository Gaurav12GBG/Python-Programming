
# IF-ELSE AND ELIF

# var1 = 6
# var2 = 56
# var3 = int(input(" Please enter the number"))
#
# if var3 > var2:
#     print("Greater")
# elif var3 == var2:
#         print("Equal")
# else:
#     print("Lesser")

#
# list1 = [5, 7, 3]
#
# if 5 in list1:
#     print("Yes it is in list")

#
# # Quiz :
# print("What is your age?")
# age = int(input())
#
# if age > 18:
#     print("U can drive")
# elif age == 18:
#         print("We will think about u")
# else:

#     print("U cannot drive")

'''
Exercise 2 : Faulty calculator
Design a calculator which will correctly solve all the problems except the following ones :
45 * 3 = 555, 56+9 = 77, 56/6= 4
Your program should take operator and the two numbers as input from the user and then return the result.
'''

print("Enter the 1st number :")
var1 = int(input())      # num1  45
print("Enter the 1st number :")
var2 = int(input())      # num2  3
print("So What you want?"+"+,-,*,/,%")
op = input()       # operator *

if var1 == 45 and  var2 == 3 and op == '*':
    print("555")
elif var1 == 56 and var2 == 9 and op == '+':
    print("77")
elif var1 == 56 and var2 == 6 and op == '/':
    print("4")
elif op == '*':
    result = var1 * var2
    print(result)
elif op == '+':
    result = var1 + var2
    print(result)
elif op == '/':
    result = var1 / var2
    print(result)
elif op == '-':
    result = var1 - var2
    print(result)
elif op == '%':
    result = var1 % var2
    print(result)
else:
    print("Error ! Please check your input")

















