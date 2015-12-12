#!/usr/bin/python
import urllib

def check_connectivity(reference):
	try:
		urllib.request.urlopen(reference, timeout=2)
		return True
	except:
		return False

if check_connectivity("8.8.8.8"):
	ipaddresmysql="192.168.1.107"
else:
	ipaddresmysql="127.0.0.1"
	
	
print (ipaddresmysql)