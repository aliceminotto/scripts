#!usr/bin/python
import timeit

ex_string='pts37plotdata.p'

def use_strip(stringa):
    alf='qwertyuiopasdfghjklzxcvbnm.'
    jump_n=int(stringa.strip(alf))
    #print jump_n
def use_translate(stringa):
    import string
    table=string.maketrans('','')
    del_numb=table.translate(table,string.digits)
    jump_n=stringa.translate(table,del_numb)
    #print jump_n

print 'strip method'
print timeit.timeit("use_strip(ex_string)",setup="from __main__ import use_strip, ex_string")
print 'translate method'
print timeit.timeit("use_translate(ex_string)",setup="from __main__ import use_translate, ex_string")
