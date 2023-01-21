# List Data Structure =>

# Here we are created one list
list1 = ['Vaishnavi', 'india', 'pratiksha']


# List operations
# 1.check length and type of lists

print("Length of the given list is :", len(list1))
print("class/type of list1 :", type(list1))

# 2.Append() - 	Adds an element at the end of the list

list1.append("Rohan Das")
print("The complete list after appending is :", list1)

# 3.copy() - Returns a copy of the list

newList = list1.copy()
print("Copied list is :", newList)

# 4.count() - Returns the number of elements with the specified value

count = newList.count("india")
print("The count of 'india' into the list is :", count)

# 5.extend() - Add the elements of countryList to the newList :

print("This is a newList :", newList)

countryList = ["Pakistan", "Austrelia"]
newList.extend(countryList)
print("Now the newList is after extending the list :", newList)

# 6.index() - Returns the index of the first element with the specified value

indexPosition = newList.index("Austrelia")
print("The position of 'Austrelia' is:", indexPosition)

# 7.insert() - Insert the value "Ram" as the second element of the newList:

newList.insert(2, "Ram")
print("After insertion of 'Ram' into the list:", newList)

# 8.pop() - Remove the 5th element of the newList:

newList.pop(5)
print("After Poping the 5th element newList is:", newList)

# 9.remove() - Remove the "Pakistan" element of the newList:

newList.remove("Austrelia")
print("After removing the 'Pakistan' element the newList is:", newList)

# 10.reverse() - Reverse the order of the newList:

newList.reverse()
print("After reversing the newList is:", newList)

# 11.sort() - Sort the list alphabetically:

newList.sort()
print("After sorting the newList is:", newList)

# 12.clear() - Remove all elements from the newList:

newList.clear()
print("After clearing list the newList is:", newList)

"""

# OUTPUT :

Length of the given list is : 3
class/type of list1 : <class 'list'>
The complete list after appending is : ['Vaishnavi', 'india', 'pratiksha', 'Rohan Das']
Copied list is : ['Vaishnavi', 'india', 'pratiksha', 'Rohan Das']
The count of 'india' into the list is : 1
This is a newList : ['Vaishnavi', 'india', 'pratiksha', 'Rohan Das']
Now the newList is after extending the list : ['Vaishnavi', 'india', 'pratiksha', 'Rohan Das', 'Pakistan', 'Austrelia']
The position of 'Austrelia' is: 5
After insertion of 'Ram' into the list: ['Vaishnavi', 'india', 'Ram', 'pratiksha', 'Rohan Das', 'Pakistan', 'Austrelia']
After Poping the 5th element newList is: ['Vaishnavi', 'india', 'Ram', 'pratiksha', 'Rohan Das', 'Austrelia']
After removing the 'Pakistan' element the newList is: ['Vaishnavi', 'india', 'Ram', 'pratiksha', 'Rohan Das']
After reversing the newList is: ['Rohan Das', 'pratiksha', 'Ram', 'india', 'Vaishnavi']
After sorting the newList is: ['Ram', 'Rohan Das', 'Vaishnavi', 'india', 'pratiksha']
After clearing list the newList is: []

"""

# ==================================================================================

# Tuple Data Structure:
print("\nTuple Operations:")

newList = ['Vaishnavi', 'india', 'pratiksha', 'Rohan Das', 'Vaishnavi']

# Now here newList is converted into the tuple

newTuple = tuple(newList)
print("The newList is converted into the tuple :", newTuple)

# 1.count() - Return the number of times the value 'Vaishnavi' appears in the newTuple:

a = newTuple.count('Vaishnavi')
print("The count of 'Vaishnavi' into the newTuple is:", a)

# 2.index() - Searches the tuple for a specified value and returns the position of where it was found

x = newTuple.index('Rohan Das')
print("The position of 'Rohan das' into the newTuple is:", x)


"""

OUTPUT:

Tuple Operations:
The newList is converted into the tuple : ('Vaishnavi', 'india', 'pratiksha', 'Rohan Das', 'Vaishnavi')
The count of 'Vaishnavi' into the newTuple is: 2
The position of 'Rohan das' into the newTuple is: 3

"""