class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

class Terrestre(Animal):
    
    def __init__(self, nome, patas):
        super().__init__(nome)
        self.patas = patas

    def andar(self):
        return f'{self._Animal__nome} está andando.'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Aquatico(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'
    


class Pinguim(Terrestre, Aquatico):
    
    def __init__(self, nome, patas):
        super().__init__(nome,patas)

# Testando

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

gato = Terrestre('Shenna', 4)
print(gato.andar())
print(gato.cumprimentar())

tux = Pinguim('Jaspion', 2)
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar()) # Method Resolution Order - MRO

print(f'Tux é uma instancia de Pinguim? {isinstance(tux, Pinguim)}')
print(f'Tux é uma instancia de Aquatico? {isinstance(tux, Aquatico)}')
print(f'Tux é uma instancia de Terrestre? {isinstance(tux, Terrestre)}')
print(f'Tux é uma instancia de Animal? {isinstance(tux, Animal)}')
print(f'Tux é uma instancia de object? {isinstance(tux, object)}')