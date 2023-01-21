"""
Recursion :- recursion occurs when a function call itself.
           - recursion can only be applied to a function.
           - Lesser coding has done in case of recursion than iteration.
           - Back tracking or reverse engineering in case of recursion can be difficult.
           - In the case of recursion , if the condition is not met, the system will repeat a few times & then crash.
           - It is still slower in execution because the function has to be called again, and again storing
            data into the stack also increases the time of execution.
           - In my opinion for smaller programs where there are lesser lines of codes, We should use recursive
            approach and in complex program, We should go with iteration to reduce the risk of bugs.
"""

# n! = n * n-1 * n-2 * n-3........1
# n! = n * (n-1)!
#
# def factorial_iterative(n):
#     """
#         :param n: Integer
#         :return:  n! = n * n-1 * n-2 * n-3........1
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac
#
# def factorial_recursive(n):
#     """
#         :param n: Integer
#         :return:  n! = n * n-1 * n-2 * n-3........1
#     """
#     if n == 1:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)

    # 5 * factorial_recursive(4)
    #   5 * 4 * factorial_recursive(3)
    #   5 * 4 * 3 * factorial_recursive(2)
    #   5 * 4 * 3 * 2 * factorial_recursive(1)
    #   5 * 4 * 3 * 2 * 1 = 120

# 0 1 1 2 3 5 8 13

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


number = int(input("Enter the number"))
# print("factorial using iterative method :", factorial_iterative(number))
# print("factorial using recursive method :", factorial_recursive(number))
print(fibonacci(number))