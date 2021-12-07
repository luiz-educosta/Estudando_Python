"""
Funções parte 2
 - Interative Help (Ajuda interativa)
    Usar uma função interna: help()
        * Ir no terminal, digitar python ou python3 e depois help().
        * Ou ir no em um arquivo .py, digitar help(função que deseja), ex.:help(print)
        * Pode usar print(input.__doc__)
 - Docstrings
    String de documentação.
        * Vide exemplo
 - Parâmetros opcionais
    Parâmetro que vc adiciona dentro de uma função para quando ela pode receber menos argumentos.
        * Vide exemplo
 - Escopo de variáveis 
    Local onde a variável vai existir e onde ela não vai existir
        * Vide exemplo
 - Retorno de resultados
    Funções em python pode ou não ter retorno através do return
        * Vide exemplo

"""
#  Exemplo de uma docstring
def contador(i, f, p):
    """
    -> Faz uma contagem e motra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Luiz Eduardo durante o Curso de Python
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')


#  contador(2, 10, 2)
#  help(contador)

#  Exemplo de um parâmetro opcional:
def somar(a, b, c = 0):       #  Nesse caso, c está sendo um parâmetro opcional, pois pode ou não ir  
    s = a + b + c             #  na função, toda essa função pode ser um parâmetro
    print(f'A soma vale {s}') #  opcional(a = 0, b = 0, c = 0)


somar(3, 2, 5)
somar(8, 2) 
# somar() caso (a = 0, b = 0, c = 0)

#  Exemplo de escôpo de variáveis
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')  #  Variável global
    print(f'Na função teste, x vale {x}')  #  Variável local


# Programa Principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
#  print(f'No programa principal, x vale {x}')  x tem um escopo local

#  Exemplo de escôpo de variáveis

def teste_global(y):
    global x  #  declarando variavel global
    x = 8
    y += 4
    z = 2
    print(f'X dentro vale {x}')
    print(f'Y dentro vale {y}')
    print(f'Z dentro vale {z}')


x = 5
teste_global(x)
print(f'X fora vale {x}')


#  Exemplo de retorno de valor
def soma(a = 0, b = 0, c = 0):         
    s = a + b + c             
    return s 


r1 = soma(3, 2, 5)
r2 = soma(2, 2)
r3 = soma(6)
print(f'Os resultados foram {r1}, {r2} e {r3}')

#  Parte prática

def fatorial (num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


print('Ver o fatorial do número')
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

def par (n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


print('Verificar se é par')
num = int(input('Digite um número:'))
if par(num):
    print('É par!')
else:
    print('Não é par!')