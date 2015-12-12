#!/usr/bin/python
# MYSQL CONFIG
from __future__ import print_function
from datetime import date, datetime, timedelta
import MySQLdb as mysql
import time
import re

wlaninterface="mon0"
#airmon-ng start $wlaninterface
outputprefix="output"
sleeptime="30s"
maxclients="150"

#ssh = paramiko.SSHClient()
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect('192.168.1.108', 22, username='pi', password='telefonica123*')



time.sleep(1)

db = mysql.connect(host="192.168.1.103", user="python", passwd="python",db="PYTHONDB")
cursor = db.cursor()

tomorrow = datetime.now().date() + timedelta(days=1)
today = datetime.now().date()
completlocaltime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
localtime = datetime.now().strftime('%H:%M:%S')

conection = ("INSERT INTO moviles "
"(id, mac, power, ap, time, date) "
"VALUES (NULL, %s, %s, %s, %s, %s)")
data_wifi = ('AA:BB:CC:DD:EE:EE', tomorrow, date(1977, 6, 14))

raw_data2 = '''\
C8:B5:B7:2A:55:EB,-127,4C:09:D4:3F:F1:90,
F8:1A:67:22:4A:31,-127,4C:09:D4:3F:F1:90,
54:72:4F:20:FD:61,-127,4C:09:D4:3F:F1:90,
F8:E0:79:DE:DC:3D,-80,(not
BC:8C:CD:71:8F:D6,-127,4C:09:D4:3F:F1:90,
BC:8C:CD:71:90:1C,-127,4C:09:D4:3F:F1:90,
00:25:22:43:6A:DC,0,4C:09:D4:3F:F1:90,
B4:18:D1:E2:C9:F4,-1,4C:09:D4:3F:F1:90,
54:72:4F:4E:E7:2E,-72,4C:09:D4:3F:F1:90,
E0:F5:C6:00:F3:19,-1,4C:09:D4:3F:F1:90,
'''
lineas = raw_data2.splitlines()
print (lineas[1])

for i in lineas:
	print (i)
	valores = i.split(",")
	data_wifi = (valores[0], valores[1], valores[2], today, localtime)
	cursor.execute(conection, data_wifi)	

# Insert new employee
#cursor.execute(conection, data_wifi)
emp_no = cursor.lastrowid
# Make sure data is committed to the database
db.commit()

cursor.close()
db.close()