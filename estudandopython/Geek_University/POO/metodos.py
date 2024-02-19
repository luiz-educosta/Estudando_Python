class Lampada():

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente():

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto():

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100
    


class Usuario():

    contador = 0

    @classmethod #TODO estudar sobre decorator
    def conta_usuario(cls): # cls é convenção para ser utilizada da classe.
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema')

    @staticmethod
    def definicao():
        return 'URLXP8'
    
    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self): # metodos publicos
        return f'{self.__nome} {self.__sobrenome}'
    

    def __gera_usuario(self): # metodos privados
        return self.__email.split('@')[0]
    


ps1 = Produto('Playstation 4', 'Video Game', 2300)

# print(ps1.desconto(50))

user1 = Usuario('Luiz', 'Costa', 'luiz@gmail.com', '1234')
print(user1.nome_completo())
# Outra forma
# print(Produto.desconto(ps1, 40)) # self, desconto

Usuario.conta_usuario() # Forma correta
user1.conta_usuario()   # Possível, mas incorreta

"""
8h13m
8h45m
"""