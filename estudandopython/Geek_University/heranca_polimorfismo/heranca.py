"""
7h46m
8h20m
"""

class Pessoa():

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de pessoa"""

    def __init__(self,nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionário herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'

cliente1 = Cliente('Luiz', 'Eduardo', '123.456.789-00', 4000)
# print(cliente1.nome_completo())

# print(cliente1.__dict__)

funcionario1 = Funcionario('Gabriel', 'Isaac', '987.654.321-00', 2482)
# print(funcionario1.nome_completo())

# print(funcionario1.__dict__)
print(cliente1.nome_completo())
print(funcionario1.nome_completo())