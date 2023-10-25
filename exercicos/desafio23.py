
# # while True:
# #     n = int(input('Quer ver a tabuada de qual número? '))
# #     if n < 0:
# #         break
# #     for c in range (1, 11):
# #         print(f' {n} x {c} = {n * c}')
    
    
# # print('Fim do programa')


# from random import randint
# v = 0
# while True:
#     jogador = int(input('Diga um valor: '))
#     computador = randint(0, 10)
#     total = jogador + computador
#     tipo = ' '
#     while tipo not in 'PI':
#         tipo = str(input('Par ou Ímpar? [P/I]  ')).strip().upper()[0]

#     print(f'Voce jogou {jogador} e o computador {computador}. total de {total}')
#     if tipo =='P':
#         if total % 2 == 0:
#             print('Voce VENCEU!!')
#             v += 1

#         else:
#             print('Voce PERDEU!!')
#             break
#     elif tipo == 'I':
#         if total % 2 == 1:
#             print('Voce VENCEU')
#             v += 1
#         else:
#             print('Voce PERDEU')
#             break
#     print('Vamos jogar novamente...')
# print(f'GAME OVER       Voce ganhou {v} vez')


totp = 0
toth = 0
totm20 = 0
while True:
    print('CADASTRE UMA PESSOA  ')
    id = int(input('Idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo: [M/F] ')).strip().upper()[0]
    conti = ' '
    while conti not in 'SN':
        conti = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('-'*30)
    if id > 18:
        totp += 1
    if sex == 'M':
        toth += 1
    if sex =='M' and id < 20:
        totm20 += 1
    if conti not in 'S':
        break
print(f'Total de pessoas com mais de 18 anos: {totp}')
print(f'Ao todo temos {toth} homens cadastrados')
print(f'E temos {totm20} mulheres com menos de 20 anos')