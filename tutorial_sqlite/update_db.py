#!/usr/bin/python

import sqlite3

conn=sqlite3.connect('provadb.db')
print 'opened database'
conn.execute('update company set salary=25000.0 where id=1;')
conn.commit
print 'total number of changes: ', conn.total_changes

cursor=conn.execute('select * from company')
for row in cursor:
	print 'id: ', row[0]
	print 'name: ', row[1]
	print 'address: ',row[3]
	print 'salary: ',row[4]
	print

print 'operation done'
conn.close()
