''' Circuitous, LLC - 
    An advanced circle analytics company
'''
#Should we add more functionality here? 
#YAGNI - You ain't gonna need it. 
from math import pi
class Circle:
    ''' An advanced circle analytics toolkit. 
        Note use of class variable version
    '''
    
    version = '0.2'   # This is a string, not a double.  
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2   # Note that we use the math library to ensure a consistent value for PI.