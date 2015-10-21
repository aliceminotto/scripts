#!/usr/bin/python
import sqlite3
import pickle
import sys
import os
lista_folder=[]
for folder in range(1,len(sys.argv)):
	lista_folder.append(sys.argv[folder])
print lista_folder
lf=[]
for folder in lista_folder:
	ldrun=os.listdir(folder)
#	print ldrun
	for f1 in ldrun:
		if f1[0:3]=='RUN':
			ldn=os.listdir(folder+f1)
#			print ldn
			for f in ldn:
				last=os.listdir(folder+f1+'/'+f)
				for f2 in last:
					lf.append(folder+f1+'/'+f+'/'+f2)
#print lf #list of file to process to update the database

conn=sqlite3.connect('maindb_pathgenomes.db')
print 'connected to maindb_pathgenomes.db'
c = conn.cursor()

for data in lf:
	#print data
	F=open(data,'rb')
	A=pickle.load(F)
	prob=A[7] #list of mutation probability from [1] to [8]
	#print type(prob)
	seed=A[8] #seed
	DT=A[12] #DT
	Jumps=A[13] #number of jumps
	RunC=A[14] #folder (run and c)
	################finish here below##############################
	c.execute('''insert into mutation_probabilities
	(hgt_Eff, hgt_Tes, Eff_mutation, Tes_duplication, m5, m6,m7,m8)
	values (?,?,?,?,?,?,?,?)
	;''', (prob[1],prob[2],prob[3],prob[4],prob[5],prob[6],prob[7],prob[8]))
	#print '*'
	c.execute('''insert into inputs
	(NJumps, DT, Seed)
	values(?,?,?)
	;''', (Jumps,DT,seed))
	c.execute('''insert into output
	(id_probabilities, id_input, Run, C, N, output)
	values (?,?,?,?,?,?)
	;'''(,,RunC[0],RunC[1],RunC[2],)) #fix this line, need to extract the right id number and to figure out what i want to store in the database

con.commit()

conn.close()

