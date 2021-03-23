"""
3. Classe Retangulo:Crie uma classe que modele um retangulo:
a.Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher);
b.Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
c.Crie  um  programa  que  utilize  esta  classe.  Ele  deve  pedir  ao  usuário  que  informe  as  medidades  de  um  local.  Depois,  deve  criar  um  objeto  com  as  medidas  e  calcular  a quantidade de pisos e de rodapés necessárias para o local.
"""
class Retangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura


    @property
    def base(self):
        return self.__base

    
    @property
    def altura(self):
        return self.__altura


    @base.setter
    def base(self, base):
        self.__base = base

    
    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    
    def area(self):
        return self.__base * self.__altura

    
    def perimetro(self):
        return (2 * self.__base) + (2 * self.__altura)

    
bas = float(input('Digite o tamanho da base: '))
alt = float(input('Digite o tamanho da altura: '))

ret = Retangulo(bas, alt)
print(f'A área do retangulo é: {ret.area()}')
print(f'O perimetro do retangulo é: {ret.perimetro()}')
