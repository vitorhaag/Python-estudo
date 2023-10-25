# # temp = list()
# # princip = list ()
# # mai = men = 0
# # while True:
# #     temp.append(str(input('Nome: ')))
# #     temp.append(float(input('Peso: ')))
# #     if len(princip) == 0:
# #         mai = men = temp[1]
# #     else:
# #         if temp[1] > mai:
# #             mai = temp[1]
# #         if temp[1] < men:
# #             men = temp[1]
# #     princip.append(temp[:])
# #     temp.clear()
# #     resp = input('Quer continuar? [S/N] ')
# #     if resp in 'Nn':
# #         break
# # print(f'os dados foram {princip}')
# # print(f'ao todo cadastramos {len(princip)} pessoas')
# # print(f'O menor peso é {men}Kg ', end='')
# # for p in princip:
# #     if p[1] == men:
# #         print(f'{p[0]}', end='')

# # print()

# # print(f'O maior é {mai} Kg ', end='')
# # for p in princip:
# #     if p[1] == mai:
# #         print(f'{p[0]}', end='')


# n = [[], []]
# valor = 0
# for c in range(1, 8):
#     valor = int(input('digite um valor: '))
#     if valor % 2 == 0:
#         n[0].append(valor)
#     else:
#         n[1].append(valor)

# print(f'Os pares são {n[0]}')
# print(f'Os impares são {n[1]}')
    


# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0,]]
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#     print()

# ///////////////////////////////////////////

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0,]]
# spar=mai=scol=0
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# for l in range(0, 3):
#     for c in range(0, 3):
#          print(f'[{matriz[l][c]:^5}]', end='')
#          if matriz[l][c] % 2 == 0:
#              spar += matriz[l][c]
#     print()
# print(f' a soma dos pares é {spar}')
# for l in range(0, 3):
#     scol += matriz [l] [2]
# print(f'a soma da terceira coluna {scol}')

# for c in range (0, 3):
#     if c == 0:
#         mai = matriz[1][c]
#     elif matriz[1][c] > mai:
#         mai = matriz[1][c]
# print(f'O maior valor da segunda linha é {max(matriz[1])}')



