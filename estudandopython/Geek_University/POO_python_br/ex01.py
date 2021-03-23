"""
1. Classe Bola:Crie uma classe que modele uma bola:
a.Atributos: Cor, circunferência, material;
b.Métodos: trocaCor e mostraCor.
"""
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material


    @property
    def cor(self):
        return self.__cor


    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    

bola = Bola('branco',4 ,'plastico')
bola.cor = 'roxo'  # Usando o Setter
print(bola.cor)  # Usando o getter
