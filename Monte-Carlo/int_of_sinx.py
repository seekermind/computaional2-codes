'''
Name:   Mamunur Rashid
Reg No: 2017132014
'''
import numpy as np

n=50000 #number of sample event
count = 0
for i in range(n):
	# choosing a random point from (0,0) to (pi,1)
    x = np.random.random()*np.pi    #   x position from 0 to pi
    y = np.random.random()          #   y position from 0 to 1
    if y < np.sin(x):
        count += 1
print(np.pi*count/n)    # since (area under sinx)/(area of a rectangle with side 1 and pi) = (no of point found under the sinx)/(total point considered)
