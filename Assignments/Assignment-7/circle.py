class Circle :
    def __init__(self,radius):
        self.radius=radius

    def perimeter(self):
        perimtr=2*3.14*self.radius
        return perimtr

    def area(self):
        ar=3.14*self.radius*self.radius
        return ar
c1=Circle(5)

print("Perimeter of the circle is:" , c1.perimeter())
print("Area of the circle is:" , c1.area())
