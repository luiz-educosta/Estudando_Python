"""
44. Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros
"""
print('=' * 10, end='')
print(' Lojas Luiz ', end='')
print('=' * 10)
preco = float(input('Preço das compras: R$'))
print("""FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opcao = int(input('Qual é a opção: '))

if opcao == 1:
    novoPreco = preco * 0.9

elif opcao == 2:
    novoPreco = preco * 0.95

elif opcao == 3:
    novoPreco = preco
    parcelado = preco / 2
    print(
        f'Parcelando em 2x no cartão você terá 2 parcelas de R${parcelado:.2f}')
elif opcao == 4:
    opcao2 = int(input('Quantas parcelas? '))
    novoPreco = preco * 1.2
    parcelado = novoPreco / opcao2
    print(
        f'Sua compra será parcelada em {opcao2}x de R${parcelado:.2f} COM JUROS')
else:
    novoPreco = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print(f'Sua compra de R${preco:.2f} vai custar R${novoPreco:.2f} no final')
