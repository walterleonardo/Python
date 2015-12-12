import mysqldbda as mdb


spl_host = "localhost"
sql_username = "python"
sqp_password = "python"
sql_database = "dbTestPython"

sql_connection = mdb.connect(sql_host, sql_username, sql_password, sql_database)

# print sql_connection

cursor = sql_connection.cursor()

cursor.execute("use NetMon")

#cursor.execute("create table FromPython (Column1 VARCHAR(10), Column2 INT(11), Column3 float(6,2))")

#cursor.execute("insert into FromPython (Column1, Column2, Column3) values("string",10, 123.4)")


cursor.execute("select * from FromPython")
output = cursor.fetchone()

print output




sql_connection.commit()
sql_connection.close()

