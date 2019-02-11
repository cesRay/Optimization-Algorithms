from sympy import *
from finite_difference import finite_difference as deriv

def gradient_descent(function, initial, eta, itr):
    xi = initial
    print(xi[0])
    for e in range(0, itr):
        dx = deriv(function, x, xi[0])      #finite differences
        dy = deriv(function, y, xi[1])
        # dx = diff(function, x)            #symbolic differentiation
        # dy = diff(function, y)
        grad = Matrix([dx.subs(x, xi[0]), dy.subs(y, xi[1])]).T # if numerical diff is used subs function is not needed.
        xi += - eta*grad
    return xi


# implementation
x = Symbol('x')
y = Symbol('y')
function = (x-2)**2 + (y-3)**2
initial = Matrix([1,1]).T 
eta = 0.1
itr = 2
print(gradient_descent(function, initial, eta, itr))