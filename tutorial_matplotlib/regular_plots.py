#tutorial from http://www.labri.fr/perso/nrougier/teaching/matplotlib/
#!usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

n = 256
X = np.linspace(-np.pi,np.pi,n,endpoint=True)
Y = np.sin(2*X)

plt.plot (X, Y+1, color='blue', alpha=1.00)
plt.fill_between(X,1,Y+1,color='blue',alpha=0.3)
plt.plot (X, Y-1, color='blue', alpha=1.00)
plt.fill_between(X,-1,Y-1,(Y-1)<-1, color='red', alpha=0.3)
plt.fill_between(X,-1,Y-1,(Y-1)>-1,color='blue',alpha=0.3)

plt.xlim(-np.pi,np.pi)
plt.xticks([]) #no ticks
plt.ylim(-2.5,2.5)
plt.yticks([]) #no ticks

plt.show()
