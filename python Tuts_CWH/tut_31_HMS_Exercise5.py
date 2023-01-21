
# Health Management System :
# 3 clients - Gaurav, Rohan, Hammid

import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k == 1:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            value = input("type here\n")
            with open("Gaurav_ex.txt", "a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written")
        elif c == 2:
            value = input("type here\n")
            with open("Gaurav_fd.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
    elif k == 2:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            value = input("type here\n")
            with open("Rohan_ex.txt", "a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written")
        elif c == 2:
            value = input("type here\n")
            with open("Rohan_fd.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
    elif k == 3:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            value = input("type here\n")
            with open("Hammid_ex.txt", "a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written")
        elif c == 2:
            value = input("type here\n")
            with open("Hammid_fd.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
    else:
        print("Please enter a valid input 1(Gaurav), 2(Rohan), 3(Hammid)")

def retrieve(k):
    if k ==1:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("Gaurav_ex.txt") as op:
                for i in op:
                    print(i, end=" ")
        elif c == 2:
            with open("Gaurav_fd.txt") as op:
                for i in op:
                    print(i, end=" ")
    elif k == 2:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("Rohan_ex.txt") as op:
                for i in op:
                    print(i, end=" ")
        elif c == 2:
            with open("Rohan_fd.txt") as op:
                for i in op:
                    print(i, end=" ")
    elif k == 2:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("hammid_ex.txt") as op:
                for i in op:
                    print(i, end=" ")
        elif c == 2:
            with open("Hammid_fd.txt") as op:
                for i in op:
                    print(i, end=" ")
    else:
        print("Please enter a valis input (Gaurav, Rohan, Hammid)")

# Main function

print("Health Management System: ")
a = int(input("Press 1 for log the value and 2 for retrieve"))

if a == 1:
    b = int(input("Press 1 for Gaurav 2 for rohan and 3 for hammid"))
    take(b)

else:
    b = int(input("Press 1 for Gaurav 2 for rohan and 3 for hammid"))
    retrieve(b)




