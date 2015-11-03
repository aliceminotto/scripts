#!usr/bin/python
import sys
a=open(sys.argv[1],'r')
def prod(N):
    res=1
    for x in range(1,N+1):
        res=res*x
    return res
stringa=''
for line in a:
    if line[0]=='>':
        pass
    else:
        stringa+=line.strip()
print stringa
A=stringa.count('A')
G=stringa.count('G')
tot=prod(A)*prod(G)
print tot
a.close()
