
# File writing and appending to a file :

# Something write in a file

# f = open("myInfo.txt", "w")
# f.write("Gaurav bhai bahut acche hai\n")
# print(a)
# f.close()

# Something Append in a file

# f = open("myInfo2.txt", "a")
# a = f.write("Gaurav bhai bahut acche hai\n")
# print(a)
# f.close()


# Handle read and write both

f = open("myInfo2.txt", "r+")
print(f.read())
f.write("thank you\n")
f.write("I am big professional in python\n")
f.write("Hey that`s a gbg`s knowledge.....")
f.close()
