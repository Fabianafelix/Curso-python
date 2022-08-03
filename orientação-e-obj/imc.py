def calcula_imc (peso, altura):
    imc=peso/(altura*altura)
    return imc

valor= calcula_imc (45,1.65)
print (f"o seu imc é {valor}")


valor= calcula_imc (50,1.60)
print ("o seu imc é {valor}")

valor= calcula_imc (55,2.60)
print (f"o seu imc é {valor}")
 