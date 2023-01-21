
# For Loop :

# list1 = [["Gaurav", 1], ["Rohan", 5],["ram", 78],["Vaishnavi", 32], ["a",8], ["try", 45]]
#
# dict1 = dict(list1)

# for item in dict1:
#     print(item)

# for item, lollypop in dict1.items():
#     print(item, "and lolly is", lollypop)

# items = [int, float, "harry", 5,3,6,48,45,62,48,789,456123,6,8,1]
#
# for item in items:
#     if str(item).isnumeric() and item > 5:
#         print(item)
#

# print("Second number pattern")
# lastNumber = 6
# for row in range(1, lastNumber):
#     for column in range(1, row + 1):
#         print(column, end="")
#     print("")

print("Second number pattern from last")
lastnumber = 5
againnum = 5
for row in range(0, lastnumber+1):     # range 1 to 6
    for column in range(againnum-row, 0, -1): # range becomes 1 to 2 for first iteration
        print(column, end=" ")
    print("")
