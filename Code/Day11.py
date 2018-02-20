# Database:-
# SQl- Mysql,Sqlite,Oracle
# NoSql- MongoDb,Cassandra
# sqlite3->MySql
# pip install --package

import sqlite3
con = sqlite3.connect('test.db')
# con.execute('''drop table EMP''')
con.execute('''	CREATE TABLE IF NOT EXISTS EMP
		(ID INT PRIMARY KEY NOT NULL,
		NAME TEXT NOT NULL,
		AGE INT NOT NULL);''')
con.commit()
con.execute('''INSERT into EMP(ID,NAME,AGE) values(3,"ABC",10)''')
con.execute('''INSERT into EMP(ID,NAME,AGE) values(4,"DEF",20)''')
con.commit()
cursor = con.execute('''SELECT * FROM EMP''')  # RETURNS CURSOR OBJECT
for row in cursor:
    print(row)
con.commit()
con.close()
