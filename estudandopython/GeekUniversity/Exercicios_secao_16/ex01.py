"""
1. Crie uma classe para representar uma pessoa, com os atributos privados de nome, idade e altura. Crite os métodos públicos necessários para sets e gets e também um método para imprimir os dados de uma pessoa.
"""
class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura


    @property
    def nome(self):
        return self.__nome


    @property
    def idade(self):
        return self.__idade

    
    @property
    def altura(self):
        return self.__altura

    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    
    @altura.setter
    def altura(self, altura):
        self.__altura = altura


    def imprimeDados(self):
        print(self.__nome)
        print(self.__idade)
        print(self.__altura)