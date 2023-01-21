# super() and Overriding
class A:
    classVar = "I am a variable in class A"
    def __init__(self):
        self.var1 ="I am a inside the class A`s constructor"
        self.classVar1 = "Instance variable in class A"   # firstup all finds instance variable
        self.special = "I am specials"

class B(A):
    classVar2 = "I am a variable in class B"
    def __init__(self):
        # super().__init__()
        self.var1 = "I am a inside the class B`s constructor"
        self.classVar1 = "Instance variable in class B"
        super().__init__()
        print(super().classVar)


a = A()
b = B()

print(b.special, b.var1, b.classVar1)