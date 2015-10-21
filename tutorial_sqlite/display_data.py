#!/usr/bin/python

import sqlite3

conn=sqlite3.connect('provadb.db')
print 'opened database'
cursor=conn.execute('select id,name, address, salary from company')
for row in cursor:
	print 'id: ',row[0]
	print 'name: ',row[1]
	print 'address: ',row[2]
	print 'salary: ',row[3]
	print

print 'operation done'
conn.close()
