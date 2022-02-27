'''
Name:   Mamunur Rashid
Reg No: 2017132014

This Program prints the probability of finding a random dot of a square inside a circle closely fitted inside the square.
A circle of radius 1 is fitted inside a square of side length 2. If you choose a point from the inside of the square randomly, what is the probability of the point also being inside the circle?
'''
import numpy as np

n=50000 #number of sample event
count = 0
for i in range(n):
	
	# choosing a random point from (0,0) to (2,2)
    x = np.random.random()*2 
    y = np.random.random()*2
	
	# since the center of the circle is at (1,1), a point is inside the circle if (x-1)^2 + (y-1)^2 < 1
    if ((x-1)**2 + (y-1)**2) <= 1:
        count += 1
print(count/n) # probality of finding the point inside the circle is (nomber of time points were inside the circle)/(number of time you choose points) 
