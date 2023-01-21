
# Faulty calculator using function :

def calculator():
    print("\nWelcome to calc: This is developed by Gaurav Gangurde")

    operation = input(" Please type in the math operation you would like to complete :\n" +
        "   + For Addition \n   - For Subtraction \n   * For Multiplication \n   / For Division \n   % For Modulus \n" +
        "   Enter your Choice :")

    num1 = int(input("Enter the 1st number :"))
    num2 = int(input("Enter the 2nd number :"))

    if operation == '+':
      if num1 == 56 and num2 == 9:
            print("56+9=77")
      else:
            print(f"{num1} + {num2} =", num1 + num2)
    elif operation == '*':
      if num1 == 45 and num2 == 3:
            print("45*3=555")
      else:
            print(f"{num1} * {num2} =", num1 * num2)
    elif operation == '/':
      if num1 == 56 and num2 == 6:
            print("56/6=4")
      else:
            print(f"{num1} / {num2} =", num1 / num2)
    elif operation == '-':
        print(f"{num1} - {num2} =",  num1 - num2 )
    elif operation == '**':
        print(f"{num1} ** {num2} =", num1 ** num2)
    elif operation == '%':
        print(f"{num1} % {num2} =", num1 % num2)
    else:
        print("   Error ! Please check your input ")
        again()

def again():
 cal_again = input("Do you want to calculate again ?\n Please type y for YES and n for NO :")

 if cal_again == "y":
     calculator()
 elif cal_again == "n":
     print("See you later !!!")

 else:
     again()

calculator()

