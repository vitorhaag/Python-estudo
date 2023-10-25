from meus_menu import *
from arquivo import *

lsta = ['Ver pessoas cadastradas', 'cadastrar pessoa', 'sair do programa']

arq = 'cursoemvideo.txt'

if not arq_existe(arq):
    criar_arq(arq)
   
while True:
    
    resp = menu_(lsta)
    if resp == 1:
        print('Opção 1 ')
        ler_arq(arq)
    elif resp == 2:
        print('opção 2')
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        pesso = [nome, idade]
        cadastrar(arq, pesso)
    elif resp == 3:
        print('opção 3')
        break
    else:
        print('ERRO! DIGITE UMA OPÇÃO VÁLIDA')

