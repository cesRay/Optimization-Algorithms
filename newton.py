# Metodo Newton 
from sympy import *

# Function
def newton(f, x0, it):
    x = Symbol('x')
    dif1 = diff(f, x)
    dif2 = diff(dif1, x)
    xi = x0
    for e in range(0, it):
        xi = float(xi - dif1.subs(x, xi)/dif2.subs(x, xi))
    res = dif2.subs(x, xi)
    if res > 0:
        itIs = 'it is a minimum: '
    else:
        itIs = 'it is a maximum: '
    xi = float(xi)
    answ = [itIs, xi]
    return answ
