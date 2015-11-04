#!usr/bin/python
import sys
a=open(sys.argv[1],'r')
z=open(sys.argv[1][:-4]+'res.txt','w')
def palindrome(s):
    s2=''
    for x in s:
        s2+=d[x]
    s2=s2[::-1]
    return s2
stringa=''
for line in a:
    if line[0]=='>':
        pass
    else:
        stringa+=line.strip()
#print stringa
#stringa='TCAATGCATGCGGGTCTATATGCAT'
mini=4
maxi=12
d={'A':'T','T':'A','C':'G','G':'C'}
for x in range(len(stringa)-mini+1):
    for y in range(mini,maxi+1):
        if x+y<=len(stringa):
            #print palindrome(stringa[x:x+y]), stringa[x:x+y]
            if palindrome(stringa[x:x+y])==stringa[x:x+y]:
                print >>z, x+1, y
a.close()
z.close()
