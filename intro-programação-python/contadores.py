cont=1
acumulador=1

while cont < 10:
    print (cont, acumulador)
    cont +=1
    acumulador = acumulador + cont

# =======================================================================================================

while cont < 10:
    print (cont, acumulador)

    if cont > 5: 
        break

    acumulador = acumulador + cont   
    cont += 1

else: # qdo o while for False entrará em else: Caso o programa pare em if, não executara esse ele, pois ainda é True.
    print ("contador é maior q 10")

print ("fim")
    # qdo encerrar o codigo esse codigo sera impresso.

# ==================================================================================================================
cont2=10

while cont2 > 0:
    print (cont)
    cont -=1

# =====================================================================================================================

for x in range (20,0,-4):
    print (x)
