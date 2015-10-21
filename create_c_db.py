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
conn.execute('''create table inputs
	(id integer primary key autoincrement,
	NJumps int not null,
	DT int not null,
	Seed int not null);''')
conn.execute('''create table output
	(id_probabilities int not null,
	id_input int not null,
	Run int not null,
	C int not null,
	N int not null,
	output array);''')
conn.execute('''create table plots
	(id_probabilities int not null,
	id_input int not null,
	figure blob,
	constraint pk_id primary key (id_probabilities,id_input));''')

conn.close()
