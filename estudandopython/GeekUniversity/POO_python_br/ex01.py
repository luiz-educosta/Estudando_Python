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


    def trocaCor(self, cor):
        self.__cor = cor

    
    def mostraCor(self):
        return self.__cor


