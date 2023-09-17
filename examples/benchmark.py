from gettext import npgettext
import numpy as np
import timeit


timeit.Timer("""
x2 = [];
for x in range(10):
x2.append(x**2)
""").timeit()

timeit.Timer("""
x2 = [ x**2 for x in range(10) ]
""").timeit()

timeit.Timer("""
x2 = map(lambda x: x**2, range(10))
""").timeit()

