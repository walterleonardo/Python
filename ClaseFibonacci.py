def fib(n):
    print "fibonacci"
    a,b=0,1
    while a<n:
        print (a, end=' ')
        a,b = b, a+b
    print()
    
#call clases
fib(200)    
    