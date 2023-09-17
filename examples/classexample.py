class Person:

#  Init is *"not* a constructor!!!!!!!"
#  self, can point to the 'you', or to your children. 
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    
p = Person('Braun Brelin', 21)

print (p)
    