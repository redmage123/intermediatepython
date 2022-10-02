''' Circuitous, LLC -
    An Advanced Circle Analytics Company
'''

from math import pi,radians,sqrt,tan
# Note, version numbers should be strings, not floating point objects.
version = '0.5'
class Circle(object):
    ''' An advanced circle analytics toolkit. '''
    def __init__(self,radius):
        self.radius = radius

# Our new area method to comply with government regulations.
# All problems have a simple, easy, logical and completely wrong way to be solved.  
# This is one of them. 
# Who is self?  It's not you, it's you or your children!  What does this break? 
# How can we fix this? 

# What if we make a copy of the perimeter method and call that instead?  Will that fix the problem? 

    def area(self):
        c = self._perimeter()  #Complying with the ISO standard. 
        r = c / pi /2.0       # Have to back the radius out of the perimeter. 
        return(pi * r ** 2.0) # then recalculate the radius and return it. 

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
        return Circle.perimeter(self) * 1.25
    
    _perimeter = perimeter  # If you can do this, so can your subclasses.  Now we're right back where we started. 
            