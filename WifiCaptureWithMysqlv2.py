#!/usr/bin/python
# MYSQL CONFIG
from __future__ import print_function
from datetime import date, datetime, timedelta
import MySQLdb as mysql
import time
import re
import os
from subprocess import call
import commands
def getmac(iface):
	data = commands.getoutput("ifconfig ")
	words = data.split()
	found = 0
	for x in words:
		#print x
		if found != 0:
			mac = x
			break
		if x == "HWaddr":
			found = 1
	if len(mac) == 0:
		mac = 'Mac not found'
	mac = mac[:17]
	return mac


mac_address = getmac("wlan0")

def check_connectivity(reference):
	try:
		urllib.request.urlopen(reference, timeout=2)
		return True
	except urllib.request.URLError:
		return False

if check_connectivity("8.8.8.8"):
	ipaddresmysql="192.168.1.107"
else:
	ipaddresmysql="127.0.0.1"


wlaninterface="mon0"
#airmon-ng start $wlaninterface
time.sleep(5)
outputprefix="output"
sleeptime="30s"
maxclients="150"
print ("pepe")
#ssh = paramiko.SSHClient()
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect('192.168.1.108', 22, username='pi', password='telefonica123*')

#time.sleep(1)
#db = mysql.connect(host="192.168.1.103", user="python", passwd="python",db="wificounter")
#cursor = db.cursor()

#tomorrow = datetime.now().date() + timedelta(days=1)
#today = datetime.now().date()
completlocaltime = datetime.now().strftime('%y-%m-%d %H:%M:%S')
#localtime = datetime.now().strftime('%H:%M:%S')
month=datetime.now().strftime("%B")


conection = ("INSERT INTO wifidevices "
"(id, rasp, mac, power, ap, time, date, fecha, mes) "
"VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)")

while True:
		today = datetime.now().date()
		completlocaltime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		localtime = datetime.now().strftime('%H:%M:%S')
		db = mysql.connect(host=ipaddresmysql, user="python", passwd="python",db="wificounter")
		cursor = db.cursor()

		#call(["rm", " output*.csv &> /dev/null"])
		remove = os.popen("rm output*.csv &> /dev/null &")
		stream = os.popen("airodump-ng -w output --output-format csv mon0 &> /dev/null &")
		time.sleep(60)
		kill = os.popen("killall airodump-ng &> /dev/null &")
		createfile = os.popen("grep -A150 MAC output*.csv | awk '{print $1$6$8}' | sed -e '/Station/d' > list_of_station")

		#rm $outputfileprefix*.csv &> /dev/null
		#airodump-ng -w $outputprefix --output-format csv $wlaninterface  &> /dev/null &
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
		raw_data = open('list_of_station','r')
		print (raw_data)
		#time.sleep(5.5)
		#lineas = raw_data.splitlines()
		lineas = raw_data.readlines()
		lineas = filter(lambda x: not re.match(r'^\s*$', x), lineas)
		#print (lineas[1])
		for i in lineas:
				if i != " ":
						print (i)
						print ("------> Enviando a MYSQL")
						valores = i.split(",")
						data_wifi = (mac_address, valores[0], valores[1], valores[2], localtime, today, completlocaltime, month )
						cursor.execute(conection, data_wifi)

		# Insert new employee
		#cursorexecute(conection, data_wifi)
		#emp_no = cursor.lastrowid
		# Make sure data is committed to the database
		db.commit()
		cursor.close()
		db.close()