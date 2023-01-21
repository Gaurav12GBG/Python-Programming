"""
Problem Statement : Write a python program that accepts a string from user and perform following string operation
                    1. Calculate length of string
                    2. String Reversal
                    3. Equality check of two string
                    4. Check palindrome
                    5. Check Substring
"""

str = input("Enter the string that you want :")

# Calculate the length of string
print(f"\nThe length of string entered by user = {len(str)}")

# String reversal :
print(f"\nThe reverse of string = {str[::-1]}")

# Check palindrome :
if str == str[::-1]:
    print("\nThe string is palindrome !!")
else:
    print("\nThe string is not palindrome !!")

# Equality check of two string

print("\nPlease Check Equality of String ==> ")
str1 = input("Enter the new string yo check equality with above string i.e.str :")
if str == str1:
    print("Both the strings are equal")
else:
    print("Both the string are not equal")

# check substring :

print("\nPlease Check Substring ==>")
sub1 = input("Enter the string to check whether the string is substring of above string or not : ")
if sub1 in str:
    print(f'(sub1==> "{sub1}") is substring of (str==> "{str}")')
else:
    print(f'(sub1==> "{sub1}") is not substring of (str==> "{str}")')


"""
Output : Enter the string that you want :Vaishnavi Gangurde

         The length of string entered by user = 18
         
         The reverse of string = edrugnaG ivanhsiaV
         
         The string is not palindrome !!

         Please Check Equality of String ==> 
         Enter the new string yo check equality with above string i.e.str :Lalita Gangurde
         Both the string are not equal

         Please Check Substring ==>
         Enter the string to check whether the string is substring of above string or not : Vaishnavi
         (sub1==> "Vaishnavi") is substring of (str==> "Vaishnavi Gangurde")
"""


