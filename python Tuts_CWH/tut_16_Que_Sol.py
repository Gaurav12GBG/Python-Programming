#
# # String In Python :
# # 1. write a python program to calculate the length of the string ?
#
# str1 = "welcome"
# print("The length of given string :", len(str1)
#
# # Output : The length of given string : 7
#
# # 2.write a python program to remove the starting four character from a non empty string
# # Given string is : " india is my country "
#
# str2 = " india is my country "
# x = str2.replace("indi", "")
# print(x)
#
# # Output : a is my country
#
# # 3. write a python program to count a occurencess of each world in given sentence .
#
# str3 = " india is my country and india is special country "
# c = str3.count(" india ")
# print(c)
# c = str3.count(" is ")
# print(c)
# c = str3.count(" my ")
# print(c)
# c = str3.count(" country ")
# print(c)
# c = str3.count(" special ")
# print(c)
# c = str3.count(" and ")
# print(c)
#
# # Output: 2
# #         2
# #         1
# #         2
# #         1
# #         1
#
# # 4. write a python script that takes input from the user and displays that input back in upper and lower cases .
#
# str1 = input(" write the msg that u want in small letter :")
# print(" input back in upper case :", str1.upper())
# print(" input back in lower case :", str1.lower())
#
# # Output :  write the msg that u want in small letter :MY name is GAURAV bharat GANGURDE
# #           input back in upper case : MY NAME IS GAURAV BHARAT GANGURDE
# #           input back in lower case : my name is gaurav bharat gangurde
#
# # 5. write a python program to sort a string .
#
# s1 = "yxz"
# s2 = sorted(s1)
# s3 = "".join(s2)
# print(s3)
#
# # Output : xyz
#
# # List In Python :
# # 1. write a python program to get the smallest number from a list.
#
# ls = [15,12,1,5,8,10.5,25]
# ls1 = min(ls)
# print("The smallest number from the list :", ls1)
#
# # Output : The smallest number from the list : 1
#
# # 2. write a python program to check list is empty or not.
#
# list1 = [5, 12.3, " Vaishnavi ", 4, 8, True, 1+5j]
# print("Given list is empty :", len(list1) == 0)           # Here we can use if-else statements....
# print("Given list is not empty :", len(list1) != 0)
#
# # Output : Given list is empty : False
# #          Given list is not empty : True
#
# # 3.write a python program to clone or copy a list.
#
# list2 = [2, 10.2, "abc", 5, 8, False]
# copied = list2.copy()
# print(copied)
#
# # output : [2, 10.2, 'abc', 5, 8, False]
#
# # 4. Write a python program to access the index of a list.
#
# my_list = ["Educated", "Student", "Python learner", "Gamer"]
# access_index = my_list.index("Python learner")
# print(access_index)
#
# # Output : 2
#
# # 5. Write a python program to append a list to the second list.
#
# my_list1 = [1, 2, 3, 4, 5]
# my_list2 = ["India", "china", "West-indies", "pakistan"]
# my_list1.append(my_list2)
# print("The appending of my_list1 and my_list2 is :", my_list1)
#
# # Output : The appending of my_list1 and my_list2 is : [1, 2, 3, 4, 5, ['India', 'china', 'West-indies', 'pakistan']]
#
# # Tuple in python :
# # 1. Write python program to create a tuple with different data types.
#
# tup = (1, 2, 5, 10.5, 15.89, 0.833333, "vaishnavi", True, 1+15j)
# print("Tuple with different data types :", tup)
#
# # Output : Tuple with different data types : (1, 2, 5, 10.5, 15.89, 0.833333, 'vaishnavi', True, (1+15j))
#
# # 2.write a python program to create a tuple with numbers and print one item.
#
# tup1 = (4,2,8,6,7,22,45,6325,859647)
# x = tup1[6]
# print(x)
#
# # Output : 45
#
# # 3.Write a python program to add an item in a tuple.
#
# tup2 = ("bhairavi", "tamanna", "minakshi", "karina")
# tup2 = tup2 + ("katrina",)
# print(tup2)
#
# # Output : {'bhairavi', 'karina', 'tamanna', 'minakshi', 'katrina'}
#
# # 4.Write a python program to convert tuple to a string.
#
# tup3 = ("my", "name", "is",  "a vaishnavi")
# str_new = str(tup3)
# print(str_new)
# print(type(str_new))
#
# # Output : ('my', 'name', 'is', 'a vaishnavi')
# #          <class 'str'>
#
# # 5.Write a python program to remove an item from a tuple.
#
# tup4 = (5, 8, "bharat", True, 1+86j, 10.5000)
# convert = list(tup4)
# convert.remove("bharat")
# tup5 = tuple(convert)
# print(tup5)
#
# # Output : (5, 8, True, (1+86j), 10.5)
#
# # Dictionary in python :
# # 1.Write a python script to add an key name "Education" with respected value to a dictionary.
# # Input : {"Name":"virat","Address":"canada"}
#
# Input = {"Name": "Ramesh", "Address": "canada"}
# Input.update({"Education": "BE"},)
# print(Input)
#
# # Output : {'Name': 'Ramesh', 'Address': 'canada', 'Education': 'BE'}
#
# # 2.Write a python script to check whether a given key exists in a dictionary or not.use above dictionary.
#
# Above_d = {'Name': 'Ramesh', 'Address': 'canada', 'Education': 'BE'}
# z = Above_d.setdefault("Name")
# print(z)
#
# # Output : Ramesh
#
# # 3.Write a python program to remove a key from dictionary.
#
# New_d = {'Name': 'Ramesh', 'Address': 'canada', 'Education': 'BE'}
# New_d.pop("Address")
# print(New_d)
#
# # output : {'Name': 'Ramesh', 'Education': 'BE'}
#
# # 4.Write a python program to check dictionary is empty or not.
#
# Again_d = {'Name': 'Ramesh', 'Education': 'BE'}
# Again_d.clear()
# print("Given list is empty :", len(Again_d) == 0)           # Here we can use if-else statements....
# print("Given list is not empty :", len(Again_d) != 0)
#
# # Output : Given list is empty : True
# #          Given list is not empty : False
#
# # 5.Write a python program to check how many keys present in dictionary.
#
# My_D = {'Name': 'Ramesh', 'Address': 'canada', 'Education': 'BE'}
# My_D.keys()
# print("The keys present in a dictionary is:", len(My_D))
#
# # Output : The keys present in a dictionary is: 3
#
#
# # SET in python :
# # 1.Write a python program to create a set with data of string type.
#
# my_set = {"mango", "banana", "apple", "orange", "guava", "grapes", "mango"}
# print("The fruits in the form of set is :", my_set)
#
# # Output : The fruits in the form of set is : {'grapes', 'orange', 'guava', 'apple', 'mango', 'banana'}
#
# # 2.Write a python program to add member(s) in a set.
#
# new_set = {"mango", "banana", "apple", "orange", "guava", "grapes", "mango"}
# new_set.add("s")
# print(new_set)
#
# # Output : {'grapes', 'apple', 'mango', 'guava', 'orange', 'banana', 's'}
#
# # 3.Write a python program to remove item(s) from a given set.
#
# again_set = {'grapes', 'apple', 'mango', 'guava', 'orange', 'banana', 's'}
# again_set.remove('s')
# print(again_set)
#
# # Output : {'mango', 'grapes', 'banana', 'orange', 'guava', 'apple'}
#
# # 4.Write a python program to create a union of sets.
#
# P = {1, 4, 6, 8, 2, 0}
# Q = {45, 2, 4, 8, 10, 12, 6}
# R = {1, 2, 3}
#
# union_set = P.union(Q,R)       # P | Q | R
# print("The union of P and Q,R is:", union_set)
#
# # Output : The union of P and Q,R is: {0, 1, 2, 3, 4, 6, 8, 10, 12, 45}
#
# # 5.Write a python program to check if a set is a subset of another set.
#
# P = {1, 4, 6, 8, 2, 0, 3}
# Q = {45, 2, 4, 8, 10, 12, 6}
# R = {1,2,3}
#
# check = P.issubset(Q)
# print("check whether p is subset of Q or not :", check)
# check_again = R.issubset(P)
# print("check whether R is subset of P or not :", check_again)
#
# # Output : check whether p is subset of Q or not : False
# #          check whether R is subset of P or not : True