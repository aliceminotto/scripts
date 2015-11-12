#tutorial from http://www.labri.fr/perso/nrougier/teaching/matplotlib/
#!usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T=np.arctan2(Y,X)

plt.scatter(X,Y,c=T, s=55, alpha=0.5) #s is the area of the amrker
plt.xlim(-1.5,1.5)
plt.xticks([])
plt.ylim(-1.5,1.5)
plt.yticks([])
plt.show()
