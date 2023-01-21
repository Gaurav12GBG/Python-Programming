
"""Exercise 4 :
Take Input = n
Boolean = True OR False

True n = 5
*
**
***
****
*****

False n = 5
*****
****
***
**
*
"""

print("Pattern printing")
num = int(input("Enter the number how many rows you want :"))
bool_Value = int(input("Type 1 Or 0 :"))
new = bool(bool_Value)
if new == True:
    for i in range(0, num + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()
elif new == False:
    for i in range(num, 0, -1):
        for j in range(1, i + 1):
            print("*", end="")
        print()




