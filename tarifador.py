def pcn_loop():
    hayMasDatos = "Si"
    while hayMasDatos == "Si":
        x = input("Ingrese un numero: ")
        if x > 0:
            print "Numero positivo"
        elif x == 0:
            print "Igual a 0"
        else:
            print "Numero negativo"
 
        hayMasDatos = raw_input("Quiere seguir? <Si-No>: ")
        
pcn_loop()