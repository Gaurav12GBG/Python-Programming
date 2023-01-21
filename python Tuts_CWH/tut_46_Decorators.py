# def function1():
#     print("Subscribe now")

# func2 = function1
# del function1
# func2()

# def funcret(num):
#     if num == 0:
#         return print
#     else:
#         return int

# a = funcret(0)
# print(a)

# def executor(func):
#     func("This")

# executor(print)

# DECORATORS :
def decorators(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("executed")
    
    return nowexec

@decorators
def who_is_gbg():
    print("gbg is a good boy")

# who_is_gbg = decorators(who_is_gbg)
who_is_gbg()
