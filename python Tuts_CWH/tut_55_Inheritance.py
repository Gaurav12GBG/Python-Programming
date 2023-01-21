# Inheritance

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
        return f"In Employee = My name is {self.name}. My salary is {self.salary} and my role is {self.role}."

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))

    @staticmethod
    def printGood(string):
        print("This is good " + string)

class programmer(Employee): # using inheritance
    def __init__(self, aname, asalary, arole, alanguage):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language = alanguage
        
    def printProg(self):
        return f"In Programmers = My name is {self.name}. My salary is {self.salary} and my role is {self.role}. The languages are {self.language}."


# main func
obj1 = Employee("Gaurav", 455, "Instructor")
obj2 = Employee("Vaishnavi", 788, "Project manager")

obj3 = programmer("Abhishek", 788, 9, ["python", "c++"])
obj4 = programmer("Ram", 988, 78, ['c', 'ccc'])

print(obj3.printProg())
print(obj3.printDetails()) #access the properties of super class
obj4.printGood("gaurav")