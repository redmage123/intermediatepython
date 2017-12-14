class Circle(object):
    def __init__(self, radius):
        self.radius

        # This will call self.perimeter() which in the case of Tire is = radius 
        # Tire.perimeter(), not Circle.perimeter.

    def area(self): 
        p = self.perimeter() 
        r = p / math.pi / 2.0
        return math.pi * r ** 2.0 

    __perimeter = perimeter
