"""
Use of map, reduce and filter functions : 
1. map() ==> A map function executes certain instruction or functionality provided to it on
             every item of an iterable. The iterable could be list, tuple, set etc.
             syntax :  map(function, iterable)

2. filter() => A filter function in python tests a specific user-defined condition for a
               function and returns an iterable for the elements and values that satisfy the condition or, in other words, return true.
               syntax : filter(function, iterable)
        
3. reduce() =>

"""

# numbers = ["3", "4", "64"]

# for i in range(0, len(numbers)):
#     numbers[i] = int(numbers[i])

# numbers = list(map(int, numbers))
    
# numbers[2] = numbers[2] + 1
# print(numbers[2])

# num = [2, 3, 4, 5, 6, 7, 8, 9]
# square = list(map(lambda x: x*x, num))
# print(square)

# def square(a):
#     return a*a

# def cube(a):
#     return a*a*a

# func = [square, cube]
# num = [2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(5):
#     val = list(map(lambda x:x(i), func))
#     print(val)
# ---------------------------FILTER---------------------------------------
# list1 = [1,2,3,4,5,6,7,8,9]
# def is_greater_5(num):
#     return num>5

# gr_than_5 = list(filter(is_greater_5, list1))
# print(gr_than_5)

#---------------------------REDUCE-----------------------------------------
from functools import reduce

list1 = [1,2,3,4]
# num = 0
# for i in list1:
#     num = num + i
# print(num)

num = reduce(lambda x, y: x+y, list1)
print(num)
 