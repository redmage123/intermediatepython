#Yahtzee!!!!   We've hit the big time!  Our new customer is a huge government department.  Lots of money, 
# but there's a problem.  We now have to adhere to their ISO standards.  One of them says that we can no longer
# compute the area of the circle from the radius.  We must use the perimeter.  



''' Circuitous, LLC -
    An Advanced Circle Analytics Company
'''

from math import pi,radians,sqrt,tan
# Note, version numbers should be strings, not floating point objects.
version = '0.3'
class Circle(object):
    ''' An advanced circle analytics toolkit. '''
    def __init__(self,radius):
        self.radius = radius

# Our new area method to comply with government regulations.
# All problems have a simple, easy, logical and completely wrong way to be solved.  
# This is one of them. 
# Who is self?  It's not you, it's you or your children!  What does this break? 
# How can we fix this? 

    def area(self):
        c = self.perimeter()  #Complying with the ISO standard. 
        r = c / pi /2.0       # Have to back the radius out of the perimeter. 
        return(pi * r ** 2.0) # then recalculate the radius and return it. 

    def perimeter(self):
        return(2 * pi * self.radius)

    @classmethod
    def frombbd(cls,bbd):
        radius = bbd / 2.0 / sqrt(2.0)
        return(cls(radius))

    @staticmethod
    def angle_to_grade(angle):
        return (tan(radians(angle)) * 100.0)