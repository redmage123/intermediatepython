''' The University has called with a complaint.  They'e received their grant and now are trying to 
    scale up their circle analysis by making ten million circles.  This is causing serious
    problems on their server as they're running out of memory.   It turns out that each Circle
    consumes several hundred bytes each even though they only store the radius.  What's up with that? 
 '''
from math import pi,radians,sqrt,tan
from random import random, seed
''' Circuitous, LLC -
    An Advanced Circle Analytics Company
'''
class Circle(object):
    ''' An advanced circle analytics toolkit. '''
    version = '0.7'
     
     # This is an example of the flyweight design pattern. 
     # Note that the __slots__ attribute is not inherited.  So if a subclass of circle 
     # wants to add its own attributes it is free to do so. 
    __slots__ = ['diameter']  #Don't use the dictionary to store attributes, instead use the slots list. 
    def __init__(self,radius):
        self.radius = radius

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

    @property
    def radius(self):
        return self.diameter / 2
    
    @radius.setter
    def radius(self):
        self.diameter = self.radius * 2
n = 10000000
seed (8675309)

circles = [Circle(random() for i in range(n))]
print ('The average area of ',n,' circles is: ')
avg = sum([c.area() for c in circles])
print (" %.1f " % (avg))
