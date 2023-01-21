class A:
    def __init__(self):
        self.a = "Guarav"
        self.__b = "Abhishek"

class B(A):
    def __init__(self):
        super().__init__()
        print("Private member of the class" + self.__b)

obj = A()
print(obj.a)
  
