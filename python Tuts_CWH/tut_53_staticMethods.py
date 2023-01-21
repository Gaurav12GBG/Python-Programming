# Class Methods => static

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

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))

    @staticmethod
    def printGood(string):
        print("This is good " + string)

# main func
obj1 = Employee("Gaurav", 455, "Instructor")
obj2 = Employee("Vaishnavi", 788, "Project manager")
obj3 = Employee.from_dash("Gaurav-455-Instructor")

print(obj3.name, obj3.salary, obj3.role)
obj3.printGood("Gaurav")