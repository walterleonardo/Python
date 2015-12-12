a = lambda x, y: x*y

print a



print a(2,9)



def myfunc(list):
	prod_list=[]
	for x in range(10):
		for y in range(5):
			product = x*y 
			prod_list.append(product)
	return prod_list + list

print myfunc([100,102,103])


b = lambda list: [x*y for x in range(10) for y in range(5) + list]

print b([100,102,103])


n=10
mylambda = lambda m,n: m*n/2

print mylambda(22,4)

