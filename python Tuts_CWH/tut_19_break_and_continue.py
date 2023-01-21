
# Break and Continue

# i = 0
#
# while(True):
#     if i+1<5:
#         i = i+1
#         continue
#
#     print(i + 1, end=" ")
#     if i == 44:
#         break    # stop the loop
#     i = i + 1
#

# Quiz :

while True:
    inp = int(input("Enter the number"))
    if inp > 100:
        print("Congrats you have entered the number greater than 100\n")
        break
    else:
        print("try again !!!!")
        continue

