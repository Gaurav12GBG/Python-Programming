# Calculator using function and library :
import math

def Choose_calculator():
       choice = str(input("Please Choose Calculator for performing Various Operations :\n  1 For SCIENTIFIC CALCULATOR \n  2 For MATHEMATICAL CALCULATOR \n  Please Enter Your Choice :"))

       if choice == '1':
           Scientific_calculator()
       elif choice == '2':
           Mathmetical_calculator()
       else:
           print("  \nError ! Please check your input ")
           again()


def Scientific_calculator():
    print("\nWelcome to Scientific calculator : This is developed by Vaishnavi Gangurde.")

    Oper_n = input("Select the input for logarithm function OR Trigonometric function. \n  trf For TRIGONOMETRIC FUNCTION  \n  logf For LOGARITHMIC FUNCTION  \n  Please Enter Your Choice :")

    if Oper_n == 'trf':
        Trigonometry_operation = input(
            " \nPlease Select Trigonometric Function that you want to perform :\n  sinx For SINE FUNCTION \n  cosx For COSINE FUNCTION \n  tanx For TANGENT FUNCTION \n  cosecx For COSEC FUNCTION \n  secx For SEC FUNCTION \n  cotx For COT FUNCTION \n  sinhx For HYPERBOLIC SINE \n  coshx For HYPERBOLIC COSINE \n  tanhx For HYPERBOLIC TANGENT \n  cosechx For HYPERBOLIC COSEC  \n  sechx For HYPERBOLIC SEC \n  cothx For HYPERBOLIC COT \n  Please Enter your Choice :")

        if Trigonometry_operation == 'sinx':
                degree = float(input("  Enter the angle in degree :"))
                radian = degree * (math.pi / 180.0)
                print(f"  sin({degree}) = {math.sin(radian)}")

        elif Trigonometry_operation == 'cosx':
                degree = float(input("  Enter the angle in degree :"))
                radian = degree * (math.pi / 180.0)
                print(f"  cos({degree}) = {math.cos(radian)}")

        elif Trigonometry_operation == 'tanx':
                degree = float(input("  Enter the angle in degree :"))
                radian = degree * (math.pi / 180.0)
                print(f"  tan({degree}) = {math.tan(radian)}")

        elif Trigonometry_operation == 'cosecx':
                degree = float(input("  Enter the angle in degree :"))
                radian = degree * (math.pi / 180.0)
                print(f"  cosec({degree}) = {1 / math.sin(radian)}")

        elif Trigonometry_operation == 'secx':
                degree = float(input("  Enter the angle in degree :"))
                radian = degree * (math.pi / 180.0)
                print(f"  sec({degree}) = {1 / math.cos(radian)}")

        elif Trigonometry_operation == 'cotx':
            degree = float(input("  Enter the angle in degree :"))
            radian = degree * (math.pi / 180.0)
            print(f"  cot({degree}) = {1 / math.tan(radian)}")

        elif Trigonometry_operation == 'sinhx':
            degree = float(input("  Enter the angle in degree :"))
            radian = degree * (math.pi / 180.0)
            print(f"  sinh({degree}) = {math.sinh(radian)}")

        elif Trigonometry_operation == 'coshx':
            degree = float(input("  Enter the angle in degree :"))
            radian = degree * (math.pi / 180.0)
            print(f"  cosh({degree}) = {math.cosh(radian)}")

        elif Trigonometry_operation == 'tanhx':
            degree = float(input("  Enter the angle in degree :"))
            radian = degree * (math.pi / 180.0)
            print(f"  tanh({degree}) = {math.tanh(radian)}")

        elif Trigonometry_operation == 'cosechx':
            degree = float(input("  Enter the angle in degree :"))
            radian = degree * (math.pi / 180.0)
            print(f"  cosech({degree}) = {1 / math.sinh(radian)}")

        elif Trigonometry_operation == 'sechx':
            degree = float(input("  Enter the angle in degree :"))
            radian = degree * (math.pi / 180.0)
            print(f"  sech({degree}) = {1 / math.cosh(radian)}")

        elif Trigonometry_operation == 'cothx':
            degree = float(input("  Enter the angle in degree :"))
            radian = degree * (math.pi / 180.0)
            print(f"  coth({degree}) = {1 / math.tanh(radian)}")

        else:
            print("  \nError ! Please check your input ")
            again()

    elif Oper_n == 'logf':
        Numeric_value = int(input("  \n  Enter the number that on you perform logarithmic operation:"))
        Base = int(input("  Enter the base of log that you will taken for perform logarithmic operation:"))
        print(f"  log{Base}({Numeric_value}) = {1 / math.log(Numeric_value, Base)}")

    else:
        print("  \nError ! Please check your input ")
        again()


def Mathmetical_calculator():
    print("\nWelcome to Mathematical calculator : This is developed by Vaishnavi Gangurde")
    operation = input(" Please type in the mathematical operation you would like to complete :\n  + For Addition \n  - For Subtraction \n  * For Multiplication \n  / For Division \n  % For Modulus \n  Please Enter your Choice :")


    num1 = int(input("  Enter the 1st number :"))
    num2 = int(input("  Enter the 2nd number :"))

    if operation == '+':
        print(f"  {num1} + {num2} =", num1 + num2)

    elif operation == '-':
        print(f"  {num1} - {num2} =", num1 - num2)

    elif operation == '*':
        print(f"  {num1} * {num2} =", num1 * num2)

    elif operation == '/':
      print(f"  {num1} / {num2} =", num1 / num2)

    elif operation == '**':
        print(f"  {num1} ** {num2} =", num1 ** num2)

    elif operation == '%':
        print(f"  {num1} % {num2} =", num1 % num2)

    else:
        print("  \nError ! Please check your input ")
        again()

def again():
    cal_again = input("Do you want to calculate again ? \nPlease type y for YES and n for NO :")

    if cal_again == "y":
        print("\nHii, Again !!!")
        Choose_calculator()

    elif cal_again == "n":
        print("See you later !!!")

    else:
        again()

Choose_calculator()

"""
Output:
1)
Please Choose Calculator for performing Various Operations :
  1 For SCIENTIFIC CALCULATOR 
  2 For MATHEMATICAL CALCULATOR 
  Please Enter Your Choice :1

Welcome to Scientific calculator : This is developed by Vaishnavi Gangurde.
Select the input for logarithm function OR Trigonometric function. 
  trf For TRIGONOMETRIC FUNCTION  
  logf For LOGARITHMIC FUNCTION  
  Please Enter Your Choice :trf
 
Please Select Trigonometric Function that you want to perform :
  sinx For SINE FUNCTION 
  cosx For COSINE FUNCTION 
  tanx For TANGENT FUNCTION 
  cosecx For COSEC FUNCTION 
  secx For SEC FUNCTION 
  cotx For COT FUNCTION 
  sinhx For HYPERBOLIC SINE 
  coshx For HYPERBOLIC COSINE 
  tanhx For HYPERBOLIC TANGENT 
  cosechx For HYPERBOLIC COSEC  
  sechx For HYPERBOLIC SEC 
  cothx For HYPERBOLIC COT 
  Please Enter your Choice :sinx
  Enter the angle in degree :30
  sin(30.0) = 0.49999999999999994


2)
Please Choose Calculator for performing Various Operations :
  1 For SCIENTIFIC CALCULATOR 
  2 For MATHEMATICAL CALCULATOR 
  Please Enter Your Choice :1

Welcome to Scientific calculator : This is developed by Vaishnavi Gangurde.
Select the input for logarithm function OR Trigonometric function. 
  trf For TRIGONOMETRIC FUNCTION  
  logf For LOGARITHMIC FUNCTION  
  Please Enter Your Choice :logf
  
  Enter the number that on you perform logarithmic operation:10
  Enter the base of log that you will taken for perform logarithmic operation:2
  log2(10) = 0.30102999566398114
  
3)
Please Choose Calculator for performing Various Operations :
  1 For SCIENTIFIC CALCULATOR 
  2 For MATHEMATICAL CALCULATOR 
  Please Enter Your Choice :2

Welcome to Mathematical calculator : This is developed by Vaishnavi Gangurde
 Please type in the mathematical operation you would like to complete :
  + For Addition 
  - For Subtraction 
  * For Multiplication 
  / For Division 
  % For Modulus 
  Please Enter your Choice :+
  Enter the 1st number :20
  Enter the 2nd number :41
  20 + 41 = 61

4)
  i)
Please Choose Calculator for performing Various Operations :
  1 For SCIENTIFIC CALCULATOR 
  2 For MATHEMATICAL CALCULATOR 
  Please Enter Your Choice :3
  
Error ! Please check your input 
Do you want to calculate again ? 
Please type y for YES and n for NO :
 
  ii)
Please Choose Calculator for performing Various Operations :
  1 For SCIENTIFIC CALCULATOR 
  2 For MATHEMATICAL CALCULATOR 
  Please Enter Your Choice :1

Welcome to Scientific calculator : This is developed by Vaishnavi Gangurde.
Select the input for logarithm function OR Trigonometric function. 
  trf For TRIGONOMETRIC FUNCTION  
  logf For LOGARITHMIC FUNCTION  
  Please Enter Your Choice :trfs
  
Error ! Please check your input 
Do you want to calculate again ? 
Please type y for YES and n for NO :

  iii)
Please Choose Calculator for performing Various Operations :
  1 For SCIENTIFIC CALCULATOR 
  2 For MATHEMATICAL CALCULATOR 
  Please Enter Your Choice :5
  
Error ! Please check your input 
Do you want to calculate again ?
Please type y for YES and n for NO :y

Hii, Again !!!
Please Choose Calculator for performing Various Operations :
  1 For SCIENTIFIC CALCULATOR 
  2 For MATHEMATICAL CALCULATOR 
  Please Enter Your Choice :
  
  iv)
Please Choose Calculator for performing Various Operations :
  1 For SCIENTIFIC CALCULATOR 
  2 For MATHEMATICAL CALCULATOR 
  Please Enter Your Choice :5
  
Error ! Please check your input 
Do you want to calculate again ? 
Please type y for YES and n for NO :n
See you later !!!

"""


