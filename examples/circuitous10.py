''' Circuitous, LLC - 
    An advanced circle analytics company
'''
from math import pi,sqrt,tan, radians
from types import ClassMethodDescriptorType 
class Circle:
    ''' An advanced circle analytics toolkit. 
        Note use of class variable version
    '''
    
    version = '0.4'    
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2   # Note that we use the math library to ensure a consistent value for PI.
    
    def perimeter(self):
        return 2 * pi * self.radius 

    @classmethod
    def frombbd(cls, bbd):
        radius = bbd / 2.0 / sqrt(2.0)
        return cls(radius)  

        
''' One of our customers wants an angle to grade function. This is just a helper function, and really
    doesn't have anything to do with circles, per se. 
'''

# Is putting the angle to grade method outside of the class scope wise? 

def angle_to_grade(angle):
    return tan(radians(angle)) * 100