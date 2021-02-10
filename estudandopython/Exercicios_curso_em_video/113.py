"""
113. Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue  #  Joga pro while dnv
        except(KeyboardInterrupt):
            print('\n\033[31mO usuário preferiu não digitar esse número!\033[m')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except(ValueError,TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mO usuário preferiu não digitar esse número!\033[m')
            return 0
        else:
            return num


#  Programa principal
i = leiaInt('Digite um número Inteiro: ')
f = leiaFloat('Digite um número Real:')
print(f'O valor inteiro digitado foi {i} e o real foi {f}')
