"""
2. Classe Quadrado:Crie uma classe que modele um quadrado:
a.Atributos: Tamanho do lado;
b.Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""
class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    
    def mudaLado(self, valor):
        self.lado = valor

    
    def retornaLado(self):
        return self.lado


    def calculaArea(self):
        return self.lado * self.lado
        