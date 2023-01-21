# Anonymous OR Lambda function :

# def add(a, b):
#     return a + b;

# def sub(x, y):
#     return x - y

# Using lambda :

add = lambda a, b : a + b
sub = lambda x, y : x - y
print("The additioon is :", add(5, 5))
print("The subtraction is :", sub(9, 4))

# def a_first(a):
#     return a[1]

a = [[1, 14], [5, 6], [10, 2]]
# a.sort(key=a_first)
a.sort(key=lambda x: x[1])
print(a)