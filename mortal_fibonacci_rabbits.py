#!usr/bin/python
import sys
'''f=sys.argv[1]
F=open(f,'r')'''

def fibonacci_variant(T):
    if T==0 or T<0:
        N=0
    elif T==1 or T==2:
        N=1
    else:
        N=fibonacci_variant(T-1)+fibonacci_variant(T-2)-(fibonacci_variant(T-m)-fibonacci_variant(T-2*m))
    return N
'''for line in F.readlines():
    par=line.split()
n=par[0] #number of month
m=par[1] #number of months after a rabbit die'''

m=3
n=6
for x in range(1,n+1):
    N=fibonacci_variant(x)
    print x, N
