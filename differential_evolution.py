import numpy as np 
#import Objective functions


def Differential_Evolution( function, D, F, Cr, N, xl, xu, iterations ):
    # Random population
    X = np.zeros((D, N))
    for i in range(N):
        for j in range(D):
            X[j, i] = xl[j] + (xu[j] - xl[j])*np.random.rand()

    
    # Define empty vector (U)

    U = np.zeros((D, 1))

    n = 0
    
    # Until the last gen

    while( n < iterations ):
        for i in range(N):

            # generate indexes r1, r2 and r3 different from each other

            r1 = i
            while r1 == i:
                r1 = np.random.randint(0,N)
            r2 = r1
            while r2 == i or r2 == r1:
                r2 = np.random.randint(0,N)
            r3 = r2
            while r3 == i or r3 == r2 or r3 == r1:
                r3 = np.random.randint(0,N)

            # Generate a random mutated solution

            V = X[:, r1] + F*(X[:, r2] -X[:, r3])

            # Choose wether the particle will come from the mutated vector or from the original population

            for j in range(D):
                if np.random.uniform(0,1) <= Cr:
                    U[j] = V[j] 
                else:
                    U[j] = X[j, i]

            # Compare the i-th particle with its mutation and adding the best of both to the population

            if function(U) < function(X[:,i]):
                    X[:,i] = U.reshape((D,))
            
        n += 1
    print(X)

# Get the best particle

    best = function(np.array(X[:, 0]))
    bindex = 0
    for i in range(N):
            feval = function(X[:, i])
            if feval < best:
                best = feval
                bindex = i


    answer = [X[:,bindex], best]
    return answer
                
# Implementation
print(Differential_Evolution(Obfun, 3, 1.2, 0.7, 50, np.array([-3, -3, -3]), np.array([3, 3, 3]), 1500))
