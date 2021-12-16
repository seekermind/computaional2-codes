# Name   : Mamunur Rashid
# Reg    : 2017132014

## Solving decay equation numerically using euler method and taylor method.

# NOTE: Euler method is actually taylor method where we only keep first two terms(up to h) from taylor series. 

import numpy as np
import matplotlib.pyplot as plt

a = 0.0
b = 10.0

h = 0.1

# Initial value, N(0) = N_0 = 100

N0 = 100

# derivatives of the function 

# dN/dt = -N0
# d^2N/dt^2 = N0

# First 10 second is divided into desecrate points with interval h = 0.1s
tPoints = np.arange(a,b,h)

def euler(tPoints, N0):
    
    nPointsEuler= []        # array to store N value by euler method
    
    for t in tPoints:
        nPointsEuler.append(N0)

        # For Euler method, solutions at each t point is found by adding h*N(0) with previous point.
        N0 += h*(-N0)  
    return nPointsEuler


def taylor(tPoints, N0):
    
    nPointsTaylor= []        # array to store N value by euler method
    
    for t in tPoints:
        nPointsTaylor.append(N0)

        # For Euler method, solutions at each t point is found by adding h*N(0) with previous point.
        N0 += h*(-N0) + (h**2/2)*N0
    return nPointsTaylor

def analytic(tPoints, N0):
    
    nPointsAnalytic= []        # array to store N value by euler method
    
    for t in tPoints:
        nPointsAnalytic.append(N0*np.exp(-t))

    return nPointsAnalytic

nPointsEuler = euler(tPoints, N0)
nPointsTaylor= taylor(tPoints, N0)
nPointsAnalytic= analytic(tPoints, N0)

plt.plot(tPoints, nPointsEuler,'g-', label='Euler method')
plt.plot(tPoints, nPointsTaylor,'b-', label='Taylor method')
plt.plot(tPoints, nPointsAnalytic,'r--', label='Analytic solution')
plt.title(r"Solution of decay equation $(\frac{dN}{dt} = -N)$ $(h=0.1)$")
plt.xlabel("Time t")
plt.ylabel("Number of nuclei remained, N(t)")
plt.legend()
plt.show()
