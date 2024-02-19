def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2)) # Por padrão eleve ao quadrado
print(exponencial(3, 5)) # Eleva á potência informada pelo usuário

# OBS: Em funções python, os parâmetro com valores default DEVEM sempre estar ao final da declaração


# Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))


"""
Por quê utilizar parâmetros com valor default?

- Nos permite ser mais flexíveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código


"""


"""
Quais tipos de dados podemos utilizar como valores default para parâmetros?

- Qualquer tipo de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc;
"""

# Exemplos
def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

# escopo - Evitar problemas e confusões

# ATENÇÃO COM VARIÁVEIS GLOBAIS (SE PUDER EVITAR, EVITE!)

total = 0

def incrementa():
    global total # Avisando que queremos utilizar a variável global

    total = total + 1
    return total

print(incrementa())