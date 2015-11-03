#!usr/bin/python
import sys
a=open(sys.argv[1],'r')
z=open(str(sys.argv[1])[:-3]+'_res.txt','w')
d={}
stringa=''
for line in a:
    line=line.strip()
    if line[0]=='>':
        if stringa!='':
            d[key]=stringa
        key=line[1:]
        stringa=''
    else:
        stringa+=line
d[key]=stringa
k=3
res_lis=[]
for x in d.keys():
    for y in d.keys():
        if x!=y:
            if d[x][-3:]==d[y][:3]:
                res_lis.append(x+' '+y)
for x in res_lis:
    print >>z, x
a.close()
z.close()
