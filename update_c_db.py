#!/usr/bin/python
import sqlite3
import pickle
import sys
import os

#creating a list of folders where there are the data to put in database

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
	t_prob=(prob[1],prob[2],prob[3],prob[4],prob[5],prob[6],prob[7],prob[8])
	c.execute('''select * from mutation_probabilities
	where hgt_Eff=? and hgt_Tes=? and Eff_mutation=?
	and Tes_duplication=? and m5=? and m6=? and m7=? and m8=?
	;''', t_prob)
	result=c.fetchone()
	#print result
	if result==None:
		c.execute('''insert into mutation_probabilities
		(hgt_Eff, hgt_Tes, Eff_mutation, Tes_duplication, m5, m6,m7,m8)
		values (?,?,?,?,?,?,?,?)
		;''', t_prob)
		print t_prob
		id_probabilities=c.lastrowid
	else:
		id_probabilities=result[0]
	#print id_probabilities
	par=(Jumps,DT,seed)
	c.execute('''select * from inputs
	where NJumps=? and DT=? and Seed=?
	;''', par)
	result2=c.fetchone()
	#print result2
	if result2==None:
		c.execute('''insert into inputs
		(NJumps, DT, Seed)
		values(?,?,?)
		;''', par)
		print par
		id_input=c.lastrowid
	else:
		id_input=result2[0]
	print id_input
	print RunC[0],RunC[1],RunC[2]
	print type(id_probabilities)
	c.execute('''insert into output
	(id_probabilities, id_input, Run, C, N, output)
	values (?,?,?,?,?,?)
	;''',(id_probabilities,id_input,RunC[0],RunC[1],RunC[2],[])) #fix this line, figure out what i want to store in the database
	#here almost same code for the image table once i decided which format use to store them
	print c.lastrow()

conn.commit()

conn.close()
