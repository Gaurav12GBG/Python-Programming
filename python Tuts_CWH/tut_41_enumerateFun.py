# Enumerate function :
l1 = ["Bhindi", "Aloo", "Chopsticks", "Chowmein"]

# i = 1
# for item in l1:
#     if i%2 != 0:
#         print(f"Jarvis please buy {item}")
#     i+=1

# Using enumerate function:

for index, item in enumerate(l1):
    if index%2 != 0:
        print(f"Jarvis please buy {item}")


l2 = [1, 4, 6, 5, 9]

for index, item in enumerate(l2):
    if index%2 != 0:
        print(f"The add from the list is = {item}")