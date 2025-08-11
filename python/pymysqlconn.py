import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="",database="classicmodels")
print("connection created")

# cur=conn.cursor()
# cur.execute("show databases")
# for i in cur:
#     print(i)
    
# fetchall(),fetchone(),fetchmany()
# print(cur.fetchall())
# print(cur.fetchone())
# print(cur.fetchmany(2))
cur=conn.cursor()
# cur.execute("show tables")
# print(cur.fetchall())
# cur=conn.cursor()
# cur.execute("create table testtable(id int,name varchar(20))")
# print(cur.fetchall())
# cur.execute("insert into testtable values(1,'a')")
# conn.commit()

# cur.execute("insert into testtable values(%s,%s)",(2,'b'))
# conn.commit()

# values=[(3,'c'),(4,'d')]
# cur.executemany("insert into testtable values(%s,%s)",values)
# conn.commit()

# cur.execute("delete from testtable where id=4")
# conn.commit()

cur.execute("update testtable set name='cc' where id=3")
conn.commit()

cur.execute("select * from testtable")
print(cur.fetchall())

conn.close()