#  Criando uma classe
class Conta:
    #  __init__ método construtor
    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto ... {self}')
        self.__numero = numero  #  atributo privado
        self.__titular = titular  #  deixando encapsulado __titular "particular"
        self.__saldo = saldo
        self.__limite = limite
        
    #  todo que esta em def depois do construtor é métodos
    def extrato(self):
        print(f'Saldo {self.__saldo} do titular {self.__titular}')

    
    def deposita(self, valor):
        self.__saldo += valor

    #  metodo privado
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.saldo + self.limite
        return valor_a_sacar <= valor_disponivel_a_sacar


    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou o limite!') 

    
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    #  O @ indica que é propriedade
    @property  #  ou get
    def saldo(self):
        return self.__saldo

    #  ou @property
    def get_titular(self):
        return self.__titular

    @property  #  ou get_limite, cuidado ao usar
    def limite(self):
        return self.__limite


    @limite.setter  #  ou set_limite, cuidado ao utilizar
    def limite(self, limite):
        self.__limite = limite
    

    # metodos estáticos, pq são da classes
    @staticmethod
    def codigo_banco():
        return '001'


    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '101', 'Bradesco': '237'}

# instânciando seria ir no terminal, com a classe importada e digitar conta = Cota(..preenchendo com algo...)