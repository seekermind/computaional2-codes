"""
Name: Mamunur Rashid
Reg No: 2017132014


Solving Laplace's equation with Gauss-Seidel iteration method.
I set all the data point to zero instead of calculating using five point formula as was discussed in class. Since this becomes very complicated as the grid size is increased. This only cost few more iteration.

"""


import numpy as np
import matplotlib.pyplot as plt

M = 10 #number of squares on each side

# setting initial guess and initial condition
A = np.zeros([M+1, M+1]) 
A[0,:] = 1

for k in range(50):
    for i in range(1,M):
        for j in range(1, M):
            A[i,j] = (1/4)*(A[i+1,j]+A[i-1,j]+A[i,j+1]+A[i,j-1])


plt.imshow(A)
plt.show()
