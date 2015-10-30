#!usr/bin/python
import argparse
import pickle

parser=argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,epilog=("""
""")) ###*
parser.add_argument("-t","--time", type=int, default=5000,help="time considered in simulation")
parser.add_argument("-o", "--host",type=int,default=5e6, help="host population")
parser.add_argument("-b","--b", type=float, default=0.001, help="host energy intake")
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
        sommatoria+=Rs[strains.index(x)]*d[x][0][-1]
    print sommatoria
    Ni_t1=((ri*NH*Ni)/((b*NH)+sommatoria))#-Ni
    if Ni_t1<1:
        Ni_t1=0
    return Ni_t1

def equilibrium(Rs,i):
    ri=Rs[i]
    eq=(1-(b/ri))*NH #so Ri>b
    return eq

N_init=1
Rs=[b+0.001, 0.0, 0.0]#,b+0.0005]
Rs[1]=Rs[0]+0.00002
Rs[2]=Rs[1]+0.000015
Ts=[0,2000,2500]#,70000]
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
#for x in range(T):
#    print d[0][0][x],d[0][1][x], d[0][2]
pickle.dump(d, A, protocol=2)

A.close
