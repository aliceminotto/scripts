#!usr/bin/python
import numpy as np
import random
#hip only damages how long?
T=10**6 #time of the simulation
N=10 #nu,ber of time to repeat to collect stathistics
#will be at least 100
MAX_AGE=110
random.seed(42) #this is the answer to the question
hope=[] #can we maybe do a continuous so that we don't need to store it?
#look in literature if it can be an approximation
offspring=[] #this will be updated each gen
diz_living_pop={} #id of person and char
#will store 0 in norm list otherwise
show=random.randrange(start,stop) ###here change start and stop according to literature parameters
leth=random.randrange(start,stop) ###again here change start and stop according to literature
#note that here I'm not considering the correlation existing between the two previous parameters.
#that will require other studies
time_counter=0 #when
