''' Circuitous, LLC -
    An Advanced Circle Analytics Company
'''

from math import pi,radians,sqrt,tan
# Note, version numbers should be strings, not floating point objects.
version = '0.6'
class Circle(object):
    ''' An advanced circle analytics toolkit. '''
    def __init__(self,radius):
        self.radius = radius


# The right way to fix this is to put a dunderscore in front of the perimeter method call.   This will automatically do 
# name mangling.  This is also called a class local reference.  Note that the dunderscore does *not* make the attribute private.

    #Changes name  to self.__<Class>.perimeter 
    # Now tire can call perimeter without any issues because the Tire class is name mangled in front of the method call. 
    def area(self):
        c = self.__perimeter()  
        r = c / pi /2.0       
        return(pi * r ** 2.0) 

    def perimeter(self):
        return(2 * pi * self.radius)

    _perimeter =  perimeter  # Save a copy of perimeter and call that, so that the Tire class can still use their perimeter method. 

    @classmethod
    def frombbd(cls,bbd):
        radius = bbd / 2.0 / sqrt(2.0)
        return(cls(radius))

    @staticmethod
    def angle_to_grade(angle):
        return (tan(radians(angle)) * 100.0)

class Tire(Circle):

    def perimeter(self):
        return Circle.perimeter(self)
    
    _perimeter = perimeter  # If you can do this, so can your subclasses.  Now we're right back where we started. 