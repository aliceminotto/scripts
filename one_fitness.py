#!usr/bin/python
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os
import pickle
import matplotlib.ticker as mtick
pth="/usr/users/TSL_20/minottoa/high_mutation_nojumps/"
print pth
xi=10+1 #jumps
nX=['n0/']#,'n1/','n2/','n3/','n4/','n5/','n6/','n7/','n8/'] #Parameters C ###*uncommented this line
rj='RUN0/'
for c_value in nX: #n0, n1, etc
    plot_this=[]
    print "processing c value", c_value
    for ji in xrange(1,xi): #number of jumps
        fitness_values=[]
        print "jump",ji
        try:
            fin=pth+rj+c_value+'pts'+str(ji)+'plotdata.p_2'
            f=open(fin,"rb")
            A=pickle.load(f)
            f.close()
            fitness_values+=A[0]
        except IOError:
            continue
        plot_this+=[(1-x) for x in fitness_values]
        print len(plot_this)
    print "plotting"
    fig1, axesa = plt.subplots(1,figsize=(10, 8))
    axesa.set_ylabel("$U_g(t)$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    plt.plot(range(len(plot_this)),plot_this,color='black')
    #plt.title('$Fitness$',fontsize=50)
    #print plot_this
    #print len(plot_this)
    #plt.xlim([0,len(average)])
    #plt.ylim([min(average)-100,max(average)+100])
    '''if c_value in ["n0/", "n1/", "n2/"]:
        plt.ylim([0,0.1])
    elif c_value=="n3/":
        plt.ylim([0,0.15])
    else:
        plt.ylim([0,0.3])'''

    namepth=pth+"one_fitness_"+str(c_value)[:-1]+"run_0"
    fig1.patch.set_alpha(0.5)
    fig1.savefig(namepth+'.png', dpi=100, bbox_inches='tight')
