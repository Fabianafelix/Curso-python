# Criar uma classe chamada "MarvelViloes" onde terão os atributos nome(str), poderes(list), perigo(int).

class MarvelViloes:
    def __init__ (self, nome, poderes, perigo):
        nome = nome
        self.poder = poderes
        self.perigo = perigo

    def get_nome (self):
        return self.nome

    def set_nome (self, nome):
       self.nome = nome

    def get_poderes (self):
        return self.poderes

    def set_poderes (self, poderes):
       self.poderes = poderes
       
    def get_perigo (self):
        return self.perigo

# O atributo perigo deve receber valores somente entre 0 a 5.

    def set_perigo (self, perigo):
        if (perigo >= 0 and perigo >=5):
            self.poderes = perigo

    def dominarOMundo (self):
        if self.perigo <= 2:
            return "Vilão morto"               # Para perigo de menor ou igual a 2 retornar "Vilão Morto"
        if self.perigo > 2 and self.perigo <5:
            return "Vilão preso"               # Para perigo maior que 2 e menor que 5 retornar "Vilão Preso""
        if self.perigo == 5:
            return "Vilão Dominou o Mundo"     # Para perigo igual a 5 retornar "Vilão Dominou o Mundo"

    

