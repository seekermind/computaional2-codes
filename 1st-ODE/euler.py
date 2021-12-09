import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return -y**3+np.sin(x)

a = 0.0
b = 10.0
h = 0.1
y0 = 0.0

def euler(f, h, y0, a, b):
    xPoints = np.arange(a, b, h)
    yPoints = []

    for x in xPoints:
        yPoints.append(y0)
        y0 += h*f(x, y0)
    return xPoints, yPoints

xPoints, yPoints = euler(f,h,y0, a, b)
xPoints2, yPoints2 = euler(f,0.001,y0, a, b)
plt.plot(xPoints, yPoints, label='h=0.1')
plt.plot(xPoints2, yPoints2, label='h=0.01')
plt.title(r'$\frac{dy}{dx} = -y^3+\sin{x}$')
plt.legend()
plt.show()
