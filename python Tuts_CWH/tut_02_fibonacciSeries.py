"""
Problem Statement : To accept from user the number of fibonacci series to be generated and print the fibonacci
                    series.
"""

Number = int(input("Enter the number :"))

num1, num2 = 0, 1
count = 0
print("Fibonacci series:")
while count < Number:
    print(num1, end=" ")
    temp = num1 + num2

    num1 = num2
    num2 = temp
    count = count + 1

"""
Output : Enter the number :10
         Fibonacci sequence:
         0 1 1 2 3 5 8 13 21 34 
"""