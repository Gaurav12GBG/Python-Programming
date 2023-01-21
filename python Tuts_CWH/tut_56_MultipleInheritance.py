# Inheritance

class Employee:
    no_of_leaves = 8
    var = 8

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

class Player:
    no_of_games = 4
    var = 9
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printDetails(self):
        return f"I am {self.name} and i am playing {self.game}."

class CoolProgrammer(Employee, Player):
    var = 10
    pass

# main func
obj1 = Employee("Gaurav", 455, "Instructor")
obj2 = Employee("Vaishnavi", 788, "Project manager")

obj3 = Player("Gaurav", "Cricket")
obj4 = CoolProgrammer("Rohan", 555, "collProgrammer")
detail = obj4.printDetails()
print(detail)
print(obj4.var)
# print(obj3.printDetails())

