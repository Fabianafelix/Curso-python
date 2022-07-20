print ("-"*20)
print("SEQUÊNCIA FIBONACCI")
print ("-"*20)

# Enquanto for vdd, este loop repetirá todo o programa
while True:

    numero = int(input("\nDigite a quantidade de números Fibonacci que você deseja ou digite 0 para encerrar: "))

# inicializando com os dois primeiros valores
    a1 = 0
    a2 = 1

# Caso o nº digitado seja = 0, o programa encerrará.
    if numero ==0:
        break

    if numero ==1:
        print(a1)

    else:
        numero >=1
        print(a1)
        print(a2)
        
 # Loop será executado enquanto numero for != 0
        for x in range (2,numero):
            a3=a1+a2
            a1=a2
            a2=a3
            print(a3)

print("\nProgama encerrado!")
    