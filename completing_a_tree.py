#!usr/bin/python
import sys
a=open(sys.argv[1],'r')
d={}
for line in a:
    line=line.strip().split()
    if len(line)==1:
        n=int(line[0])
    else:
        d[line[0]]=line[1]
lista=[]
lista.append(set([line[0],line[1]]))
for x in d:
    i=0
    for j in range(len(lista)):
        if x in lista[j] or d[x] in lista[j]:
            #print x, j, d[x]
            lista[j].update(set([x,d[x]]))
            #print 'update 1', lista
            i=1
    if i==0:
        lista.append(set([x,d[x]]))
        #print 'update2', lista
for x in range(1,n+1):
    i=0
    for j in range(len(lista)):
        if str(x) in lista[j]:
            i=1
            break
    if i==0:
        lista.append(set([str(x)]))
print lista
print len(lista)-1
tot=0
for x in lista:
    tot+=len(x)
print tot
big_set=set()
for x in lista:
    for j in x:
        if j in big_set:
            print '*****************', j
        else:
            big_set.add(j)
a.close()
