#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'user', 'user', 'data');

with con: 

    cur = con.cursor()
    cur.execute("SELECT * FROM info")

    rows = cur.fetchall()

    for row in rows:
        print row
  
#    for i in range(cur.rowcount):      
 #       row1 = cur.fetchone()
  #      print row1[0], row1[1]
  
  
with con:    

    cur = con.cursor()
        
    cur.execute("UPDATE info SET data1 = %s WHERE Id = %s",("22", "1"))        
    
    print "Number of rows updated:",  cur.rowcount