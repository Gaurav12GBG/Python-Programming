# This is a part of tut_42_workingOf_import
from typing import Mapping


a = 7

def printJoke(str):
    print(f"This is a joke {str}") 


# This is a part of tut_43_mainAndNecessity
def printGBG(string):
    return f"This is a string formatting of the recignitions {string}"

def add(num1, num2):
    return num1 + num2

print("and the name is ", __name__)
if __name__ == "__main__":
    print(printGBG("able to and unable to"))
    makeAdd = add(4, 5)
    print(makeAdd)