#!/usr/bin/python
import sqlite3
import pickle
import sys
import os

#creating a list of folders where there are the data to put in database
alf='qwertyuiopasdfghjklzxcvbnm.'
alf+=alf.upper()
lista_folder=[] #these are the DT folders
for folder in range(1,len(sys.argv)):
	lista_folder.append(sys.argv[folder])
#print lista_folder
diz_fj={} #diz with folders and number of jumps
lf=[]
for folder in lista_folder:
	ldrun=os.listdir(folder)
	#print 'ldrun',ldrun
	for f1 in ldrun: #folders in DT folder
		if f1[0:3]=='RUN': #considering just the folders created by the simulation
			ldn=os.listdir(folder+f1)
			#print 'ldn',ldn
			for f in os.listdir(folder+f1+'/'):
				if not f.startswith('.'):
					last=folder+f1+'/'+f
					#print 'last',last
					max_j=0
					for f2 in os.listdir(last):
						lf.append(last+'/'+f2)
						jump_n=int(f2.strip(alf))
						if jump_n>max_j:
							max_j=jump_n
					diz_fj[last]=max_j
						#print 'lf adding:', f2
#print lf #list of file to process to update the database
#print diz_fj

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
	if len(A)>12:
		DT=A[12] #DT
		Jumps=A[13] #number of jumps
		RunC=A[14] #folder (run and c) ['RUN4', 'n7', '3']
		RunC=[int(x.strip(alf)) for x in RunC]
	else:
		get_par=data.strip('/').split('/')
		DT=get_par[5][2:]
		try:
			int(DT)
		except ValueError:
			DT='inf'
		#print DT
		Jumps=diz_fj['/'+'/'.join(get_par[:-1])]
		#print Jumps
		RunC=[int(x.strip(alf)) for x in get_par[-3:]]
		#print RunCprova
	################finish here below##############################
	t_prob=(prob[1],prob[2],prob[3],prob[4],prob[5],prob[6],prob[7],prob[8])
	c.execute('''select * from mutation_probabilities
	where hgt_Eff=? and hgt_Tes=? and Eff_mutation=?
	and Tes_duplication=? and m5=? and m6=? and m7=? and m8=?
	;''', t_prob)
	result=c.fetchone()
	#print 'result68', result
	if result==None:
	    c.execute('''insert into mutation_probabilities
	    (hgt_Eff, hgt_Tes, Eff_mutation, Tes_duplication, m5, m6,m7,m8)
	    values (?,?,?,?,?,?,?,?)
	    ;''', t_prob)
	    #print t_prob
	    id_probabilities=c.lastrowid
	else:
	    id_probabilities=result[0]
	#print 'id_probabilities78', id_probabilities
	par=(Jumps,DT,seed)
	c.execute('''select * from inputs
	where NJumps=? and DT=? and Seed=?
	;''', par)
	result2=c.fetchone()
	#print 'result2_84',result2
	if result2==None:
	    c.execute('''insert into inputs
	    (NJumps, DT, Seed)
	    values(?,?,?)
	    ;''', par)
	    #print par
	    id_input=c.lastrowid
	else:
	    id_input=result2[0]
	#print 'id_input_94',id_input
	#print RunC[0],RunC[1],RunC[2]
	#print type(id_probabilities)
	c.execute('''insert into output
	(id_probabilities, id_input, Run, C, N, output)
	values (?,?,?,?,?,?)
	;''',(id_probabilities,id_input,RunC[0],RunC[1],RunC[2],data)) #fix this line, figure out what i want to store in the database
	#here almost same code for the image table once i decided which format use to store them
	c.execute('''select max(id_input) from output''')
	#print c.fetchone()
conn.commit()

conn.close()
