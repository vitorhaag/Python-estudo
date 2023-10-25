# listanum = []
# mai = 0
# men = 0
# for c in range(0, 5):
#     listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
#     if c == 0:
#         mai = men = listanum[c]
#     else:
#         if listanum[c] > mai:
#             mai = listanum[c]
#         if listanum[c] < men:
#             men = listanum[c]
# print(listanum)
# print(f'O menor valor é {men} nas posiçoes ', end='')
# for i, v in enumerate(listanum):
#     if v == men:
#         print(f'{i}...', )
# print(f'O maior valor foi {mai} nas posiçoes ', end='')
# for i, v in enumerate(listanum):
#     if v == mai:
#         print(f'{i}...', )


# numeros = list()
# while True:
#     n = int(input('Digite um valor: '))
#     if n not in numeros:
#         numeros.append(n)
#         print('Valor adicionado com sucesso')
#     else:
#         print('Valor duplicado. Não será adicionado')
#     r = str(input('Quer continuar? [S/N] '))
#     if r in 'Nn':
#         break
# numeros.sort()
# print(f'Voce digitou os valores {numeros}')


lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print('Adiconado no meio da lista')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')            

    