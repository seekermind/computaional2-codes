# Name   : Mamunur Rashid
# Reg    : 2017132014
# github : 

##  Growth equation, soving numarically by Euler method.


# NOTE: Euler method is actually taylor method where we only keep first two terms(up to h) from taylor series. 
# So this this is basically a copy of taylor method with change in only one line (line 40)

import numpy as np
import matplotlib.pyplot as plt

a = 0.0
b = 10.0

h = 0.01

# Initial value, N(0) = N_0 = 100

N0 = 100

# derivatives of the function 

# dN/dt = N0
# d^2N/dt^2 = N0

# First 10 second is divided into desecrate points with interval h = 0.01s
tPoints = np.arange(a,b,h)

# Two arrays are initialized to store values of N(t) at t points. One for numerical solution another for analytic solution N(t) = N_0 e^(t)
nPoints = []
solution = [] # for analytic solution

for t in tPoints:
    nPoints.append(N0)

    # Solutions at each t point is found by adding h*N(0) with previous point.

    N0 += h*(N0) 
    solution.append(100*np.exp(t))

plt.plot(tPoints, nPoints,'b-', label='Euler method')
plt.plot(tPoints, solution, '--r', label='Analytic Solution')
plt.title(r"Solution of growth equation $(\frac{dN}{dt} = N)$ by Euler method $(h=0.01)$")
plt.xlabel("Time t")
plt.ylabel("Number of nuclei remained, N(t)")
plt.legend()
plt.show()
