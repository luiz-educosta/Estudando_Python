"""
13.Faça um algoritmo que leia o salário de um funcionário e
mostre seu novo salário, com 15% de aumento.
"""
salario = float(input('Qual é o salário do Funcionario? R$'))
aumento = salario * 1.15
print(f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a recever R${aumento:.2f}')
