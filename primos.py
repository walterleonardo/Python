#numeros primos
for n in range(2,200):
    for x in range(2,n):
        if n % x == 0:
            print n , "equals" , x , "*" , n//x
            break
    else:
            ###LOOP
            print n, "es un numero primo"
