#!/usr/bin/env python3
class DoughFactory(object):

    def get_dough(self):
        return 'insecticide treated wheat dough'

class Pizza(DoughFactory):

    def order_pizza(self,*toppings):
        print ('Getting dough')
        dough=super().get_dough()
        print ('Making pie with %s' % dough)
        for topping in toppings:
            print ('Adding %s' % topping)

if __name__=='__main__':
    Pizza().order_pizza('Pepperono','Sausage')

