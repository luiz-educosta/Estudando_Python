"""
Funções com parâmetro (de entrada)

"""

def soma(a, b):
    return a + b

def multiplica (num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(outra(4, 2, 'Luiz '))

# A diferença entre parâmetros e argumentos

# Parâmetros são variáveis declaras na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;


# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos
# utilizar qualquer ordem.

print(nome_completo(nome='Luiz', sobrenome='Rodrigues'))

print(nome_completo(sobrenome='Rodrigues', nome='Luiz'))
