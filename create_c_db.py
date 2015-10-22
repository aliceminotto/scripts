#!/usr/bin/python
import sqlite3

conn=sqlite3.connect('maindb_pathgenomes.db')
print 'created database maindb_pathgenomes.db'

##################sobstitute m5-m8 with the right names, last table is not ok############################
conn.execute('''create table mutation_probabilities
	(id integer primary key autoincrement,
	hgt_Eff real not null,
	hgt_Tes real not null,
	Eff_mutation real not null,
	Tes_duplication real not null,
	m5 real not null,
	m6 real not null,
	m7 real not null,
	m8 real not null);''')
conn.execute('''create unique index prob
	on mutation_probabilities (hgt_Eff,hgt_Tes,Eff_mutation,Tes_duplication,m5,m6,m7,m8)
	''')
conn.execute('''create table inputs
	(id integer primary key autoincrement,
	NJumps int not null,
	DT int not null,
	Seed int not null);''')
#print '**' #checkpoint
conn.execute('''create table output
	(id_probabilities int,
	id_input int,
	Run int not null,
	C int not null,
	N int not null,
	output array,
	foreign key(id_probabilities) references mutation_probabilities(id),
	foreign key(id_input) references inputs(id));''')
#print '*'  #checkpoint
conn.execute('''create table plots
	(id_probabilities int,
	id_input int,
	figure blob,
	constraint pk_id primary key (id_probabilities,id_input),
	foreign key(id_probabilities) references mutation_probabilities(id),
	foreign key(id_input) references inputs(id));''')

conn.close()
