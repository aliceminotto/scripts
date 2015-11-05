#!usr/bin/python
import sys
a=open(sys.argv[1],'r')
z=open(sys.argv[1]+'res.txt','w')
for line in a:
    n=int(line.strip())
    perm=a.next().strip().split()

n=14
perm='8 7 5 2 3 9 14 4 6 10 11 12 1 13'.split()

def lon_in_seq(lista, indice):
    if len(lista[indice:])==1:
        best=[perm[-1]]
    else:
        previous=lon_in_seq(lista,indice+1)
        print type(previous),'****'
        if lista[indice]<previous[-1]:
            previous.append(lista[indice])
        best=previous
    print indice,type(best), best
    return best

print lon_in_seq(perm,0)
#not working first trial
'''for x in range(len(perm)):
    perm[x]=int(perm[x])
#print perm
best=[]
dec=[]
for x in range(1,n+1):
    loc=perm.index(x)
    seq=[x]
    print 'starting from ', x
    if len(perm[loc:])>len(best):
        for y in perm[loc+1:]:
            print 'y is ', y
            if y>x:
                print ' looking at ', y
                if len(seq)==1:
                    seq.append(y)
                    print 'seq is ', seq
                elif len(seq)>1:
                    if y<seq[-1] and y>seq[-2]:
                        seq.pop()
                        seq.append(y)
                        print 'seq is ', seq
                    elif y>seq[-1]:
                        seq.append(y)
                        print 'seq is ', seq
        if len(seq)>len(best):
            print 'update', best, seq
            best=seq
print
print best
for x in range(n,0,-1):
    loc=perm.index(x)
    seq=[x]
    #print perm, perm[1:], x+1
    #print x, loc, perm[x+1:]
    for y in perm[loc+1:]:
        #print perm[x+1:]
        #print x, y, '***'
        if y<x:
            #print x, y
            if len(seq)==1:
                seq.append(y)
            elif len(seq)>1:
                if y>seq[-1] and y<seq[-2]:
                    seq.pop()
                    seq.append(y)
                elif y<seq[-1]:
                    seq.append(y)
    if len(seq)>len(dec):
        dec=seq
print >>z,' '.join(str(x) for x in best)
print >>z,' '.join(str(x) for x in dec)
a.close()
z.close()'''
