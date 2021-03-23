"""
Programação Orientada a Objetos - POO
- Atributos -> Representam as características do objeto. Ou seja, pelos atributos conseguimos representar computacionalmente os estados de um objeto. No caso da lâmpada, possívelmente poderiamos querer saber se a lâmpada é 110 ou 220, se ela é branca, amarela, vermelha ou outra cor, qual é a luminosidade dela e etc.

Atributos é divididos em 3 grupos:
    - Atributo de Instâncias;
    - Atributos de Classe;
    - Atributos Dinâmicos;

# Atributos de instância são atributos declarados dentro do método construtor.
    
OBS: Método construtor: É um método especial utilizado para a construção de objeto.

Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é público. Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado produto deve ser tratado como privado, ou seja, que deve ser acessado/utilizado somente dentro da propria classe, onde está desclarado, utiliza-se __ duplo underscore no início de seu nome.

Isso é conhecido também como Name Mangling.

self -> Objeto que está executando o método

#  Obs: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe.

user = Acesso('user@gmail.com', '123456')
print(user.email)
#  print(user.__senha)  #  AtributeError

#  temos acesso mas não deveriamos fazer este acesso
print(user._Acesso__senha)  #  (Name Mangling)

#Atributos de instância -> Ao criar instância/ objetos de uma classe, todas as instâncias terão atributos.

# dois objetos da classe Acesso
user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

user1.mostra_email()
user2.mostra_email()
"""

#  Classes com Atributo de Instância Público


class Lampada:
    #  __init__ -> metodo construtor
    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.limite = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


#  Atributo privado
class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    
    def mostra_senha(self):
        print(self.__senha)


    def mostra_email(self):
        print(self.email)

#  Atributos de Classe
p1 = Produto('Playstation 4', 'Video game', 2300)
p2 = Produto('Xbox s', 'Video game', 4500)
# Atributos de Classe, são atributos, claro, que são declarados diretamente na classe, ou seja, fora do construtor. Geralmente já inicializamos um valor, e este valor é compartilhado entre todas as instâncias da classe ter seus próprios valores como é o caso dos atributos de instância, com os atributos de classe todas as instâncias terão o mesmo valor para este atributo.