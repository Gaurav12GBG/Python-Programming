"""
Problem Statement : To accept the number and compute
                  a) Square root of number
                  b) Square of number
                  c) Cube of number
                  d) Check For Prime
                  e) Factorial of number
                  f) Prime factors
"""

# Taking a number as a input from the user
Number = int(input("Enter the number :"))

def Choose_Operation():
     operation = (input("Please select the operation that you want to perform : \n  1. Find_Square_root() \n  2. Find_Square() \n  3. Find_Cube() \n  4. Check_prime_number() \n  5. Find_factorial() \n  6. Prime_factors() \nPlease Enter Your Choise :"))

     if operation == '1':
         Find_Square_root()
     elif operation == '2':
         Find_Square()
     elif operation == '3':
         Find_Cube()
     elif operation == '4':
         Check_prime_number()
     elif operation == '5':
         Find_factorial()
     elif operation == '6':
         Prime_factors()
     else:
         print("\nError! Please enter a valid input")
         again()

def Find_Square_root():

    print(f"The Square root of {Number} = {Number ** 0.5}")

def Find_Square():

    print(f"The Square root of {Number} = {Number ** 2}")

def Find_Cube():

    print(f"The Square root of {Number} = {Number ** 3}")

def Check_prime_number():

    if Number <= 1:
        print(f"{Number} is not a prime number")
    else:
        for i in range(2, Number):
            if Number % i == 0:
                print(f"{Number} is not a prime number")
                break
        else:
            print(f"{Number} is a prime number")

def Find_factorial():

    factorial = 1
    if Number < 0:
        print("Sorry, Factorial does not exist for negative number")
    elif Number == 0:
        print("The factorial of 0 = 1")
    else:
        for i in range(1, Number+1):
            factorial = factorial * i
        print(f"The factorial of {Number} = {factorial}")

def Prime_factors():
    global Number
    prime_factor = []
    divisor = 2
    while divisor <= Number:
        if Number % divisor == 0:
            prime_factor.append(divisor)
            Number = Number/divisor
        else:
            divisor += 1
    print(prime_factor)

def again():
    cal_again = input("Do you want to calculate again ? \nPlease type y for YES and n for NO :")

    if cal_again == "y":
        print("\nHii, Again !!!")
        Choose_Operation()


    elif cal_again == "n":
        print("See you later !!!")

    else:
        again()

Choose_Operation()