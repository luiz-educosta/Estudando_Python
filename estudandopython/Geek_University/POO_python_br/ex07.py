"""
7. Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
a.Atributos: Nome, Fome, Saúde e Idade
b.Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
c.Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquermomento.
"""

class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    
    def alterarNome(self, nome):
        self.nome = nome

    
    def alteraFome(self, fome):
        self.fome = fome


    def alteraSaude(self, saude):
        self.saude = saude


    def alteraIdade(self, idade):
        self.idade = idade


    def retornaNome(self):
        return self.nome

    
    def retornaFome(self):
        return self.fome

    
    def retornaSaude(self):
        return self.saude


    def retornaIdade(self):
        return self.idade


    def humor(self):
        return self.retornaFome() * self.retornaSaude()
