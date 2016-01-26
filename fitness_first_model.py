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
rnX=[]
for mu in range(100):
    if all(os.listdir(pth+'RUN'+str(mu)+'/'+x)==[] for x in nX): ###*
        pass
    else:
        rnX.append('RUN'+str(mu)+'/')                          #RUNS R0,R1,...,
trials=0
average=[]
for c_value in nX: #n0, n1, etc
    plot_this=[]
    print "processing c value", c_value
    for ji in xrange(1,xi): #number of jumps
        print "jump",ji
        for rj in rnX: #R0, R1, R2, ...
            print "run", rj
            fin=pth+rj+c_value+'pts'+str(ji)+'plotdata.p_2'
            try:
                f=open(fin,"rb")
                A=pickle.load(f)
                f.close()
                if len(average)==0:
                    average=[0]*len(A[0])
                fitness_values=A[0]
                trials+=1.0
                for val in xrange(len(fitness_values)):
                    average[val]+=fitness_values[val]
            except IOError:
                print "IEOerror",fin
                pass

        #for x in xrange(len(average)):
        average=[(1-x/trials) for x in average]
            #average[x]=average[x]/trials
        plot_this+=average
        print len(plot_this)
        average=[]
        trials=0
    print "plotting"
    fig1, axesa = plt.subplots(1,figsize=(10, 8))
    axesa.set_ylabel("$<U>_g(t)$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    axesa.plot(range(len(plot_this)),plot_this,color='black')
    #plt.title('$Average Fitness$',fontsize=50)
    #print plot_this
    #print len(plot_this)
    #plt.xlim([0,len(average)])
    #plt.ylim([-0.1,max(plot_this)])
    '''if c_value=='n0/':
        ax_inset=fig1.add_axes([0.5,0.55,0.3,0.3])
    elif c_value=="n1/":
        ax_inset=fig1.add_axes([0.2,0.55,0.3,0.3])
    else:
        ax_inset=fig1.add_axes([0.5,0.17,0.3,0.3])
    ax_inset.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))
    ax_inset.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))
    ax_inset.plot(range(100000,101000),plot_this[100000:101000],"k")'''

    namepth=pth+"average_fitness_"+str(c_value)[:-1]#+'_inset'
    fig1.patch.set_alpha(0.5)
    fig1.savefig(namepth+'.png', dpi=100, bbox_inches='tight')
