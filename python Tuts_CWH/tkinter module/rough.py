"""
Problem Statement : To calculate salary pf an employee given his basic pay (Take input from the User). Calculate
                    Gross Salary of employee. Let HRA be 10 % of basic pay & TA be 5 % of basic pay. Let employee
                    pay Professional Tax as 2 % of total salary. Calculate Net Salary payable after deduction.
"""
# Program Solution :
# Input From the User (Name, Salary) :
Employee_name = input("Enter the employee name :\n")
Employee_basic_salary = float(input("Enter the employee basic salary pay :\n"))

# Here we are calculates the HRA And TA WIth Basic Pay :
HRA = Employee_basic_salary * 0.1
TA = Employee_basic_salary * 0.05

# Now here is the calculation of Gross Salary and PT :
Employee_Gross_salary = Employee_basic_salary + HRA + TA
Professional_Tax = Employee_Gross_salary * 0.02

# At last total Net Salary Obtained :
Employee_Net_salary = Employee_Gross_salary - Professional_Tax

# Displaying Output :
print("About Employee Salaries :\n")

print("Employee_name :", Employee_name)
print("Employee_basic_salary :", Employee_basic_salary)
print("Employee_Gross_salary :", Employee_Gross_salary)
print("Employee_Net_salary :", Employee_Net_salary)

"""
Output : Enter the employee name :
         Vaishnavi
         Enter the employee basic salary pay :
         25000.845
         About Employee Salaries :

         Employee_name : Vaishnavi
         Employee_basic_salary : 25000.845
         Employee_Gross_salary : 28750.97175
         Employee_Net_salary : 28175.952315000002
"""