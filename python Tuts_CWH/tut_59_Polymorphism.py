"""
Polymorphism :- Ability to take various forms.

"""
# Method Overridings
class Polymorphism:
    def printPlayer(self):
        print("I am a good basketball player from Polymorphism team")

    def printAnnouncement(self):
        print("Are you ready for playing ?")

class Polycabion(Polymorphism):
    def printPlayer(self):
        print("I am good cricket player from Polycabion team")

    def Imagine(self):
        print("You are winning !!")

plyc = Polycabion()
plyc.printPlayer()
plyc.Imagine()
plyc.printAnnouncement()