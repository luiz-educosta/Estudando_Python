"""
36. Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado
"""
valorCasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos nos de financiamento?'))
prestacao = valorCasa / (anos * 12)

print(f'Para pagar aa casa de R${valorCasa:.2f} em {anos} anos a prestaçã será de R${prestacao:.2f}.')

if prestacao <= 0.3 * salario:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')
