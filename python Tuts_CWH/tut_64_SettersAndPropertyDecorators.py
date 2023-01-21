class Employee:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        print("setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

emp = Employee("gaurav", "gangurde")
print(emp.explain())
print(emp.email)

emp.fname = "vaishnavi"  # this property is accepted by using property decorators
print(emp.email)

emp.email = "this.that@gmail.com"
print(emp.fname)

del emp.email
print(emp.email)