import numpy as np
import matplotlib.pyplot as plt

L = 9.04e+10
mu = 0
alpha = 0.5
sigma = np.sqrt(1/(4*alpha))

x = np.random.normal(mu, alpha, 1000)

def f(x,L,alpha):
    return (-1/(2*L))*((4*(alpha**2)*x**2)-2*alpha) + (L/2)*x**2
def p(x, mu, sigma):
    return (1/(np.sqrt(2*np.pi*sigma**2)))*np.exp(-((x-mu)**2)/(2*sigma**2))

res = 0
for i in x:
    res += f(i, L, alpha)*p(i,mu, sigma)

print(res/L)


plt.plot(x, p(x, mu,sigma)*f(x,L,alpha)/L, 'ro')
plt.show()
