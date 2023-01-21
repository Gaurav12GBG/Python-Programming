class Area:
    def area(self, r=None, b=None, h=None):
        if h != None and b!= None:
            return 0.5*b*h
        elif r != None:
            return 3.142*r*r
        elif r != None and h != None:
            return (2*3.142*r*h) + (2*3.142*r*r)
        else:
            return 0

obj = Area()
r = int(input("Enter the radius :"))
b = int(input("Enter the breadth:"))
h = int(input("Enter the height :"))
print(f"Area of triangle => {obj.area(r)} sq.cm ")
print(f"Area of circle => {obj.area(b, h)} sq.cm")
print(f"Area of cylinder => {obj.area(r, h)} sq.cm")

