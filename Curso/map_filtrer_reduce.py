
def product10(a):
	return a*10
	
list1 = range(10)

print list1


print map(product10,list1)


print map((lambda a: a*10), list1)

print filter(lambda a: a>5, list1)

####REDUCE aplica la funciona primera a la lista segunda, y va por partes de 2
print reduce(lambda a,b: a+b, list1)

print sum(list1)
