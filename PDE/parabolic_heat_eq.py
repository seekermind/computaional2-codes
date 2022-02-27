"""
Name: Mamunur Rashid
Reg No: 2017132014

Solving 1D heat equation using Bender-Schmidt formula.

U_i(k+1) = lambda( U_i+1(k) + U_i-1(k) ) + (1 - 2*lambda) U_i(k)

This method takes lambda = 1/2.
Since lambda = alpha^2 dt/dx^2, a particular value of dx fixes the value for dt and vice versa.
"""


import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

nt = 100      # time steps in future.
length = 4      # length of the rod
nx = 20       # number of data points in length.

dx = length/nx
dt = (dx**2)/2

T = np.zeros([nt, nx])      # Temperature mesh.
l = np.linspace(0,length, nx)   # dividing length nx time and making an array.
t = np.arange(0,nt,dt)

func = lambda x: 4*x - x**2     # initial value function

# assigning initial and boundary values.

T[0,:] = func(l)    
T[:,0] = 0
T[:,-1] = 0

# calculating temperature at future times.

for i in range(1,nt):
    for j in range(1,nx-1):
        T[i,j] = 0.5*(T[i-1,j+1]+T[i-1,j-1])

# making plot and animation.

fig, ax = plt.subplots()
ax.set_xlim(0,length)
ax.set_ylim(0,max(T[0]))
line, = ax.plot(l, T[0])

def animation_frame(i):
    label = 't = {:.2f}'.format(t[i])
    line.set_ydata(T[i])
    ax.set_title(label)
    return line, ax

anim = FuncAnimation(fig, animation_frame, repeat=True, frames=len(T), interval=0.125)

plt.show()
