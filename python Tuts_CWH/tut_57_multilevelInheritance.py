class Dad:
    basketBall = 1
    pass

class Son(Dad):
    dance = 1
    def isDance(self):
        return f"Yes i am dance {self.dance} no of time"
    

class Grandson(Son):
    dance = 6
    def isDance(self):
        return f"Jackson yeah ! Yes i am dance awesomely {self.dance} no of times"

ob1 = Dad()
ob2 = Son()
ob3 = Grandson()

print(ob3.isDance())
print(ob3.basketBall) # Allowed