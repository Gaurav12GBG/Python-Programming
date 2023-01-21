
# File IO Open(), Read() and Readline() :

f = open("myInfo.txt", "rt")
# content = f.read()
# print(content)

# f = open("myInfo.txt", "rt")
# content = f.read(10)
# print("1", content)
#
# content = f.read()
# print("2", content)

# for line in f:
#     print(line, end=" ")

# print(f.readline())
# print(f.readline())
# print(f.readline())

print(f.readlines())

f.close()