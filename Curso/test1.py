newfile = open("text.txt","w")
newfile.write("I LIKE PYTHON\n DO you?\n")
newfile.close()

newfile = open("text.txt","w")
newfile.writelines(["cisco", "juniper", "hp", "ibm", "\n"])
newfile.close()


newfile = open("text.txt","a")
newfile.writelines(["Nueva linea para apendizar \n"])
newfile.close()

newfile = open("text.txt","w+")
newfile.writelines(["Nueva linea para apendizar \n"])

newfile.seek(0)
print newfile.read()

newfile.read


newfile.close()
