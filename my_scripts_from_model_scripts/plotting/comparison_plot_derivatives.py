#!usr/bin/python
#####################cell 1#########################
import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.pyplot import cm
import argparse
import os
#plt.style.use('bmh')
parser=argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,epilog=("""
""")) ###*
########each directory has a different DT
parser.add_argument("p1",help="path to the right directory")
parser.add_argument("p2", help="path to the second directory")
parser.add_argument("p3", help="path to the third directory")
parser.add_argument("p4", help="path to the last directory")
parser.add_argument("p5",help="path to the directory no jumps")
#parser.add_argument("r", type=int, help="number of runs for directory")
###*parser.add_argument("j", type=int, help="number of jumps")###*
args=parser.parse_args() ###*
pth1=args.p1
pth2=args.p2
pth3=args.p3
pth4=args.p4
pthno=args.p5
#RUNS=args.r
main_path=[pth1,pth2,pth3,pth4]
print pth1,pth2,pth3,pth4,pthno
###*xi=range(1,(args.j+1))###*
##############files with data##########################
n1=pth1+"CDATAV.p"
n2=pth2+"CDATAV.p"
n3=pth3+"CDATAV.p"
n4=pth4+"CDATAV.p"
nno=pthno+"CDATAV.p"
print n1, n2, n3, n4#*,nno
f1=open(n1,"rb")
NOPE1=pickle.load(f1)
f1.close()
f2=open(n2,"rb")
NOPE2=pickle.load(f2)
f2.close()
f3=open(n3,"rb")
NOPE3=pickle.load(f3)
f3.close()
f4=open(n4,"rb")
NOPE4=pickle.load(f4)
f4.close()
fno=open(nno,"rb")
NOJU=pickle.load(fno)
fno.close()

#######plot same Qi different DT#################
#print NOPE1[0][1], 'tempo?'
#print NOPE1[0][2]

#Data=[t,LAV,NAV,STDN,STDL]
T1=NOPE1[0]
T2=NOPE2[0]
T3=NOPE3[0]
T4=NOPE4[0]
TNO=NOJU[0]

assert T1==T2==T4

pts1=NOPE1[1].keys()
pts2=NOPE2[1].keys()
pts3=NOPE3[1].keys()
pts4=NOPE4[1].keys()
ptsno=NOJU[1].keys()

assert pts1==pts2==pts3==pts4

d={}
d['DT5000']=["$\Delta T=5.0\\times 10^3$",NOPE1,T1]
d['DT10000']=["$\Delta T= 1.0\\times 10^4$",NOPE2,T2]
d['DT15000']=["$\Delta T= 1.5 \\times 10^4$",NOPE3,T3]
d['DT20000']=["$\Delta T= 2.0\\times 10^4$",NOPE4,T4]
####no need for this d['infinity']=["$\Delta T=\infty$",NOJU,TNO]
def averaging(der_list):
    n=0
    to_plot=[]
    sn=0.0
    for x in der_list: #averaging
        sn+=x
        n+=1
        to_plot.append(sn/n)
    return to_plot

def sampling(lista):
    slices=[lista[i:i + 10] for i in range(0, len(lista), 10)]
    res=[]
    for x in slices:
        res.append(np.mean(x))
    return res

######################################################################################################
#plotting total length over time for same c and different DT (it miss the infinity and color map)
######################################################################################################
'''c=0.1
for x in pts1:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$< Lengths >$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    color=iter(cm.rainbow(np.linspace(0,1,5)))

    col=next(color)
    axesa.plot(T1,NOPE1[1][x],c=col,label="$\Delta T=5.0\\times 10^3$")
    col=next(color)
    axesa.plot(T2,NOPE2[1][x],c=col,label="$\Delta T= 1.0\\times 10^4$")
    col=next(color)
    axesa.plot(T3,NOPE3[1][x],c=col,label="$\Delta T= 1.5 \\times 10^4$")
    col=next(color)
    axesa.plot(T4,NOPE4[1][x],c=col,label="$\Delta T= 2.0\\times 10^4$")
    col=next(color)
    axesa.plot(TNO,NOJU[1]['n0/'],c=col, label="$\Delta T=\infty$")

    axesa.legend(loc='best', fancybox=True, framealpha=0.5)

    val_c=c
    titstr='$c='+str(c)+'$'
    print titstr
    c+=0.1
    axesa.set_title(titstr, fontsize=40)

    #axesa.set_xscale('log')
    axesa.set_xlim([0,200000])
    #axesa.set_xlim([0,80000])

    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'len_plot'+str(c-0.1)+'.png',format='png' ,dpi=1200, bbox_inches='tight')
    '''

###################################################################################################
#derivatives previous plot
##################################################################################################
c=0.1
for x in pts1:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$<\Delta L>_{t}$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    color=iter(cm.rainbow(np.linspace(0,1,5)))
    L=40000

    der1=np.diff(NOPE1[1][x])
    der2=np.diff(NOPE2[1][x])
    der3=np.diff(NOPE3[1][x])
    der4=np.diff(NOPE4[1][x])
    der5=np.diff(NOJU[1]['n0/'])
    col=next(color)
    axesa.plot(averaging(der1),c=col,label="$\Delta T=5.0\\times 10^3$")
    col=next(color)
    axesa.plot(averaging(der2),c=col,label="$\Delta T= 1.0\\times 10^4$")
    col=next(color)
    axesa.plot(averaging(der3),c=col,label="$\Delta T= 1.5 \\times 10^4$")
    col=next(color)
    axesa.plot(averaging(der4),c=col,label="$\Delta T= 2.0\\times 10^4$")
    col=next(color)
    axesa.plot(averaging(der5),c=col, label="$\Delta T=\infty$")

    axesa.legend(loc='best', fancybox=True, framealpha=0.5)

    val_c=c
    titstr='$c='+str(c)+'$'
    print titstr
    c+=0.1
    axesa.set_title(titstr, fontsize=40)

    #axesa.set_xscale('log')
    axesa.set_xlim([0,L])
    axesa.set_ylim([-200,200])
    #axesa.set_xlim([0,80000])

    fig.patch.set_alpha(0.5)
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'len_plot'+str(c-0.1)+'_derivatives.png',format='png' ,dpi=100, bbox_inches='tight')
     #done
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'len_plot'+str(c-0.1)+'_derivatives.svg',bbox_inches='tight')

####################################################################################################
#plotting len of eff and tes over time for same c and different DT
####################################################################################################
'''c=0.1
for x in pts1:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$< Lengths >_{Ens}$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    color=iter(cm.rainbow(np.linspace(0,1,5))) ###change 4 when adding new

    col=next(color)
    axesa.plot(T1,NOPE1[9][x],c=col,ls='-',label="$\Delta T=5.0\\times 10^3$")
    axesa.plot(T1,NOPE1[10][x],c=col,ls='--')
    col=next(color)
    axesa.plot(T2,NOPE2[9][x],c=col,ls='-',label="$\Delta T= 1.0\\times 10^4$")
    axesa.plot(T2,NOPE2[10][x],c=col,ls='--')
    col=next(color)
    axesa.plot(T3,NOPE3[9][x],c=col,ls='-',label="$\Delta T= 1.5 \\times 10^4$")
    axesa.plot(T3,NOPE3[10][x],c=col,ls='--')
    col=next(color)
    axesa.plot(T4,NOPE4[9][x],c=col,ls='-',label="$\Delta T= 2.0\\times 10^4$")
    axesa.plot(T4,NOPE4[10][x],c=col,ls='--')
    col=next(color)
    axesa.plot(TNO,NOJU[9]['n0/'],c=col,ls='-', label="$\Delta T=\infty$")
    plt.annotate('effector genes',xy=(100000, NOJU[9]['n0/'][-1000]))
    axesa.plot(TNO,NOJU[10]['n0/'],c=col,ls='--')
    plt.annotate('TEs',xy=(100000,NOJU[10]['n0/'][-1000]))

    axesa.legend(loc='best', fancybox=True, framealpha=0.5)

    val_c=c
    titstr='$c='+str(c)+'$'
    print titstr
    axesa.set_title(titstr, fontsize=40)

    #axesa.set_xscale('log')
    axesa.set_xlim([0,200000])
    #axesa.set_xlim([0,80000])

    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'len_plot_eff_te'+str(c)+'.png',format='png' ,dpi=1200, bbox_inches='tight')


    c+=0.1'''
###############################################################################################
#derivatives previous plot
################################################################################################
c=0.1
for x in pts1:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    L=40000 #time to plot

    axesa.set_ylabel("$<\Delta L>_{t}$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    color=iter(cm.rainbow(np.linspace(0,1,5))) ###change 4 when adding new

    serie1=averaging(np.diff(NOPE1[9][x]))
    serie12=averaging(np.diff(NOPE1[10][x]))
    serie2=averaging(np.diff(NOPE2[9][x]))
    serie22=averaging(np.diff(NOPE2[10][x]))
    serie3=averaging(np.diff(NOPE3[9][x]))
    serie32=averaging(np.diff(NOPE3[10][x]))
    serie4=averaging(np.diff(NOPE4[9][x]))
    serie42=averaging(np.diff(NOPE4[10][x]))
    serie5=averaging(np.diff(NOJU[9]['n0/']))
    serie52=averaging(np.diff(NOJU[10]['n0/']))
    col=next(color)
    axesa.plot(T1[1:],serie1,c=col,ls='-',label="$\Delta T=5.0\\times 10^3$")
    axesa.plot(T1[1:],serie12,c=col,ls='--')
    col=next(color)
    axesa.plot(T2[1:],serie2,c=col,ls='-',label="$\Delta T= 1.0\\times 10^4$")
    axesa.plot(T2[1:],serie22,c=col,ls='--')
    col=next(color)
    axesa.plot(T3[1:],serie3,c=col,ls='-',label="$\Delta T= 1.5 \\times 10^4$")
    axesa.plot(T3[1:],serie32,c=col,ls='--')
    col=next(color)
    axesa.plot(T4[1:],serie4,c=col,ls='-',label="$\Delta T= 2.0\\times 10^4$")
    axesa.plot(T4[1:],serie42,c=col,ls='--')
    col=next(color)
    axesa.plot(TNO[1:],serie5,c=col,ls='-', label="$\Delta T=\infty$")
    position1=min([serie1[L/2],serie2[L/2],serie3[L/2],serie4[L/2],serie5[L/2]])-10
    plt.annotate('effector genes',xy=(L/2, position1),size='x-large',ha='center',va='top',bbox=dict(alpha=0.5,facecolor='white',boxstyle='round'))
    axesa.plot(TNO[1:],serie52,c=col,ls='--')
    position2=max([serie12[L/2],serie22[L/2],serie32[L/2],serie42[L/2],serie52[L/2]])+10
    plt.annotate('TEs',xy=(L/2,position2),size='x-large',ha='center',va='bottom',bbox=dict(alpha=0.5,facecolor='white',boxstyle='round'))

    axesa.legend(loc='best', fancybox=True, framealpha=0.5)

    val_c=c
    titstr='$c='+str(c)+'$'
    print titstr
    axesa.set_title(titstr, fontsize=40)

    #axesa.set_xscale('log')
    axesa.set_xlim([0,L])
    axesa.set_ylim([-200,200])
    #axesa.set_xlim([0,80000])

    fig.patch.set_alpha(0.5)
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'len_plot_eff_te'+str(c)+'_derivatives.png',format='png' ,dpi=100, bbox_inches='tight')
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'len_plot_eff_te'+str(c)+'_derivatives.svg',bbox_inches='tight')

    c+=0.1

################################################################################################
#plotting total number of units over time for different c and same DT (it misses infinity and color map)
#################################################################################################
'''c=0.1
for x in pts1:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$< Number$ $of$ $units >_{Ens}$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    color=iter(cm.rainbow(np.linspace(0,1,5)))

    col=next(color)
    axesa.plot(T1,NOPE1[2][x],c=col,label="$\Delta T=5.0\\times 10^3$")
    col=next(color)
    axesa.plot(T2,NOPE2[2][x],c=col,label="$\Delta T= 1.0\\times 10^4$")
    col=next(color)
    axesa.plot(T3,NOPE3[2][x],c=col,label="$\Delta T= 1.5 \\times 10^4$")
    col=next(color)
    axesa.plot(T4,NOPE4[2][x],c=col,label="$\Delta T= 2.0\\times 10^4$")
    col=next(color)
    axesa.plot(TNO,NOJU[2]['n0/'],c=col, label="$\Delta T=\infty$")

    axesa.legend(loc='best', fancybox=True, framealpha=0.5)

    val_c=c
    titstr='$c='+str(c)+'$'
    print titstr
    c+=0.1
    axesa.set_title(titstr, fontsize=40)

    #axesa.set_xscale('log')
    axesa.set_xlim([0,200000])
    #axesa.set_xlim([0,80000])

    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'unit_plot'+str(c-0.1)+'.png',format='png' ,dpi=1200, bbox_inches='tight')
    '''

################################################################################################
#derivatives previous plot
###############################################################################################
c=0.1
for x in pts1:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$<\Delta N_g>_{t}$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    L=100000
    color=iter(cm.rainbow(np.linspace(0,1,5)))

    col=next(color)
    axesa.plot(T1[1:],averaging(np.diff(NOPE1[2][x])),c=col,label="$\Delta T=5.0\\times 10^3$")
    col=next(color)
    axesa.plot(T2[1:],averaging(np.diff(NOPE2[2][x])),c=col,label="$\Delta T= 1.0\\times 10^4$")
    col=next(color)
    axesa.plot(T3[1:],averaging(np.diff(NOPE3[2][x])),c=col,label="$\Delta T= 1.5 \\times 10^4$")
    col=next(color)
    axesa.plot(T4[1:],averaging(np.diff(NOPE4[2][x])),c=col,label="$\Delta T= 2.0\\times 10^4$")
    col=next(color)
    axesa.plot(TNO[1:],averaging(np.diff(NOJU[2]['n0/'])),c=col, label="$\Delta T=\infty$")

    axesa.legend(loc='best', fancybox=True, framealpha=0.5)

    val_c=c
    titstr='$c='+str(c)+'$'
    print titstr
    c+=0.1
    axesa.set_title(titstr, fontsize=40)

    #axesa.set_xscale('log')
    axesa.set_xlim([0,L])
    #axesa.set_xlim([0,80000])

    fig.patch.set_alpha(0.5)
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'unit_plot'+str(c-0.1)+'_derivatives.png',format='png' ,dpi=100, bbox_inches='tight')
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'unit_plot'+str(c-0.1)+'_derivatives.svg',bbox_inches='tight')

################################################################################################
#plotting number of tes and eff over time for same c and different DT
#############################################################################################
'''c=0.1
for x in pts1:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$< Number$ $of$ $units >_{Ens}$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    color=iter(cm.rainbow(np.linspace(0,1,5))) ###change 4 when adding new

    col=next(color)
    axesa.plot(T1,NOPE1[5][x],c=col,ls='-',label="$\Delta T=5.0\\times 10^3$")
    axesa.plot(T1,NOPE1[6][x],c=col,ls='--')
    col=next(color)
    axesa.plot(T2,NOPE2[5][x],c=col,ls='-',label="$\Delta T= 1.0\\times 10^4$")
    axesa.plot(T2,NOPE2[6][x],c=col,ls='--')
    col=next(color)
    axesa.plot(T3,NOPE3[5][x],c=col,ls='-',label="$\Delta T= 1.5 \\times 10^4$")
    axesa.plot(T3,NOPE3[6][x],c=col,ls='--')
    col=next(color)
    axesa.plot(T4,NOPE4[5][x],c=col,ls='-',label="$\Delta T= 2.0\\times 10^4$")
    axesa.plot(T4,NOPE4[6][x],c=col,ls='--')
    col=next(color)
    axesa.plot(TNO,NOJU[5]['n0/'],c=col,ls='-',label="$\Delta T=\infty$")
    axesa.plot(TNO,NOJU[6]['n0/'],c=col,ls='--')

    axesa.legend(loc='best', fancybox=True, framealpha=0.5)

    val_c=c
    titstr='$c='+str(c)+'$'
    print titstr
    c+=0.1
    axesa.set_title(titstr, fontsize=40)

    #axesa.set_xscale('log')
    axesa.set_xlim([0,200000])
    #axesa.set_xlim([0,80000])

    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'unit_plot_eff_Te'+str(c-0.1)+'.png',format='png' ,dpi=1200, bbox_inches='tight')
    '''

###################################################################################################################################
#derivatives previous plot
####################################################################################################################################
c=0.1
for x in pts1:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$<\Delta N_g>_{t}$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    L=100000 #time to plot

    color=iter(cm.rainbow(np.linspace(0,1,5))) ###change 4 when adding new

    serie1=averaging(np.diff(NOPE1[5][x]))
    serie12=averaging(np.diff(NOPE1[6][x]))
    serie2=averaging(np.diff(NOPE2[5][x]))
    serie22=averaging(np.diff(NOPE2[6][x]))
    serie3=averaging(np.diff(NOPE3[5][x]))
    serie32=averaging(np.diff(NOPE3[6][x]))
    serie4=averaging(np.diff(NOPE4[5][x]))
    serie42=averaging(np.diff(NOPE4[6][x]))
    serie5=averaging(np.diff(NOJU[5]['n0/']))
    serie52=averaging(np.diff(NOJU[6]['n0/']))

    col=next(color)
    axesa.plot(T1[1:],serie1,c=col,ls='-',label="$\Delta T=5.0\\times 10^3$")
    axesa.plot(T1[1:],serie12,c=col,ls='--')
    col=next(color)
    axesa.plot(T2[1:],serie2,c=col,ls='-',label="$\Delta T= 1.0\\times 10^4$")
    axesa.plot(T2[1:],serie22,c=col,ls='--')
    col=next(color)
    axesa.plot(T3[1:],serie3,c=col,ls='-',label="$\Delta T= 1.5 \\times 10^4$")
    axesa.plot(T3[1:],serie32,c=col,ls='--')
    col=next(color)
    axesa.plot(T4[1:],serie4,c=col,ls='-',label="$\Delta T= 2.0\\times 10^4$")
    axesa.plot(T4[1:],serie42,c=col,ls='--')
    col=next(color)
    axesa.plot(TNO[1:],serie5,c=col,ls='-',label="$\Delta T=\infty$")
    axesa.plot(TNO[1:],serie52,c=col,ls='--')

    position1=max([serie1[L/2],serie2[L/2],serie3[L/2],serie4[L/2],serie5[L/2]])+0.001
    plt.annotate('effector genes',xy=(L/2, position1),size='x-large',ha='center',va='bottom',bbox=dict(alpha=0.5,facecolor='white',boxstyle='round'))
    position2=min([serie12[L/2],serie22[L/2],serie32[L/2],serie42[L/2],serie52[L/2]])-0.001
    plt.annotate('TEs',xy=(L/2,position2),size='x-large',ha='center',va='top',bbox=dict(alpha=0.5,facecolor='white',boxstyle='round'))

    axesa.legend(loc='best', fancybox=True, framealpha=0.5)

    val_c=c
    titstr='$c='+str(c)+'$'
    print titstr
    c+=0.1
    axesa.set_title(titstr, fontsize=40)

    #axesa.set_xscale('log')
    axesa.set_xlim([0,L])
    #axesa.set_xlim([0,80000])

    fig.patch.set_alpha(0.5)
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'unit_plot_eff_Te'+str(c-0.1)+'_derivatives.png',format='png' ,dpi=100, bbox_inches='tight')
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'unit_plot_eff_Te'+str(c-0.1)+'_derivatives.svg',bbox_inches='tight')

####################################################################################################################################
#same DT different c value
###################################################################################################################################

'''for x in d:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$< Number$ $of$ $units >$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    c=0.1

    color=iter(cm.rainbow(np.linspace(0,1,len(pts1))))

    for y in pts1:

        print x, y
        col=next(color)
        axesa.plot(d[x][2],d[x][1][5][y],c=col,ls='-',label='$c='+str(c)+'$')
        axesa.plot(d[x][2],d[x][1][6][y],c=col,ls='--')

        axesa.legend(loc='best', fancybox=True, framealpha=0.5)
        c+=0.1

    titstr=d[x][0]
    print titstr
    axesa.set_title(titstr, fontsize=40)

    #axesa.set_xscale('log')
    axesa.set_xlim([0,200000])
    #axesa.set_xlim([0,80000])

    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'unit_plot_eff_Te'+str(x)+'.png',format='png' ,dpi=1200, bbox_inches='tight')
    '''

#################################################################################################################
#derivative previous plot
################################################################################################################
for x in d:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$<\Delta N_g>_{t}$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    c=0.1

    color=iter(cm.rainbow(np.linspace(0,1,len(pts1))))

    lis1=[]
    lis2=[]

    L=100000 #time to plot

    for y in pts1:

        print x, y
        col=next(color)
        axesa.plot(d[x][2][1:],averaging(np.diff(d[x][1][5][y])),c=col,ls='-',label='$c='+str(c)+'$')
        axesa.plot(d[x][2][1:],averaging(np.diff(d[x][1][6][y])),c=col,ls='--')

        lis1.append(averaging(np.diff(d[x][1][5][y]))[L/2])
        lis2.append(averaging(np.diff(d[x][1][6][y]))[L/2])
        c+=0.1

    axesa.legend(loc='best', fancybox=True, framealpha=0.5)

    position1=max(lis1)+0.001
    plt.annotate('effector genes',xy=(L/2, position1),size='x-large',ha='center',va='bottom',bbox=dict(alpha=0.5,facecolor='white',boxstyle='round'))
    position2=min(lis2)-0.001
    plt.annotate('TEs',xy=(L/2,position2),size='x-large',ha='center',va='top',bbox=dict(alpha=0.5,facecolor='white',boxstyle='round'))

    titstr=d[x][0]
    print titstr
    axesa.set_title(titstr, fontsize=40)

    #axesa.set_xscale('log')
    axesa.set_xlim([0,L])
    #axesa.set_xlim([0,80000])

    fig.patch.set_alpha(0.5)
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'unit_plot_eff_Te'+str(x)+'_derivatives.png',format='png' ,dpi=100, bbox_inches='tight')
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'unit_plot_eff_Te'+str(x)+'_derivatives.svg',bbox_inches='tight')

################################################################################################################
'''for x in d:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$< Lengths >$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    c=0.1

    color=iter(cm.rainbow(np.linspace(0,1,len(pts1))))

    for y in pts1:

        col=next(color)
        axesa.plot(d[x][2],d[x][1][9][y],c=col,ls='-',label='$c='+str(c)+'$')
        axesa.plot(d[x][2],d[x][1][10][y],c=col,ls='--')

        axesa.legend(loc='best', fancybox=True, framealpha=0.5)
        c+=0.1

    titstr=d[x][0]
    print titstr
    axesa.set_title(titstr, fontsize=40)

    #axesa.set_xscale('log')
    axesa.set_xlim([0,200000])
    #axesa.set_xlim([0,80000])

    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'len_plot_eff_Te'+str(x)+'.png',format='png' ,dpi=1200, bbox_inches='tight')
    '''

#############################################################################################
#derivatives previous plot
#############################################################################################
for x in d:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$<\Delta L>_{t}$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    c=0.1

    color=iter(cm.rainbow(np.linspace(0,1,len(pts1))))

    lis1=[]
    lis2=[]

    L=100000 #time to plot
    for y in pts1:

        col=next(color)
        axesa.plot(d[x][2][1:],averaging(np.diff(d[x][1][9][y])),c=col,ls='-',label='$c='+str(c)+'$')
        axesa.plot(d[x][2][1:],averaging(np.diff(d[x][1][10][y])),c=col,ls='--')

        lis1.append(averaging(np.diff(d[x][1][9][y]))[L/2])
        lis2.append(averaging(np.diff(d[x][1][10][y]))[L/2])
        c+=0.1

    axesa.legend(loc='best', fancybox=True, framealpha=0.5)

    position1=min(lis1)-10
    plt.annotate('effector genes',xy=(L/2, position1),size='x-large',ha='center',va='top',bbox=dict(alpha=0.5,facecolor='white',boxstyle='round'))
    position2=max(lis2)+10
    plt.annotate('TEs',xy=(L/2,position2),size='x-large',ha='center',va='bottom',bbox=dict(alpha=0.5,facecolor='white',boxstyle='round'))

    titstr=d[x][0]
    print titstr
    axesa.set_title(titstr, fontsize=40)

    #axesa.set_xscale('log')
    axesa.set_xlim([0,L])
    #axesa.set_xlim([0,80000])

    fig.patch.set_alpha(0.5)
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'len_plot_eff_Te'+str(x)+'_derivatives.png',format='png' ,dpi=100, bbox_inches='tight')
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'len_plot_eff_Te'+str(x)+'_derivatives.svg',bbox_inches='tight')

'''

##########################cell 18#############################
Rtlonga={}#
Rtlongb={}#

rtks=[]
for i in range(9):
    j='n'+str(i)+'/'
    rtks.append(j)
#print rtks

for jn in rtks:
    mua=[]
    mua=np.diff(LONG[1][jn])

    mub=[]
    mub=np.diff(LONG[2][jn])

    n=0
    avdfa=[]
    sn=0.0
    for j in mua:
        sn+=j
        n+=1
        avdfa.append(sn/n)
    Rtlonga[jn]=avdfa

    n=0
    avdfb=[]
    sn=0.0
    for j in mub:
        sn+=j
        n+=1
        avdfb.append(sn/n)

    Rtlongb[jn]=avdfb

Rtshorta={}
Rtshortb={}

for jn in rtks:
    mua=[]
    mua=np.diff(SHORT[1][jn])

    mub=[]
    mub=np.diff(SHORT[2][jn])

    n=0
    avdfa=[]
    sn=0.0
    for j in mua:
        sn+=j
        n+=1
        avdfa.append(sn/n)
    Rtshorta[jn]=avdfa

    n=0
    avdfb=[]
    sn=0.0
    for j in mub:
        sn+=j
        n+=1
        avdfb.append(sn/n)

    Rtshortb[jn]=avdfb

Rtmoda={}
Rtmodb={}

for jn in rtks:
    mua=[]
    mua=np.diff(MOD[1][jn])

    mub=[]
    mub=np.diff(MOD[2][jn])

    n=0
    avdfa=[]
    sn=0.0
    for j in mua:
        sn+=j
        n+=1
        avdfa.append(sn/n)
    Rtmoda[jn]=avdfa

    n=0
    avdfb=[]
    sn=0.0
    for j in mub:
        sn+=j
        n+=1
        avdfb.append(sn/n)

    Rtmodb[jn]=avdfb

Rtmeda={}
Rtmedb={}
for jn in rtks:
    mua=[]
    mua=np.diff(MED[1][jn])

    mub=[]
    mub=np.diff(MED[2][jn])

    n=0
    avdfa=[]
    sn=0.0
    for j in mua:
        sn+=j
        n+=1
        avdfa.append(sn/n)
    Rtmeda[jn]=avdfa

    n=0
    avdfb=[]
    sn=0.0
    for j in mub:
        sn+=j
        n+=1
        avdfb.append(sn/n)

    Rtmedb[jn]=avdfb


Rtnopea={}
Rtnopeb={}

mua=[]
mua=np.diff(NOPE[1]['n0/'])

mub=[]
mub=np.diff(NOPE[2]['n0/'])

n=0
avdfa=[]
sn=0.0
for j in mua:
    sn+=j
    n+=1
    avdfa.append(sn/n)
Rtnopea['n0/']=avdfa

n=0
avdfb=[]
sn=0.0
for j in mub:
    sn+=j
    n+=1
    avdfb.append(sn/n)

Rtnopeb['n0/']=avdfb

##########################cell 19###############################
print Rtshorta.keys(), Rtshortb.keys(), Rtmoda.keys(), Rtmodb.keys(), Rtmeda.keys(), Rtmedb.keys(), Rtlonga.keys(), Rtlongb.keys()

########################cell 20#################################
fig, axesa = plt.subplots(1,figsize=(10, 8))
#fig, axesb = plt.subplots(1,figsize=(10, 8))

c=0.1
for i in rtks:

    fig, axesa = plt.subplots(1,figsize=(10, 8))
    fig, axesb = plt.subplots(1,figsize=(10, 8))
    titstr='C='+str(c)
    print titstr, i
    c+=0.1
#raw_input()

    axesa.set_title(titstr, fontsize=40)
    axesa.plot(Rtshorta[i],label="$\Delta T=5.0\\times10^3$")
    axesa.plot(Rtmeda[i],label="$\Delta T=1.0\\times10^4$")
    axesa.plot(Rtmoda[i],label="$\Delta T=1.5\\times10^4$")
    axesa.plot(Rtlonga[i],label="$\Delta T=2.0\\times10^4$")
    axesa.plot(Rtnopea['n0/'],label="$\Delta T=\infty$")
    axesa.set_xlim([0,20000])
    axesa.set_ylabel("$<\Delta L>_{t}$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.FormatStrFormatter('%1.1e'))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.FormatStrFormatter('%1.1e'))
    axesa.legend(loc='best', fancybox=True, framealpha=0.5)




    axesb.set_title(titstr, fontsize=40)
    axesb.plot(Rtshortb[i],label="$\Delta T=5.0\\times10^3$")
    axesb.plot(Rtmedb[i],label="$\Delta T=1.0\\times10^4$")
    axesb.plot(Rtmodb[i],label="$\Delta T=1.5\\times10^4$")
    axesb.plot(Rtlongb[i],label="$\Delta T=2.0\\times10^4$")
    axesb.plot(Rtnopeb['n0/'],label="$\Delta T=\infty$")
    axesb.set_xlim([0,20000])
    axesb.set_ylabel("$<\Delta N_g>_{t}$", fontsize=40)
    axesb.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesb.xaxis.set_tick_params(labelsize=20)
    axesb.xaxis.set_major_formatter(mtick.FormatStrFormatter('%1.1e'))
    axesb.yaxis.set_tick_params(labelsize=20)
    axesb.yaxis.set_major_formatter(mtick.FormatStrFormatter('%1.1e'))
    axesb.legend(loc='best', fancybox=True, framealpha=0.5)'''
