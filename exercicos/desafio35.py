# aluno = dict()
# def notas(*n, sit=False):
    
#     aluno['total'] = len(n)
#     aluno['maior'] = max(n)
#     aluno['menor'] = min(n)
#     aluno['média'] = (sum(n)) / len(n)
#     if sit == True:
#         if aluno['média'] >= 7.0:
#             aluno['situação'] = 'Boa'
#         elif aluno['média'] >= 5.0 and aluno['média'] < 7.0:
#             aluno['situação'] = 'Razoavel'
#         elif aluno['média'] < 5.0:
#             aluno['situação'] = 'Ruim' 
    
#     return aluno




# resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
# print(resp)
# //////////////////////////////////////////
from time import sleep
c = ('\033[m', '\033[0;30;41m',  #0= sem cor, 1 = vermelho
     '\033[0;30;42m', '\033[0;30;43m', #2 = verde, 3= amarelo
     '\033[0;30;44m', '\033[0;30;45m', # 4 = azul, #5 = roxo
     '\033[7;30m'); # 6 = branco


def ajuda(com):
    titulo(f'Acessando o manual do comando \' {com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end='')
    sleep(1)


comado = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)

