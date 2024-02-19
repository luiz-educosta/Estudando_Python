class Lampada():

    def __init__(self, cor, voltagem, luminosidade) -> None:
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class Cliente():

    def __init__(self, nome, cpf) -> None:
        
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente é {self.__nome} diz oi')

class ContaCorrente():

    contador = 4999

    def __init__(self, limite, saldo, cliente) -> None:
        self.__numero = ContaCorrente.contador +1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')

class Usuario():

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


# Instâncias/Objetos

lamp1 = Lampada('Azul', 220, 70)

cliente1= Cliente("Luiz Eduardo", '123.456.789-00')

cc1 = ContaCorrente(3000, 1000, cliente1)

cc1.mostra_cliente()

cc1._ContaCorrente__cliente.diz()

user1 = Usuario('Luiz', 'Eduardo', 'luiz@gmail.com', '123456')