
# Using Seek(), Tell() and more on files :

"""
This code change the file position to 5, print the rest of the line.
"""
# f = open("myInfo3.txt", "r")
# print(f.readline())
# f.seek(5)
# print(f.readline())

# Now actually the seek() and tell():
f = open("myInfo3.txt")
f.seek(11)
print(f.tell())
print(f.readline())
# print(f.tell())

print(f.readline())
# print(f.tell())
f.close()