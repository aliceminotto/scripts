#!usr/bin/python
import sys
import itertools
a=open(sys.argv[1],'r')
for line in a:
    par=str(line).split()
    n=int(par[0])
    k=int(par[1])
res=1
for x in range(k):
    res*=(n-x)
res=res%1000000
print res
a.close()
