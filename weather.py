#!/usr/bin/python
import urllib2
import os
from xml.dom import minidom
metric="1"
name = os.name

### CLEAR SCREEN
if name == 'posix':
	os.system('clear')
elif name == 'nt' or name == 'dos':
	os.system('cls')
else:
	print("\n" * 30)

while 1:
	mydata = raw_input('City to know weather condition: ')
	url = 'http://rss.accuweather.com/rss/liveweather_rss.asp?metric=' + metric + '&locCode=' + mydata
	#print 'Get web ' + url + '####'
	f = urllib2.urlopen(url)
	doc = minidom.parse(f)
	errors = doc.getElementsByTagName("description")[0]
	error = errors.firstChild.data
	#print error
	### IF ERROR 
	if error == 'Invalid Location':
		print "ERROR"
	else:
		name = doc.getElementsByTagName("title")[2]
		nameArray = name.firstChild.data.split(':')
		print "TODAY CONDITIONS: " + nameArray[1]
		print "TODAY TEMPERATURE: " + nameArray[2]
		description = doc.getElementsByTagName("description")[3]
		descriptionArray = description.firstChild.data.split('<')
		print "TOMORROW FORECAST: " + descriptionArray[0]
		print "\n"
	choice = raw_input("Press any key to CONTINUE or 'q' to QUIT")
	if choice == 'q':
		import sys
		exit(0)
	else:
		### CLEAR SCREEN
		if name == 'posix':
			os.system('clear')
		elif name == 'nt' or name == 'dos':
			os.system('cls')
		else:
			
			
			
			print("\n" * 30)