"""
Name: Mamunur Rashid
Reg No: 2017132014


"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

alpha = 0.8

length = 1
x_points = 20

time = 1
time_points = 50

X = np.linspace(0,length,x_points)
t = np.linspace(0,time,time_points)

A = np.zeros([time_points,x_points])
A[:, 0] = 0
A[:, -1] = 0
A[0, :] = np.sin(np.pi*X)

for j in range(1,x_points-1):
    A[1,j] = ((alpha**2)/2)*(A[0,j+1]+A[0,j-1]) + (1-alpha**2)*A[0,j]

for i in range(2,time_points):
    for j in range(1,x_points-1):
        A[i,j] = (alpha**2)*(A[i-1,j+1]+A[i-1,j-1]) + 2*(1-alpha**2)*A[i-1,j] - A[i-2,j]

fig, ax = plt.subplots()
ax.set_xlim(0,1)
ax.set_ylim(-1,1)
line, = ax.plot(X,A[0,:])

def animation_frame(i):
    line.set_ydata(A[i,:])
    label = "t= {:.2f}".format(t[i])
    ax.set_title(label)
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    return line, ax

anim = FuncAnimation(fig, animation_frame, repeat=True, frames=len(A), interval=100)
plt.show()
