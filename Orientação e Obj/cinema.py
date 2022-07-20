lugares = int(input("\nCINEMA VIDA NOVA \n\nDigite o total de lugares disponíveis: "))
posicao = ()

vetor = [posicao] * lugares
print (vetor)

while True:
    assento = int(input("\nEscolha seu assento: "))

    if (assento <= lugares):
        if (vetor [assento-1]) == "X":
            print ("Assento número", assento, "está ocupado. Escolha outro.")
   
        else:
           vetor [assento-1] = "X"
           print ("Assento número", assento, "reservado com sucesso.")
     
    else:
        print ("Esse assento não existe. Escolha um assento válido.")
    
    print (vetor)
  
    # Verificando se exitem assentos não marcados

    if not (() in vetor):
        print("\nTodos assentos estão ocupados.") 

        break
    