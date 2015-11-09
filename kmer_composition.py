#!usr/bin/python
import sys
import itertools
a=open(sys.argv[1],'r')
stringa=''
k=4
alfabeto=['A','C','G','T']
for line in a:
    if line[0]=='>':
        pass
    else:
        stringa+=line.strip()
per=itertools.product(alfabeto,repeat=k)
pos=[]
for x in per:
    pos.append(''.join(x))
d={}
for x in pos:
    d[x]=0
for x in range(len(stringa)+1-k):
    s=stringa[x:x+k]
    d[s]+=1
res=''
for x in pos:
    res+=str(d[x])+' '
print res
a.close()
