#!/usr/bin/env python3

class foo(object):

    def __init__(self,a):
        self.a = a

    def bar(self):
        return self.__bar()

    def __bar(self):
        self.b = self.a ** 2
        return self.b


class meh(foo):

    def __init__(self,a):
        super().__init__(a)

    def bar(self):
        return super().bar() + 10



f = foo(2)
m = meh(2)
print (f.bar())
print (m.bar())

