import numpy as np
import matplotlib.pyplot as plt

# def f(x,y):
    # return (3*x) + (y/2)

N0 = 1000

def f(x, y):
    b = 1 / (8.617e-5 * 293)
    c = (2*b**(3/2))/np.sqrt(np.pi) 
    N0 = 1000
    return c*N0*np.sqrt(x)*np.exp(-x*b)

a = 0.0
b = 10.0

h = 0.01
y0 = 0

def euler(f, h, y0, a, b):
    xPoints = np.arange(a, b, h)
    yPoints = []

    for x in xPoints:
        yPoints.append(y0)
        y0 += h*f(x, y0)
    return xPoints, yPoints

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

def kutta2(f, h, a, b, y0):
    xPoints = np.arange(a, b, h)
    yPoints = []

    for x in xPoints:
        k1 = h*f(x, y0)
        k2 = h*f(x+h*0.5, y0+k1*0.5)
        y0 += k2
        yPoints.append(y0)

    return xPoints, yPoints
def kutta4(f, h, a, b, y0):
    xPoints = np.arange(a, b, h)
    yPoints = []

    for x in xPoints:
        k1 = h*f(x, y0)
        k2 = h*f(x+h*0.5, y0+k1*0.5)
        k3 = h*f(x+h*0.5, y0+k2*0.5)
        k4 = h*f(x+h, y0+k3)
        y0 += (1/6)*(k1+2*k2+2*k3+k4)
        yPoints.append(y0)

    return xPoints, yPoints




# xPoints, yPoints = euler(f, h, 1, a, b)
# xPoints2, yPoints2 = eulerModified(f, h, 1, a, b ,3)
# xPoints3, yPoints3 = kutta2(f, h, a, b, 1)
xPoints4, yPoints4 = kutta4(f, h, a, b, 0)

# print(xPoints[2], yPoints[2], yPoints2[2], yPoints3[2], yPoints4[2])

# ySolution = [3*np.exp(x) - x**2 - 2*x -2 for x in xPoints]

# plt.plot(xPoints, yPoints, label='euler')
# plt.plot(xPoints2, yPoints2, label='modified-euler')
# plt.plot(xPoints3, yPoints3, label='RK2')
plt.plot(xPoints4, yPoints4, label='RK4')
# # plt.plot(xPoints, ySolution,'r--', label='solution')
# plt.legend()
plt.show()
