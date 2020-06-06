xi = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
yi = []
from math import *
def func(x):
    return ((e)**x)*log(x,e) - x**2
for i in range(len(xi)):
    yi = yi + [func(xi[i]),]