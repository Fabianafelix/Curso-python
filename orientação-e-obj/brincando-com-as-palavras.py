# 1 - Quantas palavras há no arquivo?
filename = "palavras.txt"
palavras = []

with open (filename, "r", encoding = "utf-8") as documento:  
    for linha in documento:
        palavras.append (linha.upper())
        
def numero_de_palavras (palavras):
    return len(palavras)

contador_de_palavras = numero_de_palavras (palavras)
print ("\n1 - Quantas palavras há no arquivo?")
print (f"Há {contador_de_palavras} palavras no português brasileiro")


# 2 - Quantas vezes cada letra do alfabeto aparece no arquivo?
def numero_letras (palavras):
    dicionario = {}

    for palavra in palavras:
        palavras = list(palavra)
        for letra in palavras:
            if letra not in dicionario:
                dicionario [letra] = 1    
            else:
                dicionario [letra] += 1
    return dicionario

contador_de_letras = numero_letras (palavras)
print ("\n2 - Quantas vezes cada letra do alfabeto aparece no arquivo?")
print ("O número de cada letra é:\n")
print(contador_de_letras)


# 3 - Quantas palavras começam com cada letra do alfabeto?
def palavras_por_letras (palavras):
    dicionario_palavras = {}
    for palavra_letra in palavras:
        if palavra_letra [0] not in dicionario_palavras:
            dicionario_palavras [palavra_letra [0]] = 1    
        else:
            dicionario_palavras [palavra_letra [0]] += 1
    return (dicionario_palavras)

contador_de_palavras_por_letra = palavras_por_letras (palavras)
print ("\n3  - Quantas palavras iniciada com cada letra do alfabeto?")
print ("O número de palavras por letra é:\n")
print(contador_de_palavras_por_letra)

# 4 - Quantas palavras começam com as mesmas 3 letras do meu nome?

def letra_nome (palavras):
    with open ("palavras_com_iniciais_fab.txt", "a", encoding = "utf-8") as lista_iniciais_fab:
        for palavra_letra in palavras:
            if "FAB"== palavra_letra[:3]:
                lista_iniciais_fab.write(palavra_letra)
                            
letra_nome (palavras)

# 5 - Quais palavras possuem todas as letras do meu nome.
def letras_nome (palavras):
    with open ("letras_do_meu_nome.txt", "a", encoding = "utf-8") as lista_letras_nome:
        for palavra_letra in palavras:
            if "FABIN" in palavra_letra:
                lista_letras_nome.write(palavra_letra)

letras_nome (palavras)