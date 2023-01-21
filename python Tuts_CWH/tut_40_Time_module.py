# Time Module
import time

# initial1 = time.time()
# # print(initial)

# k = 0
# print("Using while-loop :")
# while k<25:
#     print("This is python tutorial")
#     k+=1
# print(f"While loop ran in {time.time() - initial1} seconds")


initial2 = time.time()       # Reset the time
print("\nUsing for-loop :")
for i in range(25):
    print("This is python tutorial")
print(f"For loop ran in {time.time() - initial2} seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)
 
print("Abhishek")
time.sleep(5)  # takes in sec

print("Gaurav")
