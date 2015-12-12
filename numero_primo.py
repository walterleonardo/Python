#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Números primos

def es_primo(num):
	if num < 2:     #si es menos que 2 no es primo, por lo tanto devolverá Falso
		return False
	for i in range(2, num/2):  #un rango desde el dos hasta el numero que nosotros elijamos
		print num
		print i
		print (num % i)  # % esto significa resto de la divicion 
		if (num % 2) == 0:
			print 'este numero es par'
		else:
			if (num % i) == 0:    #si el resto de la divicion da 0 no es primo, por lo tanto devuelve Falso
				return False
	return True    #de lo contrario devuelve Verdadero

print es_primo(30)    #para probarlo llamamos a la función