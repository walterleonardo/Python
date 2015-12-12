#!/usr/bin/python
import urllib2
import os
from xml.dom import minidom
metric="1"
name = os.name


if name == 'posix':
	os.system('clear')
elif name == 'nt' or name == 'dos':
	os.system('cls')
else:
	print("\n" * 30)

while 1:
	mydata = raw_input('City to know weather condition:')
	url = 'http://rss.accuweather.com/rss/liveweather_rss.asp?metric=' + metric + '&locCode=' + mydata
	#print 'Get web ' + url + '####'
	f = urllib2.urlopen(url)
	doc = minidom.parse(f)
	errors = doc.getElementsByTagName("description")[0]
	error = errors.firstChild.data
	#print error
	if error == 'Invalid Location':
		print "ERROR"
	else:
		name = doc.getElementsByTagName("title")[2]
		print name.firstChild.data
    #	f.close()
	raw_input("Press any Key to request again")
	if name == 'posix':
		os.system('clear')
	elif name == 'nt' or name == 'dos':
		os.system('cls')
	else:
		print("\n" * 30)