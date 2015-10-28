#!usr/bin/python
import pickle
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pylab import *
import argparse
parser=argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,epilog=("""
"""))
parser.add_argument("p",help="path to the right file")
args=parser.parse_args()
pth=args.p

data=pth
A=pickle.load(open(data,"rb"))
close(data)
print("LOADED")

fig = plt.figure()
To=0
Tmx=len(A[0][1]) #time considered
Tf=Tmx-1
y1=0.0
y2=10000.0
tprt=10
plt.style.use('fivethirtyeight')

for strain in A.keys():
    x=A[strain][1] #time
    y=A[strain][0] #pop size'''
    plt.plot(x,y, linewidth=0.5)#'-o')
#print x
#print y
#raw_input()
'''y=A[0][0]
x=A[0][1]'''

#plt.xlim([0,200])
plt.ylim([0,100])
#plt.xlabel("time  (generations)",fontsize=25)
#plt.ylabel("Pop sizes",fontsize=25)
#formatter = ScalarFormatter()
#formatter.set_powerlimits((-3, 4))
#gca().yaxis.set_major_formatter(formatter)
#fig.suptitle('T= '+str(To), fontsize=24, fontweight='bold')
#plt.clf()
'''for i in range(1+To,Tmx): #time
    if i>tprt:
        print i
        tprt+=10
        for j in A.keys(): #dict
            plt.plot(A[j][0:i],linewidth=1.0)

        #plt.plot(SN[0:i],'-',color='b',linewidth=3.0)
        plt.xlabel("time  (generations)",fontsize=25)
        plt.ylabel("Pop sizes",fontsize=25)
        formatter = ScalarFormatter()
        formatter.set_powerlimits((-3, 4))
        gca().yaxis.set_major_formatter(formatter)
        fig.suptitle('T= '+str(i), fontsize=14, fontweight='bold')
        plt.clf()'''
namepth=pth+"plot"
fig.savefig(namepth+'.png',format='png' , dpi=600, bbox_inches='tight')
