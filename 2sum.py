#!usr/bin/python
import sys
a=open(sys.argv[1],'r')
z=open(sys.argv[1][:-4]+'res.txt','w')
#j=0
for line in a:
        #print j
        #j+=1
        riga=line.strip().split()
        if len(riga)==2:
            pass
        else:
            visti=set()
            i=0
            for x in range(len(riga)):
                if int(riga[x])==0:
                    if riga[x] in visti:
                        pass
                    else:
                        if riga[x]=='0':
                            if '-'+riga[x] in visti:
                                print riga.index('-'+riga[x])+1, x+1
                                i=1
                                break
                            else:
                                visti.add(riga[x])
                        if riga[x]=='-0':
                            if riga[x][1:] in visti:
                                print riga.index(riga[x][1:])+1, x+1
                                i=1
                                break
                            else:
                                visti.add(riga[x])
                elif int(riga[x]) in visti:
                    pass
                else:
                    #print visti, riga[x], riga
                    if -int(riga[x]) in visti:
                        print riga.index(str(-int(riga[x])))+1,x+1
                        i=1
                        break
                    else:
                        visti.add(int(riga[x]))
            if i==0:
                #print x, len(visti), len(set(riga))
                #print visti
                print '-1'
a.close()
z.close()
'''b=open(sys.argv[2],'r')
res=[]
for line in b:
    line=line.strip().split()
    res.append(line)
a=open(sys.argv[1],'r')
i=0
for line in a:
    line=line.strip().split()
    if len(line)==2:
        pass
    else:
        print '******'+str(res[i])+'*******'
        for x in res[i]:
            print line[int(x)-1]
        i+=1
b.close()
a.close()'''
