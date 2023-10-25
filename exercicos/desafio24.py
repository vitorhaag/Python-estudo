

# total = 0
# totmil = 0
# menor = 0
# cont = 0
# barato = 0
# while True:
#     prod = str(input('Nome do produto: '))
#     preco = float(input('preço: R$'))
#     cont += 1
#     total += preco
#     if preco > 1000:
#         totmil += 1
#     if cont == 1:
#         menor = preco
#         barato = prod
#     else:
#         if preco < menor:
#             menor = preco
#             barato = prod
#     resp = ' '
#     while resp not in 'SN':
#         resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
#     if resp == 'N':
#         break
# print(f'-'*20, 'Fim do programa', '-'*20)
# print(f'O total foi R${total:.2f}')
# print(f'Temos {totmil} produtos custando mais de R$1000.00')
# print(f'O produto mais barato foi  {barato} e custa R${menor:.2f}')


valor = int(input('Que valor voce quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
