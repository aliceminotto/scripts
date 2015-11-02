#!usr/bin/python
import sys
import itertools
a=open(sys.argv[1],'r')
z=open(str(sys.argv[1])[:-3]+'_res.txt','w')
for line in a:
    alfabeto=str(line).strip().split()
    n=int(a.next())
#alfabeto=['D','N','A']
#n=3
res=[]
for x in range(1,n+1):
    elenco=itertools.product(alfabeto,repeat=x)
    for j in elenco:
        res.append(''.join(j))
res=sorted(res, key=lambda word: [alfabeto.index(x) for x in word])
for x in res:
    print >>z, x
a.close()
z.close()
