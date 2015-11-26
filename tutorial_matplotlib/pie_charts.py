#tutorial from http://www.labri.fr/perso/nrougier/teaching/matplotlib/#colormaps
#!usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

n = 20
Z = [1.0/21]*19+[2.0/21]
colors=list(plt.cm.binary(np.linspace(0,1,20)))
plt.pie(Z, colors)
plt.show()
