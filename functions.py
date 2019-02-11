import math as math 
#Functions to test opt algorithms 

# Sphere function
def function1( listnum ):
    res = 0
    for xi in listnum:
        res += xi**2
    return res

# Rotated hyper-ellipsoid function
def function2( listnum ):
    outer = 0
    n = len(listnum)
    i = 0
    while i < n:
        inner = 0
        j = 0
        while j <= i:
            xj = listnum[j]
            inner += xj**2
            j += 1
        outer += inner
        i += 1
    return outer

# Trid function
def function3( listnum ):
    sum1 = 0
    sum2 = 0
    n = len(listnum)
    for i in range(0, n):
        xi = listnum[i]
        sum1 += (xi -1)**2
    for i in range(1, n):
        xi = listnum[i]
        xi_1 = listnum[i - 1]
        sum2 += xi*xi_1
    res = sum1 - sum2
    return res

# Zakharov function
def function4( listnum ):
    sum1 = 0
    sum2 = 0
    i = 1
    for xi in listnum:
        sum1 += xi**2
        sum2 += 0.5*i*xi
        i += 1
    res = sum1 + sum2**2 + sum2**4
    return res

# Dixon-Price function
def function5( listnum ):
    x1 = listnum[0]
    n = len(listnum)
    term1 = (x1 -1)**2
    sum1 = 0
    j = 2
    for i in range(1, n):
        xnew = listnum[i]
        xold = listnum[i-1]
        sum1 += j*(2*xnew**2 - xold)**2
        j += 2
    res = term1 + sum1
    return res

# Rosenbrock function
def function6( listnum ):
    res = 0
    n = len(listnum)
    for i in range(0, n - 1):
        xnew = listnum[i + 1]
        xold = listnum[i]
        res += 100*(xnew - xold**2)**2 + (xold - 1)**2
    return res

# Michalewicz function
def function7( listnum, m ):
    res = 0
    i = 1
    for xi in listnum:
        res += math.sin(xi)*math.sin((i*xi**2)/math.pi)**(2*m)
        i += 1
    res = -res
    return res

# Styblinski-Tang function
def function8( listnum ):
    res = 0
    for xi in listnum:
        res += xi**4 - 16*xi**2 + 5*xi
    res = 0.5*res
    return res

# Ackley function
def function9( listnum ):
    sum1 = 0
    sum2 = 0
    n = len(listnum)
    for xi in listnum:
        sum1 += xi**2
        sum2 += math.cos(2*math.pi*xi)
    res = -20*math.exp(-0.2*math.sqrt((1/n)*sum1)) - math.exp((1/n)*math.sqrt(sum2)) + 20 + math.exp(1)
    return res

# Rastrigin function
def function10( listnum ):
    res = 0
    n = len(listnum)
    for xi in listnum:
        res += (xi**2 - 10*math.cos(2*math.pi*xi))
    res += 10*n
    return res

# Schwefel function
def function11( listnum ):
    res = 0
    n = len(listnum)
    for xi in listnum:
        res += xi*math.sin(math.sqrt(math.fabs(xi)))
    res = 418.9829*n - res
    return res

# Griewank function
def function12( listnum ):
    i = 1
    _sum_ = 0
    _mult_ = 1
    for xi in listnum:
        _sum_ += (xi**2)/4000
        _mult_ *= math.cos(xi/math.sqrt(i))
        i += 1
    res = _sum_ - _mult_ + 1
    return res

# Levy function
def function13( listnum ):
    n = len(listnum)
    w = [None]*len(listnum)
    for i in range(0, n):
        xi = listnum[i]
        w[i] = 1 + (xi - 1)/4
    term1 = math.sin(math.pi*w[1])**2
    term3 = ((w[n-1] -1)**2)*(1 + math.sin(2*math.pi*w[n-1])**2)
    sum1 = 0
    for i in range(0, n-1):
        wi = w[i]
        sum1 += ((wi - 1)**2) * (1 + 10*(math.sin(math.pi*wi + 1))**2)
    res = term1 + sum1 + term3
    return res

