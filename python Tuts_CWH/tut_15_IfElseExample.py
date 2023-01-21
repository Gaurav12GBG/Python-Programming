# conditional statements :

std1 = input("Enter the 1st student name : ")
std2 = input("Enter the 2nd student name : ")

x = len(std1)
y = len(std2)

if x > y:
    print("The bigger one is:", std1)
    print("The smaller one is:", std2)
else:
    print("The bigger one is:", std2)
    print("The smaller one is:", std1)
