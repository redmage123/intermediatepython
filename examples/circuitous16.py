''' Circuitous, LLC -
    An Advanced Circle Analytics Company
'''

# So far so good!  We've fixed all our problems so far, but our government customer has called
# and said that we need a minor change to comply with another ISO standard.   We can no longer 
# store the radius.  Instead the ISO standard  specifies that you must, instead, store the 
# diameter.   And, you cannot store both the diameter and the radius.   Note that our APU
# won't change.  We can still accept the radius in the initializer parameter signature, 
# but we just can't store it. 

# What does this break?  Just about everything.  If we had known this ahead of time, might be have done
# what a C++ or Java programmer would have done and create getter and setter methods for the attributes?
# We can do it in Python, but this is not really the 'Pythonic' way to do it.  Instead, we use properties. 


from math import pi,radians,sqrt,tan
# Note, version numbers should be strings, not floating point objects.
version = '0.6'
class Circle(object):
    ''' An advanced circle analytics toolkit. '''
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