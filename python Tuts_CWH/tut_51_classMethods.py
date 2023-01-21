# Class Methods =>

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole): # constructor creation
        self.name = aname
        self.salary = asalary
        self.role = arole

    @classmethod  # We can use it as a alternative constructor
    def changeLeaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves
        
    def printDetails(self):
        return f"My name is {self.name}. My salary is {self.salary} and my role is {self.role}."

obj1 = Employee("Gaurav", 455, "Instructor")
obj2 = Employee("Vaishnavi", 788, "Project manager")

print(obj1.printDetails())
obj1.changeLeaves(52)
print(obj1.no_of_leaves)