''' Circuitous, LLC - 
    An advanced circle analytics company
'''
from math import pi
class Circle:
    ''' An advanced circle analytics toolkit. 
        Note use of class variable version
    '''
    
    version = '0.2'    
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2   # Note that we use the math library to ensure a consistent value for PI.

# Customer is a university. 
# Note that the customer is creating ten circles, but might easily create a thousand, or a million
# of them.  You  may need to consider memory optimizations at some future point in the development cycle.

from random import random,seed
seed(8675309)
n = 10
circles = [Circle(random()) for  _ in range(n)]
print ('The average area of ',n, ' random circles ')
avg =  sum((c.area() for c in circles))
print ('{:.1f}'.format(avg))

