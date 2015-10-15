#simulation for fixation time of an allele in a population of fixed size N

import sys
import random
def print_help():
    print 'write 0 to perform a simulation with each individual witha different allele'
    print 'write 1 to add a new mutation in a population with a fixed allele'
    exit()
if len(sys.argv)<2:
    print_help()
MOD=int(sys.argv[1])
if MOD==1 or MOD==0:
    pass
else:
    print_help()

def initialize_variable():
    global INIT_ALL
    if MOD==0:
        INIT_ALL=N #number of initial different alleles in the population
        d={}
        for j in range(N):
            d[j]=j
    else:
        INIT_ALL=2
        d={}
        for j in range(N):
            if j==0:
                d[j]=0
            else:
                d[j]=1
    T=0 #number of generations
    return T, d

N=2000 #population size
TRIALS=2000 #number of trials
nt=0 #number of trials performed
average=0.0 #average fixation time of an allele
somma=0 #sum to calculate average number of generation
somma2=0#sum to calculate average number of generation before fixation ore deletion
T=0 #number of generations
INIT_ALL=0 #number of alleles in pop, to be initialized
correction=0 #dont want to count trials where the allele dont get fixated in pop when calculating average

for x in range(TRIALS):
    iv=initialize_variable()
    T=iv[0]
    d=iv[1]
    #print str(d)+'*****'
    #print T
    print
    print "TRIAL # "+str(x)
    while True:
        #print d
        dnew={} #this will be the new population
        for x in range(N):
            allele=d[random.choice(d.keys())]
            dnew[x]=allele
        del d
        d=dnew
        T+=1
        test=d[0]
        if all(alls==test for alls in d.values()):
            #print d
            print
            somma2+=T
            if MOD==0:
                somma+=T
                print 'fixation time of allele '+str(test)+': '+str(T)
            else:
                if test==0:
                    somma+=T
                    print 'fixation time of allele: '+str(T)
                else:
                    correction-=1
                    print 'new allele no more present in the sample population'
            break

if TRIALS+correction==0:
    print 'the allele was never fixated in pop in these trials'
else:
    average=float(somma)/(TRIALS+correction)
    print
    print 'average number of generation for fixation of the allele: '+str(average)
print 'average number of generation before fixation or deletion of the allele: '+str(float(somma2)/TRIALS)
print 'size of population '+str(N)
print 'initial number of alleles in population '+str(INIT_ALL)
if MOD==1:
    print 'fixation rate: '+str(float(TRIALS+correction)/TRIALS)
