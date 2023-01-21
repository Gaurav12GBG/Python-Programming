class Employee:
    no_of_leaves = 80
    def __init__(self, aname, asalary, arole) -> None:
        self.name = aname
        self.salary = asalary
        self.role = arole

    def __add__(self, other): # <------------ Dunder Method
        return self.salary + other.salary

    # def __truedev__(self, other):# <------------ Dunder Method
    #     return self.salary / other.salary

emp1 = Employee("Gaurav", 100, "Programmer")
emp2 = Employee("Harry", 100, "Cleaner")
print(emp1 + emp2)
# print(emp1 / emp2)  



