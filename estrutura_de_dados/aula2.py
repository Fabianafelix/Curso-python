# Implementar a classe de vetores não ordenados

from traceback import print_tb


class VetorNaoOrdenado:
    def __init__ (self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.vetores = self.capacidade * [0] # diferente de []

    def imprime (self):
        if self.ultima_posicao == -1:
            print ("O vetor está vazio")
        else: 
            for i in range (self.ultima_posicao + 1):
                print (i, '-', self.valores [i])

    def insere (self, valor):
        self.ultima_posicao = self.capacidade + 1
        self.valores[self.ultima_posicao] = valor
    
    def pesquisa (self, valor):
        for i in range (self.ultima_posicao + 1):
            if self.valores [i] == valor:
                 return i

    def excluir (self, valor):
        posicao = self.pesquisa (valor)
        if posicao == -1:
            return -1
        else:
            for i in range (posicao, self.ultima_posicao):
                self. valores[i] = self.valores [i + 1]
                self.ultima_posicao = self.ultima_posicao - 1


vetor = VetorNaoOrdenado (8)
vetor.imprime

vetor.insere (4)
vetor.insere (2)
print ("Inseri 4 e 2")
vetor.imprime ()
vetor.insere (1)
print ("Inseri 1")
vetor.imprime ()