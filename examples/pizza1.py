#!/usr/bin/env python3
class DoughFactory(object):

    def get_dough(self):
        return 'insecticide treated wheat dough'

class OrganicDoughFactory(DoughFactory):
    def get_dough(self):
        return 'pure untreated wheat dough'


class Pizza(DoughFactory):

    def order_pizza(self,*toppings):
        print ('Getting dough')
        dough=super().get_dough()
        print ('Making pie with %s' % dough)
        for topping in toppings:
            print ('Adding %s' % topping)

class OrganicPizza(Pizza,OrganicDoughFactory):
    pass

if __name__=='__main__':
    Pizza().order_pizza('Pepperoni','Sausage')
    print()
    OrganicPizza().order_pizza('Pepperoni','Sausage')

