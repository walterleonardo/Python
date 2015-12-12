#!/usr/bin/python
# MYSQL CONFIG
from __future__ import print_function
from datetime import date, datetime, timedelta
import MySQLdb as mysql
#import mysql.connector
#import paramiko
import time
import re

#ssh = paramiko.SSHClient()
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect('192.168.1.108', 22, username='pi', password='telefonica123*')

time.sleep(1)

db = mysql.connect(host="192.168.1.103", 
							user="python", 
							passwd="python",
							db="PYTHONDB")
cursor = db.cursor()

tomorrow = datetime.now().date() + timedelta(days=1)

add_employee = ("INSERT INTO moviles "
"(id, mac, time, date) "
"VALUES (NULL, %s, %s, %s)")
data_employee = ('AA:BB:CC:DD:EE:EE', tomorrow, date(1977, 6, 14))

# sum some data of a csv file
raw_data = '''\
Station Name,Lat,Long,Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec
Test 1,45.125478,-105.623154,3.12,0.15,0.08,0.61,0.67,1.24,2.32,1.06,0.64,0.07,0.32,1.02
Test 2,42.854123,-106.321587,0.09,3.15,1.61,0.03,0.84,1.62,3.01,1.51,0.81,0.02,0.23,1.09
Test 3,43.974532,-105.896214,2.65,2.01,0.05,3.02,1.05,0.08,0.08,1.06,0.43,0.65,0.12,1.06
'''

raw_data2 = '''\
BSSID, First time seen, Last time seen, channel, Speed, Privacy, Cipher, Authentication, Power, # beacons, # IV, LAN IP, ID-length, ESSID, Key
4C:09:D4:3F:F1:90, 2015-06-13 00:02:41, 2015-06-13 00:03:50,  5,  54, WPA2WPA , CCMP TKIP,PSK, -101,      526,     2292, 192.168.  1.117,   5, Walii,
D0:AE:EC:F9:65:3C, 2015-06-13 00:03:04, 2015-06-13 00:03:28,  6,  54, WPA , CCMP TKIP,PSK, -87,        4,        0,   0.  0.  0.  0,   9, WLAN_653C,
F8:8E:85:5F:88:CF, 2015-06-13 00:02:41, 2015-06-13 00:03:45,  5,  54, WPA , CCMP TKIP,PSK, -86,       11,        3,   0.  0.  0.  0,  13, MOVISTAR_88CE,
F8:1A:67:21:A3:52, 2015-06-13 00:02:42, 2015-06-13 00:03:47,  1,  54, OPN ,       ,   , -54,       63,        0,   0.  0.  0.  0,  18, NOMBRE DE COMERCIO,

Station MAC, First time seen, Last time seen, Power, # packets, BSSID, Probed ESSIDs
BC:8C:CD:71:8F:D6, 2015-06-13 00:02:41, 2015-06-13 00:03:49, -127,       33, 4C:09:D4:3F:F1:90,
BC:8C:CD:71:90:1C, 2015-06-13 00:02:41, 2015-06-13 00:03:50, -127,       37, 4C:09:D4:3F:F1:90,
D8:A2:5E:95:54:B8, 2015-06-13 00:02:53, 2015-06-13 00:02:55, -127,       57, 4C:09:D4:3F:F1:90,
00:19:7D:D4:8F:CD, 2015-06-13 00:02:42, 2015-06-13 00:03:43, -82,       26, (not associated) , MOVISTAR_CB7B
C8:B5:B7:2A:55:EB, 2015-06-13 00:02:46, 2015-06-13 00:02:46, -72,        3, 4C:09:D4:3F:F1:90,
54:72:4F:20:FD:61, 2015-06-13 00:03:12, 2015-06-13 00:03:46, -56,       90, 4C:09:D4:3F:F1:90,
00:25:22:43:6A:DC, 2015-06-13 00:02:41, 2015-06-13 00:03:50,   0,     2172, 4C:09:D4:3F:F1:90,

'''
# separo en partes
sentences = re.split(r' *["Station MAC"][\'"\)\]]* *', raw_data2)

for stuff in sentences:
	print ("########### NUEVA SENTENCIA ##########")
	print(stuff)  
# create the test data file
fname = "output_test.txt"
with open(fname, "w") as fout:
	fout.write(raw_data2)
# read the data file
data_list = []
for line in open(fname):
	# remove trailing newline char
	line = line.rstrip()
	# create a list
	line_list = line.split(',')
	data_list.append(line_list)
# create a months dictionary with month:index pairs
mdict = {}
for ix, item in enumerate(data_list[0]):
	print(ix, item)  # test
	if ix > 2:
		mdict[item] = ix
print(mdict)  # test
print('-'*70)
month_start = 'Station MAC'
month_end = 'Probed ESSIDs'
new_list = []
for item in data_list[1:]:
	#print(item) # test
	station = item[0]
	lat = item[1]
	long = item[2]
	start = mdict[month_start]
	end = mdict[month_end]+1
	plist = [float(x) for x in item[start : end]]
	print(plist) # test
	mysum = sum(plist)
	new_list.append([station, lat, long, mysum])
print('-'*70)
print("Result:")
for item in new_list:
	print(item)
	
# Insert new employee
cursor.execute(add_employee, data_employee)
emp_no = cursor.lastrowid
# Make sure data is committed to the database
db.commit()

cursor.close()
db.close()