''' Circuitous, LLC - 
    An advanced circle analytics company
'''
from math import pi
class Circle:
    ''' An advanced circle analytics toolkit. 
        Note use of class variable version
    '''
    
    version = '0.3'    
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2   # Note that we use the math library to ensure a consistent value for PI.
    
    def perimeter(self):
        return 2 * pi * self.radius 


# Here we see that our latest customer, a national tire manufacturer subclasses our Circle class and 
# overrides the perimeter method. 
# The lesson here is that when you create your class, you need to think about how the customer might
# subclass it.    


class Tire(Circle):
    ''' Tires are circles with a corrected perimeter '''

    def perimeter(self):
        ''' Perimeter corrected for the rubber '''
        return Circle.perimeter(self) * 1.25

t = Tire(22)
print ('A tire of radius ', t.radius)
print (' has an inner area of ',t.area())
print (' and an odometer corrected perimeter of ',t.perimeter())