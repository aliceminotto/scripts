#!usr/bin/python
import sys
import itertools
ros_file=open(sys.argv[1],'r')
res=str(sys.argv[1])[:-3]+'res.txt'
ros_file_output=open(res,'w')
for line in ros_file:
    alfabeto=str(line).split()
    line=ros_file.next()
    k=int(line)
print alfabeto
#Permutations and combinations are emitted in lexicographic sort order.
#So, if the input iterable is sorted, the permutation tuples will be produced in sorted order.
poss=itertools.product(alfabeto, repeat=k)
for x in poss:
    print >> ros_file_output,''.join(x)
ros_file.close()
ros_file_output.close()
