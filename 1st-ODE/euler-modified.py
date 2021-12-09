import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x**2 + y

a = 0.0
b = 10.0

h = 0.1
y0 = 1

def eulerModified(f, h, y0, a,b, order):

    xPoints = np.arange(a, b, h)
    yPoints = []

    for x in xPoints:
        y = y0 + h*f(x,y0)
        for i in range(order-1):
            y = y0 + (h/2)*(f(x, y0)+f(x+h, y))

        yPoints.append(y)
        y0 = y
    return xPoints, yPoints

xPoints, yPoints = eulerModified(f,h,y0,a,b,3)

ySolution = [3*np.exp(x) - x**2 - 2*x -2 for x in xPoints]

plt.plot(xPoints, yPoints, label='approx')
plt.plot(xPoints, ySolution, label='solution')
plt.title(r'$\frac{dy}{dx}= x^2+y$')
plt.legend()
plt.show()
