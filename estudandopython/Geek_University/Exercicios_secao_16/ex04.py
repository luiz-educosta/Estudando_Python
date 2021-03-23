"""
4. Crie uma classe Televisão e uma classe ControleRemoto que pode controlar o volume e trocar os canais da televisão.
    * O controle de volume permite aumentar ou diminuir a potência do volume de som em uma unidade de cada vez;
    * O controle de canal também permite aumentar e diminuir o número do canal
    * Também devem existir métodos para consultar o valor do voume de som e o canal selecionado
"""
class Televisao:
    def __init__(self, nome, marca, modelo):
        self.__nome = nome
        self.__marca = marca
        self.__modelo = modelo

    
    @property
    def nome(self):
        return self.__nome

    
    @property
    def marca(self):
        return self.__marca


    @property
    def modelo(self):
        return self.__modelo


class ControleRemoto:
    def __init__(self, aumentaVolume, diminuiVolume, aumentaCanal, diminuiCanal):
        self.aumentaVolume = aumentaVolume
        self.diminuiVolume = diminuiVolume
        self.aumentaCanal = aumentaCanal
        self.diminuiCanal = diminuiCanal

    
    