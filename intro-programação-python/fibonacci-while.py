print ("-"*20)
print ("SEQUÊNCIA FIBONACCI")
print ("-"*20)

while True:

    numero = int(input("\nDigite a quantidade de números Fibonacci que você deseja ou digite 0 para encerrar: "))

    if numero ==0:
        break

    a1=0
    a2=1

    if numero==1:
        print (a1)

    else:
        contador = 3
        print (a1)
        print (a2)

        while contador <= numero:
           a3 = a1+a2
           print(a3)
           a1 = a2
           a2 = a3
           contador += 1
    
print ("\nProgama encerrado!")

