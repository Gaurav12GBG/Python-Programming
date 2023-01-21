class Employee:
    no_of_leaves = 8
    

obj1 = Employee()
obj2 = Employee()

obj1.name = "Gaurav"
obj1.salary = 30333
obj1.role = "Instructor"

obj2.name = "Vaishnavi"
obj2.salary = 34859
obj2.role = "Project manager"

print(obj1.no_of_leaves, obj2.no_of_leaves)

Employee.no_of_leaves = 12   # Only change using class not using object
print(Employee.no_of_leaves)
print(obj1.no_of_leaves)

print(obj1.__dict__)
print(obj2.__dict__)