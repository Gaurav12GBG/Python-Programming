class Cricket:
    def crickect(self):
        print("I am playing cricket")

    def football(self):
        print("I am playing football")

class Football(Cricket):
    def football(self):
        print("I am playing football in football class")

class Hocky(Cricket):
    def hocky(self):
        print("I am playing hocky in hocky class")

obj_cricket = Cricket()
obj_football = Football()
obj_hocky = Hocky()

obj_cricket.crickect()
obj_cricket.football()

obj_football.crickect()
obj_football.football()

obj_hocky.crickect()
obj_hocky.hocky()

