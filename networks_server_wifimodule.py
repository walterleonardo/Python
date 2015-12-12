#!/usr/bin/python
# -*- coding: utf-8 -*-
#from __future__ import print_function
from datetime import date, datetime, timedelta
import MySQLdb
import SocketServer
from socket import *
import thread
#import mysql.connector
#from mysql.connector.constants import ClientFlag
import sys
#sys.path.insert(0, 'python{0}/'.format(sys.version_info[0]))
import re
#import random
#from random import randint
import signal

#PROG = re.compile('([A-Z]\d+)+')
PROG = re.compile(r'^(\d{1,3})\D*(\d{1,3})\D*(\d{1,3})\D*(\d{1,3})\D*(\d{1,3})$')
HOST = "192.168.1.108"
PORT = 9999
BUFF = 1024
#MODULE = 12
#RANDO = randint(2,9)

#TOMORROW = datetime.now().date() + timedelta(days=1)
#TODAY = datetime.now().date()

add_data = ("INSERT INTO modules (module, sensor1, sensor2, sensor3, sensor4) VALUES (%s, %s, %s, %s, %s)")
update_data = ("UPDATE modules SET sensor1=%s, sensor2=%s, sensor3=%s, sensor4=%s WHERE module=%s")
replace_data = ("REPLACE INTO modules (module, sensor1, sensor2, sensor3, sensor4) VALUES (%s, %s, %s, %s, %s)")
select_data = ("SELECT * FROM digitalout WHERE module = %s")
insertnew_data = ("INSERT INTO digitalout (module, out1, out2, out3, out4) VALUES (%s,'0','0','0','0')")
#data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))
#data_value = (MODULE,randint(200,900),randint(200,900),randint(200,900),randint(200,900))


db = MySQLdb.connect(
	host = '127.0.0.1',
	user = 'rf24',
	passwd = 'rf24',
	db = 'rf24',
	port = 3306)

cursor = db.cursor()

def signal_handler(signal, frame):
		print('You pressed Ctrl+C!')
		sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit')
print('SERVER IS RUNNING')
#signal.pause()

def handler(clientsock,addr):
	while 1:
		data = clientsock.recv(BUFF)
		if not data: break
		print repr(addr) + ' recv:' + repr(data)
		#print data
		if PROG.match(data):
				#print 'MATCH'
				INFO = data.split(',')
				#print INFO[0]
				module = INFO[0]
				print "REQUEST fron {} with module: %s".format(addr) %(INFO[0])
				#cursor.execute(add_data, data_value)
				# Execute the SQL command
				cursor.execute("SELECT * FROM digitalout WHERE module = '%s'" % (module))
				rows_affected=cursor.rowcount
				print "CANTIDAD DE RESULTADOS %d" %(rows_affected)
				if rows_affected == 1:
				#print "READ MODULE %s" %(INFO[0])
						cursor.execute(select_data,INFO[0])
						results = cursor.fetchall()
						for row in results:
								module = row[0]
								out1 = row[1]
								out2 = row[2]
								out3 = row[3]
								out4 = row[4]
				else:
						#print "REQUEST fron {} with module: %s".format(self.client_address[0]) %(INFO[0])
						print "NEW MODULE... CREATING NEW DATA for MODULE %s" %(INFO[0])
						cursor.execute(insertnew_data,INFO[0])
						out1 = 0
						out2 = 0
						out3 = 0
						out4 = 0

				data_value = (INFO[0],INFO[1],INFO[2],INFO[3],INFO[4])
				cursor.execute(add_data, data_value)
				db.commit()
				resultado = '%s,%s,%s,%s,%s,*' %(INFO[0], out1, out2, out3, out4 )
				#self.request.sendall(resultado)
				clientsock.send(resultado)
				print repr(addr) + ' sent:' + resultado
				#print resultado;
		else:
				print 'NOT REDEABLE DATA...'
				#resultado = "NO REDEABLE DATA..."
				#self.request.sendall(resultado)
				clientsock.send("*")
				print repr(addr) + ' sent:' + repr("*")

		# just send back the same data, but upper-cased
		#self.request.sendall(self.data.upper())
		#self.request.sendall()
		print "################"

		#clientsock.send(respuesta)
		#print repr(addr) + ' sent:' + repr(resultado)
		if "close" == data.rstrip(): break # type 'close' on client console to close connection from the server side

	clientsock.close()
	print addr, "- closed connection" #log on console

if __name__=='__main__':
	ADDR = (HOST, PORT)
	serversock = socket(AF_INET, SOCK_STREAM)
	serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	serversock.bind(ADDR)
	serversock.listen(5)
	while 1:
		print 'waiting for connection... listening on port', PORT
		clientsock, addr = serversock.accept()
		print '...connected from:', addr
		thread.start_new_thread(handler, (clientsock, addr))

cursor.close()
db.close()       