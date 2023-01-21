
# Function in python : It is a block of codes.

# a = 9
# b = 8
# c = sum((a, b))  # Built in function
# print(c)

# def function1(a, b):
#     print("Hello you are in function1 :", a+b)

# def function2(a, b):
#     """This is a Function which will calculate average of two numbers
#     and this function doesn`t work for three numbers..."""         # This is not a comment,this is the way of writing docstrings
#     avg = (a + b) / 2
#     # print(avg)
#     return avg
#
# # v = function2(7, 5)
# # print(v)
# print(function2.__doc__)       # In this way we can print the docstrings

'''Write a function calculator() such that it can accept two variable and calculate the addition and subtraction of them.
And also it must return both operation in a single return call'''

#
# def calculator(a, b):
#     return a+b, a-b
#
# add, sub = calculator(10, 5)
# print(add)
# print(sub)

'''Create a function showEmployee() in such way that it should accept employee name, and its salary and display both.
    if the salary is missing in the function call assign default value 9000 to salary'''

# def showEmployee(employeeName, salary=9000):
#     print(employeeName, "salary is", salary)
## showEmployee("Gaurav", 9000)
# showEmployee("Gaurav")

'''Create an inner function to calculate the addition in the fallowing way
1. Create an outer function that accept two parameters
2. Create an inner function inside an outer function that will calculate addition of two number
3. At last, an outer function will add 5 into addition and return it'''

# def outer(a, b):
#     square = a**2
#     def inner(a, b):
#         return a+b
#     add = inner(a, b)
#     return add+5
# result = outer(5, 10)
# print(result)

'''Write a recursive function to calculate the sum of numbers from 0 to 20
So what is recursive function ?
        ====> The function will call itself and repeat its behavior until some condition is met to return a result'''

# def calculateSum(num):
#        if num:
#           return num + calculateSum(num-1)
#        else:
#            return 0
#
# res = calculateSum(20)
# print(res)

'''Assign a different name to function and call it through the new name'''

# def displayStudent(name, age):
#     print(name, age)
#
# displayStudent('Gaurav', 21)
# showStudent = displayStudent
# showStudent('Gaurav', 21)

'''Generate a python list of all even numbers between 4 to 30'''

# print(list(range(4, 30, 2)))
# Here the range is one of the function..

'''Return a largest and smallest item from the list'''

# alist = [4, 56, 12, 78, 86, 48, 789, 456, 999]
# print(max(alist))
# print(min(alist))
# Here the max is one of the function...

# def personInfo(name, Edu):
#     print("my name is", name, "and my education is", Edu)
#
# personInfo("Ram" , "BE")

def addition(a, b): # Parameterised function
    return a + b

num1 = int(input("Enter the 1st number"))
num2 = int(input("Enter the 2nd number"))

res = addition(num1, num2) # This is a function call
print(res)



















