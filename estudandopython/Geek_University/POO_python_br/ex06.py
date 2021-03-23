"""
6. Classe  TV:Faça  um  programa  que  simule  um  televisor  criando-o  como  um  objeto.  O  usuário  deve  ser  capaz  de  informar  o  número  do  canal  e  aumentar  ou  diminuir  o  volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas
"""

class TV:
    def __init__(self, canal = 1, volume = 20):
        self.__canal = canal
        self.__volume = volume

    @property
    def volume(self):
        return self.__volume

    
    @property
    def canal(self):
        return self.__canal

    
    def setVolume(self,setVolume):
        if setVolume > 100:
            print(f'O volume escolhido {setVolume} é maior que o volume máximo (100%)')
        elif setVolume < 0:
            print(f'O volume escolhido {setVolume} é menor que o volume minímo (0%)')
        else:
            self.__volume = setVolume
            

    def setCanal(self,setCanal):
        if setCanal > 30:
            print(f'O canal escolhido {setCanal} é maior que o canal máximo (30)')
        elif setCanal < 1:
            print(f'O canal escolhido {setCanal} é menor que o canal minímo (1)')
        else:
            self.__canal = setCanal


    def aumentaVolume(self):
        if self.__volume < 100:
            self.__volume += 10
        else:
            print('O volume já esta no limite máximo!')

    
    def diminuiVolume(self):
        if self.__volume > 0:
            self.__volume -= 10
        else:
            print('O volume já esta no limite minímo!')

    
    def aumentaCanal(self):
        if self.__canal < 30:
            self.__canal += 1
        else:
            print('Você já esta no último canal escolhido!')

    
    def diminuiCanal(self):
        if self.__canal > 1:
            self.__canal -= 1
        else:
            print('Você já esta no menor canal escolhido!')
