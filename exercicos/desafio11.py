# n= int(input('Me diga um numero qualquer: '))
# if n % 2 == 0:
#     print(f' O número {n} é PAR')
# else:
#     print(f'O número {n} é ÍMPAR')


viaj = float(input('Quantos km é a sua viagem? '))
if viaj <= 200:
    print(f'Sua viagem vai custar R${viaj * 0.50:.2f}')
else:
    print(f'Sua viagem vai custar R${viaj * 0.45:.2f}')

