#!usr/bin/python
import sys
a=open(sys.argv[1],'r')
z=open(sys.argv[1]+'res.txt','w')
for line in a:
    n=int(line.strip())
    perm=a.next().strip().split()

#n=4
#perm='2 5 1 3 6 4 7 '.split()
for x in range(len(perm)):
    perm[x]=int(perm[x])

#after a lot of study on internet this should work

def lon_in_sub(lista):
    res=[]
    for i in range(len(lista)):
        massimo=max([res[j] for j in range(i) if res[j][-1]<lista[i]] or [[]], key=len) #max substring
        #print 'massimo', massimo
        aggiunta=massimo+[lista[i]]#add new element
        #print 'aggiunta', aggiunta
        res.append(aggiunta)
        #print res
    return max(res, key=len)

print >>z, ' '.join(str(x) for x in lon_in_sub(perm))
print >>z,' '.join(str(x) for x in lon_in_sub(perm[::-1])[::-1])
#not working first trial
'''
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
print >>z,' '.join(str(x) for x in dec)'''
a.close()
z.close()
