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
a.close()
