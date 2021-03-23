"""
28. Faça a leitura de três valores e apresente como resultado
a soma dos quadrados dos três valores lidos.
"""
n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))
n3 = int(input('Digite o terceiro valor:'))
q1 = n1 * n1
q2 = n2 * n2
q3 = n3 * n3
soma = q1 + q2 + q3
print(f'A soma dos quadrados dos números {n1, n2, n3} é {soma}')


