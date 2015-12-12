
list1=[]

for i in range(10):
		j=i**2
		list1.append(j)

print list1


list2= [x**2 for x in range(10)]


print list2


list3 = [x**2 for x in range(10) if x > 5]

print list3



set1 = {x**2 for x in range(10)}

print set1


dict1 = {x:x+1 for x in range(10)}

print dict1

