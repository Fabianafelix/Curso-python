#input -----> recebe dados do tipo string
#float -----> transforma o input em numeros inteiros

salario = float(input("\nDigite seu salário bruto: "))
if salario < 1903.98:
    print ("Isento de IR\n")

#Junção de Else+If

elif salario >= 1903.99 and salario <=2826.65:
    print ("A alíquota do seu IR é de: 7,5%")
    print ("O salário líquido a receber é de:", salario - (salario * 7.5/100 ),"\n\n")
    
elif salario >= 2826.66 and salario <=3751.05:
    print ("A alíquota do seu IR é de: 15%")
    print ("O salário líquido a receber é de:", salario - (salario * 15/100 ),"\n\n")   

elif salario >= 3751.06 and salario <=4664.68:
    print ("A alíquota do seu IR é de: 22,5%")
    print ("O salário líquido a receber é de:", salario - (salario * 22.5/100 ),"\n\n") 

elif salario > 4664.68:
    print ("A alíquota do seu IR é de: 27,5%")
    print ("O salário líquido a receber é de:", salario - (salario * 27.5/100 ),"\n\n") 