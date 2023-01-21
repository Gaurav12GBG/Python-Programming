from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printArea(self):
        None

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 7
        self.breadth = 6

    def printArea(self):
        return self.length * self.breadth

rect = Rectangle()
print(rect.printArea())