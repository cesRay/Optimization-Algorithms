import numpy as np
from sympy import *

# Functions
def random_search2d(f, xu, xl, it):
    x = Symbol('x')
    x0 = 0
    fbest = 99999999
    xbest = 0
    fval = 0
    for e in range(0, it):
        r = np.random.randint(0,100)/100
        x0 = xl + (xu - xl)*r
        fval = f.subs(x, x0)
        if fval < fbest:
            fbest = fval
            xbest = x0
    res = np.array([xbest, fbest])
    return res


def random_search3d(f, xu, xl, yu, yl, it):
    x = Symbol('x')
    y = Symbol('y')
    x0 = 0
    y0 = 0
    fbest = 99999999
    xbest = 0
    ybest = 0
    fval = 0
    for e in range(0, it):
        r1 = np.random.randint(0,100)/100 
        r2 = np.random.randint(0,100)/100 
        x0 = xl + (xu - xl)*r1
        y0 = yl + (yu - yl)*r2
        fval = f.subs([(x, x0), (y, y0)])
        if fval < fbest:
            fbest = fval
            xbest = x0
            ybest = y0
    res = np.array([xbest, ybest, fbest])
    return res
