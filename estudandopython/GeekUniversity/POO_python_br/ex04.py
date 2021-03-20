"""
4. Classe Pessoa:Crie uma classe que modele uma pessoa:
a.Atributos: nome, idade, peso e altura;
b.Métodos: Envelhercer, engordar, emagrecer, crescer.Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    
    def envelhecer(self, anos):
        self.idade += anos

        if self.idade < 21:
            self.altura += 0.5 
        

    def engordar(self, peso):
        self.peso += peso


    def emagrecer(self, peso):
        self.peso -= peso


    def crescer(self, altura):
        self.altura += altura
        