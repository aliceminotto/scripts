#!/usr/bin/python
import sqlite3
conn=sqlite3.connect('provadb.db')
print 'opened database'
conn.execute('''drop table company;''')
print 'deleted table company'
conn.close()

