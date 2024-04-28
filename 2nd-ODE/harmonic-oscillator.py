# Name   : Mamunur Rashid
# Reg    : 2017132014
# github : https://github.com/seekermind/computaional2-codes


import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# time bounderies
a = 0.0
b = 100.0

# initial values and constants
h = 0.15    # interval
X0 = 1.0
V0 = 0.0
w = 1.0

# function of the equation dv/dt = Fv(t,x,v) = -w^2 x
def Fv(t,x,v,w):
    return -x*w**2
# function of the equation dx/dt = Fx(t,x,v) = v
def Fx(t,x,v,w):
    return v

# discrete time points
tPoints = np.arange(a, b, h)

# array initialized to store discrete values of x(t), v(t) 
xPointsRK2 = []
vPointsRK2 = []
for t in tPoints:
    xPointsRK2.append(X0)
    vPointsRK2.append(V0)
    
    kx1 = h*Fx(t, X0, V0, w)
    kv1 = h*Fv(t, X0, V0, w)

    kv2 = h*Fv(t+h/2, X0+kx1/2, V0+kv1/2, w)
    kx2 = h*Fx(t+h/2, X0+kx1/2, V0+kv1/2, w)

    # x(t+h) = x(t) + kx2
    # v(t+h) = v(t) + kv2
    X0 += kx2
    V0 += kv2


# array initialized to store discrete values of x(t), v(t) using RK4
xPointsRK4 = []
vPointsRK4 = []

# X0,V0 is changed due to previous calculations, so they need re-initialization
X0 = 1
V0 = 0

for t in tPoints:
    xPointsRK4.append(X0)
    vPointsRK4.append(V0)

    kx1 = h*Fx(t, X0, V0, w)
    kv1 = h*Fv(t, X0, V0, w)

    kx2 = h*Fx(t+h/2, X0+kx1/2, V0+kv1/2, w)
    kv2 = h*Fv(t+h/2, X0+kx1/2, V0+kv1/2, w)

    kx3 = h*Fx(t+h/2, X0+kx2/2, V0+kv2/2, w)
    kv3 = h*Fv(t+h/2, X0+kx2/2, V0+kv2/2, w)

    kx4 = h*Fx(t+h, X0+kx3, V0+kv3, w)
    kv4 = h*Fv(t+h, X0+kx3, V0+kv3, w)

    X0 += (1/6)*(kx1+2*kx2+2*kx3+kx4)
    V0 += (1/6)*(kv1+2*kv2+2*kv3+kv4)

# This table is made to print out the tabular data points as the assignment requires. 
# table =[("time", "x(t) RK2", "x(t) RK4", "v(t) RK2", "v(t) RK4")] + [(round(a,2), round(b, 4), round(c, 4), round(d, 4), round(e, 4)) for a,b,c,d,e in zip(tPoints, xPointsRK2, xPointsRK4, vPointsRK2, vPointsRK4)]

# print(tabulate(table , tablefmt="grid"))

# Printing x(t), v(t) curves.
plt.subplot(211)
plt.plot(tPoints, xPointsRK2, label="x rk2")
plt.plot(tPoints, xPointsRK4, label="x rk4")
plt.title("Position of SHO by RK2 and RK4")
plt.legend()
plt.subplot(212)
plt.plot(tPoints, vPointsRK2, label="v rk2")
plt.plot(tPoints, vPointsRK4, label="v rk4")
plt.title("Velocity of SHO by RK2 and RK4")
plt.legend()
plt.show()
