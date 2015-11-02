#!usr/bin/python
import sys
from collections import deque

def fibonacci_variant(T):
    if T==0 or T<0:
        N=0
    elif T==1:
        N=1
        age_pop.pop()
        age_pop.appendleft(1)
    else:
        new=0
        for x in range(1,len(age_pop)):
            new+=age_pop[x]
        dead=age_pop.pop()
        age_pop.appendleft(new)

    return sum(age_pop)

m=3
n=6
age_pop=deque([])
for x in range(m):
    age_pop.append(0)
for x in range(0,n+1):
    N=fibonacci_variant(x)
    print x, N
