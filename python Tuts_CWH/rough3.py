
# # Empty list
# Dict = {}
#
# print("\nWELCOME IN 12TH ANNUAL MARKS PERCENTAGE WITH GRADE !!!")
#
# # It take name of student as a input
# Student_name = input("\nPlease Enter Your Name :")
#
# # Input For Choosing how many number user wants
# How_many_numbers = int(input("Enter how many subjects marks you want to insert in a dictionary :"))
#
# # List of 12th subjects
# print("\n12 th Subjects List :\n 1. Marathi \n 2. English \n 3. Physics \n 4. Chemistry \n 5. Biology \n 6. Mathematics")
#
# # Appending in a dictionary using for loop and append function
# for i in range(0, How_many_numbers):
#      subject = input("\nEnter the subject name present in above 12th subjects list :")
#      Marks = int(input("Enter the marks of subject:"))
#      Dict.update({subject:Marks})
#
# print(f"\n{Student_name} Your Results Record Present Following with Percentage !!!")
# print(Dict)
#
# Total = 0
# for i in Dict:
#     Total = Total + Dict[i]
#
# Percentage =  Total/6
#
# if Percentage > 75:
#     print(f"Congratulation {Student_name} , You got {Percentage} So Your in Distinction !!!")
# elif Percentage >= 60 and Percentage < 75:
#     print(f"Congratulation {Student_name} , You got {Percentage} So Your in First Division !!!")
# elif Percentage >= 50 and Percentage < 60:
#     print(f"Congratulation {Student_name} , You got {Percentage} So Your in Second Division !!!")
# elif Percentage >= 40 and Percentage < 50:
#     print(f"Congratulation {Student_name} , You got {Percentage} So Your in Third Division !!!")
# elif Percentage >= 35 and Percentage < 40:
#     print(f"Congratulation {Student_name} , You got {Percentage} But Your not only in Distinction but also in (1st, 2nd, 3rd)Division:")
# else:
#     print(f"SORRY {Student_name} , You got {Percentage} So Your are Fail ... :")
#
#
# """
# Output :
#
# WELCOME IN 12TH ANNUAL MARKS PERCENTAGE WITH GRADE !!!
#
# Please Enter Your Name :Vaishnavi
# Enter how many subjects marks you want to insert in a dictionary :6
#
# 12 th Subjects List :
#  1. Marathi
#  2. English
#  3. Physics
#  4. Chemistry
#  5. Biology
#  6. Mathematics
#
# Enter the subject name present in above 12th subjects list :Marathi
# Enter the marks of subject:85
#
# Enter the subject name present in above 12th subjects list :Engish
# Enter the marks of subject:63
#
# Enter the subject name present in above 12th subjects list :Physics
# Enter the marks of subject:75
#
# Enter the subject name present in above 12th subjects list :Chemistry
# Enter the marks of subject:73
#
# Enter the subject name present in above 12th subjects list :Biology
# Enter the marks of subject:85
#
# Enter the subject name present in above 12th subjects list :Mathematics
# Enter the marks of subject:92
#
# Vaishnavi Your Results Record Present Following with Percentage !!!
# {'Marathi': 85, 'Engish': 63, 'Physics': 75, 'Chemistry': 73, 'Biology': 85, 'Mathematics': 92}
# Congratulation Vaishnavi , You got 78.83333333333333 So Your in Distinction !!!
# """

print("\nWELCOME IN 12TH ANNUAL MARKS PERCENTAGE WITH GRADE !!!")

# It take name of student as a input
Student_name = input("\nPlease Enter Your Name :")

Marathi = int(input("Please Enter your marathi Marks :"))
English = int(input("Please Enter your English Marks :"))
Physics = int(input("Please Enter your physics Marks :"))
Chemistry = int(input("Please Enter your chemistry Marks :"))
Biology = int(input("Please Enter your biology Marks :"))
Mathematics = int(input("Please Enter your mathematics Marks :"))

Percentage = (Marathi + English + Physics + Chemistry + Biology + Mathematics)/6

if Percentage > 75:
    print(f"Congratulation {Student_name} , You got {Percentage} So Your in Distinction !!!")
elif Percentage >= 60 and Percentage < 75:
    print(f"Congratulation {Student_name} , You got {Percentage} So Your in First Division !!!")
elif Percentage >= 50 and Percentage < 60:
    print(f"Congratulation {Student_name} , You got {Percentage} So Your in Second Division !!!")
elif Percentage >= 40 and Percentage < 50:
    print(f"Congratulation {Student_name} , You got {Percentage} So Your in Third Division !!!")
elif Percentage >= 35 and Percentage < 40:
    print(f"Congratulation {Student_name} , You got {Percentage} But Your not only in Distinction but also in (1st, 2nd, 3rd)Division:")
else:
    print(f"SORRY {Student_name} , You got {Percentage} So Your are Fail ... :")

"""
Output :

WELCOME IN 12TH ANNUAL MARKS PERCENTAGE WITH GRADE !!!

Please Enter Your Name :Vaishnavi
Please Enter your marathi Marks :85
Please Enter your English Marks :63
Please Enter your physics Marks :75
Please Enter your chemistry Marks :72
Please Enter your biology Marks :85
Please Enter your mathematics Marks :92
Congratulation Vaishnavi , You got 78.66666666666667 So Your in Distinction !!!
"""