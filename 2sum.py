#!usr/bin/python
import sys
a=open(sys.argv[1],'r')
z=open(sys.argv[1][:-4]+'res.txt','w')
i=0
for line in a:
    if i==0:
        i=1
        pass
    else:
        lista=line.strip().split()
        ii=0
        if ii==0:
            insieme=set()
            for j in lista:
                if all(num not in insieme for num in [j,-j,y,-y]):
                    insieme.add(j)
                for y in lista[lista.index(j):]:
                    insieme.add(y)
                    if int(j)+int(y)==0 and j!=y:
                        #print lista
                        print >>z,lista.index(j)+1, lista.index(y)+1
                        ii=1
                    if ii==1:
                        break
                if ii==1:
                    break
        if ii==0:
            print >>z,'-1'
a.close()
z.close()
