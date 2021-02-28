import math
n = math.pi
class Point:
   def __init__(self, x, y):
       self.coordinates = {'x': x, 'y': y}
point_a = Point(3, 5)
point_b = Point(-1, 3)
point_c = Point(2, -2)
class Figure:
    pass
figure = Figure()

#Circle

class Circle(Figure):
    center = point_a.coordinates
    r = (3)
    def perimeter(self):
        cirp = 2 * n * cir.r
        return cirp
    def area(self):
        cira = n * (cir.r ** 2)
        return cira
cir = Circle()

#Triangle

class Triangle(Figure):
    a = point_a.coordinates
    b = point_b.coordinates
    c = point_c.coordinates
    def perimeter_noprint(self):
        trip = trisides.ab + trisides.ac + trisides.bc
        return trip 
    def perimeter(self):
        trip = tri.perimeter_noprint()
        return trip
    def area(self):
        trip = tri.perimeter_noprint()
        p = trip / 2
        tria = (p * (p - trisides.ab) * (p - trisides.ac) * (p - trisides.bc)) ** (1 / 2)
        return tria
tri = Triangle()

#Triangle support class

class TriangleSides(Triangle):
    bc = (((tri.c['x'] - tri.b['x'])**2) + ((tri.c['y'] - tri.b['y'])**2)) ** (1 / 2)
    ab = (((tri.a['x'] - tri.b['x'])**2) + ((tri.a['y'] - tri.b['y'])**2)) ** (1 / 2)
    ac = (((tri.a['x'] - tri.c['x'])**2) + ((tri.a['y'] - tri.c['y'])**2)) ** (1 / 2)
trisides = TriangleSides()

#Square

class Square(Figure):
    a = point_a.coordinates
    b = point_b.coordinates
    side = trisides.ab
    def perimeter(self):
        squp = square.side * 4
        return squp
    def area(self):
        squa = square.side ** 2
        return squa
square = Square()
