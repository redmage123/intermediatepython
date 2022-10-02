''' Circuitous, LLC - 
    An advanced circle analytics company
'''
from math import pi,sqrt # Added sqrt import for bbd_to_radius function. sq
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

        
# Next customer is a national graphics company.  Note that they have many shape vendors, not just your company.
# I.e. they have spheres, rectangles, triangles, etc. 
# They'd really like to be able to create a circle without having to convert it from a radius to 
# a bounding box diagonal. 

# They don't really want to do this...

#Customer supplies the bbd function. 
def bbd_to_radius(bbd):
    radius = bbd /2.0 / sqrt(2.0) 
    
bbd = 25.1
c = Circle(bbd_to_radius(bbd)) #This is awkward. Why does the customer have to exert effort to create a circle with a bbd?
print ('A circle with a bbd of 25.1 ')
print (' has a radius of ', c.radius)
print (' and an area of ',c.area())