#!usr/bin/python
import argparse
import pickle

parser=argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,epilog=("""
""")) ###*
parser.add_argument("-t","--time", type=int, default=10**4,help="time considered in simulation")
parser.add_argument("-o", "--host",type=int,default=100, help="host population")
parser.add_argument("-b","--b", type=float, default=1, help="host energy intake")
args=parser.parse_args()
T=args.time
NH=args.host
b=args.b
A=open("path_var.p","wb")

def N_calc(Rs,i,N_old,t,present):
    ri=Rs[i]
    sommatoria=0
    Ni=N_old
    for x in present:
        sommatoria+=Rs[strains.index(x)]*Ni
        #print sommatoria
    Ni_t1=((ri*NH*Ni)/((b*NH)+sommatoria))-Ni
    if Ni_t1<1:
        Ni_t1=0
    return Ni_t1

def equilibrium(Rs,i):
    ri=Rs[i]
    eq=(0.5-(b/ri))*NH
    return eq

N_init=1
Rs=[5,3]#,3.3]#,3.4]
Ts=[0,6000]#,5000,7000]
strains=[]
j=0
for x in range(len(Ts)):
    strains.append(j)
    j+=1
print 'strains', strains
d={}
for x in strains:
    equ=equilibrium(Rs,x)
    d[x]=[[N_init],[Ts[x]], equ]

for x in range(1,T):
    for index in range(len(Ts)):
        #print x, Ts[index], index
        if x<=Ts[index] and x>Ts[index-1]:
#            print '*******', Ts[index]
            i=index-1
#            print x,i
        elif x>Ts[-1] and x<T:
#            print '######', Ts[index]
            i=len(Ts)-1
#            print x,i
            break
        elif x>=Ts[0] and x<Ts[1]:
            i=0
#            print x,i
            break
        else:
            pass
    present=strains[:i+1]
    for strain in present:
#        print x, strains[:i+1]
#        if x==1 and d[0][0][0]==1:
        N_old=d[strain][0][-1]
        N=N_calc(Rs, strain, N_old, x, present)
        d[strain][0].append(N)
        d[strain][1].append(x)
#            print N_old, N, strain, x,present

print len(d[0][0])
print len(d[1][0])
print d[1][0][0]
print d[1][1][0]
#print len(d[2][0])
#print len(d[3][0])
#print d[0][0][0],d[0][1][0]
print d[0][0][1],d[0][1][1], d[0][2]
pickle.dump(d, A, protocol=2)

A.close
