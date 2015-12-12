myfile = open("file.txt","r")

#myfile.read()

#print myfile.read()
#print myfile.readline(10)

for lines in myfile.readlines():
	#print lines
	if lines.startswith("A"):
		print lines
		


	
