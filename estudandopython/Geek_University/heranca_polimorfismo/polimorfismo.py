class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError(
            'A classe filha precisa implementar este método')

    def comer(self):
        print(f'{self.__nome} esta comendo ...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala wau wau')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau!')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala algo..')

# Testes


luiz = Cachorro('Luiz')
luiz.comer()
luiz.falar()

shenna = Gato('Shenna')
shenna.comer()
shenna.falar()


gaia = Rato('Gaia')
gaia.comer()
gaia.falar()
