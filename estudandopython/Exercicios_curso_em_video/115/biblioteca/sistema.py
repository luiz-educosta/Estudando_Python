from interface import *
from time import sleep


while True:
        
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até logo')
        break
    else:
        print('\033[31mErro digite uma opção válida!!!\033[m')
    sleep(2)