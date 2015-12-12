mystr = "Hola como va todo tio Pepe y tia Laura"

import re

a = re.match("Hola", mystr)

print type(a)

print a.string
print a.group()


a = re.match("hola", mystr, re.I)

print type(a)

print a.string
print a.group()

###NO FUNCIONA SI LA PALABRA A BUSCAR ESTA EN MEDIO.
###PARA ESTO NECESITAMOS EL SEARCH

mystr = "Hola como va todo  You tio Pepe y tia Laura"
a = re.search("you", mystr, re.I)

print type(a)

print a.string
print a.group()


#### REGULAR EXPRESION

arp = "22.22.22.1   0     b4:c5:ff:fc:00:00 VLAN#22     L"
a = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*", arp)

print a.group(1)
print a.group(2)
print a.group(3)
print a.group(4)
print a.group(0)
### (.+?) cualquier caracter hasta el final
###  (\d) cualquier digito del 0 al 9 
### (.+?)\s{2,}(\w)* busca cualquier caracter hasta que existan mas de dos espacios y luego captura cualquier palabra o letras a-z A-Z o 0 a 9 

print re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp)

#### EN todos los casos busca lo mismo 3 digitos \d\d.\d{2}\.[0-9][0-9]\.[0-9]{1,3}

### SI QUEREMOS SEPARAR LAS IPS
print re.findall(r"(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})", arp)


b = re.sub(r"\d", "7", arp)

print b






