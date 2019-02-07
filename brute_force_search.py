import numpy as np
from sympy import *

#Functions
def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

def brute_force_search2d(f, xu, xl):
    x = Symbol('x')
    fbest = 99999999
    xbest = 0
    fval = 0

    for e in frange(xl, xu, 1):
        fval = f.subs(x, e)
        if fval < fbest:
            fbest = fval
            xbest = e
    res = [xbest, fbest]
    return res

def brute_force_search3d(f, xu, xl, yu, yl):
    x = Symbol('x')
    y = Symbol('y')
    fbest = 99999999
    xbest = 0
    ybest = 0
    fval = 0

    for e in frange(xl, xu, 1):
        for d in frange(yl, yu, 1):
            fval = f.subs([(x, e), (y, d)])
            if fval < fbest:
                fbest = fval
                xbest = e
                ybest = d
    res = [xbest, ybest, fbest]
    return res



