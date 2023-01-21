class Student:
    pass

# Both obj are different  
obj1 = Student()
obj2 = Student()

obj1.name = "Gaurav"
obj1.std = 12
obj1.section = 1

print(obj1.name, obj1.std, obj1.section)