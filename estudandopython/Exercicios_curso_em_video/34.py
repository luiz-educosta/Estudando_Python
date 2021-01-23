"""
34. Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""
salario = int(input('Qual é o salário do funcionário? R$ '))
if salario <= 1250:
    salarioAtual = salario * 1.15
else:
    salarioAtual = salario * 1.1
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${salarioAtual:.2f} agora.')