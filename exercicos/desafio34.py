# from datetime import date

# nasc = int(input('Em que ano voce nasceu? '))
# idade = date.today().year - nasc
# def vota(nasc):
#     if nasc + 16 <= date.today().year:
#         return f'Com {idade} anos: VOTA'
#     else:
#         return f'Com {idade} anos: NÃO VOTA'

# print(vota(nasc))


# def fatorial(n, show=False):
#     f = 1
#     for c in range(n, 0, -1):
#         if show:
#             print(c, end='')
#             if c>1:
#                 print(' x ', end='')
#             else:
#                 print(' = ', end='')
                
#         f *= c
#     return f
    



# print(fatorial(5))



# def futebol(j='<desconhecido>', g=0):
#     print(f'o jogador {j} fez {g} gol(s) no campeonato')

    

# jogador = str(input('Nome do jogador: '))
# gols = str(input('numero de gols: '))
# if gols.isnumeric():
#     gols = int(gols)
# else:
#     gols = 0
# if jogador.strip() == '':
#     futebol(g=gols)
# else:
#     futebol(jogador, gols)


def leiaInt(msg):
    valor = input(f'{msg}')
    while True:
        if valor.isnumeric():
            break
        else:
            print('ERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO')
            valor = input(f'{msg}')
    return valor
     
    

n = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o número {n}')
