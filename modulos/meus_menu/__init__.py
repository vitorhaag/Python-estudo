from arquivo import *

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except(KeyboardInterrupt):
            print('Entrada de dados intenrrompida pelo usuario')
            return 0
        else:
            return n


def menu_(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c+= 1
    
    opc = leiaint('Sua opção: ')
    return opc

    

        
