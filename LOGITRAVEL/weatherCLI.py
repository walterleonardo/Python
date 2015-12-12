#!/usr/bin/python
### WE NEED URLLIB to get the XML from Accuweather
import urllib2
### WE NEED xml.dom to parse data from XML
from xml.dom import minidom
### WE NEED sys to get the var from outside
from sys import argv as s

###Should be 0 or 1; 0 for F, 1 for C
metric="1"

###Only run if exist a variable to check
if len(s) > 1:
	mydata = s[1]
	url = 'http://rss.accuweather.com/rss/liveweather_rss.asp?metric=' + metric + '&locCode=' + mydata
	### BY DEBUG UNCOMMENT THE NEXT LINE
	#print 'Get web ' + url + '####'
	f = urllib2.urlopen(url)
	doc = minidom.parse(f)
	errors = doc.getElementsByTagName("description")[0]
	error = errors.firstChild.data
	### BY DEBUG UNCOMMENT THE NEXT LINE
	#print error
	### IF ERROR 
	if error == 'Invalid Location':
		print "ERROR"
		print "VALUE NOT FOUND"
		print "PLEASE TRY AGAIN"
	else:
		title = doc.getElementsByTagName("title")[0]
		titleArray = title.firstChild.data.split('-')
		print "SITE: " + titleArray[0]
		name = doc.getElementsByTagName("title")[2]
		nameArray = name.firstChild.data.split(':')
		print "TODAY CONDITIONS: " + nameArray[1]
		print "TODAY TEMPERATURE: " + nameArray[2]
		description = doc.getElementsByTagName("description")[3]
		descriptionArray = description.firstChild.data.split('<')
		print "TOMORROW FORECAST: " + descriptionArray[0]
		print "\n"
else:
	print "PLEASE INCLUDE VALUE"
	print "By example:"
	print "MADRID"
	print "BARCELONA"
	print "PALMA"
	