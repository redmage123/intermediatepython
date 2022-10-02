# New customer, a rubber sheet  manufacturer. 
# They need a new method, perimeter.  So, now we can define it. 
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

#Note here that the rubber sheet company changes our attribute radius by multiplying it by 1.1.
# This is because rubber stretches when heated. 
# The lesson here is that if you have public attributes, someone will change their value. 
        
cuts = [0.1,0.7,0.8]
circles = [Circle(r) for r in cuts]
for c in circles:
    print('A circlet with radius of ',c.radius)
    print('Has a perimeter of ',c.perimeter())
    print(' and a cold area of',c.area())
    c.radius *= 1.1
    print (' and a warm area of ',c.area())