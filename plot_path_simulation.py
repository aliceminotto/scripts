#!usr/bin/python
import pickle
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
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

To=0
Tmx=len(A[0][1]) #time considered
Tf=Tmx-1
y1=0.0
y2=10000.0
tprt=10
plt.style.use('bmh')
fig, axesa = plt.subplots(1,figsize=(10, 8))

axesa.set_ylabel("$Populations$", fontsize=40)
axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
axesa.xaxis.set_tick_params(labelsize=20)
axesa.xaxis.set_major_formatter(mtick.FormatStrFormatter('%2.2e'))
axesa.yaxis.set_tick_params(labelsize=20)
axesa.yaxis.set_major_formatter(mtick.FormatStrFormatter('%2.2e'))


for strain in A.keys():
    x=A[strain][1] #time
    y=A[strain][0] #pop size'''
    plt.plot(x,y,'-', linewidth=0.9)#'-o')

'''y=A[0][0]
x=A[0][1]'''

#plt.xlim([0,200])
#plt.ylim([0,1000])
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
