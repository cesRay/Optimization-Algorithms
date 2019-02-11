from sympy import *

def finite_difference(function, x, x0):
    d = 0.001
    function1 = function.subs(x, x0 - d/2)
    function2 = function.subs(x, x0 + d/2)
    deriv = (function2 - function1)/d
    return deriv

# implementation
x = Symbol('x')
x0 = 1
function = x**2 + 1
print(finite_difference(function, x, x0))