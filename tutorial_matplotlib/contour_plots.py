#tutorial from http://www.labri.fr/perso/nrougier/teaching/matplotlib/
#!usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

def f(x,y): return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)

plt.contourf(X, Y, f(X,Y), 8, alpha=.75, cmap='hot')
C = plt.contour(X, Y, f(X,Y), 8, colors='black', linewidth=.5)
plt.clabel(C,inline=1)

plt.xticks([])
plt.yticks([])
plt.show()
