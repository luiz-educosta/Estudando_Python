"""
8. Classe Macaco:Desenvolva uma classe Macaco, que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir().Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
"""

class Macaco:
    
    def __init__(self, nome):
        self.__nome = nome
        self.estomago = []


    def comer(self, comida):
        self.estomago.append(comida)


    def verEstomago(self):
        print('O estomago do macaco contem:')
        for comida in self.estomago:
            print(comida)


    def digerir(self):
        if len(self.estomago) > 0:
            while len(self.estomago) > 0:
                self.verEstomago()
                
                pergunta = input('O macaco quer digerir alguma comida? [S/N]').split()
                
                if 'S' in pergunta[0].upper():
                    self.estomago.pop()

                else:
                    break

nome = input('Digite o nome para o seu macaco: ')
monkey = Macaco(nome)