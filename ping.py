#!/usr/bin/python

import urllib2

def internet_on():
	try:
		response=urllib2.urlopen('http://walii.es',timeout=5)
		return True
	except urllib2.URLError as err: pass
	return False
	
print internet_on()