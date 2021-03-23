"""
2. Classe Quadrado:Crie uma classe que modele um quadrado:
a.Atributos: Tamanho do lado;
b.Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""
class Quadrado:
    def __init__(self, lado):
        self.__lado = lado


    @property
    def lado(self):
        return print(f'O quadrado encontra-se com a medida de {self.__lado}')


    @lado.setter
    def lado(self, valor):
        self.__lado = valor
        print(f'Valor do lado mudou para {self.__lado}')


    def calculaArea(self):
        area =  self.__lado * self.__lado
        return print(f'Calculando a área do quadrado {self.__lado} x {self.__lado} = {area}')
         

q = Quadrado(5)
q.calculaArea()
q.lado
q.lado = 10