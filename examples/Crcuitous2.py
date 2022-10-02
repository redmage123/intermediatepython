''' Circuitous, LLC - 
    An advanced circle analytics company
'''

class Circle:
    ''' An advanced circle analytics toolkit. 
        Note use of class variable version
    '''
    
    version = '0.1'   # This is a string, not a double.  
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.1415927 * self.radius * 2   #Note that PI is hard coded.  This is not optimal.  
    

        
