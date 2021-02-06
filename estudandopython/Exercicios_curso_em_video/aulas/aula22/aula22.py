"""
Módulos e Pacotes
Modularização: Ato de construir Módulos, foco em dividir um programa grande, aumentar a legibilidade e facilitar a manutenção.
Vantagens:
 - Organização do código
 - Facilidade na manutenção
 - Ocultação de código detalhado
 - reutilização em outros projetos

 Pacotes: Pasta que contém módulos. Apenas criar uma pasta com o nome desejado.
 Dentro de cada pasta de cada pacote, deve-se criar uma pasta com o nome __init__.py e na pasta principal também.

"""
from uteis import numeros

num = int(input('Digite um valor:'))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')