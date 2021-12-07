from interface import *
from arquivo import *
from time import sleep

arq = 'cursoEmVideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

def new_func(arq, nome, idade):
    cadastrar = (arq, nome, idade)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #  Opção de listar o conteúdo de um arquivo.
        cabecalho('opção 1')
        lerArquivo(arq)
    elif resposta == 2:
        #  Opção de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #  Opção sair do sistema.
        cabecalho('Saindo do Sistema... Até logo')
        break
    else:
        #  Digitou uma opção errada no menu.
        print('\033[31mErro digite uma opção válida!!!\033[m')
    sleep(1)
