# *args and **kwargs :

# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)

# function_name_print("Hammid", "Rohan", "Abhishek", "Gaurav", "Kaustubh")

def function_args(normal, *args, **kwargs):
    print(type(args))
    print(normal)
    for items in args:  
        print(items)

    print("\nNow i would like to introduce some of our heroes :")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

normal = "I am a normal arguments and the students are :"
user = ["Hammid", "Rohan", "Abhishek", "Gaurav", "Kaustubh"]
kw = {"Gaurav": "Monitor", "Abhishek": "Fitness Instructor",
      "Kaustubh": "The programmer", "Rohan": "cook"}
function_args(normal, *user, **kw)  # Pass tuple form into the args