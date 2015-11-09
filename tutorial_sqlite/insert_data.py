#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('provadb.db')
print "Opened database successfully";

prova=9

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (5, 'Paul', 32, 'California', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (6, 'Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (7, 'Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (8, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.execute("insert into company (id, name, age, address, salary) \
	values (prova,'anna',42,'texas',10.0)");

conn.commit()
print "Records created successfully";
conn.close()

