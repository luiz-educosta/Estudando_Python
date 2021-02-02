""" 
Funções parte 1

Funções estão ligados a: Rotina, coisa que faz constantemente
no python o nome da função é "def"
todas as funções são identificadas por parentesees no final do nome

**  funções sem parâmetro   **
def mostralinha():

**  Funções com parâmetro   **
def mostralinha(msg):


'*' desempacotar, vai passar varios parâmetros

para o python, toda passagem de parâmetro é por referência, diferente de C e java que é por valor.
"""
def mostralinha(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


mostralinha('FUNÇÃO')

def soma(a,b):
    s = a + b
    print(s)


#  Programa principal
soma(4, 5)  #  soma(a = 4, b = 5) ou soma(b = 5, a = 4)
soma(8, 9)
soma(2, 1)
#  soma(4) e soma(4, 3, 9) vai dar erro pq precisa de dois parâmetros


def contador(*num):
    print('for')
    for valor in num:
        print(valor, end=' ')
    print('FIM!')
    print('len')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1


valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)
 

#desempacotamento
def soma(*val):
    s = 0
    for num in val:
        s += num
    print(f'Somando os valores {val} temos {s}')



soma(5, 2)
soma(2, 9, 4)