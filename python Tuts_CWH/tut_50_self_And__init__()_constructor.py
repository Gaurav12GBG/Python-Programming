# __init__() Constructor ==>

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole): # constructor creation
        self.name = aname
        self.salary = asalary
        self.role = arole
        
    
    def printDetails(self):
        return f"My name is {self.name}. My salary is {self.salary} and my role is {self.role}."

obj1 = Employee("Gaurav", 455, "Instructor")
obj2 = Employee("Vaishnavi", 788, "Project manager")

# obj1.name = "Gaurav"
# obj1.salary = 30333
# obj1.role = "Instructor"

# obj2.name = "Vaishnavi"
# obj2.salary = 34859
# obj2.role = "Project manager"

print(obj1.printDetails())